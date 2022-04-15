

# ################################ Extract the rows of csv file and store it in the list so that I can update the data in the rows like extracting the dates and regions later ##############
# # Python program to read CSV file line by line
# # import necessary packages
import csv

# def update_csv(name):

#     ls = []
#     # Open file
#     with open('CSVremovedRepeated' + '\\' + '{}.csv'.format(name),'r') as file_obj:
        
#         # Create reader object by passing the file
#         # object to reader method
#         reader_obj = csv.reader(file_obj)
        
#         # Iterate over each row in the csv
#         # file using reader object
#         for row in reader_obj:
#             ls.append(row)
#     # print(ls)


#     # Extract the new data from heading
#     new_dta = []
#     for i in ls:
#         header = i[0]
#         header = header.split("#")[0]
#         header = header.split("NEW PRICI NG DETA ILS")
#         header = header[1].split(":")
#         header = header[1:]
#         # print(header)
#         region = header[0].replace("Product", "")
#         # print(region)
#         product = header[1].replace("Approved Date", "")
#         # print(product)
#         approved_date = header[2].replace("\n", "")
#         # print(approved_date)
        
#         new_dta = [region, product, approved_date]
#         # print(new_dta)
#         break

#     ############### From the above list to delete the first item for each list item ######
#     for i in ls:
#         i = i.pop(0)
#     # print(ls)


#     ######### prepare a column and rows #############

#     # extract column 1 for the column header
#     cols = ls[1]

#     newlst = ['Region', 'Product', 'Approved_Date']
#     newcols = newlst + cols  # ['Region', 'Product', 'Approved_Date', 'Station', 'RSP/KL', 'RSP/L']
#     # print(newcols)

#     # select rows for row values
#     # insert values for 'Region', 'Product', 'Approved_Date' in the row_data list
#     row_data = ls[2:]
#     new_rows = []
#     for item in row_data:
#         item = new_dta + item
#         new_rows.append(item)

#         # print(item)
#     # print(new_rows[:5])




#     # ############ ############### Create a csv file with new rows and columns added ##### ########
#     # import csv
        
#     # # writing to csv file

#     with open('AddedColAndRowsCSV' + '\\' + '{}.csv'.format(name), 'w', newline='') as csvfile:
#         # creating a csv writer object
#         csvwriter = csv.writer(csvfile)
            
#         # writing the fields
#         csvwriter.writerow(newcols)
            
#         # writing the data rows
#         csvwriter.writerows(new_rows)

# # do it for all 20 files
# for i in range(2):
#     i += 1
#     try:
#         update_csv(i)
#     finally:
#         continue


################# To merge all the csv files .. THis merges only the files present in the directory
# cd into the directory which has multiple csv files
# copy *.csv fuel_data.csv 


import pandas as pd


df = pd.read_csv("AddedColAndRowsCSV"+ "\\" + "fuel_data.csv")
df =  df[df.Region != "Region"] 

# df.column_name != whole string from the cell
# now, all the rows with the column: Name and Value: "dog" will be deleted

df.to_csv('bhutan_fuel_prices.csv', index=False)
