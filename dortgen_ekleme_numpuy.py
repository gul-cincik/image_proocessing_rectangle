import cv2
import numpy as np

resim = np.zeros((400, 400, 3), dtype='uint8')#400e 400lük 3 rengin kullanıldığı nuint8 tipinde 0 lardan oluşan bir 0 1 zemini oluşturuldu

cv2.rectangle(resim, (10,10), (390, 200), (0, 255, 255), 3)#üzerine işleme yapılacak resim, başladığı nokta, bittiği nokta, renk değeri ve kalınlık
cv2.line(resim, (10,10), (390,200), (0,0,255), 3)#çapraz çizgi çekecek
cv2.line(resim, (10,230),(390,230),(123,45,78),3)#yatay çizgi çekecek
cv2.circle(resim, (200, 350), 25, (148, 0, 56), 3)#dairenin merkezi, yarıçapı, rengi ve kalınlığı

#metin ekleme
cv2.putText(resim, 'Rose', (5, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 255 , 255), 4, cv2.LINE_4)#image, text, koordinasyon, yazı tipi,
cv2.imshow('siyah', resim)#siyah bir çıktı verecek
cv2.waitKey(0)
cv2.destroyAllWindows()