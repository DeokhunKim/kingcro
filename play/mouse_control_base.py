from pynput.mouse import Button, Controller
from time import sleep
from settings import mouse_interval


class RemoteMouse:
    def __init__(self):
        self.mouse = Controller()

    def move_position(self, xPos, yPos):
        sleep(mouse_interval)
        self.mouse.position = (xPos, yPos)
        sleep(mouse_interval)

    def click(self, xPos, yPos):
        sleep(mouse_interval)
        self.mouse.position = (xPos, yPos)
        sleep(mouse_interval)
        self.mouse.click(Button.left)
        sleep(mouse_interval)

    def double_click(self, xPos, yPos):
        sleep(mouse_interval)
        self.mouse.position = (xPos, yPos)
        sleep(mouse_interval)
        self.mouse.click(Button.left, 2)
        sleep(mouse_interval)

    def drag(self, from_x, from_y, to_x, to_y):
        sleep(mouse_interval)
        self.mouse.position = (from_x, from_y)
        sleep(mouse_interval)
        self.click()
        sleep(mouse_interval)
        self.mouse.press(Button.left)
        sleep(mouse_interval)
        self.mouse.position = (to_x, to_y)
        sleep(mouse_interval)
        self.mouse.release(Button.left)
        sleep(mouse_interval)

    def get_mouse_position(self):
        return self.mouse.position
