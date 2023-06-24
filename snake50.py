import pygame
import pygame_menu
from pygame.locals import *
import time
import random



SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

class Banana:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/benanaa.jpg").convert()
        self.x = 120
        self.y = 120

    def rasm(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,15)*SIZE
        self.y = random.randint(1,17)*SIZE

class SNAKE:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/block.jpg").convert()
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def harekat(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]


        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.rasm()

    def rasm(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("snake50")

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode((1000, 700))
        self.SNAKE = SNAKE(self.surface)
        self.SNAKE.rasm()
        self.banana = Banana(self.surface)
        self.banana.rasm()

    def play_background_music(self):
        pygame.mixer.music.load('resources/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound("resources/crash.mp3")
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound("resources/ding.mp3")

        pygame.mixer.Sound.play(sound)

    def reset(self):
        self.SNAKE = SNAKE(self.surface)
        self.banana = Banana(self.surface)

    def barkhord(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        bg = pygame.image.load("resources/back.jpg")
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()
        self.SNAKE.harekat()
        self.banana.rasm()
        self.namayesh_emtiaz_and_creator()
        pygame.display.flip()


        if self.barkhord(self.SNAKE.x[0], self.SNAKE.y[0], self.banana.x, self.banana.y):
            self.play_sound("ding")
            self.SNAKE.increase_length()
            self.banana.move()

        for i in range(3, self.SNAKE.length):
            if self.barkhord(self.SNAKE.x[0], self.SNAKE.y[0], self.SNAKE.x[i], self.SNAKE.y[i]):
                self.play_sound('crash')
                raise "barkhord !!!"

    def namayesh_emtiaz_and_creator(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"SCORE: {self.SNAKE.length}",True,(200,0,200))
        author = font.render(f"craete by Mahdi Farmahini Farahani",True,(0,0,200))
        self.surface.blit(score,(870,10))

    def namayesh_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.SNAKE.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.SNAKE.move_left()

                        if event.key == K_RIGHT:
                            self.SNAKE.move_right()

                        if event.key == K_UP:
                            self.SNAKE.move_up()

                        if event.key == K_DOWN:
                            self.SNAKE.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.namayesh_game_over()
                pause = True
                self.reset()

            time.sleep(.25)
pygame.init()
surface = pygame.display.set_mode((900, 400))



def start_the_game():
    if __name__ == '__main__':
        game = Game()
        game.run()

def back():
    menu.mainloop(surface)


def credit():
    menu = pygame_menu.Menu('Created By Mahdi Farmahini Farahani', 800, 400)
    menu.add.button('back', back)
    menu.mainloop(surface)



menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('play', start_the_game)
menu.add.button('credit', credit)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
