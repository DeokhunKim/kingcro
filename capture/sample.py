from PIL import ImageGrab
import cv2
from pynput import mouse
import numpy as np
from capture import settings
from capture import window
from capture import img_compare

# Global Definition
ROI_SET = False
WINDOW = window


# 현재 윈도우창 boundary 구하기
def get_window_boundary(x, y, button, pressed):
    global WINDOW, ROI_SET
    if not pressed:
        return False
    if WINDOW.MIN_X == 0.0 and WINDOW.MIN_Y == 0.0:
        WINDOW.MIN_X, WINDOW.MIN_Y = x, y
        print(f'get start boundary ({WINDOW.MIN_X}, {WINDOW.MIN_Y})')
    else:
        WINDOW.MAX_X, WINDOW.MAX_Y = x, y
        print(f'get end boundary ({WINDOW.MAX_X}, {WINDOW.MAX_Y})')
        ROI_SET = True
        WINDOW.initialize(WINDOW)

def print_coord(x, y, button, pressed):
    if not pressed:
        return False
    print(x, y)

with mouse.Listener(
       on_click=get_window_boundary) as listener:
    listener.join()
with mouse.Listener(
        on_click=get_window_boundary) as listener:
    listener.join()


# input command 받는다ㅂ
#   - q: 종료 
#   -
prev_image = np.zeros([WINDOW.HEIGHT, WINDOW.WIDTH, 3], np.uint8)
while True:
    if ROI_SET:
        image = cv2.cvtColor(np.array(ImageGrab.grab(
            bbox=(WINDOW.MIN_X, WINDOW.MIN_Y, WINDOW.MAX_X, WINDOW.MAX_Y)
        )), cv2.COLOR_BGR2RGB)
        out = image.copy()
        alpha = 0.5
        mask = WINDOW.shapes.astype(bool)
        # 가이드컬러
        out[mask] = cv2.addWeighted(image, alpha, WINDOW.shapes, 1 - alpha, 0)[mask]

        # Key Input
        key = cv2.waitKey(settings.wait_key_interval)
        if key == ord("q"):
            print("exit kingcro! bye!")
            break

        # Get Status
        text_shape = np.zeros_like(image, np.uint8)
        if img_compare.check_waiting(prev_image, image):
            cv2.putText(out, "Ready", (0, WINDOW.HEIGHT), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(out, "Not Ready", (0, WINDOW.HEIGHT), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)


        # Display
        cv2.imshow("image", out)  # 화면에 표시 안 할거면 해당 라인 주석

        prev_image = image



cv2.destroyAllWindows()


