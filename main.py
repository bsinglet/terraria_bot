__author__ = 'Benjamin M. Singleton'
__date__ = '28 June 2021'
__version = '0.1.0'

import pyautogui
import time
import random


def walk_left(walk_time):
    pyautogui.keyDown('a')
    time.sleep(walk_time)
    pyautogui.keyUp('a')


def walk_right(walk_time):
    pyautogui.keyDown('d')
    time.sleep(walk_time)
    pyautogui.keyUp('d')


def dig_lower_left(lower_left_area, walk_time):
    pyautogui.mouseDown(button='left', x=lower_left_area    [0], y=lower_left_area[1])
    time.sleep(5)
    pyautogui.mouseUp(button='left')

    walk_left(walk_time)


def dig_lower_right(lower_right_area, walk_time):
    pyautogui.mouseDown(button='left', x=lower_right_area    [0], y=lower_right_area[1])
    time.sleep(5)
    pyautogui.mouseUp(button='left')

    walk_right(walk_time)


def click_terraria():
    target_window = pyautogui.getWindowsWithTitle('Terraria')[0]
    x, y = target_window.topleft
    height = target_window.height
    width = target_window.width
    center_position = (x + int(width / 2), y + int(height / 2))
    lower_left_area = (x + int(0.25 * width), y + int(0.75 * height))
    lower_right_area = (x + int(0.75 * width), y + int(0.75 * height))
    # move_time = 2  # how many seconds to take to move the cursor
    # pyautogui.moveTo(lower_right_area[0], lower_right_area[1], move_time)
    # x, y = pyautogui.position()
    # print(f'Current mouse position is ({x}, {y})')

    """
    if random.randint(1, 2) < 2:
        walk_left(random.randint(10,100))
    else:
        walk_right(random.randint(10,100))
    """
    
    for i in range(100):
        random_choice = random.randint(1,2)
        for i in range(5):
            if random_choice < 2:
                dig_lower_left(lower_left_area, 2)
            else:
                dig_lower_right(lower_right_area, 2)


if __name__ == '__main__':
    time.sleep(5)
    click_terraria()
