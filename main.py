#!/usr/bin/python3
import pygame
pygame.init()

def generate_main_frame():
    output = pygame.Surface((596, 168))
    output.fill(pygame.Color("#000000"))
    output.fill(pygame.Color("#ffffff"), pygame.Rect(8, 8, 579, 151))
    output.fill(pygame.Color("#000000"), pygame.Rect(14, 14, 567, 139))
    return output

def insert_text(surface, line, text):
    font = pygame.font.Font(os.path.join("assets", "dtm.ttf"), 32)
    if line == 1:
        start_position = (188, 31)
    elif line == 2:
        start_position = (188, 67)
    elif line == 3:
        start_position = (188, 103)
    surface.blit(font.render(text, 0, pygame.Color("#ffffff"), start_position)

def insert_character(surface, char, version):
    surface.blit(pygame.load(os.path.join("assets", char, str(version))+".png", (24, 24))

def insert_asterisk(surface, line):
    font = pygame.font.Font(os.path.join("assets", "dtm.ttf"), 32)
    if line == 1:
        start_position = (153, 31)
    elif line == 2:
        start_position = (153, 67)
    elif line == 3:
        start_position = (153, 103)
    surface.blit(font.render("*", 0, pygame.Color("#ffffff"), start_position)

if __name__ == "__main__":
    d = pygame.display.set_mode((596, 168))
    d.blit(generate_main_frame(), (0,0))
    pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()

