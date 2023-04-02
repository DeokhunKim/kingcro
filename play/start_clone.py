from PIL import ImageGrab
import cv2
from pynput import mouse
import numpy as np
import settings
import window
import mouse_control as msctl
import waiting_checker
import detector

# Global Definition
ROI_SET = False
WINDOW = window
ROUND: int = 1


# 현재 윈도우창 boundary 구하기
print(f'[ACTION] Click mouse left top corner on play window.')
def get_window_boundary(x, y, button, pressed):
    global WINDOW, ROI_SET
    if not pressed:
        return False

    WINDOW.MIN_X, WINDOW.MIN_Y = x, y
    WINDOW.MAX_X, WINDOW.MAX_Y = x + settings.resolution[0], y + settings.resolution[1] # TODO 고쳐
    print(f'[INFO] Get left top coordinate ({WINDOW.MIN_X}, {WINDOW.MIN_Y})')
    print(f'[INFO] Get right down coordinate ({WINDOW.MAX_X}, {WINDOW.MAX_Y})')
    ROI_SET = True
    WINDOW.initialize(WINDOW)


def print_coord(x, y, button, pressed):
    print(f'x:{x}, y:{y}')

with mouse.Listener(
       on_click=get_window_boundary) as listener:
    listener.join()

# Input command 받는다
#   - q: 종료
#   -
print(f'[INFO] Key input description \n'
      f'- q: exit \n'
      f'- r: get back window location (not yet)')
prev_image = np.zeros([WINDOW.HEIGHT, WINDOW.WIDTH, 3], np.uint8)
while True:
    if ROI_SET:
        image = cv2.cvtColor(np.array(ImageGrab.grab(
            bbox=(WINDOW.MIN_X, WINDOW.MIN_Y, WINDOW.MAX_X, WINDOW.MAX_Y)
        )), cv2.COLOR_BGR2RGB)
        out = image.copy()
        alpha = 0.5
        mask = WINDOW.shapes.astype(bool)

        # Key Input
        key = cv2.waitKey(settings.wait_key_interval)
        if key == ord('q'):
            print("[INFO] Exit kingcro! Bye!")
            break
        elif key == ord('a'):
            print("a")
            msctl.click_merge(WINDOW, 1)
        elif key == ord('b'):
            print("b")
            msctl.click_summon(WINDOW, 1)
        elif key == ord('c'):
            print("c")
            msctl.click_start_round(WINDOW)
        elif key == ord('p'):
            print("c")
            msctl.current_mouse_position(WINDOW)




        # 가이드컬러
        #out[mask] = cv2.addWeighted(image, alpha, WINDOW.shapes, 1 - alpha, 0)[mask]

        # Display
        cv2.imshow("image", out)  # 화면에 표시 안 할거면 해당 라인 주석

        prev_image = image



cv2.destroyAllWindows()


