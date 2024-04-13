################################
# Yeshi Wangmo
# First Year Electronics and Communication Engineering (1ECE)
# 02230118
################################
# REFERENCES
# https://www.dataquest.io/blog/read-file-python/
# https://youtu.be/Vu9KJom7U8c?si=Vl2K68DvLqd2VfwL
# https://www.w3schools.com/python/python_dictionaries.asp
# https://youtu.be/KWgYha0clzw?si=FOj4hoIAFYQgC_Tf
################################
# SOLUTION
# Your Solution Score: 49843
# Put your number here: 8
################################

# Define a function to read the file
def read_input(file_path):
    # Initialize an empty list to store shape and outcome tuples
    match = []
    # Open the file as read only
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # stips and splits each line into two parts
            shape,outcome = line.strip().split()
            # append tuple containing 'shape' and 'outcome' to the 'match' list
            match.append((shape,outcome))
    # Return the list containing match
    return match

# Define a function to calculate the scores
def calculate_score(match):
    # Initialize a nested dicitonary where outer key = shape("A","B","C") and inner keys = outcome("X","Y","Z")
    score = {
        "A": {"X": 3, "Y": 4, "Z": 8},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 2, "Y": 6, "Z": 7}
    }
    # Initialize variable to store a cumulative score that is '0' right now
    total_score = 0
    # Iterate over each match in the list of match
    for shape, outcome in match:
        # Adds score to the total score
        total_score += score[shape][outcome]
    return total_score    

# specify the file path
file_path = "input_8_cap1.txt"
# calculate total_score 
total_score = calculate_score(read_input(file_path))
# print the total score the game
print(f"the total score of the rock-paper-scissors game is: {total_score}")