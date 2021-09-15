# -*- coding: utf-8 -*-
###############################

###############################
# Start of file:
#
# New Diag
# 
# Author(s): 
#  
# Based on diagnostic scripts from 

# #############################

#OPTIONS for new diagnostic that can be changed by the user

#model name list?
obs_list = []

vari_list = [] 

#what do you want script to do?
pre_processor_experiments = True
processor_calculations = True
create_plot = True
save_plot = True

#file name (.p files) note: model name superseeds this string
p_file = '_new_diag.p'

#file name (.nc file) note: model name superseeds this string
nc_file = '_new_diag.nc'

#file name (.png plot) note: model name superseeds this string
plot_file = '_new_diag_plot.png'

#new users need to edit this: the path to where you have pulled the Diagnostic_Upload repository
home_add =''

starterp = home_add+'Diagnostic_Upload/DIAGNOSTICS/New_Diag/intermediary_files/'
starterpng = home_add+'Diagnostic_Upload/DIAGNOSTICS/New_Diag/plots/'
starternc = home_add+'Diagnostic_Upload/DIAGNOSTICS/New_Diag/intermediary_files/'
