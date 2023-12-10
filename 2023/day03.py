def read_input(filename: str = "input.txt"):
    filepath = "2023/inputs/day03/"+filename
    with open(filepath, "r") as f:
        vals = f.readlines()
        vals = [val.strip("\n") for val in vals]
        return vals

def find_symbols(vals):
    symbol_positions = []
    for line_ind, line in enumerate(vals):
        for char_ind, char in enumerate(line):
            if not char.isnumeric() and char != ".":
                symbol_positions.append((line_ind, char_ind))
    return symbol_positions

def find_potential_gears(vals):
    potential_gear_positions = []
    for line_ind, line in enumerate(vals):
        for char_ind, char in enumerate(line):
            if char == "*":
                potential_gear_positions.append((line_ind, char_ind))
    return potential_gear_positions

def find_numbers(vals):
    number_positions = []
    for line_id, line in enumerate(vals):
        temp_positions = []
        for char_id, char in enumerate(line):
            if char.isnumeric():
                temp_positions.append((line_id,char_id))
            elif not char.isnumeric() and len(temp_positions) != 0:
                number_positions.append(temp_positions)
                temp_positions = []

            if char.isnumeric() and char_id == len(line)-1 and len(temp_positions) != 0:
                number_positions.append(temp_positions)
    return number_positions

def isadjacent(symbol_coordinate: tuple, number_coordinates: list):
    adjacent = False
    for number_coordinate in number_coordinates:
        if (number_coordinate[0] <= symbol_coordinate[0]+1 and 
            number_coordinate[0] >= symbol_coordinate[0]-1):
            if (number_coordinate[1] <= symbol_coordinate[1]+1 and 
                number_coordinate[1] >= symbol_coordinate[1]-1):
                adjacent = True
    return adjacent

def part1(vals):
    sum = 0
    symbol_positions = find_symbols(vals)
    number_positions = find_numbers(vals)
    adjacent_number_positions = []
    for symbol_coordinate in symbol_positions:
        for number_coordinates in number_positions:
            if isadjacent(symbol_coordinate, number_coordinates): #and 
                #number_coordinates not in adjacent_number_positions):
                adjacent_number_positions.append(number_coordinates)

    for number_positions in adjacent_number_positions:
        number = ""
        for digit_position in number_positions:
            number = number + vals[digit_position[0]][digit_position[1]]
        part_number = int(number)
        sum = sum + part_number
    return sum

def part2(vals):
    sum = 0
    potential_gear_positions = find_potential_gears(vals)
    number_positions = find_numbers(vals)
    for potential_gear_coordinate in potential_gear_positions:
        temp_adjacent_positions = []
        power = 1
        counter = 0
        for number_coordinates in number_positions:
            if isadjacent(potential_gear_coordinate, number_coordinates):
                counter = counter + 1
                temp_adjacent_positions.append(number_coordinates)
        if counter == 2:
            for number_pos in temp_adjacent_positions:
                number = ""
                for digit_position in number_pos:
                    number = number + vals[digit_position[0]][digit_position[1]]
                power = power*int(number)
            sum = sum + power
    return sum

if __name__ == "__main__":
    print(part1(read_input("input.txt")))
    print(part2(read_input("input.txt")))