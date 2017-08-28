#!/usr/bin/python3
import pygame
pygame.init()

def generate_main_frame():
    output = pygame.Surface((596, 168))
    output.fill(pygame.Color("#000000"))
    output.fill(pygame.Color("#ffffff"), pygame.Rect(8, 8, 579, 151))
    output.fill(pygame.Color("#000000"), pygame.Rect(14, 14, 567, 139))
    return output

if __name__ == "__main__":
    d = pygame.display.set_mode((596, 168))
    d.blit(generate_main_frame(), (0,0))
    pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()

