import keyboard
import time


time.sleep(10)
print("Begin Counting")
x = 0
while(x < 100):
    keyboard.write(f"wah")
    keyboard.send('enter')
    x = x+1
    time.sleep(1)
