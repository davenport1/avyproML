# script for cleaning and processing .nc files
# will convert data to readable/processable .csv file
# sorts out all data not in relevant latitude and longitude for sierra region
# LAT/LON:
# range from W to E: 119 44'46" W --> 120 33'07" W
# range from S to N:  38 26'12" N -->  39 39'51" N
# run with filename for NC file and desired CSV name

import netCDF4 as nc
import numpy as np
import xarray as xr
import os
import re


def nc_processor(filename, csvname,var):
    ds = nc.Dataset(filename)
    print(ds.variables.keys())

    data = xr.open_dataset(filename)
    df = data[['time',var]].to_dataframe()
    index_drop = df[ (df['lat'] < 38.436667) | (df['lat'] > 39.664167) ].index
    df.drop(index_drop, inplace=True)

    index_drop = df[ (df['lon'] < -120.551944) | (df['lon'] > -119.746111)].index
    df.drop(index_drop, inplace=True)
    df.shape
    df.to_csv(csvname, index=False)


def last_var(filename):
    ds = nc.Dataset(filename)
    # get last element in ds.variables.keys()
    # return element
    list_of_vars = list(ds.variables.keys())
    return list_of_vars[-1]


def filenames_to_csv():
    filenames = list()
    directory = 'C:/Users/daven/Documents/avydatacleaning/NOAAdata/season2019'
    for filename in os.listdir(directory):
        f=os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            if(f.endswith('.nc')):
                f= re.sub('nc$', 'csv', f)
                f = f[50:]
                filenames.append(f)
            ## need to change this to first check if its an nc file,
                ## if the csv corresponding to it exists,
                ## then change name to end with .csv and add to list before returning list
    return filenames



#%%
# run above function with NC file names and desired CSV file name
# need to figure out last variable in keys

csv_file_names = filenames_to_csv()
print(csv_file_names)

#%%
directory = 'C:/Users/daven/Documents/avydatacleaning/NOAAdata/season2019'
i = 0
for filename in os.listdir(directory):
    f=os.path.join(directory, filename)
    if os.path.isfile(f):
        if f.endswith('.nc'):
            nc_processor(f, csv_file_names[i], last_var(f))
            i += 1

#%%
