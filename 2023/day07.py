CARD_POWERS = { 
    'A': 13,  
    'K': 12,  
    'Q': 11,  
    'J': 10,  
    'T': 9,  
    '9': 8,  
    '8': 7,  
    '7': 6,  
    '6': 5,  
    '5': 4,  
    '4': 3,  
    '3': 2,  
    '2': 1 
} 

CARD_POWERS_JOKER = { 
    'A': 13,  
    'K': 12,  
    'Q': 11,    
    'T': 10,  
    '9': 9,  
    '8': 8,  
    '7': 7,  
    '6': 6,  
    '5': 5,  
    '4': 4,  
    '3': 3,  
    '2': 2, 
    'J': 1
} 
 
HAND_TYPE = { 
    "5": 7, 
    "41": 6, 
    "32": 5, 
    "311": 4, 
    "221": 3, 
    "2111": 2, 
    "11111": 1 
} 
 
def read_input(filename: str = "input.txt"): 
    filepath = "2023/inputs/day07/"+filename 
    with open(filepath, "r") as f: 
        vals = f.readlines() 
        vals = [val.strip("\n") for val in vals] 
        return vals 
 

def custom_joker_sort(elem): 
    integer_part = elem[0] 
    integer_sorting = HAND_TYPE[integer_part] 
    string_part = elem[1] 
    sort_string = tuple(CARD_POWERS_JOKER[char] for char in string_part) 
    return (integer_sorting, sort_string) 

def custom_sort(elem): 
    integer_part = elem[0] 
    integer_sorting = HAND_TYPE[integer_part] 
    string_part = elem[1] 
    sort_string = tuple(CARD_POWERS[char] for char in string_part) 
    return (integer_sorting, sort_string) 
 
def part1(vals): 
    product = 0 
    unsorted_list = [] 
    sorted_list = [] 
    for line in vals: 
        current_hand, bid = line.split() 
        hand_max_duplicates = sorted([current_hand.count(i) for i in set(current_hand)], reverse=True) 
        string_sorted_hand = ''.join([str(elem) for elem in hand_max_duplicates]) 
        unsorted_list.append([string_sorted_hand, current_hand, bid]) 
 
    sorted_list = sorted(unsorted_list, key=custom_sort) 
    for i, elem in enumerate(sorted_list): 
        product += (i+1)*int(elem[2]) 
    return product

def part2(vals):
    product = 0 
    unsorted_list = [] 
    sorted_list = [] 
    for line in vals: 
        current_hand, bid = line.split() 
        jokers = current_hand.count("J")
        if jokers != 0 and jokers !=5:
            hand_max_duplicates = sorted([current_hand.count(i) for i in set(current_hand)], reverse=True)
            hand_max_duplicates.remove(jokers)
            hand_max_duplicates[0] += jokers
        else:
            hand_max_duplicates = sorted([current_hand.count(i) for i in set(current_hand)], reverse=True) 
        string_sorted_hand = ''.join([str(elem) for elem in hand_max_duplicates]) 
        unsorted_list.append([string_sorted_hand, current_hand, bid]) 
 
    sorted_list = sorted(unsorted_list, key=custom_joker_sort) 
    for i, elem in enumerate(sorted_list): 
        product += (i+1)*int(elem[2]) 
    return product

if __name__ == "__main__":
    print(part1(read_input("input.txt")))
    print(part2(read_input("input.txt")))