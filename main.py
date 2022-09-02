import random

height = random.randint(11,20)
width = random.randint(10,30)

def printScenary(scenery):
    colors = ["🟩","🟫","🟦"]
    for line in scenary:
        for chunk in line:
            print(colors[chunk -1], end="\t")
        print()

def createWorld():                                          
    scenary = [] 
    for _ in range(height):
        line = []
        if _ <= height - 12:
            for _ in range(width):
                line.append(3)
        else:
            for _ in range(width):
                line.append(0)
        scenary.append(line)
    return scenary

def createFloor(scenary):
    base_floor = 0
    limit_floor = [2,3,4]
    for i in range(width):
        if i == 0:
            sorted_number = random.choice(limit_floor)
            scenary[height - sorted_number][i] = 1
            base_floor = sorted_number
            for j in range(height - base_floor + 1, height):
                scenary[j][i] = 2
        else:
            sorted_ = random.choice([1,2,3])
            sorted_1 = sorted_ in [1]
            sorted_2 = sorted_ in [2]
            sorted_3 = sorted_ in [3]
            if sorted_1:
                new_base_floor = base_floor + 1
                if new_base_floor > 4:
                    base_floor = 4
                    scenary[height - 4][i] = 1
                    for j in range(height - base_floor + 1, height):
                        scenary[j][i] = 2
                else:
                    base_floor = new_base_floor
                    scenary[height - base_floor][i] = 1
                    for j in range(height - base_floor + 1, height):
                        scenary[j][i] = 2
            if sorted_2:
                scenary[height - base_floor][i] = 1
                for j in range(height - base_floor + 1, height):
                    scenary[j][i] = 2
            if sorted_3:
                new_base_floor = base_floor - 1
                if new_base_floor < 2:
                    base_floor = 2
                    scenary[height - 2][i] = 1
                    for j in range(height - base_floor + 1, height):
                        scenary[j][i] = 2
                else:
                    base_floor = new_base_floor
                    scenary[height - base_floor][i] = 1
                    for j in range(height - base_floor + 1, height):
                        scenary[j][i] = 2
              
scenary = createWorld()
createFloor(scenary)
printScenary(scenary)