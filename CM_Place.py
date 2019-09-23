import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.pyplot import *
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import griddata

file = '.\data\OTTAWA 2006.csv'
data_f = 'test.txt'
with open(file,encoding='utf-8',errors='ignore') as f:
    reader = csv.reader(f)
    head_row = next(reader)

    #for index,name in enumerate(head_row):
    #    print(index,name)

    max_temps = []
    lats = []
    longs = []
    points = []

    for i, row in enumerate(reader):
        if i >= 31:
            try:
                lat = float(row[1])
                long = float(row[2])
                max_temp = float(row[7])
            except ValueError:
                print(row[0],'N/A')
            else:
                if long<=0:
                    lats.append(lat)
                    longs.append(long)
                    max_temps.append(max_temp)

    for i in range(len(lats)):
        point = []
        point.append(longs[i])
        point.append(lats[i])
        points.append(point)

    points = np.array(points)
    max_temps = np.array(max_temps)
    fig = plt.figure(dpi=300, figsize=(10, 6))
    xi = np.linspace(min(longs), max(longs), 100)
    yi = np.linspace(min(lats), max(lats), 100)
    X, Y = np.meshgrid(xi, yi)
    zi = griddata(points,max_temps, (X, Y), method='nearest')

    plt.contourf(xi,yi,zi)

    plt.title('Temperatures of SURREY WHITE ROCK in 1987')
    plt.xlabel('Date', fontsize='12')
    fig.autofmt_xdate()
    plt.ylabel('T', fontsize='12')
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.legend(loc=2)

    ylim(-15, 35)

    plt.show()

f1 = open(data_f,'w')
for i in range(0,len(longs)):
    f1.write(str(longs[i])+str(',')+str(lats[i])+str(',')+str(max_temps[i])+'\n')

f1.close()