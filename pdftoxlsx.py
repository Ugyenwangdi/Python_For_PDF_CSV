# Note
# MS = Petrol
# HSD = High Speed Diesel (HSD) Diesel Oil 
# SKO = Superior Kerosene Oil (SKO) Kerosenes 


import tabula as tb
import pandas as pd
import os

# # To convert pdf files to csv files with file names = 1, 2, 3,...., n
# for x in range(20):
#     x += 1
#     try:
#         file = "FuelData"+"\\"+"{}.pdf".format(x)
#         table = tb.read_pdf(file, pages='all')

#         # csv file
#         csv_table = tb.convert_into(file, 'CSVconverted'+'\\'+'{}.csv'.format(x), pages='all')
#     finally:
#         continue


# # To remove the duplicates from from the above converted files
# for i in range(11):
#     if i != 0:
#         with open('CSVconverted' + '\\' + '{}.csv'.format(i),'r') as in_file, open('CSVremovedRepeated' + '\\' + '{}.csv'.format(i),'w') as out_file:
#             seen = set() # set 
#             for line in in_file:
#                 if line in seen: 
#                     continue # skip duplicate

#                 seen.add(line)
#                 out_file.write(line)
#                 # out_file.close()




# ################################ List the rows to add to csv file ##############
# # Python program to read CSV file line by line
# # import necessary packages
# import csv

# ls = []
# # Open file
# with open('CSVremovedRepeated' + '\\' + '{}.csv'.format(1),'r') as file_obj:
	
# 	# Create reader object by passing the file
# 	# object to reader method
# 	reader_obj = csv.reader(file_obj)
	
# 	# Iterate over each row in the csv
# 	# file using reader object
# 	for row in reader_obj:
# 		ls.append(row)
# print(ls)
# print(item[0].split("#") for item in ls)



#################################### Add to Final file #################
# Write CSV file final

# Python program to demonstrate
# writing to CSV


# import csv
	
# # field names
# fields = ['Station', 'Region', 'Product', 'Approved Date', 'RSP/KL', 'RSP/L'] # , 'RSP/KL', 'RSP/L'
	
# # data rows of csv file
# rows = [ ['Nikhil', 'COE', '2', '9.0', '2', '9.0'],
# 		['Sanchit', 'COE', '2', '9.1', '2', '9.0'],
# 		['Aditya', 'IT', '2', '9.3', '2', '9.0'],
# 		['Sagar', 'SE', '1', '9.5', '2', '9.0'],
# 		['Prateek', 'MCE', '3', '7.8', '2', '9.0'],
# 		['Sahil', 'EP', '2', '9.1', '2', '9.0']]
	
# # name of csv file
# filename = "bhutan_fuel_prices.csv"
	
# # writing to csv file
# with open(filename, 'w', newline='') as csvfile:
# 	# creating a csv writer object
# 	csvwriter = csv.writer(csvfile)
		
# 	# writing the fields
# 	csvwriter.writerow(fields)
		
# 	# writing the data rows
# 	csvwriter.writerows(rows)












# from pathlib import Path

# for child in Path('CSVconverted').iterdir():
#     # print(f"{child.name}")
#     with open('{}'.format(child.name),'r') as in_file, open('CSVremovedRepeated' + '\\' + '{}'.format(child.name),'w') as out_file:
#         seen = set() # set 
#         for line in in_file:
#             if line in seen: 
#                 continue # skip duplicate

#             seen.add(line)
#             out_file.write(line)
#             # out_file.close()









# for excel extraction, we have to export the data to the dataframe
# we are using pandas library

# df = pd.concat(table)

# excel_file = df.to_excel('pdf_convert.xlsx')