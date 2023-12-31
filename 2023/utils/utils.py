def read_input(day: str ='01', filename: str = "input.txt"): 
    """
    Returns a list of strings (lines from the inputfile).
    """
    filepath = "2023/inputs/day" + str(day) + "/" + filename 
    with open(filepath, "r") as f: 
        vals = f.readlines() 
        vals = [val.strip("\n") for val in vals] 
        return vals 
    
def flip(vert_list: list, counter = False):
    """
    Takes a list of strings and returns a diagonally flipped version.
    Can be used for easier processing of lists horizontally instead of vertically.
    """
    if not counter:
        horiz_list = list(zip(*vert_list))
    else:
        horiz_list = list(zip(*vert_list))[::-1]
    horiz_list_of_strings = []
    for row in horiz_list:
        horiz_list_of_strings.append(''.join(row))
    return horiz_list_of_strings

def rotate_90_degrees(orig_list: list):
    """
    Rotates a list 90 degrees clockwise
    """
    rotated_strings = []
    rotated = list(zip(*orig_list))
    for row in rotated:
        rotated_strings.append(''.join(row))
    return rotated_strings