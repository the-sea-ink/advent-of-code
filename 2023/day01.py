DIGITS = "123456789"
WORD_DIGITS = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

def read_input(filename: str = "input.txt"):
    filepath = "2023/inputs/day01/"+filename
    with open(filepath, "r") as f:
        vals = f.readlines()
        vals = [val.strip("\n") for val in vals]
        return vals

def part1(vals):
    sum = 0
    for elem in vals:
        # first digit
        for char in elem:
            if char.isnumeric():
                first_digit = char
                break
        # second digit
        for char in elem[::-1]:
            if char.isnumeric():
                last_digit = char
                break
        calibration_value = int(first_digit+last_digit)
        sum = sum + calibration_value
    return sum

def part2(vals):
    sum = 0
    for elem in vals:
        nums = ""
        i = -1
        while i < len(elem):
            i = i + 1
            for digit in DIGITS:
                if elem[i:].startswith(digit):
                    nums=nums+str(digit)
            for word, digit in WORD_DIGITS.items():
                if elem[i:].startswith(word):
                    nums=nums+str(digit)
        calibration_value = nums[0]+nums[-1]
        sum = sum + int(calibration_value)

    return sum

if __name__ == "__main__":
    print(part1(read_input("input.txt")))
    print(part2(read_input("input.txt")))