"""
THESE SCRIPTS ARE DESIGNED TO BE EDITED - READ THE COMMENTS TO SEE WHERE
"""

import os
import pandas as pd
import numpy as np


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    

# specify path to folder containing the processed data
data_folder = os.path.join('..', 'processed_data')

# make MCR-ALS folder for saving stuff
mcrals_folder = os.path.join('..', 'MCR-ALS')
create_folder(mcrals_folder)

# iterate through the files in the processed data folder
# you could also specify a list of particular files instead
for filename in os.listdir(data_folder):
    
    if filename.endswith('.csv'):  # select only csv files
        
        # create folder for each inidividual file within MCR-ALS
        save_folder = os.path.join(mcrals_folder, filename.replace('.csv', ''))
        create_folder(save_folder)
        
        # load the data into a pandas DataFrame
        filepath = os.path.join(data_folder, filename)
        df = pd.read_csv(filepath, header=0, index_col=0)
        
        # convert column headers (times) to float (might need different replace strings for different kinds of dataset)
        df.columns = [float(x.replace('E+0.1', 'E+0')) for x in df.columns]
        
        # optional - crop wavelength range
        df = df[(df.index > 375) & (df.index < 695)]
        
        # remove wavelengths where everything is NaN
        df.dropna(how='all', axis=0, inplace=True)
        
        # optional - remove pump scatter region
        np.savetxt(os.path.join(save_folder, 'wavelengths_all.csv'), df.index.values, delimiter=',')
        df.drop(df.index[(df.index > 520) & (df.index < 550)].values, inplace=True, axis=0)
        
        # remove time points containing NaN
        df.dropna(how='any', axis=1, inplace=True)
        
        # save the data, the bare array and the wavlength and time axes
        df.to_csv(os.path.join(save_folder, 'data.csv'), header=True, index=True)
        np.savetxt(os.path.join(save_folder, 'array.csv'), df.values, delimiter=',')
        np.savetxt(os.path.join(save_folder, 'times.csv'), df.columns.values, delimiter=',')
        np.savetxt(os.path.join(save_folder, 'wavelengths.csv'), df.index.values, delimiter=',')