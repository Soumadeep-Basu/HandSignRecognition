import cv2
import mediapipe as m

class handDetector():
    def __init__(self, mode=False, maxHands=2, modelC=1 , detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.modelC = modelC

        self.mpHands = m.solutions.hands
        self.mpDraw = m.solutions.drawing_utils

        self.hands = self.mpHands.Hands(self.mode,self.maxHands, self.modelC,self.detectionCon,self.trackCon)

    def findHands(self, img, draw):
        imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)
        
        if draw==True:
            if self.results.multi_hand_landmarks:
                for handLms in self.results.multi_hand_landmarks:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPositions(self, img):
        lmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[0]

            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape

                cx, cy = int(lm.x*w) , int(lm.y*h)

                lmList.append([id, cx, cy])

        return lmList

    

        


def main():
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while(True):
        success, img = cap.read()
        img = detector.findHands(img, draw=True)

        list = detector.findPositions(img)
 
        if(len(list)>0):
            print(list[4])
            print(list[5])
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
