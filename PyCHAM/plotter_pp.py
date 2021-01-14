'''plots results for the total particle-phase concentration temporal profiles of specified components'''
# simulation results are represented graphically

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import LinearSegmentedColormap # for customised colormap
import matplotlib.ticker as ticker # set colormap tick labels to standard notation
import os
import retr_out
import numpy as np
import scipy.constants as si

def plotter(caller, dir_path, comp_names_to_plot):
	
	# inputs: ------------------------------------------------------------------
	# caller - marker for whether PyCHAM (0) or tests (2) are the calling module
	# dir_path - path to folder containing results files to plot
	# comp_names_to_plot - chemical scheme names of components to plot
	# --------------------------------------------------------------------------

	# chamber condition ---------------------------------------------------------
	# retrieve results
	(num_sb, num_comp, Cfac, yrec, Ndry, rbou_rec, x, timehr, comp_names, 
		y_MW, _, _, y_MV, _, wall_on, space_mode, _, _, _) = retr_out.retr_out(dir_path)
	
	# number of actual particle size bins
	num_asb = (num_sb-wall_on)

	if (caller == 0):
		plt.ion() # show results to screen and turn on interactive mode
		
	# prepare plot
	fig, (ax0) = plt.subplots(1, 1, figsize = (14, 7))

	if (comp_names_to_plot): # if component names specified
	
		# concentration plot ---------------------------------------------	
		for i in range(len(comp_names_to_plot)):
			
			# get index of this specified component, removing any white space
			indx_plot = comp_names.index(comp_names_to_plot[i].strip())
			
			# particle-phase concentrations of all components (molecules/cc)
			if (wall_on == 1): # wall on
				ppc = yrec[:, num_comp:-num_comp]
			if (wall_on == 0): # wall off
				ppc = yrec[:, num_comp::]
			
			# particle-phase concentration of this component over all size bins (molecules/cc)
			conc = ppc[:, indx_plot::num_comp]
			# particle-phase concentration (ug/m3)
			conc = ((conc/si.N_A)*y_MW[indx_plot])*1.e12
			
			# plot this component
			ax0.plot(timehr, conc.sum(axis = 1), '+', linewidth = 4., label = str(str(comp_names[indx_plot ])+' (total particle-phase)'))

		ax0.set_ylabel(r'Concentration ($\rm{\mu}$g$\,$m$\rm{^{-3}}$)', fontsize = 14)
		ax0.set_xlabel(r'Time through simulation (hours)', fontsize = 14)
		ax0.yaxis.set_tick_params(labelsize = 14, direction = 'in')
		ax0.xaxis.set_tick_params(labelsize = 14, direction = 'in')
		ax0.legend(fontsize = 14)

		# end of gas-phase concentration sub-plot ---------------------------------------
	

	# display
	if (caller == 2):
		plt.show()	

	return()