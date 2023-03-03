import numpy as np
from skimage.metrics import structural_similarity as ssim
import cv2



def check_waiting(img1, img2):
    grayA = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    (score, diff) = ssim(grayA, grayB, full=True)
    # diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))
    return score > 0.97