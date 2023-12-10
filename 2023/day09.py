import re
def read_input(filename: str = "input.txt"): 
    filepath = "2023/inputs/day09/"+filename 
    with open(filepath, "r") as f: 
        vals = f.readlines() 
        vals = [val.strip("\n") for val in vals] 
        return vals 
 
def part1(vals): 
    sum = 0
    for line in vals:
        finished = False
        curr_stage = 0
        observations = [re.findall('-?\d+\.?\d*', line)]
        observations = [[int(i) for i in observations[0]]]

        # fill observations
        while not finished:
            diffs = []
            for i in range(len(observations[curr_stage])):
                if i < len(observations[curr_stage])-1:
                    diffs.append(observations[curr_stage][i+1] - observations[curr_stage][i])
                else:
                    observations.append(diffs)
                    if diffs.count(0) == len(diffs):
                        finished = True
                        break
                    diffs = []
                    curr_stage +=1

        # make predictions
        observations.reverse()
        observations[0].append(0)
        for j in range(1,len(observations)):
            added = observations[j][-1]+observations[j-1][-1]
            observations[j].append(added)
        sum += observations[-1][-1]
    return sum


def part2(vals):
    sum = 0
    for line in vals:
        finished = False
        curr_stage = 0
        observations = [re.findall('-?\d+\.?\d*', line)]
        observations = [[int(i) for i in observations[0]]]

        # fill observations
        while not finished:
            diffs = []
            for i in range(len(observations[curr_stage])):
                if i < len(observations[curr_stage])-1:
                    diffs.append(observations[curr_stage][i+1] - observations[curr_stage][i])
                else:
                    observations.append(diffs)
                    if diffs.count(0) == len(diffs):
                        finished = True
                        break
                    diffs = []
                    curr_stage +=1

        # make predictions
        observations.reverse()
        observations[0].insert(0, 0)
        for j in range(1,len(observations)):
            added = observations[j][0]-observations[j-1][0]
            observations[j].insert(0,added)
        sum += observations[-1][0]
    return sum

if __name__ == "__main__":
    print(part1(read_input("input.txt")))
    print(part2(read_input("input.txt")))