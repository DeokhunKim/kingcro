from mouse_control_base import RemoteMouse
import mouse_coord

mouse = RemoteMouse()


def click_summon(WINDOW, num: int = 10):
    for i in range(num):
        mouse.click(WINDOW.MIN_X + mouse_coord.summon[0], WINDOW.MIN_Y + mouse_coord.summon[1])


def click_merge(WINDOW, num: int = 10):
    for i in range(num):
        mouse.click(WINDOW.MIN_X + mouse_coord.merge[0], WINDOW.MIN_Y + mouse_coord.merge[1])


def click_start_round(WINDOW):
    mouse.click(WINDOW.MIN_X + mouse_coord.start_round_btn[0], WINDOW.MIN_Y + mouse_coord.start_round_btn[1])

def current_mouse_position(WINDOW):
    position = mouse.get_mouse_position()
    print(f'[DEBUG] current mouse position: {(position[0] - WINDOW.MIN_X), (position[1] - WINDOW.MIN_Y)}')


if __name__ == '__main__':
    print('test')