#Project: Health and Relationships
# imports
import pandas as pd
import re

#loading data 

# Python program to convert .tsv file to .csv file
 
# reading given tsv file
with open("/Users/Owner/Desktop/DSCourses/CS506/FinalProj/ICPSR_37404/DS0002/37404-0002-Data.tsv", 'r') as myfile:  
  with open("2Data.csv", 'w') as csv_file:
    for line in myfile:
       
      # replace every tab with comma
      fileContent = re.sub("\t", ",", line)
       
      # writing into csv file
      csv_file.write(fileContent)
 
# output
print("Successfully made csv file")


#loading data




#cleading data




#exploratory analysis