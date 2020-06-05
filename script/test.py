import cv2

img = cv2.imread('img/K20D5136-1.jpg')
gimg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_, tgimg = cv2.threshold(gimg,60,255,cv2.THRESH_BINARY)
cv2.imshow('threshold',tgimg)
cv2.waitKey(0)
contours, hierarchy = cv2.findContours(tgimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
det_img = cv2.drawContours(img,contours,-1,(0,255,0),1)
cv2.imshow('test',det_img)
cv2.waitKey(0)
cv2.destroyAllWindows()