from utils.utils import read_input

def check_for_reflection(buckets, times):
    result = 0
    for bucket in buckets:
        i = 0
        while i+1 < len(bucket):
            l = 0
            r = 0
            if bucket[i] == bucket[i+1]:
                l = i
                r = i
                while l-1 >= 0 or r+1+1 <= len(bucket):
                    if l-1 < 0 or r+1+1 >= len(bucket):
                        result += (i+1)*times 
                        break
                    elif bucket[l-1] != bucket[r+1+1]:
                        break                  
                    l -= 1
                    r +=1
                i += 1
            else:
                i += 1
    return result


def check_for_reflection_with_smudges(buckets, times):
    result = 0
    for n, bucket in enumerate(buckets):
        i = 0
        while i+1 < len(bucket):
            l = 0
            r = 0
            total_smudge_amount = 0
            smudge_amount = sum(1 for a, b in zip(bucket[i], bucket[i+1]) if a != b)
            if smudge_amount == 1 or smudge_amount == 0:
                total_smudge_amount += smudge_amount
                l = i
                r = i
                while l-1 >= 0 or r+1+1 <= len(bucket):
                    if l-1 < 0 or r+1+1 >= len(bucket):  
                        if total_smudge_amount == 1:
                            result += (i+1)*times 
                            break
                        else:
                            break
                    elif (sum(1 for a, b in zip(bucket[l-1], bucket[r+1+1]) if a != b) > 1):
                        break
                    else:
                        second_smudge_amount = sum(1 for a, b in zip(bucket[l-1], bucket[r+1+1]) if a != b)
                        total_smudge_amount += second_smudge_amount                  
                    if total_smudge_amount > 1:
                        break
                    l -= 1
                    r +=1
                i += 1
            else:
                i += 1
    return result

def part1(vals): 
    sum = 0
    buckets = []
    j = 0
    for i, line in enumerate(vals):
        if line == '':
            buckets.append(vals[j:i])
            j = i+1
        elif i == len(vals)-1:
            buckets.append(vals[j:i+1])

    sum += check_for_reflection(buckets,100)
    
    flipped_buckets = []
    for bucket in buckets:
        bucket = list(zip(*bucket))
        flipped_bucket = []
        for row in bucket:
            flipped_bucket.append(''.join(row))
        flipped_buckets.append(flipped_bucket)

    sum += check_for_reflection(flipped_buckets,1)
    return sum

def part2(vals): 
    sum = 0
    buckets = []
    j = 0
    for i, line in enumerate(vals):
        if line == '':
            buckets.append(vals[j:i])
            j = i+1
        elif i == len(vals)-1:
            buckets.append(vals[j:i+1])

    sum += check_for_reflection_with_smudges(buckets,100)
    
    flipped_buckets = []
    for bucket in buckets:
        bucket = list(zip(*bucket))
        flipped_bucket = []
        for row in bucket:
            flipped_bucket.append(''.join(row))
        flipped_buckets.append(flipped_bucket)

    sum += check_for_reflection_with_smudges(flipped_buckets,1)
    return sum 

if __name__ == "__main__":
    print(part1(read_input(13, "input.txt")))
    print(part2(read_input(13, "input.txt")))
