import math
import re

def read_input(filename: str = "input.txt"): 
    filepath = "2023/inputs/day10/"+filename 
    with open(filepath, "r") as f: 
        vals = f.readlines() 
        vals = [val.strip("\n") for val in vals] 
        return vals 
 
def part1(vals): 
    steps=0
    curr_pos = [(row, col) for row, row_elements in enumerate(vals) for col, element in enumerate(row_elements) if element == 'S'][0]
    # find initial direction
    # try up
    if curr_pos[0]-1 >=0 and (vals[curr_pos[0]-1][curr_pos[1]] == '|' or vals[curr_pos[0]-1][curr_pos[1]] == 'F' or vals[curr_pos[0]-1][curr_pos[1]] == '7'):
        new_pos = (curr_pos[0]-1,curr_pos[1])
    # try down
    elif curr_pos[0]+1<len(vals) and (vals[curr_pos[0]+1][curr_pos[1]] == '|' or vals[curr_pos[0]-1][curr_pos[1]] == 'J' or vals[curr_pos[0]-1][curr_pos[1]] == 'L'):
        new_pos = (curr_pos[0]+1,curr_pos[1])
    # try left
    elif curr_pos[1]-1 >=0 and (vals[curr_pos[0]][curr_pos[1]-1] == '-' or vals[curr_pos[0]][curr_pos[1]-1] == 'F' or vals[curr_pos[0]][curr_pos[1]-1] == 'L'):
        new_pos = (curr_pos[0],curr_pos[1]-1)
    # try right
    elif curr_pos[1]+1<len(vals[0]) and (vals[curr_pos[0]][curr_pos[1]+1] == '-' or vals[curr_pos[0]][curr_pos[1]+1] == 'L' or vals[curr_pos[0]][curr_pos[1]+1] == '7'):
        new_pos = (curr_pos[0],curr_pos[1]+1)
    prev_pos = curr_pos
    curr_pos = new_pos
    # loop through pipes
    while True:
        if vals[curr_pos[0]][curr_pos[1]] == 'S':
            break
        elif vals[curr_pos[0]][curr_pos[1]] == '|':
            if prev_pos[0] == curr_pos[0]+1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0]-1,curr_pos[1])
                steps += 1
            elif prev_pos[0] == curr_pos[0]-1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0]+1,curr_pos[1])
                steps += 1
        elif vals[curr_pos[0]][curr_pos[1]] == 'F':
            if prev_pos[0] == curr_pos[0]+1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0],curr_pos[1]+1)
                steps += 1
            elif prev_pos[1] == curr_pos[1]+1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0]+1,curr_pos[1])
                steps += 1
        elif vals[curr_pos[0]][curr_pos[1]] == '-':
            if prev_pos[1] == curr_pos[1]-1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0],curr_pos[1]+1)
                steps += 1
            elif prev_pos[1] == curr_pos[1]+1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0],curr_pos[1]-1)
                steps += 1
        elif vals[curr_pos[0]][curr_pos[1]] == 'J':
            if prev_pos[1] == curr_pos[1]-1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0]-1,curr_pos[1])
                steps += 1
            elif prev_pos[0] == curr_pos[0]-1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0],curr_pos[1]-1)
                steps += 1
        elif vals[curr_pos[0]][curr_pos[1]] == '7':
            if prev_pos[0] == curr_pos[0]+1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0],curr_pos[1]-1)
                steps += 1
            elif prev_pos[1] == curr_pos[1]-1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0]+1,curr_pos[1])
                steps += 1
        elif vals[curr_pos[0]][curr_pos[1]] == 'L':
            if prev_pos[0] == curr_pos[0]-1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0],curr_pos[1]+1)
                steps += 1
            elif prev_pos[1] == curr_pos[1]+1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0]-1,curr_pos[1])
                steps += 1
    return math.ceil(steps/2)

