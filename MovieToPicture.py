import cv2
import os

class MovieToPicture():
    def __init__(self, result_path, movie_path, picture_name):
        self.rpath = result_path
        self.mpath = movie_path
        self.picname = picture_name
        self.cap = cv2.VideoCapture(self.mpath)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.count = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.num = 0

    def change(self):
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret == True:
                cv2.imwrite('{}/{}_{}.jpg'.format(self.rpath, self.picname, str(self.num).zfill(3)), frame)
                self.num += 1
            else:
                break
        self.cap.release