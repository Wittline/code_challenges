
#https://leetcode.com/problems/robot-bounded-in-circle/

def isRobotBounded(instructions):
    dirX, dirY = 0, 1
    x, y = 0, 0

    for ins in instructions:
        if ins == 'G':
            x, y = x + dirX, y + dirY
        elif ins == 'L':
            dirX, dirY = -1*dirY, dirX 
        else:
            dirX, dirY = dirY, -1*dirX

    return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)