import pyautogui
pyautogui.FAILSAFE = True

def keyboard_mapping_right():
    pyautogui.press('right')
    print("Right key pressed")


def keyboard_mapping_left():
    pyautogui.press('left')
    print("Left key pressed")