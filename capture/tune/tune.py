from PIL import ImageGrab
import cv2
from skimage.metrics import structural_similarity as ssim
from pynput import mouse
import numpy as np
from capture import settings
from capture import window
from capture import img_compare


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
    back = cv2.imread('find-object-game-template.jpeg')
    normal = cv2.imread('티라노_normal.png')
    big = cv2.imread('티라노_big.png')
    small = cv2.imread('티라노_small.png')

    compare_and_view(back, normal, '1')
    compare_and_view(back, big, '2')
    compare_and_view(back, small, '3')


    cv2.waitKey(0)
    cv2.destroyAllWindows()




def compare_and_view(image1, image2, name):
    #score = compare_ssim(image1, image2)
    score = matchTemplate(image1, image2, cv2.TM_CCOEFF_NORMED)
    #score = unknown(image1, image2)
    print(score)

    if(image1.shape[0] != image2.shape[0]):
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    hconcat = cv2.hconcat([image1, image2])
    cv2.putText(hconcat, str(score), (0, hconcat.shape[0]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow(name, hconcat)






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