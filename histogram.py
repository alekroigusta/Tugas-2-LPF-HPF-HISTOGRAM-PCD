# Nama  : Alek Roigusta
# NIM   : 5301414038
# Prodi : Pendidikan Teknik Elektro, S1
# Makul : Pengolahan Citra DIgital

#Histogram

import numpy as np 
# untuk mengambil deklarasi library numpy dan dipanggil dengan np
import cv2 
# deklarasi untuk import library open cv
from matplotlib import pyplot as plt
#untuk mengambil deklarasi library pyplot dari matplotlib dan dipanggil dengan plt

gray_img = cv2.imread('logo.jpg', cv2.IMREAD_GRAYSCALE)
#inisialisasi untuk membaca gambar logo.jpg dalam bentuk gray(hitam putih)
cv2.imshow('Image', gray_img)
#untuk menampilkan gambar logo.jpg dalam sebuah jendela
hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
#cv.2calcHist inisialisasi untuk mengkalkulasikan histogram pada sebuah gambar
#[gray_img] gambar yang digunakan adalah type unit8

plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histogram')
plt.show()
#untuk menampilkan hasil dengan nama jendela 'Histogram'

while True:
     k = cv2.waitKey(0) & 0xFF
     if k == 27 : break
cv2.destroyAllWindows()