from searching_framework.utils import Problem
from searching_framework.informed_search import *

class Wanderer(Problem):

    def __init__(self, initial, goal):
        super().__init__(initial,goal)

    def successor(self, state):
        successors = {}

        px = state[0]
        py = state[1]

        b1x, b1y, b1d = state[2]
        b2x, b2y, b2d = state[3]

        # move box1
        if b1d == -1 and b1y>0:
            b1y-=1
        elif b1d == -1:
            b1y+=1
            b1d = 1
        elif b1d == 1 and b1y<5:
            b1y+=1
        elif b1d ==1:
            b1y-=1
            b1d = -1

        # move box2
        if b2d == -1 and b2y>0:
            b2y-=1
        elif b2d == -1:
            b2y+=1
            b2d = 1
        elif b2d == 1 and b2y<5:
            b2y+=1
        elif b2d ==1:
            b2y-=1
            b2d = -1

        obstacles = [(b1x,b1y), (b2x, b2y)]

        #move human

        if py < 5 and (px, py + 1) not in obstacles:
            successors['Up'] = (px, py + 1, (b1x, b1y, b1d), (b2x, b2y, b2d))

        if py > 0 and (px, py - 1) not in obstacles:
            successors['Down'] = (px, py - 1, (b1x, b1y, b1d), (b2x, b2y, b2d))

        # right
        if px < 7 and (px + 1,py) not in obstacles:
            successors['Right'] = (px +1, py, (b1x, b1y,b1d), (b2x,b2y,b2d))

        if px > 0 and (px - 1, py) not in obstacles:
            successors['Left'] = (px + 1, py, (b1x, b1y, b1d), (b2x, b2y, b2d))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]

    def h(self, node):
        return abs(node.state[0]-self.goal[0]) + abs(node.state[1]-self.goal[1])

if __name__ == "__main__":
    sx, sy = 0, 2
    ob1 = (2, 5, -1)
    ob2 = (5, 0, 1)
    goal = (7, 4)

    problem = Wanderer((sx, sy, ob1, ob2), goal)
    solution = astar_search(problem)
    print(solution.solution())