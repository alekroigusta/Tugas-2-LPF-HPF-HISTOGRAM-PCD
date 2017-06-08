# Nama  : Alek Roigusta
# NIM   : 5301414038
# Prodi : Pendidikan Teknik Elektro, S1
# Makul : Pengolahan Citra DIgital

#Low Pass Filter

import numpy as np 
# untuk mengambil deklarasi library numpy dan dipanggil dengan np
import cv2 
# deklarasi untuk import library open cv
from matplotlib import pyplot as plt
#untuk mengambil deklarasi library pyplot dari matplotlib dan dipanggil dengan plt

img = cv2.imread('logo.jpg')
#inisialisasi untuk membaca gambar dengan nama logo.jpg
blur = cv2.blur(img,(5,5))
#untuk mengganti setiap nilai pixel didalam sebuah gambar dengan rata-rata nilai dari pixel tetanggannya
blur2 = cv2.GaussianBlur(img,(5,5),0)
#untuk inisialisasi efek LOW PASS FILTER yaitu GAUSSIAN BLUR

plt.subplot(2,2,1),plt.imshow(img),plt.title('Awal')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(blur),plt.title('Blur')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(blur2),plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([])
plt.show()
#untuk menampilkan hasil dalam satu jendela.