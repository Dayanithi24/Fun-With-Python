import cv2
import cvzone
import time
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
from playsound import playsound
while True:
    cap = cv2.VideoCapture(0)
    start=time.time()
    detector = FaceMeshDetector(maxFaces=1)
    plotY =LivePlot(640,360,[15,50],invert=True)
    idList = [22,23,24,26,110,157,158,159,160,161,130,243]
    ratiolist=[]
    blinkcounter=0
    counter=0
    color=(255,0,255)
    flag=True

    while True:
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        success, img = cap.read()
        img, faces = detector.findFaceMesh(img,draw=False)
        if faces:
            face=faces[0]
            for id in idList:
                cv2.circle(img,face[id],5,color,cv2.FILLED)

            leftUp=face[159]
            leftDown=face[23]
            leftLeft=face[130]
            leftRight=face[243]
            lenV,_=detector.findDistance(leftUp,leftDown)
            lenH, _ = detector.findDistance(leftLeft, leftRight)
            cv2.line(img,leftUp,leftDown,(0,200,0),3)
            cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)
            ratio=int((lenV/lenH)*100)
            ratiolist.append(ratio)
            if len(ratiolist)>3:
                ratiolist.pop(0)
            ratioAvg=sum(ratiolist)/len(ratiolist)
            if ratioAvg<30 and counter==0:
                blinkcounter+=1
                if blinkcounter > 30:
                    print('You slept')
                    playsound('loudest-alarm-ever-36964.mp3')
                    flag=False
                    break
                color=(0,200,0)
                counter=1
            if counter!=0:
                counter+=1
                if counter>10:
                    color=(255,0,255)
                    counter=0
            cvzone.putTextRect(img,f'Blink Count: {blinkcounter}',(50,100),colorR=color)
            imgPlot = plotY.update(ratioAvg,color)
            img = cv2.resize(img, (640, 360))
            # cv2.imshow("ImagePlot", imgPlot)
            imgStack = cvzone.stackImages([img, imgPlot], 1, 1)
        else:
            img = cv2.resize(img, (640, 360))
            # cv2.imshow("Image", imgStack)
            imgStack = cvzone.stackImages([img, img], 1, 1)

        cv2.imshow("Image",imgStack)
        if (time.time()-start)>60:
            break
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            exit()
        cv2.waitKey(1)
    if(blinkcounter<=6):
        print('You are falling sleep')
    elif (flag):
        print("Congratulations, You're active.. Keep it up")
        flag=True
    cap.release()
    cv2.destroyAllWindows()
    time.sleep(5)
