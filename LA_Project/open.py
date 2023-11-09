# from PIL import Image, ImageFilter
# img = Image.open("img2.jpg")
# gray_img = img.convert("L")
# sharp_img = gray_img.filter(ImageFilter.SHARPEN)
# edge_enhance_img = sharp_img.filter(ImageFilter.EDGE_ENHANCE)
# edge_enhance_img.show()

import cv2
import numpy as np
from PIL import Image
import pickle

def Img_arr():
    img = cv2.imread('img1.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cov_mat = np.cov(gray)
    eigenvalues, eigenvectors = np.linalg.eig(cov_mat)
    sharpen_filter=np.array([[-1,-1,-1],
                    [-1,9,-1],
                    [-1,-1,-1]])

    img = cv2.filter2D(gray,-1,sharpen_filter)
    #cv2.imshow('gray', gray)

    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    #cv2.imshow('thresh', thresh)

    ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    op = 0
    split = []
    bwlist = []
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        area = w*h

        if 250 < area < 12000:
            roi = img[y:(y + h), x:(x + w)]
            roi = cv2.resize(roi, (28, 28))
            bw = Image.fromarray(roi)
            bw = bw.convert('L').point(lambda x: 255 if x < 128 else 0, '1')
            roi = 255 * np.array(bw, int)
            split.append(roi)
            #rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #cv2.imshow('rect', rect)
    split = np.array(split)
    print(split.shape)
    # for i in range(len(split)):
    #     cv2.imshow(str(i),split[i])
    cv2.waitKey(0)
    img_file = open("img_file", "wb")
    pickle.dump(split, img_file)
    img_file.close()