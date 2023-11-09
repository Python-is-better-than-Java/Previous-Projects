import cv2
import numpy as np

img = cv2.imread('C:\\Users\\Dell\\Desktop\\LA project\\image.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cov_mat = np.cov(gray)

eigenvalues, eigenvectors = np.linalg.eig(cov_mat)


sharpen_filter=np.array([[-1,-1,-1],
                 [-1,9,-1],
                [-1,-1,-1]])

sharp_image=cv2.filter2D(gray,-1,sharpen_filter)
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', gray)
cv2.imshow('Required image',sharp_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
