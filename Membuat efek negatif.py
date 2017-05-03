import numpy as np
import cv2
#import library numpy dan cv2/opencv

cap = cv2.VideoCapture(0)
#melakukan inisialisasi pada webcam, dari kamera yg berlokasi "0" (menggunakan webcam internal)
while(True):
#melakukan looping imshow, objek yang ditangkap oleh webcam dilakukan secara realtime
     ret, frame = cap.read()
     #menangkap gambar dengan format berwarna/BGR
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     #mengkonversi objek yang ditangkap webcam dari yang sebelumnya berwarna diubah menjadi grayscale (skala keabuan)
     cv2.imshow('frame',245-gray)
     #mengubah objek dari grayscale (skala keabuan) menjadi objek dengan skala negatif, sekaligus ditampilkan 
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #perintah untuk menghentikan program dengan menekan tombol 'q'

cap.release()
cv2.waitKey()
cv2.destroyAllWindows()
