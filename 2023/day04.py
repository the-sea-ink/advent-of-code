def read_input(filename: str = "input.txt"):
    filepath = "2023/inputs/day04/"+filename
    with open(filepath, "r") as f:
        vals = f.readlines()
        vals = [val.strip("\n") for val in vals]
        return vals

def part1(vals):
    sum = 0
    for line in vals:
        card_num, numbers = line.split(":")
        elf_card, winning_card = numbers.split("|")
        winning_numbers = winning_card.split()
        elf_numbers = elf_card.split()

        init = False
        winning_points = 0
        for number in elf_numbers:
            if number in winning_numbers and not init:
                winning_points = 1
                init = True
            elif number in winning_numbers:
                winning_points = winning_points*2
        sum = sum + winning_points
    return sum

def part2(vals):
    sum = 0
    card_instances = {}
    
    for id, line in enumerate(vals):
        # amount of cards, winning points
        card_instances[id] = (1)

    for id, line in enumerate(vals):
        card_num, numbers = line.split(":")
        elf_card, winning_card = numbers.split("|")
        winning_numbers = winning_card.split()
        elf_numbers = elf_card.split()

        counter = 0
        for number in elf_numbers:
            if number in winning_numbers:
                counter = counter + 1

        amount_of_cards = card_instances[id]
        for j in range(0, amount_of_cards):
            for i in range(1, counter+1):
                card_instances[id+i] = card_instances[id+i]+1
            j = j + 1

    for card_num, amount in card_instances.items():
        sum = sum + amount

    return sum

if __name__ == "__main__":
    print(part1(read_input("input.txt")))
    print(part2(read_input("input.txt")))