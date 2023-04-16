from PIL import ImageGrab
import cv2
from pynput import mouse
import numpy as np
import settings
import window
import waiting_checker
import detector
import mouse_control as msctl
import action

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
        if key == ord("q"):
            print("[INFO] Exit kingcro! Bye!")
            break
        elif key == ord('s'):
            msctl.click_start_round(WINDOW)
            ROUND = ROUND + 1
        elif key == ord('p'):
            msctl.current_mouse_position(WINDOW)

        # Get Status
        #text_shape = np.zeros_like(image, np.uint8)
        if waiting_checker.check_waiting(prev_image, image):
            status = ''
            stage = detector.find_stage(out, WINDOW)
            if stage is None:
                status = 'Ready'

            # 악마의 제안:
            elif stage == 'devil':
                # 필요하다면 수락, 아니라면 거절
                status = 'Devil''s propose'
                print(f'[INFO][Round_{ROUND}] Devil''s propose')
                action.action_devil(
                    detector.find_object(out, WINDOW, 'devil_item'), WINDOW
                )


            # 장비 제련:
            elif stage == 'reforge':
                # 1라 라면 지팡이면 클릭 아니라면 재감정
                # 최종까지 지팡이 안나오면 최고 나은거 고름
                # 다른 라운드라면 라운드별 점수?
                status = 'Equipment reforging'
                print(f'[INFO][Round_{ROUND}] Equipment reforging')

                action.action_reforge(
                    detector.find_object(out, WINDOW, 'reforge_item'), WINDOW
                )

            # 상인 방문
            elif stage == 'trader':
                # 필요하다면 구매
                status = 'Trader shop'
                print(f'[INFO][Round_{ROUND}] Trader shop')
                detector.find_object(out, WINDOW, 'trader_item')

            # 대기 상태
            elif stage == 'start1':
                print(f'[INFO][Round_{ROUND}] Rearrange time.')
                # 1라운드
                if ROUND == 1:
                    # 소환 하고 합치고 배치
                    print('')

            # 대기 상태인데 화면이 상단으로 올라감
            elif stage == 'start2':
                print(f'[INFO][Round_{ROUND}] Screen is up. Scroll down')

            # 게임이 종료
            elif stage == 'end':
                # 버튼 누르고 나가자
                print(f'[INFO][Round_{ROUND}] Game is done. ')
                ROUND = 1

            else:
                print(f'[ERROR] Unknown stage text ({stage})')

            # Debug text
            cv2.putText(out, status, (0, WINDOW.HEIGHT), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)




            # 대기상태라면 넘어오자
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
            # 6. stage++

            # 아무조건에도 없으면 대기하자

            #detector.find_entry(out, WINDOW)
        else:
            cv2.putText(out, "Not Ready", (0, WINDOW.HEIGHT), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)



        # 가이드컬러
        #out[mask] = cv2.addWeighted(image, alpha, WINDOW.shapes, 1 - alpha, 0)[mask]

        # Display
        cv2.imshow("image", out)  # 화면에 표시 안 할거면 해당 라인 주석

        prev_image = image



cv2.destroyAllWindows()


