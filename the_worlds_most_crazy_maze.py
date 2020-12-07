import random

obstacles = []

def generate_obstacles():
    global obstacles
    for x in range(-80,-35,4):
        obstacles.append((x,156))
    for y in range(152,-100,-4):
        obstacles.append((-80,y))
    for y in range(-112,-160,-4):
        obstacles.append((-80,y))
    for x in range(-80,-10,4):
        obstacles.append((x,-160))
    for y in range(-160,-60,4):
        obstacles.append((-8,y))
    for x in range(-76,-50,4):
        obstacles.append((x,20))
    for x in range(-16,76,4):
        obstacles.append((x,156))
    for y in range(156,-80,-4):
        obstacles.append((76,y))
    for y in range(-68,-148,-4):
        obstacles.append((76,y))
    for x in range(76,10,-4):
        obstacles.append((x,-160))
    for x in range(-46,30,4):
        obstacles.append((x,-10))
    for y in range(-10,-100,-4):
        obstacles.append((-46,y))
    for y in range(72,-142,-4):
        obstacles.append((30,y))
    for x in range(-46,36,4):
        obstacles.append((x,106))
    for y in range(-10,106,4):
        obstacles.append((-8,y))
    for x in range(34,60,4):
        obstacles.append((x,72))
    for y in range(72,-158,-4):
        obstacles.append((62,y))
    return obstacles
    


def get_obstacles():
    '''
    This returns the function that generates the boundry
    '''
    return generate_obstacles()

def is_position_blocked(x,y):
    '''
    This function checks if the position you want to go to has a obstacle or if there is no obstacle in the way
    '''
    global obstacles
    for i in obstacles:
        if i[0] <= x <= i[0]+4 and i[1] <= y <= i[1]+4:
            return True
    return False            


def is_path_blocked(x1,y1,x2,y2):
    if x1 > x2 :
        x1,x2 = x2,x1

    if y1 > y2 :
        y1,y2 = y2,y1

    if x1==x2:
        for y in range(y1,y2+1):
            if is_position_blocked(x1,y):
                return True
    
    if y1==y2:
        for x in range(x1,x2+1):
            if is_position_blocked(x,y1):
                return True
    return False
