import serial
import pyautogui
import subprocess
import time
import sys

# Configure PyAutoGUI
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.005

# Open the Chrome Dino game
try:
    if sys.platform.startswith('win'):
        subprocess.call(['start', 'chrome', 'chrome://dino'], shell=True)
    elif sys.platform.startswith('darwin'):
        subprocess.call(['open', '-a', 'Google Chrome', 'chrome://dino'])
    else:
        subprocess.call(['chromium-browser', 'chrome://dino'])
except Exception as e:
    print(f"Error opening browser: {e}")
    print("Please manually open chrome://dino in Chrome.")
    time.sleep(5)  # Give time to open manually

# Ensure browser focus
print("Focusing on browser window...")
print("Please ensure the Chrome Dino game window is visible and click it once to focus.")
pyautogui.click(x=500, y=500)  # Initial focus attempt
pyautogui.press('space')  # Start the game
time.sleep(1)

# Initialize serial
try:
    ser = serial.Serial('COM9   ', 9600, timeout=0.1)  # Verify port
    time.sleep(2)
except serial.SerialException as e:
    print(f"Serial error: {e}")
    exit()

print("Dino Game Controller Started. Flex your muscle to jump! Press Ctrl+C to exit.")
print("Keep the Chrome Dino game window focused for jumps to work.")

last_jump_time = 0
jump_cooldown = 0.2  # Sync with Arduino debounce

try:
    while True:
        if ser.in_waiting > 0:
            try:
                while ser.in_waiting:
                    data = ser.readline().decode('utf-8').strip()
                    print(f"Received: '{data}'")
                    current_time = time.time()
                    if data == '1' and current_time - last_jump_time >= jump_cooldown:
                        print("Attempting jump...")
                        pyautogui.press('space')  # Simplified key press
                        time.sleep(0.1)  # Ensure game registers
                        print("Jump triggered!")
                        last_jump_time = current_time
                    else:
                        print(f"Skipped jump: data='{data}', cooldown={current_time - last_jump_time:.2f}s")
            except Exception as e:
                print(f"Serial read error: {e}")

except KeyboardInterrupt:
    print("Program terminated by user.")

finally:                
    ser.close()
    print("Serial connection closed.")                        