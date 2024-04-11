# Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

# Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

# 1. Exploring Python's OS Module
# Objective:
# The goal of this assignment is to deepen your understanding of the OS module in Python. You will engage in tasks that involve file and directory operations, path manipulations, and practical applications of these operations in real-world scenarios.

# Task 1: Directory Inspector:

# Problem Statement:
# Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

# Code Example:
# import os

# def list_directory_contents(path):
#     # List and print all files and subdirectories in the given path
# Expected Outcome:
# The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.
# Task 2: File Size Reporter:

# Problem Statement:
# Write a Python program that reports the sizes of all files in a specific directory. The program should ask the user for a directory path and then print each file's name and size within that directory.

# Code Example:
# def report_file_sizes(directory):
#     # Iterate through files in the directory and print their names and sizes
# Expected Outcome:
# Your program should display the name and size (in bytes) of each file in the given directory. Ensure that the program only reports on files, not directories, and handles any errors gracefully.
# Task 3: File Extension Counter:

# Problem Statement:
# Develop a Python script that counts the number of files of each extension type in a directory. For instance, in a directory with five '.txt' files and three '.py' files, the script should report "TXT: 5" and "PY: 3".

# Code Example:
# def count_file_extensions(directory):
#     # Count and print the number of files of each extension type in the directory
# Expected Outcome:
# The script should accurately count and display the number of files for each extension type in the specified directory. Handle different cases of file extensions (e.g., '.TXT' and '.txt' should be considered the same).
# 2. Regex-Powered Text Data Processing
# Objective:
# The purpose of this assignment is to harness the power of regular expressions (regex) in Python for advanced text data processing. You will apply regex to extract, manipulate, and analyze data from text files, combining it with efficient file handling techniques.

# Task 1: Email Extractor:

# Problem Statement:
# Write a Python script to extract all email addresses from a given text file (contacts.txt). The file contains a mix of text and email addresses.

# File Example:
# Contact List:

# John Doe - john.doe@example.com
# Jane Smith - jane.smith@gmail.com

# For inquiries, please contact info@example.com
# Code Example:
# import re

# def extract_emails(filename):
#     # Read the file and use regex to find and return all email addresses
# Expected Outcome:
# The script should output a list of all unique email addresses found in the file. 
# Utilize regex to accurately identify email addresses amidst other text.

# 3. Advanced Python Data Processing and Analysis Challenge
# Objective:
# This assignment is aimed at challenging your skills in advanced data processing and analysis using Python. It encompasses a broad range of topics, including file handling, regular expressions, data structures, and complex problem-solving, at a medium-hard difficulty level.

# Task 1: Travel Blog Sentiment Analysis:

# Problem Statement:
# Perform sentiment analysis on a collection of travel blog entries stored in travel_blogs.txt. Identify and count the occurrences of positive words (e.g., "amazing", "enjoy", "beautiful") and negative words (e.g., "bad", "disappointing", "poor").
# - Dataset Example:
# Travel Blog Entries:

# Code Example:
# def analyze_blog_sentiments(blog_file):
#     # Implement sentiment analysis logic on the blog file
# Expected Outcome:
# A summary report indicating the number of positive and negative words in the travel blogs, demonstrating the ability to process text data and apply basic sentiment analysis.
# Task 2: Historical Weather Data Compiler

# Problem Statement:
# Compile and analyze historical weather data from multiple files (weather_2020.txt, weather_2021.txt, etc.). Each file contains daily temperature data. Calculate the average temperature for each year and identify the year with the highest average.

# - Dataset Example:
# File: weather_2020.txt

# File: weather_2021.txt

# Code Example:
# def compile_weather_data(file_list):
#     # Aggregate temperature data and calculate the yearly averages
# Expected Outcome:
#An aggregated view of average temperatures for each year and identification of the year with the highest average temperature, showcasing data aggregation and analysis skills
