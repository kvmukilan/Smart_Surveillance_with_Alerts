
import pygame

def play_sound():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("alert_system/alert.wav")
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Sound error: {e}")
