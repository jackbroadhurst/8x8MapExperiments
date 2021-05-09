import numpy as np
import pygame
pygame.init()
n = 8
colors = [(51, 51, 51) for i in range(n ** 2)]
reward = np.zeros((n, n))
terminals = []
scrx = n * 100
scry = n * 100
screen = pygame.display.set_mode((scrx, scry))
font = pygame.font.SysFont('arial',100)

def layout(current_position, colors):
    colors[0] = (0, 0, 255)
    c = 0
    for i in range(0, scrx, 100):
        for j in range(0, scry, 100):
            pygame.draw.rect(screen, (255, 255, 255), (j, i, j + 100, i + 100), 0)
            pygame.draw.rect(screen, colors[c], (j + 10, i + 10, j + 95, i + 95), 0)
            c += 1
            pygame.draw.circle(screen, (255, 255, 0), (current_position[1] * 100 + 50, current_position[0] * 100 + 50), 30, 0)


class Mazes():
    def __init__(self):
        self.colors = colors
        self.terminals = terminals
        self.reward = reward

    def reset(self):
        global colors
        for i in range(n):
            for j in range(n):
                reward[(i, j)] = 0
        colors = [(51, 51, 51) for i in range(n ** 2)]
        terminals.clear()

    def getMaze1Rewards(self):
        reward[0, 1] = -10
        reward[0,2] = -10
        reward[0,3] = -10
        reward[0,4] = -10
        reward[0,5] = -10
        reward[0,7] = -10
        reward[1,1] = -10
        reward[1,5] = -10
        reward[1,7] = -10
        reward[2,3] = -10
        reward[3,0] = -10
        reward[3,1] = -10
        reward[3,2] = -10
        reward[3,3] = -10
        reward[3,4] = -10
        reward[3,6] = -10
        reward[3,7] = -10
        reward[4,3] = -10
        reward[5,1] = -10
        reward[5,3] = -10
        reward[5,5] = -10
        reward[5,6] = -10
        reward[5,7] = -10
        reward[7,0] = -10
        reward[7,1] = -10
        reward[7,3] = -10
        reward[7,4] = -10
        reward[7,6] = -10
        reward[7,7] = 10
        return reward

    def getMaze1Colors(self):
        colors[n * 0 + 1] = (255, 0, 0)
        colors[n * 0 + 2] = (255, 0, 0)
        colors[n * 0 + 3] = (255, 0, 0)
        colors[n * 0 + 4] = (255, 0, 0)
        colors[n * 0 + 5] = (255, 0, 0)
        colors[n * 0 + 7] = (255, 0, 0)
        colors[n * 1 + 1] = (255, 0, 0)
        colors[n * 1 + 5] = (255, 0, 0)
        colors[n * 1 + 7] = (255, 0, 0)
        colors[n * 2 + 3] = (255, 0, 0)
        colors[n * 3 + 0] = (255, 0, 0)
        colors[n * 3 + 1] = (255, 0, 0)
        colors[n * 3 + 2] = (255, 0, 0)
        colors[n * 3 + 3] = (255, 0, 0)
        colors[n * 3 + 4] = (255, 0, 0)
        colors[n * 3 + 6] = (255, 0, 0)
        colors[n * 3 + 7] = (255, 0, 0)
        colors[n * 4 + 3] = (255, 0, 0)
        colors[n * 5 + 1] = (255, 0, 0)
        colors[n * 5 + 3] = (255, 0, 0)
        colors[n * 5 + 5] = (255, 0, 0)
        colors[n * 5 + 6] = (255, 0, 0)
        colors[n * 5 + 7] = (255, 0, 0)
        colors[n * 7 + 0] = (255, 0, 0)
        colors[n * 7 + 1] = (255, 0, 0)
        colors[n * 7 + 3] = (255, 0, 0)
        colors[n * 7 + 4] = (255, 0, 0)
        colors[n * 7 + 6] = (255, 0, 0)
        colors[n * 7 + 7] = (0, 255, 0)
        return colors

    def getMaze1altRewards(self):
        reward[0, 1] = -10
        reward[0, 2] = -10
        reward[0, 3] = -10
        reward[0, 4] = -10
        reward[0, 5] = -10
        reward[0, 7] = -10
        reward[1, 1] = -10
        reward[1, 5] = -10
        reward[1, 7] = -10
        reward[2, 3] = -10
        reward[3, 0] = -10
        reward[3, 1] = -10
        reward[3, 2] = -10
        reward[3, 3] = -10
        reward[3, 4] = -10
        reward[3, 6] = -10
        reward[3, 7] = -10
        reward[4, 3] = -10
        reward[5, 1] = -10
        reward[5, 3] = -10
        reward[5, 5] = -10
        reward[5, 6] = -10
        reward[5, 7] = -10
        reward[7, 0] = -10
        reward[7, 1] = -10
        reward[7, 3] = -10
        reward[7, 4] = -10
        reward[7, 6] = -10
        reward[0, 6] = 10
        return reward

    def getMaze1altColors(self):
        colors[n * 0 + 1] = (255, 0, 0)
        colors[n * 0 + 2] = (255, 0, 0)
        colors[n * 0 + 3] = (255, 0, 0)
        colors[n * 0 + 4] = (255, 0, 0)
        colors[n * 0 + 5] = (255, 0, 0)
        colors[n * 0 + 7] = (255, 0, 0)
        colors[n * 1 + 1] = (255, 0, 0)
        colors[n * 1 + 5] = (255, 0, 0)
        colors[n * 1 + 7] = (255, 0, 0)
        colors[n * 2 + 3] = (255, 0, 0)
        colors[n * 3 + 0] = (255, 0, 0)
        colors[n * 3 + 1] = (255, 0, 0)
        colors[n * 3 + 2] = (255, 0, 0)
        colors[n * 3 + 3] = (255, 0, 0)
        colors[n * 3 + 4] = (255, 0, 0)
        colors[n * 3 + 6] = (255, 0, 0)
        colors[n * 3 + 7] = (255, 0, 0)
        colors[n * 4 + 3] = (255, 0, 0)
        colors[n * 5 + 1] = (255, 0, 0)
        colors[n * 5 + 3] = (255, 0, 0)
        colors[n * 5 + 5] = (255, 0, 0)
        colors[n * 5 + 6] = (255, 0, 0)
        colors[n * 5 + 7] = (255, 0, 0)
        colors[n * 7 + 0] = (255, 0, 0)
        colors[n * 7 + 1] = (255, 0, 0)
        colors[n * 7 + 3] = (255, 0, 0)
        colors[n * 7 + 4] = (255, 0, 0)
        colors[n * 7 + 6] = (255, 0, 0)
        colors[n * 0 + 6] = (0, 255, 0)
        return colors

    def getMaze1Terminals(self):
        terminals.append(n * 0 + 1)
        terminals.append(n * 0 + 2)
        terminals.append(n * 0 + 3)
        terminals.append(n * 0 + 4)
        terminals.append(n * 0 + 5)
        terminals.append(n * 0 + 7)
        terminals.append(n * 1 + 1)
        terminals.append(n * 1 + 5)
        terminals.append(n * 1 + 7)
        terminals.append(n * 2 + 3)
        terminals.append(n * 3 + 0)
        terminals.append(n * 3 + 1)
        terminals.append(n * 3 + 2)
        terminals.append(n * 3 + 3)
        terminals.append(n * 3 + 4)
        terminals.append(n * 3 + 6)
        terminals.append(n * 3 + 7)
        terminals.append(n * 4 + 3)
        terminals.append(n * 5 + 1)
        terminals.append(n * 5 + 3)
        terminals.append(n * 5 + 5)
        terminals.append(n * 5 + 6)
        terminals.append(n * 5 + 7)
        terminals.append(n * 7 + 0)
        terminals.append(n * 7 + 1)
        terminals.append(n * 7 + 3)
        terminals.append(n * 7 + 4)
        terminals.append(n * 7 + 6)
        return terminals

    def getMaze2Rewards(self):
        reward[0, 4] = -10
        reward[1, 0] = -10
        reward[1, 1] = -10
        reward[1, 2] = -10
        reward[1, 4] = -10
        reward[1, 5] = -10
        reward[1, 6] = -10
        reward[2, 1] = -10
        reward[2, 4] = -10
        reward[3, 1] = -10
        reward[3, 2] = -10
        reward[3, 4] = -10
        reward[3, 5] = -10
        reward[3, 7] = -10
        reward[4, 2] = -10
        reward[4, 4] = -10
        reward[5, 0] = -10
        reward[5, 2] = -10
        reward[5, 6] = -10
        reward[6, 0] = -10
        reward[6, 4] = -10
        reward[6, 6] = -10
        reward[7, 1] = -10
        reward[7, 0] = -10
        reward[7, 2] = -10
        reward[7, 3] = -10
        reward[7, 4] = -10
        reward[7, 6] = -10
        return reward

    def getMaze2Colors(self):
        colors[n * 0 + 4] = (255, 0, 0)
        colors[n * 1 + 0] = (255, 0, 0)
        colors[n * 1 + 1] = (255, 0, 0)
        colors[n * 1 + 2] = (255, 0, 0)
        colors[n * 1 + 4] = (255, 0, 0)
        colors[n * 1 + 5] = (255, 0, 0)
        colors[n * 1 + 6] = (255, 0, 0)
        colors[n * 2 + 1] = (255, 0, 0)
        colors[n * 2 + 4] = (255, 0, 0)
        colors[n * 3 + 1] = (255, 0, 0)
        colors[n * 3 + 2] = (255, 0, 0)
        colors[n * 3 + 4] = (255, 0, 0)
        colors[n * 3 + 5] = (255, 0, 0)
        colors[n * 3 + 7] = (255, 0, 0)
        colors[n * 4 + 2] = (255, 0, 0)
        colors[n * 4 + 4] = (255, 0, 0)
        colors[n * 5 + 0] = (255, 0, 0)
        colors[n * 5 + 2] = (255, 0, 0)
        colors[n * 5 + 6] = (255, 0, 0)
        colors[n * 6 + 0] = (255, 0, 0)
        colors[n * 6 + 4] = (255, 0, 0)
        colors[n * 6 + 6] = (255, 0, 0)
        colors[n * 7 + 1] = (255, 0, 0)
        colors[n * 7 + 0] = (255, 0, 0)
        colors[n * 7 + 2] = (255, 0, 0)
        colors[n * 7 + 3] = (255, 0, 0)
        colors[n * 7 + 4] = (255, 0, 0)
        colors[n * 7 + 6] = (255, 0, 0)
        colors[n * 7 + 7] = (0, 255, 0)

        return colors

    def getMaze2Terminals(self):
        terminals.append(n * 0 + 4)
        terminals.append(n * 1 + 0)
        terminals.append(n * 1 + 1)
        terminals.append(n * 1 + 2)
        terminals.append(n * 1 + 4)
        terminals.append(n * 1 + 5)
        terminals.append(n * 1 + 6)
        terminals.append(n * 2 + 1)
        terminals.append(n * 2 + 4)
        terminals.append(n * 3 + 1)
        terminals.append(n * 3 + 2)
        terminals.append(n * 3 + 4)
        terminals.append(n * 3 + 5)
        terminals.append(n * 3 + 7)
        terminals.append(n * 4 + 2)
        terminals.append(n * 4 + 4)
        terminals.append(n * 5 + 0)
        terminals.append(n * 5 + 2)
        terminals.append(n * 5 + 6)
        terminals.append(n * 6 + 0)
        terminals.append(n * 6 + 4)
        terminals.append(n * 6 + 6)
        terminals.append(n * 7 + 1)
        terminals.append(n * 7 + 0)
        terminals.append(n * 7 + 2)
        terminals.append(n * 7 + 3)
        terminals.append(n * 7 + 4)
        terminals.append(n * 7 + 6)
        return terminals