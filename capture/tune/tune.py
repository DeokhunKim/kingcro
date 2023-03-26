from PIL import ImageGrab
import cv2
from skimage.metrics import structural_similarity as ssim
from pynput import mouse
import numpy as np
from capture.settings import find_object



print('Load find object image.')
for o in find_object:
    o.image = cv2.imread(o.imgurl, cv2.COLOR_BGR2RGB)


def evan_test(image, WINDOW):
    highscore_result_dict = {}
    for o in find_object:
        data = new_find_template(o, image)
        if not data[0]:
            continue
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(data[1])
        center_loc = (min_loc[0] + max_loc[0]) / 2, (min_loc[1] + max_loc[1]) / 2
        # 화면 절반 위쪽은 제외한다(엔트리만 찾자)
        if min_loc[1] < WINDOW.HEIGHT / 2:
            continue

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


    for object_text, r in highscore_result_dict.items():
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(r)
        # TODO 여기는 찾는건 나중에 dict로 바꾸자
        for object in find_object:
            if object.text == object_text:
                o = object
                break
        template_h, template_w = o.image.shape[:-1]
        top_left = min_loc
        bottom_right = (top_left[0] + template_w, top_left[1] + template_h)
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
        cv2.putText(image, o.text, (top_left[0], bottom_right[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)


def is_in_boundary(center_loc, result):
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_loc[0] < center_loc[0] < min_loc[0] and min_loc[1] < center_loc[1] < max_loc[1]:
        return True
    else:
        return False







def new_find_template(object, image):
    method = cv2.TM_SQDIFF_NORMED

    result = cv2.matchTemplate(image, object.image, method, mask=None)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if min_val < object.threshold:
        return (True, result)
    else:
        return (False, result)







    ##############################################
###########   legacy   #######################
##############################################
def run():
    '''
    evan_empty = cv2.imread('evan_empty.png')
    evan_noise = cv2.imread('evan_noise.png')
    evan_noise_nohp = cv2.imread('evan_noise_nohp.png')
    t1 = cv2.imread('t1.png')
    t2 = cv2.imread('t2.png')
    t3 = cv2.imread('t3.png')
    t4 = cv2.imread('t4.png')
    compare_and_view(evan_noise_nohp, evan_noise, '1')
    compare_and_view(evan_noise_nohp, t1, '2')
    compare_and_view(evan_noise_nohp, t2, '3')
    compare_and_view(evan_noise_nohp, t3, '4')
    compare_and_view(evan_noise_nohp, t4, '5')
    '''

    #back = cv2.imread('find-object-game-template.jpeg')
    #normal = cv2.imread('티라노_normal.png')
    #big = cv2.imread('티라노_big.png')
    #small = cv2.imread('티라노_small.png')

    #image = cv2.imread('newevan/IMG_1219_1.png', cv2.IMREAD_UNCHANGED)
    image = cv2.imread('newevan/IMG_1222.png')

    #compare_and_view(evan, image, '1')
    find_template(evan1, image, 'evan-1')
    find_template(evan2, image, 'evan-2')
    find_template(evan3, image, 'evan-3')
    find_template(evan4, image, 'evan-4')
    find_template(evan5, image, 'evan-5')
    find_template(evan6, image, 'evan-6')

    cv2.imshow('sample', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




def compare_and_view(image1, image2, name):
    #score = compare_ssim(image1, image2)
    #score = matchTemplate(image1, image2, cv2.TM_SQDIFF_NORMED)
    #score = unknown(image1, image2)
    score = find_template(image1, image2)
    print(score)

    fontsize = 1
    fontwidth = 2

    '''
    if(image1.shape[0] != image2.shape[0]):
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
    fontsize = 1
    fontwidth = 2
    '''
    if (image2.shape[0] != image1.shape[0]):
        image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))
    fontsize = 5
    fontwidth = 10


    hconcat = cv2.hconcat([image1, image2])
    cv2.putText(hconcat, str(score), (0, hconcat.shape[0]), cv2.FONT_HERSHEY_SIMPLEX, fontsize, (0, 0, 255), fontwidth, cv2.LINE_AA)
    cv2.imshow(name, hconcat)


def find_template(template, image, text, threshold=0.15):
    method = cv2.TM_SQDIFF_NORMED

    result = cv2.matchTemplate(image, template, method, mask=None)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if min_val < threshold:
        template_h, template_w = template.shape[:-1]
        top_left = min_loc
        bottom_right = (top_left[0] + template_w, top_left[1] + template_h)
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
        cv2.putText(image, text, (top_left[0], bottom_right[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    return min_val







# 이미지 크기가 다르면 비교 못함
def compare_ssim(image1, image2):
    grayA = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    (score, diff) = ssim(grayA, grayB, full=True)
    return score


    # cv2.TM_SQDIFF
    # cv2.TM_SQDIFF_NORMED
    # cv2.TM_CCORR
    # cv2.TM_CCORR_NORMED
    # cv2.TM_CCOEFF
    # cv2.TM_CCOEFF_NORMED
def matchTemplate(image1, image2, method):
    result = cv2.matchTemplate(image1, image2, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # TM_SQDIFF : 최소값이 good matching
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        match_val = min_val
    else:
        top_left = max_loc
        match_val = max_val

    return match_val


def unknown(image1, image2):
    imgs = []
    imgs.append(image1)
    imgs.append(image2)
    hists = []
    for img in imgs:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
        cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
        hists.append(hist)
    query = hists[0]
    # methods = ['CORREL', 'CHISQR', 'INTERSECT', 'BHATTACHARYYA', 'EMD']
    methods = ['BHATTACHARYYA']

    for index, name in enumerate(methods):
        #print('%-10s' % name)
        for i, histogram in enumerate(hists):
            ret = cv2.compareHist(query, histogram, index)

            if index == cv2.HISTCMP_INTERSECT:
                ret = ret / np.sum(query)
            print("img%d :%7.2f" % (i + 1, ret))
            if i == 1:
                return ret









if __name__ == '__main__':
    run()