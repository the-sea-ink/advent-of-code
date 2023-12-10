COMBI = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def read_input(filename: str = "input.txt"):
    filepath = "2023/inputs/day02/"+filename
    with open(filepath, "r") as f:
        vals = f.readlines()
        vals = [val.strip("\n") for val in vals]
        return vals

def part1(vals):
    sum = 0
    for line in vals:
        passes = True
        line_to_parse = line.split(":")
        zuege = line_to_parse[1].split(";")
        for zug in zuege:
            colors_to_check = zug.split(",")
            for color_to_check in colors_to_check:
                camount, ccolor = color_to_check.split()
                for color, num in COMBI.items():
                    if  ccolor == color and int(camount)>num:
                        passes = False
        if passes==True:
            game = line_to_parse[0].split()
            sum = sum + int(game[1])
    return sum

def part2(vals):
    sum = 0
    for line in vals:
        reds = []
        greens = []
        blues=[]
        line_to_parse = line.split(":")
        zuege = line_to_parse[1].split(";")
        for zug in zuege:
            colors_to_check = zug.split(",")
            for color_to_check in colors_to_check:
                camount, ccolor = color_to_check.split()
                if ccolor == "red":
                    reds.append(int(camount))
                elif ccolor == "green":
                    greens.append(int(camount))
                else:
                    blues.append(int(camount))
        power = max(reds)*max(greens)*max(blues)
        sum = sum + power             
    return sum

if __name__ == "__main__":
    print(part1(read_input("input.txt")))
    print(part2(read_input("input.txt")))
    