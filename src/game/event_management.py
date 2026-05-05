import pygame
from pygame import (K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN,
                    QUIT, K_q, K_RETURN)
from pygame import USEREVENT
from pygame.time import set_timer

class EventHandler:
    def __init__(self, screen, game_state):
        self._screen = screen
        self._game_screen = game_state

    def pygame_quit(self):
        self._game_screen.running = False

    def key_bindings(self, key):
        if key == K_LEFT:
            self._game_screen.direction = "l"
        elif key == K_RIGHT:
            self._game_screen.direction = "r"
        elif key == K_UP:
            self._game_screen.direction = "u"
        elif key == K_DOWN:
            self._game_screen.direction = "d"

    def handle_events(self, event):
        if event.type == QUIT:
            self.pygame_quit()

        if event.type == KEYDOWN:
            print("KEY PRESSED:", event.key)
            # Wenn sich das Spiel noch im Startmenü befindet,
            # soll nur die ENTER-Taste ausgewertet werden.
            if self._game_screen.in_menu:

                # ENTER beendet das Menü und startet das Spiel
                if event.key == K_RETURN:
                    print("ENTER DETECTED")
                    self._game_screen.in_menu = False

            else:
                # Außerhalb des Menüs werden die normalen
                # Steuerungstasten (Bewegung) verarbeitet.
                self.key_bindings(event.key)
           #Mit Taste P wird der Pause-Zustand umgeschaltet (True/False)
            if event.key == pygame.K_p:
                self._game_screen.is_paused = not self._game_screen.is_paused
        
        if event.type == self._game_screen.custom_event:
            curr_mode = self._game_screen.ghost_mode
            if curr_mode == 'scatter':
                self._game_screen.ghost_mode = 'chase'
            elif curr_mode == 'chase':
                self._game_screen.ghost_mode = 'scatter'
            CUSTOM_EVENT = USEREVENT + 1
            set_timer(CUSTOM_EVENT, 
                                self._game_screen.mode_change_events * 1000)
            self._game_screen.custom_event = CUSTOM_EVENT
        
        if event.type == self._game_screen.power_up_event:
            self._game_screen.is_pacman_powered=False

