import os
import csv

udemy_csv = os.path.join("..", "HW_Task2_UdemyZip","web_starter_KG.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(udemy_csv, encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    
    for row in csvreader:
        
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        length.append(row[9])
        review_percent.append(row)
        
        
# Define the function to calculate the percentage of reviews:
        
def percent_of_reviews(reviews_left, subscribers):
    
    reviews_left = float(reviews_left)
    subscribers = float(subscribers)
    percent_of_reviews =  '{0:.2f}'.format((reviews_left / subscribers * 100))
    return percent_of_reviews


    for row in csvreader:
        percent_of_reviews =  '{0:.2f}'.format((reviews_left / subscribers * 100))
        print(percent_of_reviews)


zipped_data = zip(title,price, subscribers, reviews, length) 
    

# Set variable for output file
output_file = os.path.join("web_final_KG.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left", "Length", "Percent of Reviews"])

    writer.writerows(zipped_data)
    
  

spyder--reset

