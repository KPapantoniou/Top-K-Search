## Top-K and Topogram Queries

Author: Konstantinos Papantoniou-Hatzigiorgis

### Description

This project implements algorithms for finding the top-K pairs with the highest sum of instance weight for pairs of the same age from demographic data sourced from the [UCI Machine Learning Repository](https://kdd.ics.uci.edu/databases/census-income/census-income.html). The goal is to compare the efficiency of two different algorithms using various parameters.

### Part 1

In the first part of the assignment, the HRJN algorithm is developed. It reads data alternately from two files and returns pairs directly when a suitable pair is found without reading the rest of the files. This approach mimics a genetic function and is invoked K times to return K results. The program consists of three helper functions and one main function:

- **read_file**: Reads data from a file, checking specific criteria (adult, unmarried).
- **get_next_valid_entry**: Uses `yield` to return the next valid entries from the file.
- **hrjn_algorithm**: Core algorithm that iterates through data, categorizing and comparing pairs based on age and gender.
- **Main**: Executes the `hrjn_algorithm` K times and prints the top pairs along with execution time.

### Part 2

The second part implements the B-Top algorithm, which reads all data first and then returns all K pairs with the best score at the end. It includes similar helper functions as Part 1:

- **read_file**: Reads data from a file, checking specific criteria (adult, unmarried).
- **get_next_valid_entry**: Uses `yield` to return the next valid entries from the file.
- **b_top_algorithm**: Contrary to Part 1, it initializes dictionaries and queues, processes male entries first, and then compares with valid female entries to determine top pairs.
- **Main**: Executes the `b_top_algorithm` K times and prints the top pairs along with execution time.

### Part 3

The third part compares the performance of both algorithms for multiple values of K (1, 2, 5, 10, 20, 50, 100, 150, 200, 250). A Python program is used to run both algorithms, storing their execution times in an array for each K value. Additionally, it prints the number of valid individuals (both male and female) and plots a simple graph of execution times against K pairs.

### Instructions

To run the program, execute the following commands:

```bash
python part1.py K
python part2.py K
python main.py
```
Replace K with the desired number of top pairs to retrieve.
