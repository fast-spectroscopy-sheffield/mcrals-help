import os
import pandas as pd
import numpy as np
      

# specify datasets to post-process
folders = [
    'folder_1',
    'folder_2',
    'folder_3'
    ]

# give the components names
component_names = ['C1', 'C2']

# iterate through specificed datasets
for folder in folders:
    
    # path to combined data folder
    save_folder = os.path.join('..', 'MCR-ALS', folder)
    
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
    copt = np.loadtxt(os.path.join(save_folder, 'copt.csv'), delimiter=',')
    times = np.loadtxt(os.path.join(save_folder, 'times.csv'), delimiter=',')
    
    # save concentrations
    concentrations = pd.DataFrame(index=times, columns=component_names, data=copt)
    concentrations.to_csv(os.path.join(save_folder, 'mcrals_concentrations.csv'), header=True, index=True)
    

