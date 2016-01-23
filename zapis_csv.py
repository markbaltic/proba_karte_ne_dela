import csv
from volotea_api import VoloteaAPI
from ryanair_api import RyanairAPI
import time

###meseci do marca naprej in stevilo dni v mesecu
dnevi_v_letu = [('03', 31),('04', 30),('05', 31),('06', 30),('07', 31),('08', 31),('09', 30),('10', 31),('11', 30),('12',31)]

ryanair_cene = RyanairAPI().get('TSF', 'CFU', dnevi_v_letu, '2016')
volotea_cene = VoloteaAPI().get('VCE', 'CFU', dnevi_v_letu, '2016')
ryanair_return_cene = RyanairAPI().get('CFU', 'TSF', dnevi_v_letu, '2016')
volotea_return_cene = VoloteaAPI().get('CFU', 'VCE', dnevi_v_letu, '2016')

#zapisejo slovarje v csv
with open('volotea_{0}.csv'.format(time.strftime("%Y-%m-%d")),'w', encoding='utf-8', ) as f:
    w = csv.writer(f)
    w.writerows(volotea_cene.items())

with open('ryanair_{0}.csv'.format(time.strftime("%Y-%m-%d")),'w', encoding='utf-8', ) as f:
    w = csv.writer(f)
    w.writerows(ryanair_cene.items())

with open('volotea_return_{0}.csv'.format(time.strftime("%Y-%m-%d")),'w', encoding='utf-8', ) as f:
    w = csv.writer(f)
    w.writerows(volotea_return_cene.items())

with open('ryanair_return_{0}.csv'.format(time.strftime("%Y-%m-%d")),'w', encoding='utf-8', ) as f:
    w = csv.writer(f)
    w.writerows(ryanair_return_cene.items())


###primer slovarja cen
# ryanair_21_1_TSF_CFU = {'2016-09-29': 33.99, '2016-10-02': 33.99, '2016-06-19': 57.99, '2016-06-05': 40.99, '2016-08-14': 67.99, '2016-06-30': 48.99, '2016-10-09': 33.99, '2016-04-28': 30.59, '2016-05-08': 30.59, '2016-07-24': 48.99, '2016-08-11': 57.99, '2016-09-22': 40.99, '2016-07-14': 40.99, '2016-07-07': 48.99, '2016-06-26': 48.99, '2016-07-03': 48.99, '2016-05-22': 36.89, '2016-08-07': 67.99, '2016-08-28': 40.99, '2016-08-21': 48.99, '2016-06-12': 48.99, '2016-05-12': 22.54, '2016-10-20': 33.99, '2016-05-01': 22.54, '2016-10-06': 33.99, '2016-09-08': 33.99, '2016-06-02': 48.99, '2016-09-11': 33.99, '2016-06-23': 40.99, '2016-07-17': 57.99, '2016-06-09': 40.99, '2016-05-26': 22.54, '2016-05-29': 33.99, '2016-10-27': 33.99, '2016-08-25': 48.99, '2016-07-28': 57.99, '2016-09-25': 33.99, '2016-07-31': 67.99, '2016-05-15': 30.59, '2016-09-04': 40.99, '2016-05-19': 22.54, '2016-10-16': 33.99, '2016-07-10': 48.99, '2016-05-05': 22.54, '2016-09-15': 33.99, '2016-09-18': 33.99, '2016-09-01': 40.99, '2016-07-21': 57.99, '2016-08-04': 67.99, '2016-10-23': 33.99, '2016-10-13': 33.99, '2016-08-18': 57.99, '2016-06-16': 40.99}
# volotea_21_1_VCE_CFU = {'2016-08-05': 139.81, '2016-08-24': 47.28, '2016-08-19': 119.25, '2016-07-18': 57.56, '2016-07-13': 47.28, '2016-08-08': 78.12, '2016-09-02': 119.25, '2016-07-04': 98.68, '2016-08-10': 78.12, '2016-07-29': 139.81, '2016-08-31': 47.28, '2016-08-26': 119.25, '2016-07-20': 57.56, '2016-08-12': 139.81, '2016-08-17': 57.56, '2016-08-03': 78.12, '2016-08-01': 57.56, '2016-07-22': 139.81, '2016-06-27': 78.12, '2016-08-22': 57.56, '2016-07-11': 78.12, '2016-08-15': 78.12, '2016-07-27': 57.56, '2016-06-29': 57.56, '2016-07-06': 57.56, '2016-07-25': 57.56, '2016-08-29': 47.28}
#print(time.strftime("%Y-%m-%d"))

###zbrise prazne vrstice in \n na koncu vrstice ter doda v prvi stolpec danasnji datum
# with open('volotea_return_{0}.csv'.format(time.strftime("%Y-%m-%d")),'r', encoding='utf-8', ) as beri:
# 	with open('danes_volotea_return_{0}.csv'.format(time.strftime("%Y-%m-%d")),'w', encoding='utf-8', ) as pisi:
# 		for vrstica in beri:
# 			vrstica = vrstica.strip()
# 			if len(vrstica) > 0:
# 				print(time.strftime("%Y-%m-%d") + ',' + vrstica,file = pisi)

###ko pozenem spet, se \n na koncu vrstice spet pojavi...
#a = []
# with open('danes_volotea_return_{0}.csv'.format(time.strftime("%Y-%m-%d")),'r', encoding='utf-8', ) as beri:
# 	for vrstica in beri:
# 		a.append(vrstica)
# 		print(vrstica)
#print(a)
