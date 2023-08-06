# Limonade-plot-utils

Limonade is a library meant to simplify handling of list mode data from different sources. The scripts 
provided in limonade-plot-utils are example scripts on how to plot and sort list-mode data with limonade 
and matplotlib.

Included are:
* **read_list_data:** Load and plot list mode data using specific plot configuration. 
  * By default the data is loaded with the
  setup frozen in the data directory, but different detector configuration can be given.
  * Only part of the data can be plotted by using time-slices.
  * Histograms can be exported to comma separated ASCII-files.
  * Histograms can be exported to .phd files with command line inputs for efficiency calibration files and data 
  collection information. 
* **read_hist_data:** Load and plot comma separated ASCII-files saved with read_list_data. The metadata contains all 
    the necessary information.
* **setup_dirs:** setup the local configuration directory.

## Installation
It is preferable to either use the pip install limonade_plot_utils --user parameter with pip, or install to a virtual 
environment because the operating system may prevent writing path environment to system site_packages -directory.

