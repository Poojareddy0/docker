import os
import re
from collections import Counter
import socket

# Corrected file paths
file1_path = 'C:/Users/poojaReddy/Downloads/DockerProject-main/DockerProject-main/IF.txt'
file2_path = 'C:/Users/poojaReddy/Downloads/DockerProject-main/DockerProject-main/AlwaysRememberUsThisWay.txt'
output_path = 'C:/Users/poojaReddy/Downloads/DockerProject-main/DockerProject-main/result.txt'  # corrected 'Users'

# Function to count words
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        
        # Handle common contractions
        text = re.sub(r"won't", "will not", text)
        text = re.sub(r"can't", "cannot", text)
        text = re.sub(r"n't", " not", text)
        text = re.sub(r"'re", " are", text)
        text = re.sub(r"'s", " is", text)
        text = re.sub(r"'d", " would", text)
        text = re.sub(r"'ll", " will", text)
        text = re.sub(r"'ve", " have", text)
        text = re.sub(r"'m", " am", text)
        text = re.sub(r"wanna", "want to", text)
        text = re.sub(r"gonna", "going to", text)
        
        # Extract words and count
        words = re.findall(r'\b\w+\b', text)
        return words, len(words)

# Get word counts for each file
words_file1, count_file1 = count_words(file1_path)
words_file2, count_file2 = count_words(file2_path)

# Grand total of words
grand_total = count_file1 + count_file2

# Top 3 most frequent words in IF.txt
top_3_file1 = Counter(words_file1).most_common(3)

# Top 3 most frequent words in AlwaysRememberUsThisWay.txt
top_3_file2 = Counter(words_file2).most_common(3)

# Get the IP address of the container
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Ensure the directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write results to output file
with open(output_path, 'w') as output_file:
    output_file.write("A text file made by pooja putta\n\n")
    output_file.write(f"Total words in IF.txt: {count_file1}\n")
    output_file.write(f"Total words in AlwaysRememberUsThisWay.txt: {count_file2}\n")
    output_file.write(f"Grand total of words: {grand_total}\n\n")
    
    output_file.write("Top 3 words in IF.txt:\n")
    for word, count in top_3_file1:
        output_file.write(f"{word}: {count}\n")
    
    output_file.write("\nTop 3 words in AlwaysRememberUsThisWay.txt:\n")
    for word, count in top_3_file2:
        output_file.write(f"{word}: {count}\n")
    
    output_file.write(f"\nIP address of the machine: {ip_address}\n")

# Print results to the console
with open(output_path, 'r') as result_file:
    print(result_file.read())
