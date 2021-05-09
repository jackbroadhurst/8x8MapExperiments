import pandas
#from mazes import *
from time import time,sleep
from numpy import savetxt
from random import randint as r
import random
import numpy as np
from random import randint as r
import pygame
import random
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

    def Random_Maze(self):
        penalities = 15
        while penalities != 0:
            i = r(0, n - 1)
            j = r(0, n - 1)
            if reward[i, j] == 0 and [i, j] != [0, 0] and [i, j] != [n - 1, n - 1]:
                reward[i, j] = -1
                penalities -= 1
                colors[n * i + j] = (255, 0, 0)
                terminals.append(n * i + j)

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
        reward[7, 7] = 10
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




path1 = 'C:/Users/Jack/PycharmProjects/QGame/PROPER8x8DATA/'
path5 = '.csv'
maze1 = Mazes()
maze1alt = Mazes()
maze2 = Mazes()


def select_action(current_state):
    global current_position, epsilon
    possible_actions = []
    if np.random.uniform(0, 1) < epsilon:  # exploration
        global ModeFlag
        if current_position[0] != 0:
            possible_actions.append("up")
        if current_position[0] != n - 1:
            possible_actions.append("down")
        if current_position[1] != 0:
            possible_actions.append("left")
        if current_position[1] != n - 1:
            possible_actions.append("right")
        action = actions[possible_actions[r(0, len(possible_actions) - 1)]]
        ModeFlag = True
    else:  # Use Q table
        minQ = np.min(Q[current_state])
        if current_position[0] != 0:  # up
            possible_actions.append(Q[current_state, 0])
        else:
            possible_actions.append(minQ - 100)
        if current_position[0] != n - 1:  # down
            possible_actions.append(Q[current_state, 1])
        else:
            possible_actions.append(minQ - 100)
        if current_position[1] != 0:  # left
            possible_actions.append(Q[current_state, 2])
        else:
            possible_actions.append(minQ - 100)
        if current_position[1] != n - 1:  # right
            possible_actions.append(Q[current_state, 3])
        else:
            possible_actions.append(minQ - 100)
        action = random.choice([i for i, a in enumerate(possible_actions) if a == max(
            possible_actions)])
        ModeFlag = False
    return action


def epoch(terminals, reward):
    global current_position, epsilon, its, wins, oldwins, safesteps, steps, step, ouches
    current_state = states[(current_position[0], current_position[1])]
    action = select_action(current_state)
    if action == 0:  # move up
        current_position[0] -= 1
    elif action == 1:  # move down
        current_position[0] += 1
    elif action == 2:  # move left
        current_position[1] -= 1
    elif action == 3:  # move right
        current_position[1] += 1
    new_state = states[(current_position[0], current_position[1])]
    if new_state not in terminals:
        Q[current_state, action] += alpha * (
                    reward[current_position[0], current_position[1]] + gamma * (np.max(Q[new_state])) - Q[
                current_state, action])
        step += 1
        safesteps += 1
        if current_position == [7, 7]:
            wins += 1
            updateStacks()
            current_position = [0, 0]
            its += 1
            step = 0
            safesteps = 0
            ouches = 0
            if epsilon > 0:
                epsilon -= EDegrade
    else:
        Q[current_state, action] += alpha * (
                    reward[current_position[0], current_position[1]] + gamma * (np.max(Q[new_state])) - Q[
                current_state, action])
        step += 1
        ouches += 1
    outState1.append(place)
    outStep1.append(step)
    outWins1.append(wins)


