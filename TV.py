import pygame as pg
import cv2
from constants import *

# Creating the Channel class to make our life easier, cause we'll not be needed in doing all that code 10 times
# Cycle 'for' is also will be longer and harder
class Channel:
    # when we will create(initialize) an object of that class we will bind video and sound to it
    def __init__(self, video_path: str, sound_path: str) -> object: # so we need the path to it
        # video path will be used later in the main file for the recapturing, so we'll safe it as an object's sign
        self.__video_path = video_path    
        self.__cap = cv2.VideoCapture(self.__video_path)    # creating first capture of the video
        # success is a bool variable that shows success of the video read
        self.__success, self.__img = self.__cap.read()      # img - is the next(or now - the first) frame of the video
        self.__img = cv2.resize(self.__img, (VID_WIDTH, VID_HEIGHT)) 
        self.__img = cv2.transpose(self.__img)      # there we are make img readable for the pygame
        self.sound = pg.mixer.Sound(sound_path)     # sound is an object that we wiil later play by sound.play() method

        # and the last - creating surface of the img size, then we will use it to blit img to the screen
        self.__surface = pg.surface.Surface((self.__img.shape[0], self.__img.shape[1]))   

    # method next_frame will blit img to the "screen" and change img to the next frame
    def next_frame(self, screen: pg.surface.Surface) -> bool:
        self.__success, self.__img = self.__cap.read()   # reinitialize success and img(that will change img to the next frame)
        if not self.__success:    # if success is false(for example at the end of the video), we will return True(see main.py)
            return True
        self.__img = cv2.cvtColor(self.__img, cv2.COLOR_BGR2RGB)    # cv2 module read img in brg so recolor it as an rgb for the pygame

        self.__img = cv2.resize(self.__img, (VID_WIDTH, VID_HEIGHT))    # resize it to an setted settings
        self.__img = cv2.transpose(self.__img)      # transpose again(it need to do to the all of the frames, so we repeat)
        pg.surfarray.blit_array(self.__surface, self.__img)       # img now is an array of pixels, so we need to blit it to a surface to blit it on a screen later
        screen.blit(self.__surface, (TV_POSX + 5, TV_POSY + 5))   # blit img surface to the screen in pos of TV with an indent of TV frame
        return False    # if everything is OK - return false, see main.py

    # recapture needed to start video from the beginning(it's needed cause i can't start sound not from beginning)
    def recapture(self):
        self.__cap = self.__cap = cv2.VideoCapture(self.__video_path)
