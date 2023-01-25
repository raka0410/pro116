import cv2
img = cv2.imread("solar-system.jpg")

cv2.imshow("Displaying the image",img)
cv2.putText(img,"Sun",(20,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2,color=(255,255,255))
cv2.putText(img,"Mercury",(70,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"Venus",(160,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"Earth",(280,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"Mars",(370,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"Jupiter",(500,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"Saturn",(750,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"Uranus",(930,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"Neptune",(1080,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))




cv2.imshow("Displaying the image",img)
cv2.waitKey(0)