def epochGoalChange(terminals, reward):
    global current_position, epsilon, its, oldwins, wins, safesteps, steps, step, last_position, ouches
    current_state = states[(current_position[0], current_position[1])]
    action = select_action(current_state)
    if action == 0:  # move up
        current_position[0] -= 1
    elif action == 1:  # move down
        current_position[0] += 1
    elif action == 2:  # move left
        current_position[1] -= 1
    elif action == 3:  # move right
        current_position[1] += 1
    new_state = states[(current_position[0], current_position[1])]
    if new_state not in terminals:
        Q[current_state, action] += alpha * (
                reward[current_position[0], current_position[1]] + gamma * (np.max(Q[new_state])) - Q[
            current_state, action])
        step += 1
        safesteps += 1
        if wins < 30 and current_position == [7, 7]:
            wins += 1
            updateStacks()
            its += 1
            step = 0
            ouches = 0
            current_position = [0, 0]
            if epsilon > 0:
                epsilon -= EDegrade
        if wins >= 30 and current_position == [7, 7]:
            oldwins += 1
        if wins >= 30 and current_position == [0, 6]:
            wins += 1
            updateStacks()
            oldwins = 0
            its += 1
            step = 0
            ouches = 0
            current_position = [0, 0]
            if epsilon > 0:
                epsilon -= EDegrade
    else:
        Q[current_state, action] += alpha * (
                reward[current_position[0], current_position[1]] + gamma * (np.max(Q[new_state])) - Q[
            current_state, action])
        step += 1
        ouches += 1
    outState1.append(place)
    outStep1.append(step)
    outWins1.append(wins)

def updateStacks():
    outMoves.append(place)
    outSteps.append(step)
    outIts.append(its)
    outWins.append(wins)
    outMode.append(ModeFlag)
    outOuches.append(ouches)
    outOldWins.append(oldwins)
    outSafeSteps.append(safesteps)
    outEpsilon.append(epsilon)
    outTest.append(test)

