import numpy as np
import cv2
#import library numpy dan cv2/opencv

cap = cv2.VideoCapture(0)
#melakukan inisialisasi pada webcam, dari kamera yg berlokasi "0" (menggunakan webcam internal)
while(True):
#melakukan looping imshow, objek yang ditangkap oleh webcam dilakukan secara realtime
    ret, frame = cap.read()
    #menangkap gambar dengan format berwarna/BGR
    bright = cv2.addWeighted(frame,1.5,np.zeros(frame.shape,frame.dtype),0,25)
    #memberikan efek yaitu meningkatkan nilai kecerahan gambar 
    cv2.imshow('webcam',bright)
    #menampilkan gambar yang telah diberi efek
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #perintah untuk menghentikan program dengan menekan tombol 'q'

cap.release()
cv2.waitKey()
cv2.destroyAllWindows()
