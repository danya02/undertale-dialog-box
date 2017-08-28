#!/usr/bin/python3
import os
import pygame
import random
pygame.init()

def generate_main_frame():
    output = pygame.Surface((596, 168))
    output.fill(pygame.Color("#000000"))
    output.fill(pygame.Color("#ffffff"), pygame.Rect(8, 8, 579, 151))
    output.fill(pygame.Color("#000000"), pygame.Rect(14, 14, 567, 139))
    return output

def insert_text(surface, line, text, sans=False, papyrus=False):
    if sans and papyrus:
        raise ValueError(random.choice("Papyrus doesn't want to talk while Sans is around.", "Sans doesn't want to talk while Papyrus is around."))
    elif sans:
        font = pygame.font.Font(os.path.join("assets", "sans.ttf"), 32)
        if line == 1:
            start_position = (188, 32)
        elif line == 2:
            start_position = (188, 68)
        elif line == 3:
            start_position = (188, 104)
    elif papyrus:
        font = pygame.font.Font(os.path.join("assets", "papyrus.ttf"), 32)
        if line == 1:
            start_position = (154, 28)
        elif line == 2:
            start_position = (154, 64)
        elif line == 3:
            start_position = (154, 100)
    else:
        font = pygame.font.Font(os.path.join("assets", "dtm.ttf"), 32)
        if line == 1:
            start_position = (188, 31)
        elif line == 2:
            start_position = (188, 67)
        elif line == 3:
            start_position = (188, 103)
    surface.blit(font.render(text, 0, pygame.Color("#ffffff")), start_position)

def insert_character(surface, char, version):
    surface.blit(pygame.image.load("assets/"+char+"/"+str(version)+".png"), (24, 24))

def insert_asterisk(surface, line, sans=False):
    if sans:
        font = pygame.font.Font(os.path.join("assets", "sans.ttf"), 32)
    else:
        font = pygame.font.Font(os.path.join("assets", "dtm.ttf"), 32)
    if line == 1:
        start_position = (153, 31)
    elif line == 2:
        start_position = (153, 67)
    elif line == 3:
        start_position = (153, 103)
    surface.blit(font.render("*", 0, pygame.Color("#ffffff")), start_position)

if __name__ == "__main__":
    d = pygame.display.set_mode((596, 168))
    d.blit(generate_main_frame(), (0,0))
    insert_character(d, "Flowey", "1_1")
    insert_asterisk(d, 1)
    insert_asterisk(d, 2)
    insert_asterisk(d, 3)
    insert_text(d, 1, "Howdy!")
    insert_text(d, 2, "I'm FLOWEY!")
    insert_text(d, 3, "FLOWEY the FLOWER!")
    pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()

