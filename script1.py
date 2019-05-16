# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:56:39 2019

@author: u5644101
"""#messing around with fourier transforms.
import numpy as np
import copy
from matplotlib import pyplot as plt
a = b7[0]
forier = np.fft.fft2(a)
x = copy.deepcopy(forier)

def create_circular_mask(h, w, center=None, radius=None):#stole this function from internet:https://stackoverflow.com/questions/44865023/circular-masking-an-image-in-python-using-numpy-arrays

    if center is None: # use the middle of the image
        center = [int(w/2), int(h/2)]
    if radius is None: # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w-center[0], h-center[1])

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius
    return mask

mask = create_circular_mask(400,400,radius = 80)
x80 = np.fft.fftshift(x) * mask
mask = create_circular_mask(400,400,radius = 40)
x40 = np.fft.fftshift(x) * mask
mask = create_circular_mask(400,400,radius = 20)
x20 = np.fft.fftshift(x) * mask
mask = create_circular_mask(400,400,radius = 10)
x10 = np.fft.fftshift(x) * mask
y = forier -np.fft.fftshift(x80)
x80 = x80-x40
x40 = x40 - x20
x20 = x20-x10
x80 = np.fft.fftshift(x80)
x40 = np.fft.fftshift(x40)
x20 = np.fft.fftshift(x20)
x10 = np.fft.fftshift(x10)

im1 = np.real(np.fft.ifft2(x80))
im2 = np.real(np.fft.ifft2(x40))
im3 = np.real(np.fft.ifft2(x20))
im4 = np.real(np.fft.ifft2(x10))
im5 = np.real(np.fft.ifft2(y))
plt.imshow(im1)
#plt.imshow(im2)
#plt.imshow(np.log(np.abs(np.fft.fftshift(x))**2))