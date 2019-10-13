# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

filepath = os.path.join("..", "03_E-mail", "employees_list.csv")

new_employee_data = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # print(row)
        first_name = row['first_name']
        last_name = row['last_name']
        # print(first_name,last_name)
        email = "{}.{}@example.com".format(first_name,last_name)
        # print(email)

        new_dict = {}
        new_dict['First Name'] = first_name
        new_dict['Last Name'] = last_name
        new_dict['Email'] = email
        new_dict['SSN'] = row['ssn']
        # print(new_dict)

        new_employee_data.append(new_dict)

# print(new_employee_data)

with open("output.csv", "w",newline="") as csvfile:
    fieldnames = ['First Name', 'Last Name','Email','SSN']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in new_employee_data:
        writer.writerow(i)
