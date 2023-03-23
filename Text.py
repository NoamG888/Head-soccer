import pygame


class Text:

    def __init__(self, text, x_pos, y_pos, size, color, font):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
        self.color = color
        self.font = font

    def display(self, screen):
        text_font = pygame.font.SysFont(self.font, self.size)
        text_surf = text_font.render(str(self.text), True, self.color)
        text_rect = text_surf.get_rect(center=(self.x_pos, self.y_pos))
        screen.blit(text_surf, text_rect)
