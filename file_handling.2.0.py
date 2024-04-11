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
import re
def extract_emails():
    email_pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    with open('mails.txt', 'r') as file:
        text = file.read()
    emails=re.findall(email_pattern, text)
    for email in emails:
        print(email)
extract_emails()