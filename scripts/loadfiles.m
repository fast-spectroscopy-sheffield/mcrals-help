% THESE SCRIPTS ARE DESIGNED TO BE EDITED - READ THE COMMENTS TO SEE WHERE

% specify a folder e.g. 'combined'
folder = 'combined';

data_path = ['../MCR-ALS/', folder];
addpath(data_path)

% load the data
data = transpose(importdata([data_path '/array.csv']));

% load reference spectra
ref = transpose(importdata(['../', 'MCR-ALS/', 'reference_spectra/', 'ref_spectra.csv']));