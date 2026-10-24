# CSE 583 Homework 1

## Process of homework
To setup folder structure, I input commands in my terminal to create directories and download the data. (I added ignore the csv file in the gitignore to avoid uploading the file as said in the instruction)

Then for the hw1.py, I first use my prior knowledge with panda to read the data then I ask AI to explain to me how to convert the date in the csv file to a format that panda can recognize and I also noticed the missing value mentioned in the instruction so I use coerce to address the missing values, while converting them to Int64 so the missing values can be preserved. Since it is already converted to datetime format, I then use .hour and .year to store the values in the new columns. Then I find the year == 2016 and create a copy of that subset to be a new dataframe. 

Since I previously preserved the missing value, I can find it by .isna() to locate it, and I count and print the number of missing data so I can document it later. Then I drop missing rows to prevent them from affecting the later plot and busiest hour calculation. I use .groupby to locate and group bicycle count for each hour and use .mean to average it, then I can directly plot it. After I save it under the same folder, I use .idxmax to find the maximum value in the index of the group I just created for the plot, which is 17, and it means 5:00 PM - 5:59 PM as the busiest hour with most bicycle counts. 

## Bonus: Datetime Formats
Python has three common ways to represent dates and times:

- **Python `datetime.datetime`**: A built-in Python class for representing individual dates and times. It is easy to use for general date operations.

- **NumPy `datetime64`**: A NumPy data type designed for efficiently storing and processing arrays of dates and times.

- **Pandas datetime**: Built on NumPy's datetime functionality and provides convenient tools for analyzing dates in DataFrames, such as extracting hours, days, and years.