__author__ = 'Benjamin M. Singleton'
__date__ = '05 July 2021'
__version = '0.2.1'

from typing import Tuple
import pyautogui
import time
import random
import numpy as np
import cv2
import os

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


def find_template(template_filename: str, target_picture_filename: str, threshold: float) -> None:
    """
    Simple test function for finding desired images in screenshots. This will
    be refactored or removed from production builds.
    :param template_filename: The filename of the screenshot to search inside of.
    :type template_filename: str
    :param target_picture_filename: The filename of the image we hope to locate in the screenshot.
    :type target_picture_filename: str
    :param threshold: The minimum confidence level OpenCV should trust for matching the
    template. Experimental testing indicates 0.7 is a very good value.
    :type threshold: float
    :return: None
    :rtype: None
    """

    # load the image we're going to be searching inside of
    img_rgb = cv2.imread(target_picture_filename)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # load the smaller image that we want to find in img_gray
    template = cv2.imread(template_filename, 0)
    width, height = template.shape[::-1]

    # find all occurrences of template in img_gray above the given threshold
    # and render a red rectangle around each.
    result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    location = np.where(result >= threshold)
    for each_point in zip(*location[::-1]):
        cv2.rectangle(img_rgb, each_point, (each_point[0] + width, each_point[1] + height), (0, 0, 255), 2)

    # save the resulting image with highlighted rectangles in the format [item_name]_threshold_[threshold].png
    # for example, 'torch_0_threshold_0.7.png' or 'iron_ore_threshold_0.8.png'
    item_name = template_filename.split('/')[-1]
    item_name = item_name.split('.png')[0]
    cv2.imwrite(f'{item_name}_threshold_{str(threshold)}.png', img_rgb)
    return


def test_thresholds() -> None:
    """
    Takes each template image (i.e., images of items, monsters, etc) in the
    `Imagges/cropped_images` directory. Then it tries to find that template
    in the `target_image_0.png` image with different thresholds. The results
    of these tests are saved in appropriately named files.
    :return: None
    """
    template_files = list()
    for (dirpath, dirname, filenames) in os.walk('Images/cropped_images/'):
        for each_filename in filenames:
            template_files.append(dirpath + each_filename)
    for each_template in template_files:
        for threshold in [0.6, 0.7, 0.8]:
            find_template(each_template, 'target_image_0.PNG', threshold)
        break


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
    # time.sleep(5)
    # main_terraria()
    test_thresholds()
