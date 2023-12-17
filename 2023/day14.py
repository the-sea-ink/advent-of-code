from utils.utils import read_input, flip, rotate_90_degrees

def roll(dish):
    focused_dish = []
    for i, row in enumerate(dish):
        focused_row = ''
        prev = 0
        end = False
        while not end:
            indices = [y for y, x in enumerate(row) if x == "#"]
            if len(indices) == 0:
                focused_row += 'O'*row.count('O') + '.'*row.count('.')
                break
            for k, curr in enumerate(indices):
                bucket = row[prev:curr]
                if bucket != '#':
                    focused_row += 'O'*bucket.count('O') + '.'*bucket.count('.')
                focused_row += '#'
                prev = curr
                if curr == indices[-1] and curr != len(row)-1:
                    bucket = row[curr:]
                    focused_row += 'O'*bucket.count('O') + '.'*bucket.count('.')
            
            else:
                end = True
        focused_dish.append(focused_row)
    return focused_dish

def part1(vals): 
    sum = 0

    dish = flip(vals)
    focused_dish = roll(dish)
    focused_rotated_dish = flip(focused_dish, counter = True)

    for l, row in enumerate(focused_rotated_dish):
        sum += row.count('O')*(l+1)
    return sum

def part2(vals):
    sum = 0
    counter = 0
    cycle_list = []
    curr_dish = vals
    while True:
        for i in range(4):
            dish = flip(curr_dish)
            focused_dish = roll(dish)
            focused_rotated_dish = flip(focused_dish, counter = True)
            curr_dish = rotate_90_degrees(focused_rotated_dish)
        counter +=1
        if curr_dish not in cycle_list:
            cycle_list.append(curr_dish)
        else:
            found_dish_id = cycle_list.index(curr_dish)+1
            cycle = counter-found_dish_id
            leftover = (1000000000-counter)%cycle
            break
        
    for k in range(leftover):
        for i in range(4):
            dish = flip(curr_dish)
            focused_dish = roll(dish)
            focused_rotated_dish = flip(focused_dish, counter = True)
            curr_dish = rotate_90_degrees(focused_rotated_dish)

    rever_list = curr_dish[::-1]
    for l, row in enumerate(rever_list):
        sum += row.count('O')*(l+1)
              
    return sum


if __name__ == "__main__":
    print(part1(read_input(14, "input.txt")))
    print(part2(read_input(14, "input.txt")))
