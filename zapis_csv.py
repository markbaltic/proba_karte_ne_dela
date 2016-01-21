import csv

a = {'2016-08-19': {'VoloteaAPI': 119.25}, '2016-08-29': {'VoloteaAPI': 47.28}, '2016-08-24': {'VoloteaAPI': 47.28}, '2016-08-10': {'VoloteaAPI': 78.12}, '2016-08-01': {'VoloteaAPI': 57.56}, '2016-08-22': {'VoloteaAPI': 57.56}, '2016-08-03': {'VoloteaAPI': 78.12}, '2016-08-31': {'VoloteaAPI': 47.28}, '2016-08-26': {'VoloteaAPI': 119.25}, '2016-08-17': {'VoloteaAPI': 57.56}, '2016-08-12': {'VoloteaAPI': 139.81}, '2016-08-08': {'VoloteaAPI': 78.12}, '2016-08-05': {'VoloteaAPI': 139.81}, '2016-08-15': {'VoloteaAPI': 78.12}}
b = {'2016-08-18': 57.56, '2016-08-23': 57.56, '2016-08-11': 98.68, '2016-08-25': 47.28, '2016-08-30': 57.56, '2016-08-16': 78.12, '2016-08-02': 78.12, '2016-08-09': 78.12, '2016-08-04': 98.68}



##writer = csv.writer(open('dict.csv', 'wb'))
##for key, value in b.items():
##   writer.writerow([key, value])

ryanair_21_1 = {'2016-09-29': 33.99, '2016-10-02': 33.99, '2016-06-19': 57.99, '2016-06-05': 40.99, '2016-08-14': 67.99, '2016-06-30': 48.99, '2016-10-09': 33.99, '2016-04-28': 30.59, '2016-05-08': 30.59, '2016-07-24': 48.99, '2016-08-11': 57.99, '2016-09-22': 40.99, '2016-07-14': 40.99, '2016-07-07': 48.99, '2016-06-26': 48.99, '2016-07-03': 48.99, '2016-05-22': 36.89, '2016-08-07': 67.99, '2016-08-28': 40.99, '2016-08-21': 48.99, '2016-06-12': 48.99, '2016-05-12': 22.54, '2016-10-20': 33.99, '2016-05-01': 22.54, '2016-10-06': 33.99, '2016-09-08': 33.99, '2016-06-02': 48.99, '2016-09-11': 33.99, '2016-06-23': 40.99, '2016-07-17': 57.99, '2016-06-09': 40.99, '2016-05-26': 22.54, '2016-05-29': 33.99, '2016-10-27': 33.99, '2016-08-25': 48.99, '2016-07-28': 57.99, '2016-09-25': 33.99, '2016-07-31': 67.99, '2016-05-15': 30.59, '2016-09-04': 40.99, '2016-05-19': 22.54, '2016-10-16': 33.99, '2016-07-10': 48.99, '2016-05-05': 22.54, '2016-09-15': 33.99, '2016-09-18': 33.99, '2016-09-01': 40.99, '2016-07-21': 57.99, '2016-08-04': 67.99, '2016-10-23': 33.99, '2016-10-13': 33.99, '2016-08-18': 57.99, '2016-06-16': 40.99}
volotea_21_1 = {'2016-08-05': 139.81, '2016-08-24': 47.28, '2016-08-19': 119.25, '2016-07-18': 57.56, '2016-07-13': 47.28, '2016-08-08': 78.12, '2016-09-02': 119.25, '2016-07-04': 98.68, '2016-08-10': 78.12, '2016-07-29': 139.81, '2016-08-31': 47.28, '2016-08-26': 119.25, '2016-07-20': 57.56, '2016-08-12': 139.81, '2016-08-17': 57.56, '2016-08-03': 78.12, '2016-08-01': 57.56, '2016-07-22': 139.81, '2016-06-27': 78.12, '2016-08-22': 57.56, '2016-07-11': 78.12, '2016-08-15': 78.12, '2016-07-27': 57.56, '2016-06-29': 57.56, '2016-07-06': 57.56, '2016-07-25': 57.56, '2016-08-29': 47.28}

with open('volotea_21_1.csv','w', encoding='utf-8', ) as f:
    w = csv.writer(f)
    w.writerows(volotea_21_1.items())

#print(len(volotea_21_1))