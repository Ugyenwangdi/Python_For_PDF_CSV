# Note
# MS = Petrol
# HSD = High Speed Diesel (HSD) Diesel Oil 
# SKO = Superior Kerosene Oil (SKO) Kerosenes 


import tabula as tb

def convert_to_csv():
    # To convert pdf files to csv files with file names = 1, 2, 3,...., n
    for x in range(1220):
        x += 1
        try:
            file = "FuelData"+"\\"+"{}.pdf".format(x)     # for 1 - 500
            # file = "SecondFuelData"+"\\"+"{}.pdf".format(x)  # for 518 - 1218

            # file = "518.pdf"

            table = tb.read_pdf(file, pages='all')

            # csv file
            csv_table = tb.convert_into(file, 'CSVconverted'+'\\'+'{}.csv'.format(x), pages='all') # for 1 - 500

            # csv_table = tb.convert_into(file, 'CSVconverted2'+'\\'+'{}.csv'.format(x), pages='all') # for 518 - 1218
            # csv_table = tb.convert_into(file, '518.csv', pages='all')

        finally:
            continue

def remove_repeated():

    # To remove the duplicates from from the above converted files
    for i in range(1220):
        i += 1
        try:
            with open('CSVconverted' + '\\' + '{}.csv'.format(i),'r') as in_file, open('CSVremovedRepeated' + '\\' + '{}.csv'.format(i),'w') as out_file:   # for 1 - 500

            # with open('CSVconverted2' + '\\' + '{}.csv'.format(i),'r') as in_file, open('CSVremovedRepeated2' + '\\' + '{}.csv'.format(i),'w') as out_file:  # for 518 - 1218
            # with open('518.csv','r') as in_file, open('518converted.csv','w') as out_file:

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
        pass


