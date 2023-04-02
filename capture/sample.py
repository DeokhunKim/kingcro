from PIL import ImageGrab
import cv2
from pynput import mouse
import numpy as np
from capture import settings
from capture import window
from capture import img_compare
from capture.tune.tune import find_entry

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
        WINDOW.MAX_X, WINDOW.MAX_Y = x+480, y+800
        print(f'get left top coord ({WINDOW.MIN_X}, {WINDOW.MIN_Y})')
        print(f'get right down coord ({WINDOW.MAX_X}, {WINDOW.MAX_Y})')
        ROI_SET = True
        WINDOW.initialize(WINDOW)
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

        # Key Input
        key = cv2.waitKey(settings.wait_key_interval)
        if key == ord("q"):
            print("exit kingcro! bye!")
            break

        # Get Status
        if img_compare.check_waiting(prev_image, image):
            cv2.putText(out, "Ready", (0, WINDOW.HEIGHT), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            # 장비 제련 화면인가:
                # 1라 라면 지팡이면 클릭 아니라면 재감정
                # 최종까지 지팡이 안나오면 최고 나은거 고름
                # 다른 라운드라면 라운드별 점수?

            # 악마의 제안 화면인가:
                # 필요하다면 수락, 아니라면 거절

            # 상인방문 화면 인가:
                # 필요하다면 구매


            # 전투개시하단과 전투개시상단을 찾는다(상단이라면 하단으로 스크롤)
            # 찾았다면 대기 상태이다:
                # 이런저런 알고리즘 수행 후 전투 개시 누른다 >
                # 먼저 모든 칸 다 더블클릭 두바퀴 돈다 (아이템 합성을 위함)
                # 1. 영웅소환 10번 노르고 성급합체 누르기 반복
                    # 1-1 은화 0,1,2 원일때까지
                    # 1-1 은화가 0,1,2 안될때(템꽉찼을때, 상세처리도 가능하나, 지금은 무리니까 최대 3~5번 제한 두자)
                # 2. 에반 제외하고 판매한한 - (어떻게?)
                # 3. 모든 칸 다 더블클릭 한바퀴 돈다 (에반 합성을 위함)
                # 1,2,3 반복 - 횟수로 하거나, 판매한게 없는데 돈이 0~2원일때까지
                # 4. 아이템 넣을게 있으면 넣는다
                # 5. 전투 개시 클릭
                # + 15라운드 이상부터는 에반 합성 안해도 될듯? 템만 처리

            # 아무조건에도 없으면 대기하자

            find_entry(out, WINDOW)
        else:
            cv2.putText(out, "Not Ready", (0, WINDOW.HEIGHT), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)




        # 가이드컬러
        #out[mask] = cv2.addWeighted(image, alpha, WINDOW.shapes, 1 - alpha, 0)[mask]

        # Display
        cv2.imshow("image", out)  # 화면에 표시 안 할거면 해당 라인 주석

        prev_image = image



cv2.destroyAllWindows()





