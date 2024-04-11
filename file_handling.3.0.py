# 3. Advanced Python Data Processing and Analysis Challenge
# Objective:
# This assignment is aimed at challenging your skills in advanced data processing and analysis using Python. It encompasses a broad range of topics, including file handling, regular expressions, data structures, and complex problem-solving, at a medium-hard difficulty level.

# Task 1: Travel Blog Sentiment Analysis:

# Problem Statement:
# Perform sentiment analysis on a collection of travel blog entries stored in 
# travel_blogs.txt. Identify and count the occurrences of positive words 
# (e.g., "amazing", "enjoy", "beautiful") and negative words (e.g., "bad", "disappointing", "poor").
# - Dataset Example:
# Travel Blog Entries:
import re 


def analyze_blog_sentiments():
        good_counter=0
        bad_counter=0
        with open('travel_blogs.txt', 'r') as file:
            text = file.read()
        print(text)
        good=["excellent","enlightening","fantastic","amazing","wonderful","unique experience","memorable","brilliant","stunning"]
        bad=["disappointing","lackluster","bad","worst"]
        for word in good:
            if word in text:
                good_counter+=1
        for word in bad:
            if word in text:
                bad_counter+=1        
        print(f"There is {bad_counter} negative words and {good_counter} positive words")
analyze_blog_sentiments()

# Expected Outcome:
# A summary report indicating the number of positive and negative words in the travel blogs, demonstrating the ability to process text data and apply basic sentiment analysis.
# Task 2: Historical Weather Data Compiler

# Problem Statement:
# Compile and analyze historical weather data from multiple files (weather_2020.txt, weather_2021.txt, etc.). Each file contains daily temperature data. Calculate the average temperature for each year and identify the year with the highest average.

# - Dataset Example:
# File: weather_2020.txt

# File: weather_2021.txt


def compile_weather_data():
    with open('weather_2020.txt', 'r') as file:
        year2020 = file.read()
    with open('weather_2021.txt', 'r') as file:
        year2021 = file.read()
    temperatures_pattern=r',(\d+)Â°C'
    temperatures2020 = [int(temp) for temp in re.findall(temperatures_pattern, year2020)]
    temperatures2021 = [int(temp) for temp in re.findall(temperatures_pattern, year2021)]
    prom_temp_2020=sum(temperatures2020)/len(temperatures2020)
    prom_temp_2021=sum(temperatures2021)/len(temperatures2021)
    print(f"Average temperature in 2020: {prom_temp_2020}")
    print(f"Average temperature in 2021: {prom_temp_2021}")

compile_weather_data()

# Expected Outcome:
#An aggregated view of average temperatures for each year and identification of the year with the highest average temperature, showcasing data aggregation and analysis skills
