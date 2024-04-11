import pygame
import random
import time

class TriSelection():
    def __init__(self):
        self.black = (0,0,0)

    def text_not_align(self,font, text_size, text_content, color, x, y):
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.Window.blit(text, text_rect)

    def trier(self,list):
        start_time = time.perf_counter()
        for i in range(len(list)-1):
            i_min = i
            for j in range(i+1, len(list)):
                if list[j] < list[i_min]:
                    i_min = j
            list[i], list[i_min] = list[i_min], list[i]
        end_time = time.perf_counter()
        print(f"Temps d'exécution du tri : {end_time - start_time} secondes")
        self.text_not_align(None,12,end_time - start_time,self.black,30,30)
        return list

class InterfaceGraphique:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.background_color = (255, 255, 255)
        self.rect_width = 400
        self.rect_height = 400
        self.rect_x = (self.screen_width - self.rect_width) // 2
        self.rect_y = (self.screen_height - self.rect_height) // 2
        self.colors = [(random.randint(0, 255), 255, 255) for _ in range(400)]
        

    def draw_gradient(self):
        for i, color in enumerate(self.colors):
            pygame.draw.line(self.screen, color, (self.rect_x + i, self.rect_y), (self.rect_x + i, self.rect_y + self.rect_height), 10)

    def draw_button(self):
        pygame.draw.rect(self.screen, (200, 200, 200), (700, 550, 50, 40))
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Trier", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(700 + 50 // 2, 550 + 40 // 2))
        self.screen.blit(text_surface, text_rect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 700 <= mouse_pos[0] <= 750 and 550 <= mouse_pos[1] <= 590:
                        self.colors = TriSelection.trier(self.colors)
                        self.screen.fill(self.background_color)
                        pygame.draw.rect(self.screen, (200, 200, 200), (self.rect_x, self.rect_y, self.rect_width, self.rect_height))
                        self.draw_gradient()
                        self.draw_button()
                        pygame.display.flip()

            self.screen.fill(self.background_color)
            pygame.draw.rect(self.screen, (200, 200, 200), (self.rect_x, self.rect_y, self.rect_width, self.rect_height))
            self.draw_gradient()
            self.draw_button()
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    pygame.init()
    interface = InterfaceGraphique(800, 600)
    interface.run()
