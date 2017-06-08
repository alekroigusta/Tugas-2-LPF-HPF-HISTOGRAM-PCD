# Nama  : Alek Roigusta
# NIM   : 5301414038
# Prodi : Pendidikan Teknik Elektro, S1

#High Pass Filter
import numpy as np 
# untuk mengambil deklarasi library numpy dan dipanggil dengan np
import cv2 
# deklarasi untuk import library open cv
from matplotlib import pyplot as plt
#untuk mengambil deklarasi library pyplot dari matplotlib dan dipanggil dengan plt
img0 = cv2.imread('logo.jpg')
#inisialisasi untuk membaca gambar dengan nama logo.jpg
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
#inisialisasi untuk merubah img0 menjadi gray(hitam putih)
img = cv2.GaussianBlur(gray,(3,3),0)
#inisialisasi untuk memberi efek GAUSSIAN BLUR agar noise pada gambar hilang.
laplacian = cv2.Laplacian(img, cv2.CV_64F)
#untuk mengkonvolusi gambar dengan meminta ukuran gambar
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
#inisialisasi gambar menjadi efek sobel x-dir
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
#inisialisasi gambar menjadi efek sobel y-dir
plt.subplot(2,2,1), plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(sobelx, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()
#untuk menampilkan hasil dalam satu jendela.