run1 = True
run2 = False
run3 = False
run4 = False
run5 = False
for Experiment in range (0,5,1):
    if Experiment == 0:
        path2 = 'Map1/'
        run1 = True
        run2 = False
        run3 = False
        run4 = False
        run5 = False
    if Experiment == 1:
        path2 = 'Map2/'
        run1 = False
        run2 = True
        run3 = False
        run4 = False
        run5 = False
    if Experiment == 2:
        path2 = 'MapCQReset/'
        run1 = False
        run2 = False
        run3 = True
        run4 = False
        run5 = False
    if Experiment == 3:
        path2 = 'GoalC/'
        run1 = False
        run2 = False
        run3 = False
        run4 = True
        run5 = False
    if Experiment == 4:
        path2 = "MapC/"
        run1 = False
        run2 = False
        run3 = False
        run4 = False
        run5 = True
    for Eps in range(0,5,1):
        if Eps == 0:
            epsilon = 0
            baseE = 0
            path3 = 'E0_'
        if Eps == 1:
            epsilon = 0.25
            baseE = 0.25
            EDegrade = 0.0125
            path3 = 'E025_'
        if Eps == 2:
            epsilon = 1
            EDegrade = 0.05
            baseE = 1
            path3 = 'E1_'
        if Eps == 3:
            epsilon = 0.5
            EDegrade = 0.025
            baseE = 0.5
            path3 = "E05_"
        if Eps == 4:
            epsilon = 0.75
            EDegrade = 0.0375
            baseE = 0.75
            path3 = "E075_"
        for test in range(0,50,1):
            maze1.reset()
            ds = str(test)
            path4 = ds
            safesteps = 0
            step = 0
            its = 0
            wins = 0
            oldwins = 0
            ouches = 0
            state = 0
            steps = np.zeros((2,1))
            outTest= []
            outSafeSteps = []
            outMode = []
            outSteps = []
            outIts = []
            outMoves = []
            outWins = []
            outOldWins = []
            outOuches = []
            outState = []
            outState1 = []
            outWins1 = []
            outStep1 = []
            outEpsilon = []
            # for i in range(n):
            #     for j in range(n):
            #         reward[i, j] = 1
            ModeFlag = False

            Q = np.zeros((n ** 2, 4))
            actions = {"up": 0, "down": 1, "left": 2, "right": 3}
            states = {}
            goal = n ** 2

            k = 0
            for i in range(n):
                for j in range(n):
                    states[(i, j)] = k
                    k += 1

            alpha = 0.6
            gamma = 0.7


            current_position = [0, 0]

            PReset = True
            ##Map 1
            while run1:
                layout(current_position, maze1.getMaze1Colors())
                pygame.display.flip()
                place = states[(current_position[0], current_position[1])]
                epoch(maze1.getMaze1Terminals(), maze1.getMaze1Rewards())
                print("map1")
                print("TEST: ", test, "Starting Epsilon: ", baseE, "Epsilon: ", epsilon, "iteration: ", its, "movement: ", current_position, "Wins: ", wins, "Ouches: ", ouches)
                if wins == 30:
                    QPath = path1 + path2 + 'Q/' + path3 + path4 + path5
                    np.savetxt(QPath, Q, delimiter = ',')
                    rpath = path1 + path2 + "R/" + path3 + path4 + path5
                    np.savetxt(rpath, reward, delimiter=',')
                    break
            ##Map 2
            while run2:
                layout(current_position, maze2.getMaze2Colors())
                pygame.display.flip()
                place = states[(current_position[0], current_position[1])]
                epoch(maze2.getMaze2Terminals(), maze2.getMaze2Rewards())
                print("map2")
                print("TEST: ", test, "Starting Epsilon: ", baseE, "Epsilon: ", epsilon, "iteration: ", its, "movement: ", current_position, "Wins: ", wins, "Ouches: ", ouches)
                if wins == 30:
                    QPath = path1 + path2 + 'Q/' + path3 + path4 + path5
                    np.savetxt(QPath, Q, delimiter = ',')
                    rpath = path1 + path2 + "R/" + path3 + path4 + path5
                    np.savetxt(rpath, reward, delimiter=',')
                    break
            ##Map Change QReset
            while run3:
                if 30 < wins < 60:
                    while PReset:
                        epsilon = baseE
                        QPath = path1 + path2 + 'Q/' + "mid" + path3 + path4 + path5
                        np.savetxt(QPath, Q, delimiter=',')
                        Q = np.zeros((n ** 2, 4))
                        rpath = path1 + path2 + "R/" + "mid" + path3 + path4 + path5
                        np.savetxt(rpath, reward, delimiter=',')
                        PReset = False
                    maze1.reset()
                    layout(current_position, maze2.getMaze2Colors())
                    pygame.display.flip()
                    place = states[(current_position[0], current_position[1])]
                    epoch(maze2.getMaze2Terminals(), maze2.getMaze2Rewards())
                    print("mapchange reset: maze 2")
                    print("TEST: ", test, "Starting Epsilon: ", baseE, "Epsilon: ", epsilon, "iteration: ", its,
                          "movement: ", current_position, "Wins: ", wins, "Ouches: ", ouches)
                else:
                    layout(current_position, maze1.getMaze1Colors())
                    pygame.display.flip()
                    place = states[(current_position[0], current_position[1])]
                    epoch(maze1.getMaze1Terminals(), maze1.getMaze1Rewards())
                    print("mapchange reset: maze 1")
                    print("TEST: ", test, "Starting Epsilon: ", baseE, "Epsilon: ", epsilon, "iteration: ", its,
                         "movement: ", current_position, "Wins: ", wins, "Ouches: ", ouches)
                if wins == 60:
                    QPath = path1 + path2 + "Q/" + path3 + path4 + 'Q' + path5
                    np.savetxt(QPath, Q, delimiter=',')
                    rpath = path1 + path2 + "R/" + path3 + path4 + path5
                    np.savetxt(rpath, reward, delimiter=',')
                    break
            ##Goal Change
            while run4:
                if step == 50000:
                    break
                if baseE == 0:
                    break
                if wins < 30:
                    layout(current_position, maze1.getMaze1Colors())
                    pygame.display.flip()
                    place = states[(current_position[0], current_position[1])]
                    epochGoalChange(maze1.getMaze1Terminals(), maze1.getMaze1Rewards())
                    print("Goal Change: Goal 1")
                    print("TEST: ", test, "Starting Epsilon: ", baseE, "Epsilon: ", epsilon, "iteration: ", its,"movement: ", current_position, "Wins: ", wins, "Ouches: ", ouches)
                if 30 <= wins < 60:
                    if PReset:
                        QPath = path1 + path2 + 'Q/' + "mid" + path3 + path4 + path5
                        np.savetxt(QPath, Q, delimiter=',')
                        epsilon = baseE
                        rpath = path1 + path2 + "R/" + "mid" + path3 + path4 + path5
                        np.savetxt(rpath, reward, delimiter=',')
                        PReset = False
                    maze1.reset()
                    reward[7, 7] = 0
                    layout(current_position, maze1alt.getMaze1altColors())
                    pygame.display.flip()
                    place = states[(current_position[0], current_position[1])]
                    epochGoalChange(maze1alt.getMaze1Terminals(), maze1alt.getMaze1altRewards())
                    print("Goal Change: Goal 2")
                    print("TEST: ", test, "Starting Epsilon: ", baseE, "Epsilon: ", epsilon, "iteration: ", its,"movement: ", current_position, "Wins: ", wins, "Ouches: ", ouches)
                if wins == 60:
                    QPath = path1 + path2 + "Q/" + path3 + path4 + 'Q' + path5
                    np.savetxt(QPath, Q, delimiter=',')
                    rpath = path1 + path2 + "R/" + path3 + path4 + path5
                    np.savetxt(rpath, reward, delimiter=',')
                    break
            ##Map Change
            while run5:
                if baseE == 0:
                    break
                if 30 < wins < 60:
                    while PReset:
                        epsilon = baseE
                        QPath = path1 + path2 + 'Q/' + "mid" + path3 + path4 + path5
                        np.savetxt(QPath, Q, delimiter=',')
                        rpath = path1 + path2 + "R/" + "mid" + path3 + path4 + path5
                        np.savetxt(rpath, reward, delimiter=',')
                        PReset = False
                    maze1.reset()
                    layout(current_position, maze2.getMaze2Colors())
                    pygame.display.flip()
                    place = states[(current_position[0], current_position[1])]
                    epoch(maze2.getMaze2Terminals(), maze2.getMaze2Rewards())
                    print("mapchange: maze 2")
                    print("TEST: ", test, "Starting Epsilon: ", baseE, "Epsilon: ", epsilon, "iteration: ", its,"movement: ", current_position, "Wins: ", wins, "Ouches: ", ouches)
                    if step == 30000:
                        QPath = path1 + path2 + "Q/" + path3 + path4 + 'Q' + path5
                        np.savetxt(QPath, Q, delimiter=',')
                        rpath = path1 + path2 + "R/" + path3 + path4 + path5
                        np.savetxt(rpath, reward, delimiter=',')
                        break
                else:
                    layout(current_position, maze1.getMaze1Colors())
                    pygame.display.flip()
                    place = states[(current_position[0], current_position[1])]
                    epoch(maze1.getMaze1Terminals(), maze1.getMaze1Rewards())
                    print("mapchange: maze 1")
                    print("TEST: ", test, "Starting Epsilon: ", baseE, "Epsilon: ", epsilon, "iteration: ", its, "movement: ", current_position, "Wins: ", wins, "Ouches: ", ouches)
                if wins == 60:
                    QPath = path1 + path2 + "Q/" + path3 + path4 + 'Q' + path5
                    np.savetxt(QPath, Q, delimiter=',')
                    rpath = path1 + path2 + "R/" + path3 + path4 + path5
                    np.savetxt(rpath, reward, delimiter=',')
                    break
            path = path1 + path2 + path3 + path5
            pathM = path1 + path2 + "M/" + path3 + path5
            dataMoves = pandas.DataFrame({"Wins": outWins1, "Step": outStep1, "place": outState1})
            data = pandas.DataFrame({"Test": outTest, "iteration ": outIts, "Step": outSteps, "Move": outMoves, "Ouches": outOuches,
                                     "Safe Steps": outSafeSteps, "Wins": outWins, "Old Wins": outOldWins, "Exploration?": outMode,
                                     "Epsilon": outEpsilon})
            dataMoves.to_csv(pathM, mode = 'a')
            data.to_csv(path, mode='a')
            epsilon = baseE
pygame.quit()