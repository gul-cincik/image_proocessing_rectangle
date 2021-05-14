import cv2

resim = cv2.imread('cicek.png')
cv2.imshow('Cicek', resim)

cv2.rectangle(resim, (200, 70), (320,180), (255, 0, 0), 2)
cv2.imshow('dortgen', resim)

cv2.waitKey(0)
cv2.destroyAllWindows()