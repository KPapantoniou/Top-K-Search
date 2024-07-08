## Author: Konstantinos Papantoniou-Chatzigiosis (A.M. 4769)
##Description: This script is used to compare the two algorithms of part1.py and part2.py
## and plot the time taken for each K value.

from part1 import hrjn_algorithm
import part1,part2
from part2 import b_top_algorithm
import subprocess
import time
import matplotlib.pyplot as plt

def plot_graph(K, time1, time2):
    plt.plot(K, time1, label='part1.py')
    plt.plot(K, time2, label='part2.py')
    plt.xlabel('K')
    plt.ylabel('Time taken')
    plt.title('Time taken vs K')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    K =[1,2,5,10,20,50,100,150,200,250]
    time1,time2 = [],[]

    
    
    for k in K:
        start_time = time.time()
        hrjn_opt = hrjn_algorithm('males_sorted','females_sorted')
        
        for idx in range(k):            
            result = next(hrjn_opt)
        

        end_time = time.time()
        print(f"Valid line for {k} first algorithm:{part1.count}")
        time1.append((end_time - start_time))
        hrjn_opt.close()
        part1.count = 0
    for k in K:
        start_time = time.time()
        hrjn = b_top_algorithm('males_sorted','females_sorted',k)
        for idx, result in enumerate(hrjn, start=1):
            pass
        end_time = time.time()
        print(f"Valid lines for {k} second algorith: {part2.count}")
        time2.append(end_time - start_time)
        hrjn = []
        
    plot_graph(K, time1, time2)
if __name__ == "__main__":
    main()
