import re
import pyautogui
import time

with open("data.txt", "r") as f:
    text = f.read()



name = re.findall(r'<name>(.*?)<name>', text, re.MULTILINE)
student_mail = re.findall(r'<smail>(.*?)<smail>', text, re.MULTILINE)
student_id = re.findall(r'<id>(.*?)<id>', text, re.MULTILINE)
number = re.findall(r'<number>(.*?)<number>', text, re.MULTILINE)
fb = re.findall(r'<fb>(.*?)<fb>', text, re.MULTILINE)

msg = len(name)-1
time.sleep(3)

while msg > 0:
    time.sleep(1)
    pyautogui.typewrite("Nawjubillah")
    pyautogui.press('enter')
    msg = msg - 1
