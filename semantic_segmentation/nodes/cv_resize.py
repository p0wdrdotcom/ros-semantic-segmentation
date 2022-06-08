#!/usr/bin/env python3

"""
Nearest neighbor resize using numpy only.
Unfortunately the ROS-provided cv2.so is fantastically compiled without python3 bindings so it cannot be used with python3. This allows people who only need nearest neighbor resize to avoid these shenanigans entirely and avoid OpenCV dependency.

Author: dheera@dheera.net
Author: geoff@p0wdr.com - opencv is way faster....  just install it
```pip3 install opencv-python```
"""


import cv2

def resize(img, new_shape):
    """
    Nearest-neighbor resize.
    img = an opencv image
    shape = (width, height) as per OpenCV convention NOT numpy convention
    """

    return cv2.resize(img, dsize=new_shape, interpolation=cv2.INTER_LINEAR)
