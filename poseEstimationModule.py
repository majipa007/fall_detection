import cv2 as cv
import mediapipe as mp
import time
import math


class poseDetector:
    def __init__(self):
        self.results = None
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
        self.mpDraw = mp.solutions.drawing_utils

    def findPose(self, img, draw=True):
        # imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.resize(img, (1000, 500))
        self.results = self.pose.process(img)
        # print(results.multi_hand_landmarks)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            myPose = self.results.pose_landmarks
            for id, lm in enumerate(myPose.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 4, (0, 225, 0), cv.FILLED)
        return self.lmList

    def findAngle(self, img, p1, p2, p3, draw=True):
        # getting the landmarks
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        if (angle > 180):
            angle = 360 - angle
        if (angle < 0):
            angle = -angle
        # calculating the angle
        print(angle)

        # drawing in the image
        if draw:
            cv.line(img, (x1, y1), (x2, y2), (0, 225, 0), 2)
            cv.line(img, (x3, y3), (x2, y2), (0, 225, 0), 2)
            cv.circle(img, (x1, y1), 4, (0, 225, 0), cv.FILLED)
            cv.circle(img, (x1, y1), 10, (0, 225, 0), 2)
            cv.circle(img, (x2, y2), 4, (0, 225, 0), cv.FILLED)
            cv.circle(img, (x2, y2), 10, (0, 225, 0), 2)
            cv.circle(img, (x3, y3), 4, (0, 225, 0), cv.FILLED)
            cv.circle(img, (x3, y3), 10, (0, 225, 0), 2)

        # displaying the angle value
        cv.putText(img, str(int(angle)), (x2 - 70, y2 - 20), cv.FONT_HERSHEY_PLAIN, 2,
                   (255, 0, 255), 3)


