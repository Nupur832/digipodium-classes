import cv2
cam = cv2.VideoCapture(0)
while cam.isOpened():
    status, image = cam.read()
    if status:
        cv2.imshow("Live Camera", image)
        # kuch or code karenge
        if cv2.waitKey(1) == 27: # 27 is the ASCII code for the escape key
            break
cam.release()
cv2.destroyAllWindows()