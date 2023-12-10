# more regex exercise, yay
import re
# and a mathematical solution for part 2, yay
import math

def read_input(filename: str = "input.txt"): 
    filepath = "2023/inputs/day08/"+filename 
    with open(filepath, "r") as f: 
        vals = f.readlines() 
        vals = [val.strip("\n") for val in vals] 
        return vals 
 
def part1(vals): 
    this_is_the_way = []
    directions = vals[0]
    connections = [re.sub(r'[^a-zA-Z\s]', '', line).split() for line in vals[2:]]
    # find index of the first AAA to start navigation:
    curr_position = [i for i, spot in enumerate(connections) if spot[0]=="AAA"][0]
    # navigate:
    z_found = False
    while not z_found:
        for direction in directions:
            if direction == "L":
                next_spot = connections[curr_position][1]
            else:
                next_spot = connections[curr_position][2]
            this_is_the_way.append(next_spot)
            curr_position = [i for i, spot in enumerate(connections) if spot[0]==next_spot][0]
            if this_is_the_way[-1] == "ZZZ":
                z_found = True
                break
    return len(this_is_the_way)

def find_way_for_one(directions,curr_position,connections,this_is_the_way):
    z_found = False
    while not z_found:
        for direction in directions:
            if direction == "L":
                next_spot = connections[curr_position][1]
            else:
                next_spot = connections[curr_position][2]
            this_is_the_way.append(next_spot)
            curr_position = [i for i, spot in enumerate(connections) if spot[0]==next_spot][0]
            if this_is_the_way[-1].endswith("Z"):
                return len(this_is_the_way)

def part2(vals):
    directions = vals[0]
    connections = [re.sub(r'[^a-zA-Z0-9\s]', '', line).split() for line in vals[2:]]
    # search for all **A nodes:
    curr_positions = [i for i, spot in enumerate(connections) if bool(re.search(r'A$', spot[0]))]
    required_steps = []
    for curr_position in curr_positions:
        this_is_the_way = []
        required_steps.append(find_way_for_one(directions, curr_position,connections,this_is_the_way))
    return math.lcm(*required_steps)

if __name__ == "__main__":
    print(part1(read_input("input.txt")))
    print(part2(read_input("input.txt")))