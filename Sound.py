'''
Authors: Timo
Date: 09/27/2024
Last modified: 09/27/2024
Purpose: Sound Effects
'''

from playsound import playsound

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
