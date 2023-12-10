# time to finally learn regex..
import re

def read_input(filename: str = "input.txt"):
    filepath = "2023/inputs/day05/"+filename
    with open(filepath, "r") as f:
        vals = f.readlines()
        return [val.strip("\n") for val in vals]
    
def part1(vals):
    pos_act = []
    pos_next = [int(i) for i in re.findall('[0-9]+', vals[0])]
    pos_to_check = vals[2:]

    for line in pos_to_check:
        numbers = re.findall('[0-9]+', line)
        if len(numbers) == 0:
            pos_next.extend(pos_act)
            pos_act = pos_next
            pos_next = []
        else:
            destination = int(numbers[0])
            source = int(numbers[1])
            rng = int(numbers[2])
            for pos in pos_act:
                if pos >= source and pos < source + rng:
                    distance = pos - source 
                    pos_next.append(destination + distance)
                    pos_act = [n for n in pos_act if n != pos]

    pos_next.extend(pos_act)
    pos_act = pos_next
    return min(pos_act)

def part2(vals):
    pos_act = []
    init_seeds = [int(i) for i in re.findall('[0-9]+', vals[0])]

    seeds = [n for i,n in enumerate(init_seeds) if i % 2 ==0]
    ranges = [n for i,n in enumerate(init_seeds) if i % 2 !=0]

    pos_next = []
    for elem in zip(seeds,ranges):
        range_list = []
        range_list.extend(range(1,elem[1]+1))
        pos_next.extend([elem[0]])
        pos_next.extend([x+elem[0] for x in range_list])
        # l.extend(range(1, 6))
    print(len(pos_next))
    pos_to_check = vals[2:]

    for line in pos_to_check:
        numbers = re.findall('[0-9]+', line)
        if len(numbers) == 0:
            pos_next.extend(pos_act)
            pos_act = pos_next
            pos_next = []
        else:
            destination = int(numbers[0])
            source = int(numbers[1])
            rng = int(numbers[2])
            for pos in pos_act:
                if pos >= source and pos < source + rng:
                    distance = pos - source 
                    pos_next.append(destination + distance)
                    pos_act = [n for n in pos_act if n != pos]

    pos_next.extend(pos_act)
    pos_act = pos_next
    return min(pos_act)

if __name__ == "__main__":
    print(part1(read_input("input.txt")))
    #print(part2(read_input("input.txt")))