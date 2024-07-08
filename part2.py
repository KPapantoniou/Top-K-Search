## Author: Konstantinos Papantoniou-Chatzigiosis (A.M. 4769)
##Description: This script is used to implement the btop-k algorithm

import heapq
import sys
import time

count =0

def read_file(file):
    global count
    line = file.readline()
    if not line:
        return None
    parts = line.strip().split(',')
    if parts[8].strip().startswith('Married') or int(parts[1]) < 18:
        return -1
    count += 1
    id = int(parts[0])
    age = int(parts[1])
    weight = float(parts[25])
    return id, age, weight

def get_next_valid_entry(file):
    while True:
        entry = read_file(file)
        if entry != -1:
            return entry

def b_top_algorithm(male_file, female_file, K):
    males_file = open(male_file, 'r')
    females_file = open(female_file, 'r')

    male_hash = {}
    priority_queue = []

    while True:
            male_entry = get_next_valid_entry(males_file)
            if male_entry is None:
                break
            id, age, weight = male_entry
            if age not in male_hash:
                male_hash[age] = []
            male_hash[age].append((id, weight))

    while True:
            female_entry = get_next_valid_entry(females_file)
            if female_entry is None:
                break
            id, age, weight = female_entry
            if age in male_hash:
                for male_id, male_weight in male_hash[age]:
                    score = weight + male_weight
                    if len(priority_queue) < K:
                        heapq.heappush(priority_queue, (score, (male_id, id)))
                    elif score > priority_queue[0][0]:
                        heapq.heappushpop(priority_queue, (score, (male_id, id)))
    
    males_file.close()
    females_file.close()



    priority_queue = sorted(priority_queue, key=lambda x: (x[0], -x[1][1]), reverse=True)

    return priority_queue

def main(K):
    global count
    start_time = time.time()
    top_k_results = b_top_algorithm('males_sorted', 'females_sorted', K)

    for idx, result in enumerate(top_k_results, start=1):
        print(f"pair: {result[1][0]},{result[1][1]} score: {result[0]:.2f}")

    end_time = time.time()
    print(f"Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    K = int(sys.argv[1])
    main(K)
