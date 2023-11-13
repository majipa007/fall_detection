import cv2 as cv
import mediapipe as mp
import time
import poseEstimationModule as pm


class runner:
    def __init__(self):
        self.detector = None
        self.cTime = 0
        self.pTime = 0
        self.img = None
        self.lmlist = None

    def angle(self):
        if len(self.lmlist) != 0:
            self.detector.findAngle(self.img, 12, 14, 16, True)
            self.detector.findAngle(self.img, 11, 13, 15, True)

    def run(self, ang=True):
        self.detector = pm.poseDetector()
        #cap = cv.VideoCapture(0)
        #cap = cv.VideoCapture('/home/sukuna/PycharmProjects/AdancedCV/fight.mp4')
        cap = cv.VideoCapture('fall.mp4')

        while True:
            success, self.img = cap.read()
            self.img = cv.flip(self.img, 1)
            #self.img = cv.resize(self.img, (800, 600))
            self.img = self.detector.findPose(self.img, False)
            self.cTime = time.time()
            fps = 1 / (self.cTime - self.pTime)
            self.pTime = self.cTime

            cv.putText(self.img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,
                       (255, 0, 255), 3)
            self.img = self.detector.findPose(self.img, True)
            self.lmlist = self.detector.findPosition(self.img, False)
            # Uncomment for angle
            # if ang:
            #     self.angle()
            if len(self.lmlist) != 0:
                val = self.detector.fallDetector(0.01)
                if val:
                    cv.putText(self.img, "fall", (70, 70), cv.FONT_HERSHEY_PLAIN, 3,
                               (255, 0, 255), 3)
                else:
                    cv.putText(self.img, "stand", (70, 70), cv.FONT_HERSHEY_PLAIN, 3,
                               (255, 0, 255), 3)
            cv.imshow('img', self.img)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break


def main():
    print('hello')
    start = runner()
    start.run(True)


if __name__ == '__main__':
    main()
