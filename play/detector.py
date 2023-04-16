from PIL import ImageGrab
import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np
from settings import object_entry, object_stage, object_devil_item, object_reforge_item, object_trader_item



print('[INFO] Loading find object image')
for o in object_entry:
    o.image = cv2.imread(o.imgurl, cv2.COLOR_BGR2RGB)
for o in object_stage:
    o.image = cv2.imread(o.imgurl, cv2.COLOR_BGR2RGB)
for o in object_devil_item:
    o.image = cv2.imread(o.imgurl, cv2.COLOR_BGR2RGB)
for o in object_reforge_item:
    o.image = cv2.imread(o.imgurl, cv2.COLOR_BGR2RGB)
for o in object_trader_item:
    o.image = cv2.imread(o.imgurl, cv2.COLOR_BGR2RGB)


def find_object(image, WINDOW, target: str):
    target_object = None
    if target == 'entry':
        target_object = object_entry
    elif target == 'devil_item':
        target_object = object_devil_item
    elif target == 'trader_item':
        target_object = object_trader_item
    elif target == 'reforge_item':
        target_object = object_reforge_item
    highscore_result_dict = {}
    for o in target_object:
        data = new_find_template(o, image)
        if not data[0]:
            continue
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(data[1])
        center_loc = (min_loc[0] + o.image.shape[:-1][1]/2), (min_loc[1] + o.image.shape[:-1][0]/2)
        # 화면 절반 위쪽은 제외한다(엔트리만 찾자)
        #if min_loc[1] < WINDOW.HEIGHT / 3:
        #    continue

        # 찾은 바운더리에 다른게 있으면 비교해서 더 정확한걸 넣는다
        is_overlap = False
        for object_text in list(highscore_result_dict.keys()):
            r = highscore_result_dict[object_text]
            if is_in_boundary(center_loc, r):
                if min_val < cv2.minMaxLoc(r)[0]:
                    del highscore_result_dict[object_text]
                    highscore_result_dict[o.text] = data[1]
                is_overlap = True
                break
        if not is_overlap:
            highscore_result_dict[o.text] = data[1]

    result = []
    for object_text, r in highscore_result_dict.items():
        # TODO 여기는 찾는건 나중에 dict 로 바꾸자
        for object in target_object:
            if object.text == object_text:
                o = object
                break

        # Get Location
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(r)
        # Display
        template_h, template_w = o.image.shape[:-1]
        top_left = min_loc
        bottom_right = (top_left[0] + template_w, top_left[1] + template_h)
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
        cv2.putText(image, o.text, (top_left[0], bottom_right[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Store
        result.append((o, min_loc))

    return result


def is_in_boundary(center_loc, result):
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if min_loc[0] < center_loc[0] < min_loc[0] + 50 and min_loc[1] < center_loc[1] < min_loc[1] + 50:
        return True
    else:
        return False


def find_stage(image, WINDOW):
    for o in object_stage:
        data = new_find_template(o, image)
        if not data[0]:
            continue
        print(f'[DEBUG] Find {o.text}')
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(data[1])
        template_h, template_w = o.image.shape[:-1]
        top_left = min_loc
        bottom_right = (top_left[0] + template_w, top_left[1] + template_h)
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
        cv2.putText(image, o.text, (top_left[0], bottom_right[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        return o.text
    return None



def new_find_template(object, image):
    method = cv2.TM_SQDIFF_NORMED

    result = cv2.matchTemplate(image, object.image, method, mask=None)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if min_val < object.threshold:
        return (True, result)
    else:
        return (False, result)


