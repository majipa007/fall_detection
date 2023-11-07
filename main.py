import cv2 as cv
import mediapipe as mp
import time
import poseEstimationModule as pm

class runner:
    def __init__(self):
        self.cTime = 0
        self.pTime = 0
        self.img = None
        self.lmlist = None
    def angle(self):
        if len(self.lmlist) != 0:
            detector.findAngle(self.img, 12, 14, 16, True)
            detector.findAngle(self.img, 11, 13, 15, True)
    def run(self):
        detector = pm.poseDetector()
        cap = cv.VideoCapture(0)
        while True:
            success, self.img = cap.read()
            self.img = cv.flip(self.img, 1)
            self.img = cv.resize(self.img, (800, 600))
            self.img = detector.findPose(self.img, False)
            self.cTime = time.time()
            fps = 1 / (self.cTime - self.pTime)
            self.pTime = self.cTime
            cv.putText(self.img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,
                       (255, 0, 255), 3)
            self.img = detector.findPose(self.img, False)
            self.lmlist = detector.findPosition(self.img, False)

            cv.imshow('img', self.img)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break



def main():
    print('hello')
    start = runner()
    start.run()
    start.angle()


if __name__ == '__main__':
    main()
