import cv2              # for using OpenCV4.5 and CUDNN.
import numpy as np      # for making variety zeros array.
import os
import io
import time
import multiprocessing
import copy
from csi_camera import CSI_Camera


def draw_label(cv_image, label_text, label_position):
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.5
    color = (255,255,255)
    cv2.putText(cv_image, label_text, label_position, font_face, scale, color, 1, cv2.LINE_4)

# 신호 들어오면 시작 

def signal():
    while True:
        if GPIO:
            head_detection()


def HeadDetection():
    boxes = 3
    return boxes


# 위의 HeadDetection과의 연결고리는 바로 boxes. box의 개수는 중요하지 않음 
def BodyDetection():

    # 일단, 각도도 중요하다 시발 -> 바닥과 수평 이루기 
    # 주변 조도 통제가 필요할 수 있다 -> 배경은 하얀 LED 패널(전원OFF) 고정
    # 최대 떨어진 거리는 35cm ~ 40cm 사이로, 피사체와의 거리가 35cm 이상이면 상관없다. 
    return 10

def Main():
    print(HeadDetection())

def ErrorDeteciton():
    return 10

def Test():
    
    # 스티커 불량품 여부 판단은 아래 논리로 이루어진다. 
    # <가설>
    # 1. HeadDetection 최대값은 10
    # 2. 10개 초과 잡는거 해결 
    # 3. 
    
    # HeadDetection 개수를 변수에 저장
    HeadCountNumber = HeadDetection()

    if  HeadCountNumber == 10:
        if BodyDetection() == 10: # Head가 10개인데, Body도 10개이다.
            return "정상"
        else: # Head가 10개인데, Body가 10개가 아니다. 
            ErrorDeteciton() # 비정상이므로 어떤 오류인지 검사 시작 
            return "비정상", "어떤오류"

    elif HeadCountNumber <7 : # 라이터 Head 개수가 7개 미만인 경우는 발생하지 않는다고 가정. 흔들린 경우로 판단 
        continue;
        
    else: # 라이터 Head 개수가 8~9개인 경우, 불량품이 발생한 경우로 판단한다. 
        ErrorDeteciton() 
        return "비정상", "어떤오류"
