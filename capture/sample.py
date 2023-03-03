from PIL import ImageGrab
import cv2
from pynput import mouse
import numpy as np
import settings

# Global Definition
ROI_SET = False
WINDOW_MIN_X, WINDOW_MIN_Y, WINDOW_MAX_X, WINDOW_MAX_Y = 0, 0, 0, 0


# 현재 윈도우창 boundary 구하기
def get_window_boundary(x, y, button, pressed):
    if pressed:
        global WINDOW_MIN_X, WINDOW_MIN_Y
        WINDOW_MIN_X, WINDOW_MIN_Y = x, y
    else:
        global WINDOW_MAX_X, WINDOW_MAX_Y, ROI_SET
        WINDOW_MAX_X, WINDOW_MAX_Y = x, y
        ROI_SET = True
    if not pressed:
        return False

with mouse.Listener(
       on_click=get_window_boundary) as listener:
    listener.join()


# input command 받는다
#   - q: 종료
#   -
while True:
    if ROI_SET:
        image = cv2.cvtColor(np.array(ImageGrab.grab(
            bbox=(int(WINDOW_MIN_X), int(WINDOW_MIN_Y), int(WINDOW_MAX_X), int(WINDOW_MAX_Y))
        )), cv2.COLOR_BGR2RGB)
        cv2.imshow("image", image)  # 화면에 표시 안 할거면 해당 라인 주석
        key = cv2.waitKey(settings.wait_key_interval)
        if key == ord("q"):
            print("Quit")
            break
cv2.destroyAllWindows()


