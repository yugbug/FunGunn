import cv2

face_cascade = cv2.CascadeClassifier("/Users/gnir/PycharmProjects/games/Summer_Py/open_cv_course"
                                     "/haarcascades/haarcascade_frontalface_default.xml")

web_cam = cv2.VideoCapture(0)
web_cam.set(3, 640)
web_cam.set(4, 480)
web_cam.set(10, 100)

min_area = 500

while True:
    _, img = web_cam.read()

    # img = cv2.imread("/Users/gnir/PycharmProjects/games/Images/Screen Shot 2019-10-09 at 22.28.31.png")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 3)

    for (x, y, w, h) in faces:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            face_detected = cv2.putText(img, "Face Detected", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                                        (255, 0, 255), 2)
            face_detected = cv2.flip(face_detected, 1)

    # img = cv2.flip(img, 1)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

web_cam.release()
