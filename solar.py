import cv2

img=cv2.imread("C:/Users/vijay.LAPTOP-6K2HIQ6S/OneDrive/Desktop/VS Projects Python/Project-116/solar-system.jpg")
cv2.putText(img,"Sun",(0,225),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0))
cv2.putText(img,"Mercury",(100,220),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0))
cv2.putText(img,"Venus",(180,220),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0))
cv2.putText(img,"Earth",(300,220),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0))
cv2.putText(img,"Mars",(375,220),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0))
cv2.putText(img,"Jupiter",(500,225),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0))
cv2.putText(img,"Saturn",(750,225),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0))
cv2.putText(img,"Uranus",(950,222),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0))
cv2.putText(img,"Neptune",(1100,222),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0))
cv2.imshow("planets",img)
cv2.waitKey(0)