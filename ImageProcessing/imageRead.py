import cv2

class ImageRead:
    def __init__(self,FileName):
        self.img = cv2.read(FileName)