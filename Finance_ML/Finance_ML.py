# CONVICTIONSUMMARY_270_opt3_best2(1).csv

import csv

with open('Assets\CONVICTIONSUMMARY_270_opt3_best2(1).csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif row[4] == ' MERGED ':
            print(f'\t{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} ')
            line_count += 1
    print(f'Processed {line_count} lines.')
