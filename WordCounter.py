import os
from tkinter import filedialog
from collections import Counter

# Set current working directory as default directory for file dialog
default_dir = os.getcwd()

# Open file dialog and get selected file path
file_path = filedialog.askopenfilename(initialdir=default_dir)

# Check if file was selected
if file_path:
    with open(file_path, 'r') as file:
        text = file.read()

    word_list = text.split()

    # Use Counter to count word frequencies
    word_freq = Counter(word_list)

    # Print most common words and total word count
    for word, freq in word_freq.most_common():
        print(word, freq)
    print("total words:", len(word_list))
else:
    print("No file selected.")