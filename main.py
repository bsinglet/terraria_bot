__author__ = 'Benjamin M. Singleton'
__date__ = '28 June 2021'
__version = '0.2.0'

from typing import Tuple
import pyautogui
import time
import random
import cv2

PICKAXE_HOTKEY = '2'
TORCH_HOTKEY = '5'


def press_button(button: str, press_time: int) -> None:
    pyautogui.keyDown(button)
    time.sleep(press_time)
    pyautogui.keyUp(button)


def dig(target_area: Tuple[int, int], walk_direction: str, walk_time: int) -> None:
    pyautogui.mouseDown(button='left', x=target_area[0], y=target_area[1])
    time.sleep(5)
    pyautogui.mouseUp(button='left')

    press_button(walk_direction, walk_time)


def place_torch(target_area: Tuple[int, int]) -> None:
    press_button(TORCH_HOTKEY, 2)

    time.sleep(2)
    pyautogui.mouseDown(button='left', x=target_area[0], y=target_area[1])
    time.sleep(5)
    pyautogui.mouseUp(button='left')

    press_button(PICKAXE_HOTKEY, 2)


def look_for_drowning():
    pass


def look_for_water():
    pass


def check_if_moving():
    pass


def main_terraria() -> None:
    target_window = pyautogui.getWindowsWithTitle('Terraria')[0]
    x, y = target_window.topleft
    height = target_window.height
    width = target_window.width
    center_position = (x + int(width / 2), y + int(height / 2))
    lower_left_area = (x + int(0.25 * width), y + int(0.75 * height))
    lower_right_area = (x + int(0.75 * width), y + int(0.75 * height))
    left_area = (x + int(0.25 * width), y + int(0.5 * height))
    right_area = (x + int(0.75 * width), y + int(0.5 * height))
    down_area = (x + int(0.5 * width), y + int(0.75 * height))
    upper_left_area = (x + int(0.25 * width), y + int(0.25 * height))
    upper_right_area = (x + int(0.75 * width), y + int(0.25 * height))

    for i in range(100):
        random_choice = random.randint(3, 3)
        if random_choice <= 2:
            dig_target = right_area
            torch_target = upper_left_area
            walk_direction = 'd'
        elif random_choice == 3:
            dig_target = left_area
            torch_target = upper_right_area
            walk_direction = 'a'
        elif random_choice > 3:
            dig_target = lower_left_area
            torch_target = upper_right_area
            walk_direction = 'a'
        elif random_choice > 4:
            dig_target = lower_right_area
            torch_target = upper_left_area
            walk_direction = 'd'
        else:
            dig_target = lower_left_area
            torch_target = upper_right_area
            walk_direction = 'a'
        for j in range(5):
            dig(dig_target, walk_direction, 2)
        place_torch(torch_target)


if __name__ == '__main__':
    time.sleep(5)
    main_terraria()
