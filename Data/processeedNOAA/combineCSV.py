# Program to combine avy data CSVs for one season into one aggregate CSV
#       55 variables for X data
#       See readme for variable codes.

import numpy as np
import pandas as pd
import os


# first element -> variables
# second element: longitude
# third element: latitude

directory = "C:/Users/daven/Documents/avydatacleaning/processeedNOAA"
# use list to store data first then create DataFrame using a list


#%%


# create list of col names for new csv. init csv with col names
x_avy = []
x_avy_col_names = []

i = 0

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        if f.endswith('csv'):
            df = pd.read_csv(f)
            # print(df.head())
            x_avy_col_names.append(df.columns[0])
            x_avy.append(df.iloc[:, 0])
print(x_avy_col_names)
print(x_avy)

#%%
x_avy = np.asarray(x_avy)
print(x_avy.shape)
# print(x_avy)
print(x_avy)

#%%
n = 9
averaged_day = np.zeros((54, 161))
print(averaged_day)
#%%


for i in range(54):
    averaged_day[i] = np.average(x_avy[i].reshape(-1,n),axis=1)




print(averaged_day.shape)
print(averaged_day)

#%%
print(len(x_avy_col_names))
print(averaged_day.shape)
print(x_avy_col_names)


#%%


d = {}
i = 0
for name in x_avy_col_names:
    d[name] = (averaged_day[i].tolist())
    i += 1

print(d.keys())
# theres two entries for pres and uwnd
# pres = tropopause_geopotential_height && ?
# uwnd = u_wind && ?
#%%
print(len(d.keys()))

#%%
newcsv = pd.DataFrame(d, index=pd.date_range(start='11/25/2019', end='05/03/2020'))
print(newcsv.shape)


#%%
# get lon/lat coordinates added in
# get dates added in

# coordinates = []
# df = pd.read_csv("accum_snow_2019-2020.csv")
# coord_col_1 = df.columns[1]
# coord_col_2 = df.columns[2]
# print(coord_col_1)
# coordinates.append(df.iloc[:, 1])
# coordinates.append(df.iloc[:, 2])
#
# coordinates = np.asarray(coordinates)
# print(coordinates)
# newcsv[coord_col_1] = (coordinates[0].tolist())
# newcsv[coord_col_2] = (coordinates[1].tolist())


# NO COORDINATES NEEDED TOOK AVERAGES
print(len(newcsv.columns))
print(newcsv.index)

#%%
print(newcsv.head)
print(newcsv.shape)

newcsv.to_csv("x_data_2019-2020_totals")

#%%
#every 9th element a new day starts
# take averages for every group of 9 elements

print(df)