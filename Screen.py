import pygame
import math
from Element import Element

class Screen(Element):
    def __init__(self):
        Element.__init__()
        pygame.init()
    
    def draw_vector_circle(self,center, radius, num_samples):
        for i in range(num_samples):
            angle = i * (2 * math.pi / num_samples)
            x = center[0] + radius * math.cos(angle)
            y = center[1] + radius * math.sin(angle)
            color = (int(255 * math.cos(angle)), int(255 * math.sin(angle)), 128)
            pygame.draw.circle(self.Window, color, (int(x), int(y)), 3)

    def run(self):
        clock = pygame.time.Clock()
        while running:
            running = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.Window.fill(self.color)

            self.draw_vector_circle((self.width // 2, self.height // 2), 200, 100)

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()
test = Screen()
test.run()