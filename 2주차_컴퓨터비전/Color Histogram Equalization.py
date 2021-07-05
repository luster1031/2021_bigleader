import cv2
import numpy as np
import argparse
import os
import matplotlib.pyplot as plt

path = "image.jpg"

# 이미지 불러오기
src = cv2.imread(path)

# hsv 컬러 변형
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# h, s, v로 컬러 영상 분리
h, s, v = cv2.split(hsv)
# v값을 히스토그램 평활화
equalizedV = cv2.equalizeHist(v)
equalizedS = cv2.equalizeHist(s)
equalizedh = cv2.equalizeHist(h)

# h,s,equalizedV를 합쳐서 새로운 hsv 이미지 만듦
hsv2 = cv2.merge([h,s,equalizedV])
hsv3 = cv2.merge([h,equalizedS, equalizedV])
hsv4 = cv2.merge([equalizedh,equalizedS, equalizedV])

# 마지막으로 hsv2를 다시 BGR 형태로 변경
hsvDst = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)
hsvDst1 = cv2.cvtColor(hsv3, cv2.COLOR_HSV2BGR)
hsvDst2 = cv2.cvtColor(hsv4, cv2.COLOR_HSV2BGR)


# 출력합니다.
cv2.imshow('original', src)
cv2.imshow('v equalized', hsvDst)
cv2.imshow('sv equalized', hsvDst1)
cv2.imshow('hsv equalized', hsvDst2)
cv2.waitKey()
cv2.destroyAllWindows()
