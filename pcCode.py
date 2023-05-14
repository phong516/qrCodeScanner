import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import urllib.request
from webbrowser import open_new_tab
#cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
 
url='http://192.168.43.14/'
cv2.namedWindow("Camera Sensor", cv2.WINDOW_AUTOSIZE)
 
prev=""
pres=""
while True:
    img_resp=urllib.request.urlopen(url+'cam-mid.jpg')
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgnp,-1)
    #_, frame = cap.read()
 
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        pres=obj.data
        if prev == pres:
            pass
        else:
            print("Type:",obj.type)
            qr=obj.data
            qr_data=qr.decode('utf-8')
            print("Data: ",qr_data)
            prev=pres
            if qr_data[0:4]=="http":
                open_new_tab(qr_data)
        cv2.putText(frame, str(qr_data), (50, 50), font, 2,
                    (255, 0, 0), 3)
 
    cv2.imshow("Camera Sensor", frame)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cv2.destroyAllWindows()