def part2(vals):
    curr_pos = [(row, col) for row, row_elements in enumerate(vals) for col, element in enumerate(row_elements) if element == 'S'][0]
    # building a cleared pipe map
    pipes = [['.' for _ in range(len(vals[0]))] for _ in range(len(vals))]
    pipes[curr_pos[0]][curr_pos[1]] = 'S'
    
    # find initial direction
    # try up
    if curr_pos[0]-1 >=0 and (vals[curr_pos[0]-1][curr_pos[1]] == '|' or vals[curr_pos[0]-1][curr_pos[1]] == 'F' or vals[curr_pos[0]-1][curr_pos[1]] == '7'):
        new_pos = (curr_pos[0]-1,curr_pos[1])
    # try down
    elif curr_pos[0]+1<len(vals) and (vals[curr_pos[0]+1][curr_pos[1]] == '|' or vals[curr_pos[0]-1][curr_pos[1]] == 'J' or vals[curr_pos[0]-1][curr_pos[1]] == 'L'):
        new_pos = (curr_pos[0]+1,curr_pos[1])
    # try left
    elif curr_pos[1]-1 >=0 and (vals[curr_pos[0]][curr_pos[1]-1] == '-' or vals[curr_pos[0]][curr_pos[1]-1] == 'F' or vals[curr_pos[0]][curr_pos[1]-1] == 'L'):
        new_pos = (curr_pos[0],curr_pos[1]-1)
    # try right
    elif curr_pos[1]+1<len(vals[0]) and (vals[curr_pos[0]][curr_pos[1]+1] == '-' or vals[curr_pos[0]][curr_pos[1]+1] == 'L' or vals[curr_pos[0]][curr_pos[1]+1] == '7'):
        new_pos = (curr_pos[0],curr_pos[1]+1)
    prev_pos = curr_pos
    curr_pos = new_pos
    # cycle through pipes to build a "pipe loop-only" grid
    while True:
        if vals[curr_pos[0]][curr_pos[1]] == 'S':
            break
        elif vals[curr_pos[0]][curr_pos[1]] == '|':
            pipes[curr_pos[0]][curr_pos[1]] = '|'
            if prev_pos[0] == curr_pos[0]+1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0]-1,curr_pos[1])
            elif prev_pos[0] == curr_pos[0]-1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0]+1,curr_pos[1])
        elif vals[curr_pos[0]][curr_pos[1]] == 'F':
            pipes[curr_pos[0]][curr_pos[1]] = 'F'
            if prev_pos[0] == curr_pos[0]+1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0],curr_pos[1]+1)
            elif prev_pos[1] == curr_pos[1]+1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0]+1,curr_pos[1])
        elif vals[curr_pos[0]][curr_pos[1]] == '-':
            pipes[curr_pos[0]][curr_pos[1]] = '-'
            if prev_pos[1] == curr_pos[1]-1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0],curr_pos[1]+1)
            elif prev_pos[1] == curr_pos[1]+1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0],curr_pos[1]-1)
        elif vals[curr_pos[0]][curr_pos[1]] == 'J':
            pipes[curr_pos[0]][curr_pos[1]] = 'J'
            if prev_pos[1] == curr_pos[1]-1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0]-1,curr_pos[1])
            elif prev_pos[0] == curr_pos[0]-1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0],curr_pos[1]-1)
        elif vals[curr_pos[0]][curr_pos[1]] == '7':
            pipes[curr_pos[0]][curr_pos[1]] = '7'
            if prev_pos[0] == curr_pos[0]+1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0],curr_pos[1]-1)
            elif prev_pos[1] == curr_pos[1]-1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0]+1,curr_pos[1])
        elif vals[curr_pos[0]][curr_pos[1]] == 'L':
            pipes[curr_pos[0]][curr_pos[1]] = 'L'
            if prev_pos[0] == curr_pos[0]-1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0],curr_pos[1]+1)
            elif prev_pos[1] == curr_pos[1]+1:
                prev_pos = curr_pos
                curr_pos = (curr_pos[0]-1,curr_pos[1])

    # inspired by https://github.com/ricbit/advent-of-code/blob/main/2023/adv10-r.py
    counter = 0
    for row in pipes:
        insides = 0
        # replace walls that are made of "turns" a wall, 
        # so that by crossing them we count them as a legit wall
        row = re.sub(r"F-*J|L-*7", "|", "".join(row))
        for elem in row:
            if elem == "|":
                insides += 1
            if insides % 2 == 1 and elem == ".":
                counter += 1
    return counter 

if __name__ == "__main__":
    print(part1(read_input("input.txt")))
    print(part2(read_input("input.txt")))