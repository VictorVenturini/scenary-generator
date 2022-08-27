import random

height = random.choice([10,20])
width = random.choice([10,20])

def printScenery(scenery):
    colors = ["🟩", "🟨","🟧","🟩", "🟦"]
    for line in scenery:
        for chunk in line:
            print(colors[chunk -1], end="\t")
        print()

def createWorld():
    scenery = [] 
    for _ in range(height):
        line = []
        for _ in range(width):
           line.append(0)
        scenery.append(line)
    return scenery

def createFloor(scenery):
    base_floor = 0
    limit_floor = [2,3,4]
    for i in range(width):
        if i == 0:
            sorted_number = random.choice(limit_floor)
            scenery[height - sorted_number][i] = 1
            base_floor = sorted_number
        else:
            sorted_ = random.choice([1,2,3])
            sorted_1 = sorted_ in [1]
            sorted_2 = sorted_ in [2]
            sorted_3 = sorted_ in [3]
            if sorted_1:
                new_base_floor = base_floor + 1
                if new_base_floor > 4:
                    base_floor = 4
                    scenery[height - 4][i] = 1
                else:
                    base_floor = new_base_floor
                    scenery[height - base_floor][i] = 1
            if sorted_2:
                scenery[height - base_floor][i] = 1
            if sorted_3:
                new_base_floor = base_floor - 1
                if new_base_floor < 2:
                    base_floor = 2
                    scenery[height - 2][i] = 1
                else:
                    base_floor = new_base_floor
                    scenery[height - base_floor][i] = 1

scenery = createWorld()
createFloor(scenery)
printScenery(scenery)