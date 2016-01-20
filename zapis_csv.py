import csv

a = {'2016-08-19': {'VoloteaAPI': 119.25}, '2016-08-29': {'VoloteaAPI': 47.28}, '2016-08-24': {'VoloteaAPI': 47.28}, '2016-08-10': {'VoloteaAPI': 78.12}, '2016-08-01': {'VoloteaAPI': 57.56}, '2016-08-22': {'VoloteaAPI': 57.56}, '2016-08-03': {'VoloteaAPI': 78.12}, '2016-08-31': {'VoloteaAPI': 47.28}, '2016-08-26': {'VoloteaAPI': 119.25}, '2016-08-17': {'VoloteaAPI': 57.56}, '2016-08-12': {'VoloteaAPI': 139.81}, '2016-08-08': {'VoloteaAPI': 78.12}, '2016-08-05': {'VoloteaAPI': 139.81}, '2016-08-15': {'VoloteaAPI': 78.12}}
b = {'2016-08-18': 57.56, '2016-08-23': 57.56, '2016-08-11': 98.68, '2016-08-25': 47.28, '2016-08-30': 57.56, '2016-08-16': 78.12, '2016-08-02': 78.12, '2016-08-09': 78.12, '2016-08-04': 98.68}



##writer = csv.writer(open('dict.csv', 'wb'))
##for key, value in b.items():
##   writer.writerow([key, value])


with open('mycsvfile.csv','w', encoding='utf-8', ) as f:
    w = csv.writer(f)
    w.writerows(b.items())
