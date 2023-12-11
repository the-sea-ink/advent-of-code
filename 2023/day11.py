# one function for both solutions; 
# idea: instead of creating an actual map with millions of empty spaces 
# is to just calculate add the millions into calculation by searching for the stars position
from utils.utils import read_input

def part1_2(vals, increase): 
    sum = 0
    horizontal_expansion = []
    for i, row in enumerate(vals):
        if row.count(".") == len(row):
            horizontal_expansion.append(i)

    vertical_expansion = []
    num_rows = len(vals)
    num_cols = len(vals[0])
    for col in range(num_cols):
        if all(vals[row][col] == '.' for row in range(num_rows)):
            vertical_expansion.append(col)
            
    star_map = [list(t) for t in vals]
    
    star_positions = []
    st = 1
    horizontal_offset = 0
    for i, row in enumerate(star_map):
        vertical_offset = 0
        if i in horizontal_expansion:
            horizontal_offset += increase
        for j, star in enumerate(row):
            if j in vertical_expansion:
                vertical_offset += increase
            if star == '#':
                star_positions.append((st, (horizontal_offset,vertical_offset)))
                st += 1
            vertical_offset += 1
        horizontal_offset += 1

    unique_stars = list(range(1, st))
    star_pairs = set([(unique_stars[i], unique_stars[j]) for i in range(len(unique_stars)) for j in range(i+1, len(unique_stars))])
    
    for pair in star_pairs:
        for star_info in star_positions:
            if pair[0] == star_info[0]:
                first_star_pos = star_info[1]
            elif pair[1] == star_info[0]:
                second_star_pos = star_info[1]
        diff = abs(first_star_pos[0]-second_star_pos[0]) + abs(first_star_pos[1]-second_star_pos[1])
        sum += diff

    return sum

if __name__ == "__main__":
    print(part1_2(read_input('11',"input.txt"),999999))