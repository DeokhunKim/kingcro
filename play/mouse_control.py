from mouse_control_base import RemoteMouse
import mouse_coord

mouse = RemoteMouse()

# 영웅 소환 갈기기
def click_summon(WINDOW, num: int = 10):
    for i in range(num):
        mouse.click(WINDOW.MIN_X + mouse_coord.summon[0], WINDOW.MIN_Y + mouse_coord.summon[1])

# 유닛 자동합성
def click_merge(WINDOW, num: int = 2):
    for i in range(num):
        mouse.click(WINDOW.MIN_X + mouse_coord.merge[0], WINDOW.MIN_Y + mouse_coord.merge[1])

# 전투시작
def click_start_round(WINDOW):
    mouse.click(WINDOW.MIN_X + mouse_coord.start_round_btn[0], WINDOW.MIN_Y + mouse_coord.start_round_btn[1])

# 악마의 제한 수락
def click_devil_accept(WINDOW):
    mouse.click(WINDOW.MIN_X + mouse_coord.devil_accept[0], WINDOW.MIN_Y + mouse_coord.devil_accept[1])

# 악마의 제안 거절
def click_devil_deny(WINDOW):
    mouse.click(WINDOW.MIN_X + mouse_coord.devil_deny[0], WINDOW.MIN_Y + mouse_coord.devil_deny[1])

# 제련 - 왼쪽템 클릭
def click_reforge_left(WINDOW):
    mouse.click(WINDOW.MIN_X + mouse_coord.reforge_left[0], WINDOW.MIN_Y + mouse_coord.reforge_left[1])

# 제련 - 중간템 클릭
def click_reforge_middle(WINDOW):
    mouse.click(WINDOW.MIN_X + mouse_coord.reforge_middle[0], WINDOW.MIN_Y + mouse_coord.reforge_middle[1])

# 제련 - 오른쪽템 클릭
def click_reforge_right(WINDOW):
    mouse.click(WINDOW.MIN_X + mouse_coord.reforge_right[0], WINDOW.MIN_Y + mouse_coord.reforge_right[1])

# 제련 - 리롤 클릭
def click_reforge_reroll(WINDOW):
    mouse.click(WINDOW.MIN_X + mouse_coord.reforge_reroll[0], WINDOW.MIN_Y + mouse_coord.reforge_reroll[1])

# 제련 - 제련하기 클릭
def click_reforge_confirm(WINDOW):
    mouse.click(WINDOW.MIN_X + mouse_coord.reforge_confirm[0], WINDOW.MIN_Y + mouse_coord.reforge_confirm[1])



# 디버깅용 포지션 로깅
def current_mouse_position(WINDOW):
    position = mouse.get_mouse_position()
    print(f'[DEBUG] current mouse position: {(position[0] - WINDOW.MIN_X), (position[1] - WINDOW.MIN_Y)}')


if __name__ == '__main__':
    print('test')