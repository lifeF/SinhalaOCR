import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ImageRead:
    def __init__(self,FileName):
        self.img=mpimg.imread(FileName)
    
    def get(self):
        return self.img