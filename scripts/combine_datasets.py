"""
THESE SCRIPTS ARE DESIGNED TO BE EDITED - READ THE COMMENTS TO SEE WHERE
"""

import os
import pandas as pd
import numpy as np


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


# give path to MCR-ALS folder
mcrals_path = os.path.join('..', 'MCR-ALS')        

# specify datasets to combine
folders = [
    'folder_1',
    'folder_2',
    'folder_3'
    ]

# create folder to save combined datasets
save_folder = os.path.join('..', 'MCR-ALS', 'combined')
create_folder(save_folder)

# initialise tuples for combined data and time axis
combined_array = ()
combined_times = ()

# combine the datas and times of the specified datasets, writing the number of time points in each to nrows.csv
with open(os.path.join(save_folder, 'nrows.csv'), 'w+') as f:
    for folder in folders:
        wavelengths_all = np.loadtxt(os.path.join(mcrals_path, folder, 'wavelengths_all.csv'), delimiter=',')  # if pump scatter was removed
        wavelengths = np.loadtxt(os.path.join(mcrals_path, folder, 'wavelengths.csv'), delimiter=',')
        array = np.loadtxt(os.path.join(mcrals_path, folder, 'array.csv'), delimiter=',')
        times = np.loadtxt(os.path.join(mcrals_path, folder, 'times.csv'), delimiter=',')
        combined_array += (array,)
        combined_times += (times,)
        f.write(str(times.shape[0])+'\n')        
combined_array = np.hstack(combined_array)
combined_times = np.hstack(combined_times)

# save
np.savetxt(os.path.join(save_folder, 'array.csv'), combined_array, delimiter=',')
np.savetxt(os.path.join(save_folder, 'times.csv'), combined_times, delimiter=',')

np.savetxt(os.path.join(save_folder, 'wavelengths_all.csv'), wavelengths_all, delimiter=',')  # if pump scatter was removed
np.savetxt(os.path.join(save_folder, 'wavelengths.csv'), wavelengths, delimiter=',')


