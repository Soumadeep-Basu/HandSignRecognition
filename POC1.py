import cv2
import mediapipe as m 

#poc screen creation

cap = cv2.VideoCapture(0)

mpHands = m.solutions.hands
mpDraw = m.solutions.drawing_utils

hands = mpHands.Hands()

while True:
    success, img = cap.read()
    imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    if(results.multi_hand_landmarks):
        for handLms in results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                #get the indexes
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
