% specify a folder e.g. 'combined'
folder = 'combined';

% load the data
data = transpose(importdata(['..', 'MCR-ALS', folder, '\array.csv']));

% load reference spectra
data = transpose(importdata(['..', 'MCR-ALS', 'reference_spectra', '\ref_spectra.csv']));