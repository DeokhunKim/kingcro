import mouse_control as msctl
from item_score import score_dict as score
from settings import max_reforge_reroll_count as reroll_cnt


def action_devil(result, WINDOW):
    print(f'[DEBUG] Devil''s propose do action')
    if result is None or len(result) == 0:
        print(f'[WARNING] Can not found devil''s propose item')
        msctl.click_devil_deny(WINDOW)
        return

    for r in result:
        is_agree = score[r[0].text][3] == 1
        print(f'[DEBUG] + item name: {r[0].text}, agree : {is_agree}')
        if is_agree:
            print(f'[DEBUG] + click 수락')
            msctl.click_devil_accept(WINDOW)
        else:
            print(f'[DEBUG] + click 거절')
            msctl.click_devil_deny(WINDOW)
        return


def action_reforge(result, WINDOW):
    print(f'[DEBUG] Equipment reforge do action')
    action = 's' # s(stay), l(left), m(middle), r(right), re(reroll)
    for reroll in range(reroll_cnt):
        if result is None or len(result) == 0:
            print(f'[WARNING] Can not found Equipment reforge item')
            if reroll == reroll_cnt:
                msctl.click_reforge_middle(WINDOW)
                msctl.click_reforge_confirm(WINDOW)
                return
            else:
                msctl.click_reforge_reroll(WINDOW)
                continue

        max_score = 0
        tier = -1
        for r in result:
            if r[0].text == 'tier1':
                tier = 0
            elif r[0].text == 'tier2':
                tier = 1
            elif r[0].text == 'tier3':
                tier = 2

        if tier == -1:
            print(f'[WARNING] Can not found reforge tier')
            tier = 0
        else:
            print(f'[DEBUG] Reforge tier is {tier + 1}')

        for r in result:
            if r[0].text == 'tier1' or r[0].text == 'tier2' or r[0].text == 'tier3':
                continue
            elif max_score < score[r[0].text][tier]:
                max_score = score[r[0].text][tier]
                max_score_loc = r[1]

            # 디버깅 로그
            if 70 <= r[1][0] <= 130:
                print(f'[DEBUG] Left item score: {score[r[0].text][tier]}')
            elif 170 <= r[1][0] <= 230:
                print(f'[DEBUG] Middle item score: {score[r[0].text][tier]}')
            elif 270 <= r[1][0] <= 330:
                print(f'[DEBUG] Right item score: {score[r[0].text][tier]}')

        print(f'[DEBUG] Max item score: {max_score}')
        # 10점 이거나 리롤 없으면 위치 정하고
        if max_score == 10 or reroll == reroll_cnt:
            if 70 <= max_score_loc[0] <= 130:
                action = 'l'
            elif 170 <= max_score_loc[0] <= 230:
                action = 'm'
            elif 270 <= max_score_loc[0] <= 330:
                action = 'r'
        # 리롤 남았으면 리롤
        else:
            action = 're'
        # 클릭
        if action == 're':
            print(f'[DEBUG] Reroll reforge!')
            msctl.click_reforge_reroll(WINDOW)
            continue
        elif action == 'l':
            print(f'[DEBUG] Select left item!')
            msctl.click_reforge_left(WINDOW)
            msctl.click_reforge_confirm(WINDOW)
            return
        elif action == 'r':
            print(f'[DEBUG] Select right item!')
            msctl.click_reforge_right(WINDOW)
            msctl.click_reforge_confirm(WINDOW)
            return
        else: # action == 'r' or 's':
            print(f'[DEBUG] Select middle item!')
            msctl.click_reforge_middle(WINDOW)
            msctl.click_reforge_confirm(WINDOW)
            return


def action_trader(result, WINDOW):

    return