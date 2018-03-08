import numpy as np
import cv2
import cv2.aruco as aruco

videoCap = cv2.VideoCapture(0)
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()

while(True):
    ret, frame = videoCap.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedImgs = aruco.detectMarkers(grayscale, aruco_dict, parameters = parameters)
    print(corners)

    grayscale = aruco.drawDetectedMarkers(grayscale, corners)

    cv2.imshow('frame', grayscale)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCap.release()
cv2.destroyAllWindows()
    
