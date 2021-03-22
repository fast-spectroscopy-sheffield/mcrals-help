"""
THESE SCRIPTS ARE DESIGNED TO BE EDITED - READ THE COMMENTS TO SEE WHERE
"""

import os
import pandas as pd
import numpy as np
      

# specify datasets that were combined
folders = [
    'folder_1',
    'folder_2',
    'folder_3'
    ]

# give the components names
component_names = ['S', 'T']

# path to combined data folder
save_folder = os.path.join('..', 'MCR-ALS', 'combined')

# load wavelengths
wavelengths_all = np.loadtxt(os.path.join(save_folder, 'wavelengths_all.csv'), delimiter=',')  # if pump scatter was removed
wavelengths = np.loadtxt(os.path.join(save_folder, 'wavelengths.csv'), delimiter=',')

# load MCR-ALS fitted spectra
spectra = np.loadtxt(os.path.join(save_folder, 'sopt.csv'), delimiter=',')
spectra = pd.DataFrame(index=wavelengths, columns=component_names, data=spectra)

# run this bit only if pump scatter was removed - it puts NaN values where pump scatter was
full_index_df = pd.DataFrame(index=wavelengths_all, columns=['dummy'])
spectra = spectra.join(full_index_df, how='right')
spectra.drop('dummy', inplace=True, axis=1)

# save spectra
spectra.to_csv(os.path.join(save_folder, 'mcrals_spectra.csv'), header=True, index=True)

# load time axis stuff
np_nrows = np.loadtxt(os.path.join(save_folder, 'nrows.csv'), delimiter=',', dtype=int)
copt = np.loadtxt(os.path.join(save_folder, 'copt.csv'), delimiter=',')
times = np.loadtxt(os.path.join(save_folder, 'times.csv'), delimiter=',')

# split concentrations according to nrows and save with time axis
row = 0
for i, nrows in enumerate(np_nrows):
    concentrations = copt[row:row+nrows, :]
    time = times[row:row+nrows]
    concentrations = pd.DataFrame(index=time, columns=component_names, data=concentrations)
    row += nrows
    concentrations.to_csv(os.path.join(save_folder, 'mcrals_concentrations_{0}.csv'.format(folders[i])), header=True, index=True)
    

