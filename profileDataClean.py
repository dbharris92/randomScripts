# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 19:25:33 2018

A script to clean and plot elevation profile data generated from QGIS Profile Tool
Includes orignal and smoothed values

@author: Drew
"""
### import packages
import pandas as pd
import matplotlib.pyplot as plt 

### import CSV
dataFrame = pd.read_csv('FCprofile.csv')

### create distance in miles column
dataFrame['distance_mi'] = dataFrame['Distance_ft'] / 5280

### drop the Distance_ft column
del dataFrame['Distance_ft']

### round elevation values to zero decimals
dataFrame['Elev_ft'] = dataFrame['Elev_ft'].round(0)

### round distance_mi values to one decimal
dataFrame['distance_mi'] = dataFrame['distance_mi'].round(1)

### remove duplicate rows
dataFrame2 = dataFrame.drop_duplicates(keep= 'first')

###############################
### plot data in line graph ###
###############################

### declare x and y axis
#y = dataFrame2['Elev_ft']
#x = dataFrame2['distance_mi']

### generate line plot
#plt.plot(x,y)
#plt.title('Thermal Belt Rail Trail Elevation Profile \n Gilkey to Forest City')
#plt.ylabel('Elevation (ft)')
#plt.xlabel('Distance (mi)')
#plt.show

###############################################
### drop distance duplicates to smooth data ###
###############################################

dataFrameI = dataFrame.drop_duplicates(subset = ['distance_mi'], keep= 'first')

y = dataFrameI['Elev_ft']
x = dataFrameI['distance_mi']

### generate line plot
plt.plot(x,y, 'g')
plt.title('Elevation Profile')
plt.ylabel('Elevation (ft)')
plt.xlabel('Distance (mi)')
plt.axis([0, 14, 265, 350])

### show points along the way
plt.text(0, 330, 'Gilkey')
plt.text(10.5, 273, 'FW Hunt School')



plt.show
