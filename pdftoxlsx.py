# Note
# MS = Petrol
# HSD = High Speed Diesel (HSD) Diesel Oil 
# SKO = Superior Kerosene Oil (SKO) Kerosenes 


import tabula as tb

def convert_to_csv():
    # To convert pdf files to csv files with file names = 1, 2, 3,...., n
    for x in range(20):
        x += 1
        try:
            file = "FuelData"+"\\"+"{}.pdf".format(x)
            table = tb.read_pdf(file, pages='all')

            # csv file
            csv_table = tb.convert_into(file, 'CSVconverted'+'\\'+'{}.csv'.format(x), pages='all')
        finally:
            continue

def remove_repeated():

    # To remove the duplicates from from the above converted files
    for i in range(20):
        i += 1
        try:
            with open('CSVconverted' + '\\' + '{}.csv'.format(i),'r') as in_file, open('CSVremovedRepeated' + '\\' + '{}.csv'.format(i),'w') as out_file:
                seen = set() # set 
                for line in in_file:
                    if line in seen: 
                        continue # skip duplicate

                    seen.add(line)
                    out_file.write(line)
                    # out_file.close()
        finally:
            continue


if __name__ == "__main__":

    try:
        convert_to_csv()
        remove_repeated()
    except:
        print("Couldn't perform convert")



# # Note
# # MS = Petrol
# # HSD = High Speed Diesel (HSD) Diesel Oil 
# # SKO = Superior Kerosene Oil (SKO) Kerosenes 


# import tabula as tb

# def convert_to_csv():
#     # To convert pdf files to csv files with file names = 1, 2, 3,...., n
#     for x in range(20):
#         x += 1
#         try:
#             file = "FuelData"+"\\"+"fuel1.pdf"
#             table = tb.read_pdf(file, pages='all')

#             # csv file
#             csv_table = tb.convert_into(file, 'detail.csv', pages='all')
#         finally:
#             continue

# def remove_repeated():

#     # To remove the duplicates from from the above converted files
#     for i in range(20):
#         i += 1
#         try:
#             with open('detail.csv','r') as in_file, open('finaldetail.csv','w') as out_file:
#                 seen = set() # set 
#                 for line in in_file:
#                     if line in seen: 
#                         continue # skip duplicate

#                     seen.add(line)
#                     out_file.write(line)
#                     # out_file.close()
#         finally:
#             continue


# if __name__ == "__main__":

#     try:
#         convert_to_csv()
#         remove_repeated()
#     except:
#         print("Couldn't perform convert")







