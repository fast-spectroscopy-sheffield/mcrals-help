# mcrals-help

This repository aims to help with using [MCR-ALS](https://mcrals.wordpress.com/) (MATLAB toolbox) to perform deconvolution of datasets such as time-resolved photoluminescence and transient absorption. The scripts provided here are aimed more at TA data, but can easily be edited for use with TRPL data. The scripts are written mainly in python. I would recommend [miniconda](https://docs.conda.io/en/latest/miniconda.html) to start, and install packages that you need as you go ([pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/), [matplotlib](https://matplotlib.org/), [scipy](https://www.scipy.org/) etc.).

Follow the instructions on the [MCR-ALS website](https://mcrals.wordpress.com/) to get the MATLAB toolbox. You'll need a MATLAB installation on your machine. Have a read of the publications listed there as well.

### dataset processing

To convert TA data from the CSV files output by our homebuilt TA setup to UFS files required by [Surface Xplorer](https://ultrafastsystems.com/surface-xplorer-data-analysis-software/), use the code found [here](https://bitbucket.org/ptapping/csv2ufs/src/master/).

TA data should first be processed in [Surface Xplorer](https://ultrafastsystems.com/surface-xplorer-data-analysis-software/) before attempting [MCR-ALS](https://mcrals.wordpress.com/). Common operations include cropping, background subtration, bad spectra removal and chirp correction.

TRPL data from the iCCD can be joined together into a single kinetic using the app found [here](https://github.com/fast-spectroscopy-sheffield/iCCD-kinetics).

### preparation of datasets for MCR-ALS

Download the repository and unzip it somewhere. Keep it for reference.

Copy the `scripts` folder to the directory where you will be working. The folder structure should look something like this:
```
directory\
	scripts
	processed_data
```
The `processed_data` folder should contain CSV files of the processed dataset(s) you want to work with.

Open your favourite python IDE (e.g. [spyder](https://www.spyder-ide.org/)) and open up all the python files in the copied `scripts` folder. You want to be able to edit and run them.

To begin with, you want to edit (as appropriate) and run `prepare_data.py`. The editing of the script should be obvious from the comments in the file. This will create a folder `MCR-ALS` containing subfolders for each dataset. Within each subfolder there are several files: `data.csv` is the original dataset, `wavelengths.csv` is the wavelength axis, `times.csv` is the time axis and `array.csv` is the dataset without the wavelength and time axes, as required by MCR-ALS. If you decided to remove the pump scatter spectral region, you should also save `wavelengths_all.csv` containing the untrimmed wavelength axis.

You are now in a position to run MCR-ALS on individual datasets, one at a time.

MCR-ALS for individual datasets.
