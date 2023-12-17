from utils.utils import read_input

def part1(vals):
    sum = 0
    separated_vals = vals[0].split(',')
    for code in separated_vals:
        curr_val = 0
        for symbol in code:
            curr_val += ord(symbol)
            curr_val *= 17
            curr_val = curr_val%256
        sum += curr_val
    return sum

def part2(vals):
    return

if __name__ == "__main__":
    print(part1(read_input(15, "input.txt")))
    #print(part2(read_comma_sep_input(15, "test_input.txt")))