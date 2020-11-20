import pygame
import random
from pygame.locals import *
import sys
import os


pygame.init()
pygame.time.set_timer(USEREVENT, 2000)
screen = pygame.display.set_mode((500, 700))
done = False
clock = pygame.time.Clock()


image_car = pygame.image.load("images/car01.png")
image_car = pygame.transform.scale(image_car, (40, 80))
image_obstacle = pygame.image.load("images/car04.png")
image_obstacle = pygame.transform.scale(image_obstacle, (40, 80))
image_start = pygame.image.load("images/start.png")
image_start = pygame.transform.scale(image_start, (96, 40))
image_lawn = pygame.image.load('images/lawn.jpg')
image_lawn = pygame.transform.scale(image_lawn, (96, 700))
image_coin = pygame.image.load('images/oil1.png')
image_coin = pygame.transform.scale(image_coin, (30, 30))

road_speed = 0
place = [112, 176, 240, 304, 368]
"""lateral_left_line = 
lateral_right_line = """


class Car:
    def __init__(self, x, y):
        print(x, '-------------')
        self.x = x
        self.y = y


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Score:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def crash():
    python = sys.executable
    os.execl(python, python, * sys.argv)


blocks = []
scores = []

block_speed = 6
num_of_obstacles = []
num_of_coin = []
direction = ""
money = 0


car = Car(place[2], 500)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if 0 < car.x < 98:
            car.x += 6
        car.x -= 5
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if 380 < car.x < 700:
            car.x -= 6
        car.x += 5

    k = pygame.time.get_ticks() % 2000

    screen.fill((65, 65, 65))

    for i in range(163, 419, 64):
        for j in range(0, 720, 20):
            if ((j+road_speed+10) % 700-(j+road_speed) % 700) < 0:
                pygame.draw.line(screen, (255, 255, 255), (i, 0), (i, (j+road_speed+10) % 700), 3)
            else:
                pygame.draw.line(screen, (255, 255, 255), (i, (j+road_speed) % 700), (i, (j+road_speed+10) % 700), 3)
    pygame.draw.line(screen, (255, 255, 255), (98, 0), (98, 700), 3)
    pygame.draw.line(screen, (255, 255, 255), (418, 0), (418, 700), 3)
    screen.blit(image_lawn, (0, 0))
    screen.blit(image_lawn, (420, 0))
    screen.blit(image_car, (car.x, car.y))
    screen.blit(image_start, (212, road_speed))

    if 1300 < k < 1340:
        obstacle_line_appear = random.randint(0, 4)
        coin_line_appear = random.randint(0, 4)

        num_of_obstacles.append(obstacle_line_appear)
        num_of_coin.append(coin_line_appear)

        num_of_coin = list(dict.fromkeys(num_of_coin))
        num_of_obstacles = list(dict.fromkeys(num_of_obstacles))

        for i in num_of_obstacles:
            block = Block(place[i], 0)
            blocks.append(block)

        for i in num_of_coin:
            score = Score(place[i], 0)
            scores.append(score)  

    for block in blocks:
        screen.blit(image_obstacle, (block.x, block.y))
        block.y += block_speed
        if block.y > 700:
            blocks.remove(block)
            num_of_obstacles = []
        
        if (block.x < car.x < block.x + 40 and block.y < car.y < block.y + 80) or ((car.x + 40 > block.x and car.x+40 <
                                                                                    block.x + 40) and block.y < car.y <
                                                                                   block.y + 80):
            print("CRASH")
            print(block.x, car.x, block.y, car.y)
            road_speed = 0
            block_speed = 0
            crash()
    
    for score in scores:
        screen.blit(image_coin, (score.x, score.y))
        score.y += block_speed
        if score.y > 700:
            scores.remove(score)
            a = []

        if ((score.x <= car.x <= score.x + 30) and (car.y <= car.y <= score.y + 30)) or ((score.x <= car.x + 40 <=
                                                                                          score.x + 30) and score.y <
                                                                                         car.y <= score.y + 30):
            #print("\n++money!!!!!\n")
            money += 1
            scores.remove(score)
    """if (0 < car.x < 98) or (700 > car.x + 40 > 418):
        print("CRASH")
        road_speed = 0
        crash()"""

    road_speed += 4

    pygame.display.flip()
    clock.tick(40)
print(money)
