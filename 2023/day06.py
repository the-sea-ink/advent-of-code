# not a brute force solution, yay!
import re
def read_input(filename: str = "input.txt"):
    filepath = "2023/inputs/day06/"+filename
    with open(filepath, "r") as f:
        vals = f.readlines()
        vals = [val.strip("\n") for val in vals]
        return vals

def part1(vals):
    product = 1
    times = [int(i) for i in re.findall('[0-9]+', vals[0])]
    distances = [int(i) for i in re.findall('[0-9]+', vals[1])]
    for time, distance in zip(times, distances):
        beating_record_possibilities = 0
        for charge_time in range (1, time+1):
            remaining_time = time - charge_time
            travel_distance = remaining_time*charge_time
            if travel_distance>distance:
                beating_record_possibilities = (remaining_time-charge_time + 1)
                break
        product = product*beating_record_possibilities
    return product

def part2(vals):
    sum = 0
    time = int(re.sub('[^0-9]', '', vals[0]))
    distance = int(re.sub('[^0-9]', '', vals[1]))
    for charge_time in range (1, time+1):
        remaining_time = time - charge_time
        travel_distance = remaining_time*charge_time
        if travel_distance>distance:
            return remaining_time-charge_time + 1
    return sum

if __name__ == "__main__":
    print(part1(read_input("input.txt")))
    print(part2(read_input("input.txt")))