'''
Authors: Timo
Date: 09/27/2024
Last modified: 09/27/2024
Purpose: Sound Effects
'''

import pygame.mixer
import threading
import time

pygame.mixer.init()

def playsound(sound_file):
    def play():
        sound = pygame.mixer.Sound(sound_file)
        sound.play()

        while pygame.mixer.get_busy():
            time.sleep(0.5)

    sound_thread = threading.Thread(target=play)
    sound_thread.start()
        

class Sound:
    @staticmethod
    def play_Missed():
        playsound('sounds/splash_cc0.wav')
    @staticmethod
    def play_Win():
        playsound('sounds/win_cc0.wav')
    @staticmethod
    def play_Error():
        playsound('sounds/error_cc0.wav')
    @staticmethod
    def play_Hit():
        playsound('sounds/hit_cc0.wav')
    @staticmethod
    def play_Sunk():
        playsound('sounds/cloud_cc0.wav')
    @staticmethod
    def play_Turn():
        playsound('sounds/turn_cc0.wav')
