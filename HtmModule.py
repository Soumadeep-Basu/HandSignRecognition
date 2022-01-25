import cv2
import mediapipe as m
import time


class handDetector():

    alert_List = []

    def __init__(self, mode=False, maxHands=2, modelC=1 , detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.modelC = modelC

        self.mpHands = m.solutions.hands
        self.mpDraw = m.solutions.drawing_utils

        self.hands = self.mpHands.Hands(self.mode,self.maxHands, self.modelC,self.detectionCon,self.trackCon)

    def getter(self):
        return self.alert_List
    

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

    start = time.time()
        
    elapsed = 0
    
    while(True):
        success, img = cap.read()
        img = detector.findHands(img, draw=False)
        
        lists = detector.findPositions(img)
        
        if(elapsed>6):
            elapsed = 0 
            start = time.time()
            del handDetector.alert_List[:]
        else:
            elapsed = time.time() - start
 
        if(len(lists)>0):
            #check for h
            if (lists[4][2] < lists[3][2] and lists[3][2] < lists[1][2]) and (lists[8][2] < lists[7][2] and lists[7][2] < lists[5][2]) and (lists[12][2] < lists[11][2] and lists[11][2] < lists[9][2]) and (lists[16][2] < lists[15][2] and lists[15][2] < lists[13][2]) and (lists[20][2] < lists[19][2] and lists[19][2] < lists[17][2]) and (lists[4][1]>lists[5][1]):
                # print("H has been detected")
                
                if(handDetector.alert_List.count("H")==0):
                    
                    handDetector.alert_List.append("H")
                    
                    print("h Detetcted")
            if(lists[4][1]<lists[5][1]) and (lists[4][2] < lists[3][2] and lists[3][2] < lists[1][2]) and (lists[8][2] < lists[7][2] and lists[7][2] < lists[5][2]) and (lists[12][2] < lists[11][2] and lists[11][2] < lists[9][2]) and (lists[16][2] < lists[15][2] and lists[15][2] < lists[13][2]) and (lists[20][2] < lists[19][2] and lists[19][2] < lists[17][2]):
                if(handDetector.alert_List.count("E")==0 and handDetector.alert_List.count("H")==1):
                    handDetector.alert_List.append("E")
                    handDetector.alert_List.append("L")
                    
                    print("HEL detected")
            if (lists[8][2] > lists[5][2]) and (lists[12][2] > lists[9][2]) and (lists[16][2] > lists[13][2]) and (lists[20][2] >  lists[17][2] and lists[4][1]<lists[5][1] ):
                if(handDetector.alert_List.count("P")==0 and handDetector.alert_List.count("H")==1 and handDetector.alert_List.count("E")==1):
                    handDetector.alert_List.append("P")
                    
                    print("HELP detected")
                    path = "C:/Users/soumadeep basu/Pictures/POC/" + str(time.time()) + ".jpg"
                    cv2.imwrite(path,img)


                



            

            #wait for 5s
            ##check for elp and then fire alert

            #delete list and start again if not in 5s
       
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
