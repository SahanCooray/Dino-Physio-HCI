import serial
import pyautogui
import subprocess
import time
import sys

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.005

# Open Chrome Dino Game
try:
    subprocess.Popen(["chromium-browser", "--kiosk", "chrome://dino"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except Exception as e:
    print("Error opening browser:", e)
    print("Please manually open chrome://dino in Chromium.")
    time.sleep(5)

# Focus the browser window
print("Click the browser window manually to focus the game.")
time.sleep(5)
pyautogui.click(x=500, y=500)
pyautogui.press('space')
time.sleep(1)

# Replace with your Arduino's serial port (use `ls /dev/tty*`)
try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1)
    time.sleep(2)
except serial.SerialException as e:
    print("Serial error:", e)
    exit()

print("Game Started. Flex to jump! Press Ctrl+C to stop.")

last_jump_time = 0
jump_cooldown = 0.3

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            if data == '1':
                current_time = time.time()
                if current_time - last_jump_time >= jump_cooldown:
                    pyautogui.press('space')
                    print("Jump!")
                    last_jump_time = current_time
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()
