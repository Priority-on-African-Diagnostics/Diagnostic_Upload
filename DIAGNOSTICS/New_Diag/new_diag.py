# -*- coding: utf-8 -*-

###############################
# Start of file:
#
# **Please edit this section with your diagnostic name
# and your affiliation!**
#
# New Diag 
# 
# Author(s): 
# 
# Based on diagnostic scripts from 
# 
###############################

###############################
#import required libraries

#**please edit this list for your diagnostic!***
###############################
import os
import iris
import iris.coords
import iris.analysis
import iris.analysis.cartography
import iris.plot as iplt
import iris.quickplot as qplt
from iris.experimental.equalise_cubes import equalise_attributes
import matplotlib.pyplot as plt
import iris.coord_categorisation 
import numpy as np
import numpy.ma as ma
import sys
import cartopy
import cartopy.crs as ccrs
import matplotlib.dates as mdates
import collections
import cartopy
import cartopy.crs as crs
import cartopy.feature as cfeature
import cloudpickle as pickle
import operator
import xarray as xr
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from pylab import *

from new_diag_config import *
sys.path.insert(1,home_add+'LaunchPAD/files/CONFIG')
from find_files import *
from config import *
from config_functions import *

###############################
#unpickle files
###############################    
def unpickle_cubes(path):
    """Load cube list from path."""
    with open(path, 'rb') as fh:
        cubes = pickle.load(fh)
    return cubes	

###############################
#Extraction function(s)
###############################


def load_expt(expt, vari):

     CUBE = iris.load(monthly_file_location(expt, vari))
     return CUBE
	
###############################
#calculation function(s)
###############################

def calc(expt, vari):
    
    calcval = vari
    
    return val
    	
###############################
#plot diagnostic
###############################

def plot(green_list):
           
    return None
        
###############################
#main execution
###############################
if pre_processor_experiments:
    print('entering pre-processor models routine')

    green_list = create_greenlist(vari_list)
    green_list =obs_list+green_list
    pickle.dump(green_list, open(starterp+'green_list'+p_file, "wb" ))
    print('new mod list', green_list)

    for expt in green_list:
        for vari in vari_list:
            if vari == 'ua':
                CUBE = load_expt(expt,vari)
                pickle.dump(CUBE, open(starterp+expt+'_'+vari+'_'+'CUN'+p_file, "wb" ))
                
        print('model data from '+expt+' pre-processed sucessfully')
             
###############################
#Calculation control
###############################

if processor_calculations:
    print('entering CALCULATION routines')

    green_list = unpickle_cubes(starterp+'green_list'+p_file)
    for expt in green_list:
        for vari in vari_list:
	
 	            CUBE_CALC = calc(expt,vari)    
              pickle.dump(CUBE_CALC, open(starterp+expt+'_'+'CUBE_CALC'+'_'+p_file, "wb"))
                
###############################
      
###############################
#Plotting control
###############################

if create_plot:

    print('entering PLOTTING routines')

    green_list = unpickle_cubes(starterp+'green_list'+p_file)
    for vari in vari_list:
        plot(green_list)

    print('plotting complete')
         
###############################
#End of file
###############################	
