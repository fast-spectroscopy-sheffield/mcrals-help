% specify a folder e.g. 'combined'
folder = 'combined';

% save spectra and concentrations
csvwrite(['..', 'MCR-ALS', folder, '\copt.csv'], copt);
csvwrite(['..', 'MCR-ALS', folder, '\sopt.csv'], transpose(sopt));