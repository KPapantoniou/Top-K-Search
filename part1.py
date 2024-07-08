## Author: Konstantinos Papantoniou-Chatzigiosis (A.M. 4769)
##Description: This script is used to implement the Atop-k algorithm using hrjn
import heapq
import time
import sys

ending_reached = False
count =0
def read_file(file):
    global count, ending_reached
    line = file.readline()
    if not line:
        ending_reached = True
        return 
    parts = line.strip().split(',')
    if parts[8].strip().startswith('Married') or int(parts[1]) < 18:
        return -1
    
    count += 1
    id = int(parts[0])
    age = int(parts[1])
    weight = float(parts[25])
    return id, age, weight

def get_next_valid_entry(file):
    global ending_reached
    while True and not ending_reached:
        entry = read_file(file)
        if entry != -1 and entry != -2 and entry is not None:
            yield entry[0], entry[1], entry[2]
        
    

def hrjn_algorithm(male_file, female_file):
    global ending_reached
    males_file = open(male_file, 'r')
    females_file = open(female_file, 'r')

    male_hash = {}
    female_hash = {}
    priority_queue = []
    
    Ltop = Rtop = float('-inf')
    Lbottom = Rbottom = float('inf')
    threshold = float('-inf')

    male_next_gen = get_next_valid_entry(males_file)

    
    female_next_gen = get_next_valid_entry(females_file)

    if male_next_gen is None or female_next_gen is None:
        male_file.close()
        female_file.close()
        return None
    male_next = next(male_next_gen, None)
    female_next = next(female_next_gen, None)

    read_male = True  

    while male_next or female_next or priority_queue and not ending_reached:
        if read_male and male_next:
            id, age, weight = male_next
            if age not in male_hash:
                male_hash[age] = []
            male_hash[age].append((id, weight))

            if age in female_hash:
                for other_id, other_weight in female_hash[age]:
                    score = weight + other_weight
                    heapq.heappush(priority_queue, (-score, (id, other_id)))

            Lbottom = min(Lbottom, weight)
            Ltop = max(Ltop, weight)
            male_next = next(male_next_gen, None)


        elif not read_male and female_next:
            id, age, weight = female_next
            if age not in female_hash:
                female_hash[age] = []
            female_hash[age].append((id, weight))

            if age in male_hash:
                for other_id, other_weight in male_hash[age]:
                    score = weight + other_weight
                    heapq.heappush(priority_queue, (-score, (other_id, id)))

            Rbottom = min(Rbottom, weight)
            Rtop = max(Rtop, weight)
            female_next = next(female_next_gen, None)
    

        threshold = max(Ltop + Rbottom, Lbottom + Rtop)
        read_male = not read_male

        while priority_queue and -priority_queue[0][0] > threshold and not ending_reached:
            highest_score_pair = heapq.heappop(priority_queue)
            yield (-highest_score_pair[0], highest_score_pair[1])

    males_file.close()
    females_file.close()

    ending_reached = True
    return None

def main(K):
    global count, ending_reached
    start_time = time.time()
    hrjn = hrjn_algorithm('males_sorted', 'females_sorted')
    
    k_count = 0
    for idx in range(K):
        try:
            result = next(hrjn)
             
            print(f"pair: {result[1][0]},{result[1][1]} score: {result[0]:.2f}")
            k_count += 1
        except StopIteration:
            break
            
    print(f"Time taken: {time.time() - start_time:.3f} seconds")


if __name__ == "__main__":
    K = int(sys.argv[1])
    main(K)