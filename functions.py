import cv2
import numpy as np
import os
import re
from os.path import isfile, join


def get_images():
    col_frames = os.listdir('frames')
    col_frames.sort(key=lambda f: int(re.sub(r'\D', '', f)))

    col_images = []
    for frame in col_frames:
        img = cv2.imread('frames/' + frame)
        col_images.append(img)

    return col_images


def frame_mask(img):
    stencil = np.zeros_like(img)
    polygon = np.array([[0, 600], [300, 400], [500, 400], [800, 600]])
    cv2.fillConvexPoly(stencil, polygon, (255, 255, 255))
    return stencil


def frame_mask_vid(img):
    stencil = np.zeros_like(img)
    polygon = np.array([[50, 270], [220, 160], [360, 160], [480, 270]])
    cv2.fillConvexPoly(stencil, polygon, (255, 255, 255))
    return stencil


def apply_mask(img, mask):
    return cv2.bitwise_and(img, mask)


def thresholding(img):
    ret, thresh = cv2.threshold(img, 190, 200, cv2.THRESH_BINARY)
    return thresh


def thresholding_vid(img):
    ret, thresh = cv2.threshold(img, 130, 145, cv2.THRESH_BINARY)
    return thresh


def hough_line_transformation(img, original_img):
    lines = cv2.HoughLinesP(img, 1, np.pi/180, 30, maxLineGap=200)
    dmy = original_img.copy()
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(dmy, (x1, y1), (x2, y2), (0, 255, 0), 3)
    return dmy


def to_video():
    path_in = 'output/'
    path_out = 'detected_lane.mp4'
    fps = 30
    files = [f for f in os.listdir(path_in) if isfile(join(path_in, f))]
    files.sort(key=lambda f: int(re.sub(r'\D', '', f)))

    frame_list = []
    for k in range(len(files)):
        file_name = path_in + files[k]
        img = cv2.imread(file_name)
        height, width, layers = img.shape
        size = (width, height)
        frame_list.append(img)

    out = cv2.VideoWriter(path_out, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for l in range(len(frame_list)):
        out.write(frame_list[l])
    out.release()




