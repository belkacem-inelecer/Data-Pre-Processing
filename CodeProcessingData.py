# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:15:26 2021

@author: Belkacem
"""

import os
from PIL import Image as im
import cv2
import numpy as np
import random
import glob
from pathlib import Path


path=Path("E://Pycharm projects/DataSetCDTA")


images=[]


for imagepath in path.glob("*.jpg"):
    
    img=cv2.imread(str(imagepath))
    imgResize = cv2.resize(img, (1000,500))
    HSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(HSV)
    for Value in np.arange(5.0, 255.0, 2.5):
        v.fill(Value)
        hsv_image = cv2.merge([h, s, v])
        n = random.randint(0,999999)
        final_image = im.fromarray(hsv_image)
        final_image.save('pngs/{}.jpg'.format(n))
        #hsv_image.save('pngs/{}.jpg'.format(n))
