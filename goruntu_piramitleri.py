import cv2
resim = cv2.imread('messi.jpg')
up = cv2.pyrUp(resim)#piksel değerini arttırdı
down = cv2.pyrDown(resim)
cv2.imshow('Orijinal', resim)
cv2.imshow('up', up)
cv2.imshow('down', down)#pikselini küçülttü yani boyutu küçülttük
cv2.waitKey(0)
cv2.destroyAllWindows()
