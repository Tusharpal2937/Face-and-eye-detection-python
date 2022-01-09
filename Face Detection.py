from cv2 import cv2
data = cv2.CascadeClassifier("C:\\Users\\Tushar Pal\\Desktop\\My Projects\\Python Projects\\dataset.xml")
data_eye = cv2.CascadeClassifier("C:\\Users\\Tushar Pal\\Desktop\\My Projects\\Python Projects\\eye.xml")
webcam = cv2.VideoCapture(0)

#By this code we could use any different camera (such as mobile camera) as our webcam and perform detection
# address = 'http://xxxxxxxxxxx:8080/video'
# webcam.open(address)

while True:
    successfull, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    coordinates_eye = data_eye.detectMultiScale(gray)
    coordinates = data.detectMultiScale(gray)
    for (x,y,w,h) in coordinates:
        cv2.putText(frame,"Face",(x, y-17), cv2.FONT_HERSHEY_PLAIN ,1,(0,255,0), 2)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)
        cv2.rectangle(frame, (x+10,y+10), (x+w-10, y+h-10), (220,255,0), 1)
    for (x,y,w,h) in coordinates_eye:
        cv2.putText(frame,"eye",(x, y+h+17), cv2.FONT_HERSHEY_PLAIN ,1,(0,255,0), 2)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    # print(coordinates)
    cv2.imshow('Detection', frame)
    cv2.waitKey(1)


