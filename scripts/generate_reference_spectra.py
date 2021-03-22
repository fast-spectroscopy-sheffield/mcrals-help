"""
THESE SCRIPTS ARE DESIGNED TO BE EDITED - READ THE COMMENTS TO SEE WHERE
"""

import os
import pandas as pd
import numpy as np


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        

# give the filepath to the data from which reference spectra are to be obtained
filepath = os.path.join('..', 'processed_data', 'filename.csv')

# give the filepath to the a folder in which reference spectra are to be saved
save_folder = os.path.join('..', 'MCR-ALS', 'reference_spectra')
create_folder(save_folder)

# load the data into a pandas DataFrame
df = pd.read_csv(filepath, header=0, index_col=0)

# convert column headers (times) to float
df.columns = [float(x.replace('E+0.1', 'E+0')) for x in df.columns]

# optional - crop wavelength range
df = df[(df.index > 375) & (df.index < 695)]

# remove wavelengths where everything is NaN
df.dropna(how='all', axis=0, inplace=True)

# optional - remove pump scatter region
df.drop(df.index[(df.index > 520) & (df.index < 550)].values, inplace=True, axis=0)

# remove time points containing NaN
df.dropna(how='any', axis=1, inplace=True)

# reference spectrum 1 will be early time spectrum - say 0.5-1ps averaged
component_1_ref = df.loc[:, (df.columns > 0.1) & (df.columns < 0.2)].mean(axis=1)
component_1_ref /= component_1_ref.max()

# reference spectrum 2 will be late time spectrum - say 3-7ns averaged
component_2_ref = df.loc[:, (df.columns > 3000) & (df.columns < 7000)].mean(axis=1)
component_2_ref /= component_2_ref.max()

# combine reference spectra into a single array without wavelength values
ref_spectra = np.transpose(np.vstack((component_1_ref.values, component_2_ref.values)))

# save
np.savetxt(os.path.join(save_folder, 'ref_spectra.csv'), ref_spectra, delimiter=',')