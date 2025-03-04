import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# import modules for data visualization and analysis(part B)

csv = open('D:\\UWA SEM1\\BUSN5101 Programming for Business\\airports.csv')
# create a variable 'csv' to store the airports.csv file

airport_location = open('D:\\UWA SEM1\\BUSN5101 Programming for Business\\Airport Location.txt', 'w')
# the above text file is created to add airport names, Latitudes and Longitudes
# a new text file is created in the desired directory if no text file is present in the directory python creates the
# file the w denotes the file is writable

airport_specific = open('D:\\UWA SEM1\\BUSN5101 Programming for Business\\Airport Specific.txt', 'w')
#  Airport names with -> 32o< lat < 37o and -100o < long< -80o

negative_long = open('D:\\UWA SEM1\\BUSN5101 Programming for Business\\Negative Longitude.txt', 'w')
# this file includes airport names with negative longitude values

# empty lists is created

comma_list = []  # list is created because there are commas in original data file
airport_list = []  # converting csv file to a list
neg = []  # for negative longitude values

# Lists below created for data visualization
coordinate_plot_lat = []
coordinate_plot_long = []

for row in csv:
    airport_list.append(row.split(','))
# using a for loop to iterate over each row in the csv file, split the data with delimiter(,) and saving it to
# airport_list


# writing the headers to text file
negative_long.write(
    (airport_list[0][1] + '  ' + '\n') + (airport_list[0][5] + '    ') + (airport_list[0][6] + '\n' + '\n'))
airport_specific.write(airport_list[0][1] + '\n')

# removing rows which has comma and adding them to a new list
for element in airport_list:
    if len(element) == 8:
        airport_list.remove(element)
        comma_list.append(element)

# add data to text files airport names with latitude and longitude, specific coordinates range with airport names and
# add latitude and longitude values to different list for scatter diagram
for i in range(1, len(airport_list)):
    airport_location.write((airport_list[i][1] + '       \n') + (airport_list[i][5] + '     ')
                           + (airport_list[i][6] + '\n' + '\n'))

    # using indexing to access the nested list. adding '\n' so data written goes to new line which improves readability
    # blank spaces so data is not cluttered together
    # the first row had header names so 1 is added to take the iteration to next row

    if 32 < float(airport_list[i][5]) < 37 and -100 < float(airport_list[i][6]) < -80:
        airport_specific.write(airport_list[i][1] + '\n')
    if float(airport_list[i][6]) < 0:
        negative_long.write(
            (airport_list[i][1] + '  ' + '\n') + (airport_list[i][5] + '    ') + (airport_list[i][6] + '\n' + '\n'))
        coordinate_plot_lat.append(airport_list[i][5])
        coordinate_plot_long.append(airport_list[i][6])
        neg.append(airport_list[i][6])

# a separate for loop is created for the lis with commas in data file and same data is written in text files and lists
for i in range(len(comma_list)):
    if 32 < float(comma_list[i][6]) < 37 and -100 < float(comma_list[i][7]) < -80:
        airport_specific.write(comma_list[i][1] + '\n')
    if float(comma_list[i][7]) < 0:
        negative_long.write(
            (comma_list[i][1] + '  ' + '\n') + (comma_list[i][6] + '    ') + (comma_list[i][7] + '\n' + '\n'))
        coordinate_plot_lat.append(comma_list[i][6])
        coordinate_plot_long.append(comma_list[i][7])
        neg.append(comma_list[i][7])



