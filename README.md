# mcrals-help

This repository aims to help with using [MCR-ALS](https://mcrals.wordpress.com/) (MATLAB toolbox) to perform deconvolution of datasets such as time-resolved photoluminescence and transient absorption. The scripts provided here are aimed more at TA data, but can easily be edited for use with TRPL data. The scripts are written mainly in python. I would recommend [miniconda](https://docs.conda.io/en/latest/miniconda.html) to start, and install packages that you need as you go ([pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/), [matplotlib](https://matplotlib.org/), [scipy](https://www.scipy.org/) etc.).

These scripts are examples only, but they give an idea of how to prepare datasets for MCR-ALS. They are designed to be edited for each use case. You can achieve the same thing with Origin, for example.

Please read [this publication](https://doi.org/10.1016/j.chemolab.2014.10.003) before using MCR-ALS.

Follow the instructions on the [MCR-ALS website](https://mcrals.wordpress.com/) to get the MATLAB toolbox. You'll need a MATLAB installation on your machine. Have a read of [this publication](https://doi.org/10.1016/j.chemolab.2014.10.003). I would recommend saving the `mcr_toolbox2` folder to your `MATLAB` folder.

### dataset processing

To convert TA data from the CSV files output by our homebuilt TA setup to UFS files required by [Surface Xplorer](https://ultrafastsystems.com/surface-xplorer-data-analysis-software/), use the code found [here](https://bitbucket.org/ptapping/csv2ufs/src/master/).

TA data should first be processed in [Surface Xplorer](https://ultrafastsystems.com/surface-xplorer-data-analysis-software/) before attempting [MCR-ALS](https://mcrals.wordpress.com/). Common operations include cropping, background subtraction, bad spectra removal and chirp correction.

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

### MCR-ALS for individual datasets

Launch MATLAB. Navigate to your `MATLAB` folder where the `mcr_toolbox2` folder is saved.
```
Right click > Add to Path > Selected Folders and Subfolders
```
Load the `mcr_main.m` file into the Editor window. Change your working directory to the copied `scripts` folder and open `loadfiles.m`. Edit the folder name as desired, comment out the reference spectra loading if not required then run the script to load the necessary data.

Run the `mcr_main.m` file and follow the prompts. Refer to documentation (e.g. [this paper](https://doi.org/10.1016/j.chemolab.2014.10.003)) for help.

Once you have obtained a deconvolution that you are happy with, change the folder in `savefiles.m` as appropriate and run the script to save the outputs.

Back in python, edit the folder names in `individual_post_mcrals.py` and run it. This adds the wavelength and time axes back on to the MCR-ALS outputs.

### MCR-ALS for combined datasets

It can be sensible to run a single deconvolution on multiple datasets, for example a power series where the spectral components should remain the same but the dynamics (concentrations) might change. Not all spectral components need to be present in each dataset.

To begin with, run `combine_datasets.py`, first changing the folder list to reflect the datasets you want to combine. You should specify a working folder name as well (default is just `combined`).

Next, repeat the MCR-ALS process as you would for a single dataset, remembering to change the folder name to the combined working folder. On the second screen of the MCR-ALS GUI, specify the number of submatrices (i.e. how many datasets did you combine).

In the next window, select column-wise augmented (since we are keeping spectral components constant). Using the `nrows.csv` file output in the combined working folder, enter the number of rows of each submatrix.

Next you have the option to apply constraints to all submatrices or specify constraints for individual datasets. Here you also tell the program whether or not all spectral components are present in all datasets. Read the section on `isp_matrix` in the [paper](https://doi.org/10.1016/j.chemolab.2014.10.003).

Once the MCR-ALS has finished, edit and run `combined_post_mcrals.py`, which splits the concentration results into the individual datasets and saves them along with the spectra.
