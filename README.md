# Diagnostic_Upload
Use this repository to download diagnostic code templates and upload your new diagnostics to be integrated into the hub.

## For more information on LaunchPAD and the diagnostics that have been created and how they work please see:

https://github.com/Priority-on-African-Diagnostics/LaunchPAD/blob/master/README.md

## Cloning and creating diagnostics

Once you have set up github on your computer (https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) you can clone the whole Diagnostic_Upload repository. __The directory you are in when you clone the repository needs to be added to the *diagnostic*\_config.py in the home_add field as described above. This needs to be done in the config file of each diagnostic you want to run.__

\> git clone git@github.com:Priority-on-African-Diagnostics/Diagnostic_Upload.git

If you would rather only clone one or a selection of diagnostics you can. If you take this approach you must always clone the files/CONFIG area with your diagnostics of choice. Follow the steps below that show how to pull only the new temploate New_Diag:

\> git clone --filter=blob:none --no-checkout  https://github.com/Priority-on-African-Diagnostics/Diagnostic_Upload.git

\> cd Diagnostic_Upload/

\> git sparse-checkout set DIAGNOSTICS/New_Diag/ files/CONFIG

\> git checkout master

Create a copy of the New_Diag folder with the *diagnostic* name of your choice and make edits to that folder

To run diagnostics on JASMIN move to the DIAGNOSTICS/*diagnostic* of your choice and alter home_add in *diagnostic*\_config.py is described above. Load the jaspy module (> *load jaspy*) and run *diagnostic*.py. Figure will appear in the plots directory and any intermediary netcdf files will appear in intermediary_files. 

If you are not running on JASMIN you can load any conda environment that contains modules in files/CONFIG and *diagnostic*.py before running the diagnostic. 

## Push your new diagnostic back to this repository

git add $new diagnostic folder

git commit –m “$message to describe your new changes” 

git push –u origin $master 

---------
