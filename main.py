import poseEstimation as pe
import time
import cv2 as cv




def main():
    pTime = 0
    cTime = 0
    print("hello1")
    cap = cv.VideoCapture(0)
    detector = pe.poseDetector()
    print("hello2")
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=True)
        if len(lmList) != 0:
            print(lmList[4])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,
                   (255, 0, 255), 3)
        cv.imshow("img", img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()
