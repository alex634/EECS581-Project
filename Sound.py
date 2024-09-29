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
    '''
    This is called and is the only thing called when a sound effect is to be played. The audio is contained in a subdirectory called "sounds". Originally this used the playsound library to play audio, but issues occurred getting it to run consistently. We are now using pygame but we wrote code to make it callable as if it were playsound. All of the audio used in our program was sourced from `freesound.org <https://freesound.org>`_
    '''
    @staticmethod
    def play_Missed():
        '''
        Plays when a ship is missed. 
        '''
        playsound('sounds/splash_cc0.wav')
    @staticmethod
    def play_Win():
        '''
        Plays when the game is won.
        '''
        playsound('sounds/win_cc0.wav')
    @staticmethod
    def play_Error():
        '''
        Plays when a user error occurs.
        '''
        playsound('sounds/error_cc0.wav')
    @staticmethod
    def play_Hit():
        '''
        Plays when a ship is hit.
        '''
        playsound('sounds/hit_cc0.wav')
    @staticmethod
    def play_Sunk():
        '''
        Plays when a ship is sunk.
        '''
        playsound('sounds/cloud_cc0.wav')
    @staticmethod
    def play_Turn():
        '''
        Plays when games switches to the next player.
        '''
        playsound('sounds/turn_cc0.wav')
