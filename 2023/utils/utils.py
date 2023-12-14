def read_input(day: str ='01', filename: str = "input.txt"): 
    filepath = "2023/inputs/day" + str(day) + "/" + filename 
    with open(filepath, "r") as f: 
        vals = f.readlines() 
        vals = [val.strip("\n") for val in vals] 
        return vals 