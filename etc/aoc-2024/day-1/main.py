import requests
import os

# Configuration
# set session cookie from browser after logging in to adventofcode.com
SESSION_COOKIE = '53616c7465645f5fb454558770532e35dba1525e60cdb44be3332cb5790ecb1641bdb5613fc18e99e4514d63f5c48850bf442793c69802b9c200097a4f593f3b'
# set input url and save path
INPUT_URL = 'https://adventofcode.com/2024/day/1/input'
SAVE_PATH = 'etc/aoc-2024/day-1/input.txt'

# Step 1: Fetch input and save to file
def fetch_input_and_save(url, session_cookie, save_path):
    headers = {'Cookie': f'session={session_cookie}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Save input to file
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'w') as file:
            file.write(response.text.strip())
        print(f"Input saved to {save_path}")
    else:
        raise Exception(f"Failed to fetch input: {response.status_code}")

# Step 2: Read and parse input into two arrays
def read_and_parse_input(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    array1, array2 = [], []
    for line in data:
        # Parse line into two integers
        nums = list(map(int, line.split()))
        # Append to arrays
        array1.append(nums[0])
        array2.append(nums[1])
    return array1, array2

# Step 3: Sort arrays, compute differences, and sum them up
def compute_sum_of_array_difference(array1, array2):
    array1.sort()
    array2.sort()
    differences = [abs(a - b) for a, b in zip(array1, array2)]
    return sum(differences)

# Step 4: Compute similarity score for star 2
def compute_similarity_score(array1, array2):
    array1.sort()
    array2.sort()
    values = [a for a in array1 if a in array2]
    return sum([a * array2.count(a) for a in values])

# Main Execution
try:
    # Fetch and save input
    fetch_input_and_save(INPUT_URL, SESSION_COOKIE, SAVE_PATH)
    
    # Read and parse input
    arr1, arr2 = read_and_parse_input(SAVE_PATH)
    
    # compute and print result for star 1
    star1_result = compute_sum_of_array_difference(arr1, arr2)
    print(f"The sum of the array1 and array2 differences is: {star1_result}")
    
    # Compute and print result for star 2
    star2_result = compute_similarity_score(arr1, arr2)
    print(f"The similarity score is: {star2_result}")
except Exception as e:
    print(f"Error: {e}")
