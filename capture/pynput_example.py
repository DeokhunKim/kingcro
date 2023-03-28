from pynput.mouse import Button, Controller
from pynput import mouse
import time

"""
def on_click(x, y, button, pressed):
    print('\r{0} {1}'.format(
        '클릭 위치' if pressed else '뗀  위치',
        (x, y)))
    if not pressed:
        return False

with mouse.Listener(
    on_click=on_click
) as listner:
    listner.join()
    
    
#클릭 위치 (-1577.23828125, 48.19921875)
#뗀  위치 (-1311.375, 272.5859375)

"""
# 마우스 콘트롤러 객체
mouse = Controller()

def drag_mouse(mouse, from_position, to_position):
    time.sleep(0.2)
    mouse.position = from_position
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.position = to_position
    time.sleep(0.2)
    mouse.release(Button.left)
    time.sleep(0.2)


def click_mouse(mouse, position, num=1):
    time.sleep(0.2)
    mouse.position = position
    time.sleep(0.2)
    mouse.click(Button.left, num)
    time.sleep(0.2)


# 마우스 드래그
drag_mouse(mouse, (-1577.23828125, 48.19921875), (-1311.375, 272.5859375))

# 클릭 한다
click_mouse(mouse, (-1311.375, 272.5859375))

# 더블클릭 한다
click_mouse(mouse, (-1577.23828125, 48.19921875), num=2)

# 마우스 포지션 이동
#mouse.move(100, -100)
#print('바뀐 마우스 포지션: {0}'.format(mouse.position))



