import pandas as pd
import csv

# file_threshold is the number of desired rows in a file
file_threshold = 119
# file_count labels the alternation in file name
file_count = 1
# 239 for 8.5  / 119 for 17GB
# division_checker check the number of files that will be created
division_checker = int(18446 / 119)
# skip is the number of rows to skip when creating new file
skip = 0
# row1 is the header we want to repeat for all files
row1 = ['Beneficiary Msisdn','Beneficiary Name', 'Voice(Minutes)', 'Data (MB) (1024MB = 1GB)','Sms(Unit)']

print(division_checker)

for x in range(division_checker):

    df = pd.read_csv("Uploads January 9 2024 - 17gb - b1-b155.csv", index_col=False, sep=",", nrows=file_threshold, skiprows=skip, header=0, dtype='object')
    df.columns = row1
    # dtype='object' formats the xlsx to add leading zeroes to the file

    print(df)
    # CSV FILES/ write = df.to_csv("Uploads October 3 - 10gb - b"+str(file_count)+".csv", header=1, index=False)
    write = df.to_excel("Uploads January 9 2024 - 17gb - b"+str(file_count)+".xlsx", header=1, index=False)
    # FOR XLSX FILES
    file_count += 1
    skip = skip + 119




