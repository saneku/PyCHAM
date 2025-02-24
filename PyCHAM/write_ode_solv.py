##########################################################################################
#                                                                                        											 #
#    Copyright (C) 2018-2022 Simon O\'Meara : simon.omeara@manchester.ac.uk                  				 #
#                                                                                       											 #
#    All Rights Reserved.                                                                									 #
#    This file is part of PyCHAM                                                         									 #
#                                                                                        											 #
#    PyCHAM is free software: you can redistribute it and/or modify it under              						 #
#    the terms of the GNU General Public License as published by the Free Software       					 #
#    Foundation, either version 3 of the License, or (at your option) any later          						 #
#    version.                                                                            										 #
#                                                                                        											 #
#    PyCHAM is distributed in the hope that it will be useful, but WITHOUT                						 #
#    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS       			 #
#    FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more              				 #
#    details.                                                                            										 #
#                                                                                        											 #
#    You should have received a copy of the GNU General Public License along with        					 #
#    PyCHAM.  If not, see <http://www.gnu.org/licenses/>.                                 							 #
#                                                                                        											 #
##########################################################################################
'''generate the module to solve ODEs'''
# writes a module based on the supplied chemical scheme and user inputs,
# since the solved ODEs can represent gas-phase photochemistry,
# gas-particle partitioning and gas-wall partitioning, note use %f when
# writing floats from inputs

import datetime

# function to generate the ordinary differential equation (ODE)
# solver file
def ode_gen(con_infl_indx, int_tol, rowvals, num_comp, 
		num_asb, testf, eqn_num, sav_nam, pcont, self):
	
	# inputs: ------------------------------------------------
	# con_infl_indx - indices of components with continuous influx
	# int_tol - integration tolerances
	# rowvals - indices of rows for Jacobian
	# self.wall_on - marker for whether to consider wall 
	# 	partitioning
	# num_comp - number of components
	# num_asb - number of actual size bins (excluding wall)
	# testf - marker for whether in test mode or not
	# eqn_num - number of gas- and particle-phase reactions
	# self.dil_fac - fraction of chamber air extracted/s
	# sav_nam - name of file to save results to
	# pcont - flag for whether seed particle injection is 
	#	instantaneous (0) or continuous (1)
	# self - reference to PyCHAM
	# -------------------------------------------------------
	
	# create new  file to store solver module
	f = open('PyCHAM/ode_solv.py', mode='w')
	f.write('##########################################################################################\n')
	f.write('#                                                                                        											 #\n')
	f.write('#    Copyright (C) 2018-2022 Simon O\'Meara : simon.omeara@manchester.ac.uk                  				 #\n')
	f.write('#                                                                                       											 #\n')
	f.write('#    All Rights Reserved.                                                                									 #\n')
	f.write('#    This file is part of PyCHAM                                                         									 #\n')
	f.write('#                                                                                        											 #\n')
	f.write('#    PyCHAM is free software: you can redistribute it and/or modify it under              						 #\n')
	f.write('#    the terms of the GNU General Public License as published by the Free Software       					 #\n')
	f.write('#    Foundation, either version 3 of the License, or (at your option) any later          						 #\n')
	f.write('#    version.                                                                            										 #\n')
	f.write('#                                                                                        											 #\n')
	f.write('#    PyCHAM is distributed in the hope that it will be useful, but WITHOUT                						 #\n')
	f.write('#    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS       			 #\n')
	f.write('#    FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more              				 #\n')
	f.write('#    details.                                                                            										 #\n')
	f.write('#                                                                                        											 #\n')
	f.write('#    You should have received a copy of the GNU General Public License along with        					 #\n')
	f.write('#    PyCHAM.  If not, see <http://www.gnu.org/licenses/>.                                 							 #\n')
	f.write('#                                                                                        											 #\n')
	f.write('##########################################################################################\n')
	f.write('\'\'\'solution of ODEs, generated by eqn_pars.py\'\'\'\n')
	f.write('# module to solve system of ordinary differential equations (ODEs) using solve_ivp of Scipy \n')
	f.write('# File Created at %s\n' %(datetime.datetime.now()))	
	f.write('\n')
	f.write('import numpy as np\n')
	f.write('import scipy.sparse as SP\n')
	f.write('from scipy.integrate import solve_ivp\n')
	f.write('\n')	
	f.write('# define function\n')
	f.write('def ode_solv(y, integ_step, rindx, pindx, rstoi, pstoi, \n')
	f.write('	nreac, nprod, rrc, jac_stoi, njac, jac_den_indx, \n')
	f.write('	jac_indx, Cinfl_now, y_arr, y_rind, uni_y_rind, \n')
	f.write('	y_pind, uni_y_pind, reac_col, prod_col, \n')
	f.write('	rstoi_flat, pstoi_flat, rr_arr, rr_arr_p,\n') 
	f.write('	rowvals, colptrs, num_comp, num_sb,\n')
	f.write('	Psat, Cw, act_coeff, kw, jac_wall_indx,\n') 
	f.write('	core_diss, kelv_fac, kimt, num_asb,\n')
	f.write('	jac_part_indx, jac_extr_indx,\n')
	f.write('	rindx_aq, pindx_aq, rstoi_aq, pstoi_aq,\n')
	f.write('	nreac_aq, nprod_aq, jac_stoi_aq, njac_aq, jac_den_indx_aq, jac_indx_aq,\n')
	f.write('	y_arr_aq, y_rind_aq, uni_y_rind_aq, y_pind_aq, uni_y_pind_aq,\n')
	f.write('	reac_col_aq, prod_col_aq, rstoi_flat_aq,\n')
	f.write('	pstoi_flat_aq, rr_arr_aq, rr_arr_p_aq, eqn_num, jac_mod_len,\n')
	f.write('	jac_part_hmf_indx, rw_indx, N_perbin, jac_part_H2O_indx,\n')
	f.write('	H2Oi, Cinfl_nowp_indx,\n')
	f.write('	Cinfl_nowp, self):\n')
	f.write('\n')
	f.write('	# inputs: -------------------------------------\n')
	f.write('	# y - initial concentrations (# molecules/cm3)\n')
	f.write('	# integ_step - the maximum integration time step (s)\n')
	f.write('	# rindx - index of reactants per equation\n')
	f.write('	# pindx - index of products per equation\n')
	f.write('	# rstoi - stoichiometry of reactants\n')
	f.write('	# pstoi - stoichiometry of products\n')
	f.write('	# nreac - number of reactants per equation\n')
	f.write('	# nprod - number of products per equation\n')
	f.write('	# rrc - reaction rate coefficient\n')
	f.write('	# jac_stoi - stoichiometries relevant to Jacobian\n')
	f.write('	# njac - number of Jacobian elements affected per equation\n')
	f.write('	# jac_den_indx - index of component denominators for Jacobian\n')
	f.write('	# jac_indx - index of Jacobian to place elements per equation (rows)\n')
	f.write('	# Cinfl_now - influx of components with continuous influx \n')
	f.write('	#		(# molecules/cm3/s)\n')
	f.write('	# y_arr - index for matrix used to arrange concentrations of gas-phase reactants, \n')
	f.write('	#	enabling calculation of reaction rate coefficients \n')
	f.write('	# y_rind - index of y relating to reactants for reaction rate \n')
	f.write('	# 	coefficient equation\n')
	f.write('	# uni_y_rind - unique index of reactants \n')
	f.write('	# y_pind - index of y relating to products\n')
	f.write('	# uni_y_pind - unique index of products \n')
	f.write('	# reac_col - column indices for sparse matrix of reaction losses\n')
	f.write('	# prod_col - column indices for sparse matrix of production gains\n')
	f.write('	# rstoi_flat - 1D array of reactant stoichiometries per equation\n')
	f.write('	# pstoi_flat - 1D array of product stoichiometries per equation\n')
	f.write('	# rr_arr - index for reaction rates to allow reactant loss\n')
	f.write('	# 	calculation\n')
	f.write('	# rr_arr_p - index for reaction rates to allow reactant loss\n')
	f.write('	# 	calculation\n')
	f.write('	# rowvals - row indices of Jacobian elements\n')
	f.write('	# colptrs - indices of  rowvals corresponding to each column of the\n') 
	f.write('	# 	Jacobian\n')
	f.write('	# num_comp - number of components\n')
	f.write('	# num_sb - number of size bins\n')
	f.write('	# self.wall_on - flag saying whether to include wall partitioning\n')
	f.write('	# Psat - pure component saturation vapour pressures (molecules/cm3)\n')
	f.write('	# Cw - effective absorbing mass concentration of wall (molecules/cm3) \n')
	f.write('	# act_coeff - activity coefficient of components\n')
	f.write('	# kw - mass transfer coefficient to wall (/s)\n')
	f.write('	# jac_wall_indx - index of inputs to Jacobian by wall partitioning\n')
	f.write('	# self.seedi - index of seed material\n')
	f.write('	# core_diss - dissociation constant of seed material\n')
	f.write('	# kelv_fac - kelvin factor for particles\n')
	f.write('	# kimt - mass transfer coefficient for gas-particle partitioning (s)\n')
	f.write('	# num_asb - number of actual size bins (excluding wall)\n')
	f.write('	# jac_part_indx - index for sparse Jacobian for particle influence \n')
	f.write('	# jac_extr_indx - index for sparse Jacobian for air extraction influence \n')
	f.write('	# rindx_aq - index of aqueous-phase reactants \n')
	f.write('	# eqn_num - number of gas- and aqueous-phase reactions \n')
	f.write('	# jac_mod_len - modification length due to high fraction of component(s)\n')
	f.write('	# 	in particle phase\n')
	f.write('	# jac_part_hmf_indx - index of Jacobian affected by water\n')
	f.write('	#	 in the particle phase\n')
	f.write('	# rw_indx - indices of rows affected by water in particle phase\n')
	f.write('	# N_perbin - number concentration of particles per size bin (#/cc)\n')
	f.write('	# jac_part_H2O_indx - sparse Jacobian indices for the effect of\n')
	f.write('	#	particle-phase water on all other components\n')
	f.write('	# H2Oi - index for water\n')
	f.write('	# self.dil_fac - dilution factor for chamber (fraction of chamber air removed/s)\n')
	f.write('	# self.RO2_indx - index of organic peroxy radicals\n')
	f.write('	# self.comp_namelist - chemical scheme names of components\n')
	f.write('	# self.Psat_Pa - saturation vapour pressure of components (Pa) at starting\n')
	f.write('	#	temperature of chamber\n')
	f.write('	# Cinfl_nowp_indx - index of particle-phase components with continuous influx \n')
	f.write('	# Cinfl_nowp - concentration (# molecules/cm3/s) of particle-phase components with\n')
	f.write('	#	continuous influx\n')
	f.write('	# self - reference to program \n')
	f.write('	# ---------------------------------------------\n')
	f.write('\n')
	
	# the module if needed for testing
	if (testf > 0):
		f.write('	# gas-particle partitioning-----------------\n')
		f.write('	# transform particle phase concentrations into\n')
		f.write('	# size bins in rows, components in columns\n')
		f.write('	ymat = (y[num_comp:num_comp*(num_asb+1), 0]).reshape(num_asb, num_comp)\n')
		f.write('	# total particle-phase concentration per size bin (molecules/cm3 (air))\n')
		f.write('	csum = ((ymat.sum(axis=1)-ymat[:, self.seedi])+((ymat[:, self.seedi]*core_diss))).reshape(-1, 1)\n')
		f.write('	# size bins with contents \n')
		f.write('	isb = (csum[:, 0]>0.)\n')
		f.write('	\n')
		f.write('	# container for gas-phase concentrations at particle surface\n')
		f.write('	Csit = np.zeros((num_asb, num_comp))\n')
		f.write('	# mole fraction of components at particle surface\n')
		f.write('	Csit[isb, :] = (ymat[isb, :]/csum[isb, :])\n')
		f.write('	\n')
		f.write('	return(Csit)\n')
		f.close() # close file
		return()


	# testing with 16 size bins and the MCM alpha-pinene chemical scheme
	# showed that using the vectorised Python code gave just 1 %
	# increase in wall clock time compared to using numba, and won't
	# give the gradual slow down in computation that arises with numba
	# when many integration time steps are set, furthermore it means that 
	# for fast integration systems, time isn't wasted on compilation, 
	# therefore we use the
	# vectorised form by default and the numba version is commented out 
	# below
	
	f.write('	def dydt(t, y): # define the ODE(s)\n')
	f.write('		\n')
	f.write('		# inputs: ----------------\n')
	f.write('		# y - concentrations (# molecules/cm3), note when using\n')
	f.write('		#	scipy integrator solve_ivp, this should have shape\n')
	f.write('		#	(number of elements, 1)\n')
	f.write('		# t - time interval to integrate over (s)\n')
	f.write('		# ---------------------------------------------\n')
	f.write('		\n')
	f.write('		# ensure y is correct shape\n')
	f.write('		if (y.shape[1] > 1):\n')
	f.write('			y = y[:, 0].reshape(-1, 1)\n')
	f.write('		# empty array to hold rate of change per component\n')
	f.write('		dd = np.zeros((y.shape[0], 1))\n')
	f.write('		\n')
	
	
	if (eqn_num[0] > 0): # if gas-phase reactions present
		f.write('		# gas-phase reactions -------------------------\n')
		f.write('		# empty array to hold relevant concentrations for\n')
		f.write('		# reaction rate coefficient calculation\n')
		f.write('		rrc_y = np.ones((rindx.shape[0]*rindx.shape[1]))\n')
		f.write('		rrc_y[y_arr] = y[y_rind, 0]\n')
		f.write('		rrc_y = rrc_y.reshape(rindx.shape[0], rindx.shape[1], order = \'C\')\n')
		f.write('		# reaction rate (molecules/cm3/s) \n')
		f.write('		rr = rrc[0:rindx.shape[0]]*((rrc_y**rstoi).prod(axis=1))\n')
		f.write('		# loss of reactants\n')
		f.write('		data = rr[rr_arr]*rstoi_flat # prepare loss values\n')
		f.write('		# convert to sparse matrix\n')
		f.write('		loss = SP.csc_matrix((data, y_rind, reac_col))\n')
		f.write('		# register loss of reactants\n')
		f.write('		dd[uni_y_rind, 0] -= np.array((loss.sum(axis = 1))[uni_y_rind])[:, 0]\n')
		f.write('		# gain of products\n')
		f.write('		data = rr[rr_arr_p]*pstoi_flat # prepare loss values\n')
		f.write('		# convert to sparse matrix\n')
		f.write('		loss = SP.csc_matrix((data, y_pind, prod_col))\n')
		f.write('		# register gain of products\n')
		f.write('		dd[uni_y_pind, 0] += np.array((loss.sum(axis = 1))[uni_y_pind])[:, 0]\n')
		f.write('		\n')

	if ('JPAC' in sav_nam): # wall losses for the Julich Plant and Atmosphere Chamber
		#f.write('		try:\n')
		f.write('		lr = 1./1200. # first order loss rate to wall (/s)\n')
		f.write('		lrnr = 1200. # first order loss rate to wall of non-radical ELVOC and LVOC (/s)\n')
		
		#f.write('		dd[0:num_comp][((self.Psat_Pa[0, :]> 3.8e2)*(self.Psat_Pa[0, :]<= 3.8e6))] -= y[0:num_comp][((self.Psat_Pa[0, :]> 3.8e2)*(self.Psat_Pa[0, :]<= 3.8e6))]*(0.)  \n')
		#f.write('		dd[(num_comp*num_sb)::][((self.Psat_Pa[0, :]> 3.8e2)*(self.Psat_Pa[0, :]<= 3.8e6))] += y[0:num_comp][((self.Psat_Pa[0, :]> 3.8e2)*(self.Psat_Pa[0, :]<= 3.8e6))]*(0.)  \n')
		
		#f.write('		dd[0:num_comp][((self.Psat_Pa[0, :]> 3.8e-2)*(self.Psat_Pa[0, :]<= 3.8e2))] -= y[0:num_comp][((self.Psat_Pa[0, :]> 3.8e-2)*(self.Psat_Pa[0, :]<= 3.8e2))]*(1./(lrnr-600))  \n')
		#f.write('		dd[(num_comp*num_sb)::][((self.Psat_Pa[0, :]> 3.8e-2)*(self.Psat_Pa[0, :]<= 3.8e2))] += y[0:num_comp][((self.Psat_Pa[0, :]> 3.8e-2)*(self.Psat_Pa[0, :]<= 3.8e2))]*(1./(lrnr-600))  \n')
		
		f.write('		dd[0:num_comp][((self.Psat_Pa[0, :]> 3.8e-6)*(self.Psat_Pa[0, :]<= 3.8e-2))] -= y[0:num_comp][((self.Psat_Pa[0, :]> 3.8e-6)*(self.Psat_Pa[0, :]<= 3.8e-2))]*(1./(lrnr-0)) \n')
		f.write('		dd[(num_comp*num_sb)::][((self.Psat_Pa[0, :]> 3.8e-6)*(self.Psat_Pa[0, :]<= 3.8e-2))] += y[0:num_comp][((self.Psat_Pa[0, :]> 3.8e-6)*(self.Psat_Pa[0, :]<= 3.8e-2))]*(1./(lrnr-0)) \n')		

		f.write('		dd[0:num_comp][((self.Psat_Pa[0, :]> 3.8e-10)*(self.Psat_Pa[0, :]<= 3.8e-6))] -= y[0:num_comp][((self.Psat_Pa[0, :]> 3.8e-10)*(self.Psat_Pa[0, :]<= 3.8e-6))]*(1./(lrnr+0)) # LVOCs following Sarrafzadeh et al. (2016) \n')
		f.write('		dd[(num_comp*num_sb)::][((self.Psat_Pa[0, :]> 3.8e-10)*(self.Psat_Pa[0, :]<= 3.8e-6))] += y[0:num_comp][((self.Psat_Pa[0, :]> 3.8e-10)*(self.Psat_Pa[0, :]<= 3.8e-6))]*(1./(lrnr+0)) # LVOCs following Sarrafzadeh et al. (2016) \n')
		
		f.write('		dd[0:num_comp][self.Psat_Pa[0, :] <= 3.8e-10] -= y[0:num_comp][self.Psat_Pa[0, :] <= 3.8e-10]*(1./lrnr) # ELVOCs following Ehn et al. (2014) \n')
		f.write('		dd[(num_comp*num_sb)::][self.Psat_Pa[0, :] <= 3.8e-10] += y[0:num_comp][self.Psat_Pa[0, :] <= 3.8e-10]*(1./lrnr) # ELVOCs following Ehn et al. (2014) \n')
		
		f.write('		dd[self.RO2_indices[:, 1]] -= y[self.RO2_indices[:, 1]]*(lr) # RO2 components following Silvia thesis\n')
		f.write('		dd[(num_comp*num_sb)+self.RO2_indices[:, 1]] += y[self.RO2_indices[:, 1]]*(lr) # RO2 components following Silvia thesis\n')

		f.write('		dd[self.comp_namelist.index(\'HO2\')] -= y[self.comp_namelist.index(\'HO2\')]*(lr) # following Silvia thesis \n')
		f.write('		dd[(num_comp*num_sb)+self.comp_namelist.index(\'HO2\')] += y[self.comp_namelist.index(\'HO2\')]*(lr) # following Silvia thesis \n')
		
		f.write('		dd[self.comp_namelist.index(\'SA\')] -= y[self.comp_namelist.index(\'SA\')]*(1./120.) # following Silvia email \n')
		f.write('		dd[(num_comp*num_sb)+self.comp_namelist.index(\'SA\')] += y[self.comp_namelist.index(\'SA\')]*(1./120.) # following Silvia email \n')
		
		f.write('		dd[self.comp_namelist.index(\'OH\')] -= y[self.comp_namelist.index(\'OH\')]*(4.) # following Silvia email (originally 4 /s)\n')
		f.write('		dd[(num_comp*num_sb)+self.comp_namelist.index(\'OH\')] += y[self.comp_namelist.index(\'OH\')]*(4.) # following Silvia email (originally 4 /s)\n')
		
		#f.write('		except:\n')
		#f.write('			dd[:] = dd[:]\n')
		f.write('		\n')

	if (eqn_num[1] > 0): # if particle-phase reactions present
		f.write('		# particle-phase reactions -------------------------\n')
		f.write('		\n')
		f.write('		# empty array to hold relevant concentrations for\n')
		f.write('		# reaction rate coefficient calculation\n')
		f.write('		# tile aqueous-phase reaction rate coefficients\n')
		f.write('		rr_aq = np.tile(rrc[rindx.shape[0]::], num_asb)\n')
		f.write('		# prepare aqueous-phase concentrations\n')
		f.write('		rrc_y = np.ones((rindx_aq.shape[0]*rindx_aq.shape[1]))\n')
		f.write('		rrc_y[y_arr_aq] = y[y_rind_aq, 0]\n')
		f.write('		rrc_y = rrc_y.reshape(rindx_aq.shape[0], rindx_aq.shape[1], order = \'C\')\n')
		f.write('		# reaction rate (molecules/cm3/s) \n')
		f.write('		rr = rr_aq*((rrc_y**rstoi_aq).prod(axis=1))\n')
		f.write('		# loss of reactants\n')
		f.write('		data = rr[rr_arr_aq]*rstoi_flat_aq # prepare loss values\n')
		f.write('		# convert to sparse matrix\n')
		f.write('		loss = SP.csc_matrix((data[0, :], y_rind_aq, reac_col_aq))\n')
		f.write('		# register loss of reactants\n')
		f.write('		dd[uni_y_rind_aq, 0] -= np.array((loss.sum(axis = 1))[uni_y_rind_aq])[:, 0]\n')
		f.write('		# gain of products\n')
		f.write('		data = rr[rr_arr_p_aq]*pstoi_flat_aq # prepare loss values\n')
		f.write('		# convert to sparse matrix\n')
		f.write('		loss = SP.csc_matrix((data[0, :], y_pind_aq, prod_col_aq))\n')
		f.write('		# register gain of products\n')
		f.write('		dd[uni_y_pind_aq, 0] += np.array((loss.sum(axis = 1))[uni_y_pind_aq])[:, 0]\n')
		f.write('		\n')
	
	if (len(con_infl_indx) > 0): # if a component has a continuous gas-phase influx
		
		f.write('		# account for components with continuous gas-phase influx\n')	
		f.write('		dd[[')	
		for Ci in range(len(con_infl_indx)):
			# components prior to the last in the continuous influx group
			if (Ci < len(con_infl_indx)-1):
				f.write('%d, ' %int(con_infl_indx[Ci]))
			else: # last component in the continuous influx group
				f.write('%d], 0] += Cinfl_now[:, 0]\n' %int(con_infl_indx[Ci]))

	#if ((pcont == 1).any()): # if there is continuous influx of seed particles
		
	#	f.write('		# account for components with continuous particle-phase influx\n')
	#	f.write('		if (len(Cinfl_nowp_indx) > 0): # if index available\n')	
	#	f.write('			dd[Cinfl_nowp_indx, 0] += Cinfl_nowp[:]\n')	
	#	f.write('		\n')

	if (self.dil_fac > 0): # if chamber air being extracted
		f.write('		# account for continuous extraction of chamber air\n')
		f.write('		if (self.wall_on == 1): # if wall on\n')
		f.write('			df_indx = np.ones((len(dd)-num_comp)).astype(\'int\') # index for estimating dilution factors\n')
		f.write('			df_indx[H2Oi::num_comp] = 0 # water diluted in water solver \n')
		f.write('			df_indx = df_indx==1 # transform to Boolean array \n')
		f.write('			dd[0:-num_comp, 0][df_indx] -= y[0:-num_comp, 0][df_indx]*1.*self.dil_fac\n')
		f.write('		if (self.wall_on == 0): # if wall off\n')
		f.write('			df_indx = np.ones((len(dd))).astype(\'int\') # index for estimating dilution factors\n')
		f.write('			df_indx[H2Oi::num_comp] = 0 # water diluted in water solver \n')
		f.write('			df_indx = df_indx==1 # transform to Boolean array \n')
		f.write('			dd[df_indx, 0] -= y[df_indx, 0]*1.*self.dil_fac\n')
		f.write('		\n')
		
	# note the following needs two indents (as for the reaction section), so that it
	# sits within the dydt function
	if (num_asb > 0): # include gas-particle partitioning in ode solver
		f.write('		# gas-particle partitioning-----------------\n')
		f.write('		# transform particle phase concentrations into\n')
		f.write('		# size bins in rows, components in columns\n')
		f.write('		ymat = (y[num_comp:num_comp*(num_asb+1), 0]).reshape(num_asb, num_comp)\n')
		f.write('		# force all components in size bins with no particle to zero\n')
		f.write('		ymat[N_perbin[:, 0] == 0, :] = 0\n')	
		f.write('		# total particle-phase concentration per size bin (molecules/cm3 (air))\n')
		f.write('		csum = ((ymat.sum(axis=1)-ymat[:, self.seedi].sum(axis=1))+((ymat[:, self.seedi]*core_diss).sum(axis=1)).reshape(-1)).reshape(-1, 1)\n')
		f.write('		# tile over components\n')
		f.write('		csum = np.tile(csum, [1, num_comp])\n')
		f.write('		# size bins with contents\n')
		f.write('		isb = (csum[:, 0] > 0.)\n')
		f.write('		\n')
		f.write('		if (any(isb)): # if particle-phase components present\n')
		f.write('			# container for gas-phase concentrations at particle surface\n')
		f.write('			Csit = np.zeros((num_asb, num_comp))\n')
		f.write('			# mole fraction of components at particle surface\n')
		f.write('			Csit[isb, :] = (ymat[isb, :]/csum[isb, :])\n')	
		f.write('			# gas-phase concentration of components at\n')
		f.write('			# particle surface (molecules/cm3 (air))\n')
		f.write('			Csit[isb, :] = Csit[isb, :]*Psat[isb, :]*kelv_fac[isb]*act_coeff[isb, :]\n')	
		f.write('			# partitioning rate (molecules/cm3/s)\n')
		f.write('			dd_all = kimt*(y[0:num_comp, 0].reshape(1, -1)-Csit)\n')
		f.write('			# gas-phase change\n')
		f.write('			dd[0:num_comp, 0] -= dd_all.sum(axis=0)\n')
		f.write('			# particle change\n')
		f.write('			dd[num_comp:num_comp*(num_asb+1), 0] += (dd_all.flatten())\n')
		f.write('		\n')
		
	if (self.wall_on > 0): # include gas-wall partitioning in ode solver
		f.write('		# gas-wall partitioning ----------------\n')
		f.write('		# concentration on wall (# molecules/cm3 (air))\n')
		f.write('		Csit = y[num_comp*(num_asb+1):num_comp*(num_asb+2), 0]\n')
		f.write('		# saturation vapour pressure on wall (molecules/cm3 (air))\n')
		f.write('		# note, just using the top rows of Psat and act_coeff\n')
		f.write('		# as do not need the repetitions over size bins\n')
		f.write('		if (Cw > 0.):\n')
		f.write('			Csit = Psat[0, :]*(Csit/Cw)*act_coeff[0, :]\n')
		f.write('			# rate of transfer (# molecules/cm3/s)\n')
		f.write('			dd_all = kw*(y[0:num_comp, 0]-Csit)\n')
		f.write('			dd[0:num_comp, 0] -= dd_all # gas-phase change\n')
		f.write('			dd[num_comp*num_sb:num_comp*(num_sb+1), 0] += dd_all # wall change\n')
		
		f.write('		\n')
	
	# non-vectorised code for use with numba compiler
	#	f.write('	# numba compiler to convert to machine code\n')
	#	f.write('	@jit(f8[:](f8, f8[:]), nopython=True, cache=False)\n')
	#	f.write('	# ode solver -------------------------------------\n')
	#	f.write('	def dydt(t, y): # define the ODE(s)\n')
	#	f.write('		\n')
	#	f.write('		# empty array to hold rate of change per component\n')
	#	f.write('		dd = np.zeros((len(y)))\n')
	#	f.write('		# gas-phase rate of change -----------------------\n')
	#	f.write('		for i in range(nreac.shape[0]): # equation loop\n')
	#	f.write('			# gas-phase rate of change (molecules/cm3 (air).s)\n')
	#	f.write('			if (y[rindx[i, 0:nreac[i]], 0]==0.0).sum()>0:\n')	
	#	f.write('				continue # if any reactants not present skip this reaction\n')			
	#	f.write('			else:\n')
	#	f.write('				gprate = ((y[rindx[i, 0:nreac[i]], 0]**rstoi[i, 0:nreac[i]]).prod())*rrc[i]\n')
	#	f.write('				# loss of reactants\n')
	#	f.write('				dd[rindx[i, 0:nreac[i]]] -= gprate*rstoi[i, 0:nreac[i]]\n')
	#	f.write('				# gain of products\n')
	#	f.write('				dd[pindx[i, 0:nprod[i]]] += gprate*pstoi[i, 0:nprod[i]]\n')
	#	f.write('		\n')
	#	# only write next section if particles present
	#	if (num_asb > 0):
	#		f.write('		# if size bins present estimate gas-particle partitioning\n')
	#		f.write('		for ibin in range(num_asb): # size bin loop\n')
	#		f.write('			# particle-phase concentrations in this size bin (moclecules/cc)\n')
	#		f.write('			Csit = y[num_comp*(ibin+1):num_comp*(ibin+2), 0]\n')
	#		f.write('			# prepare for # sum of molecular concentrations per bin (molecules/cm3 (air))\n')
	#		f.write('			conc_sum = np.zeros((1))\n')
	#		f.write('			conc_sum[0] = ((Csit.sum()-Csit[self.seedi])+Csit[self.seedi]*core_diss)\n')
	#		f.write('			# only need to continue if particles present\n')
	#		f.write('			if (conc_sum[0]>1.e-20):\n')
	#		f.write('				# particle surface gas-phase concentration (molecules/cm3 (air))\n')
	#		f.write('				Csit = (Csit/conc_sum)*Psat[0, :]*kelv_fac[ibin]*act_coeff[0, :]\n')
	#		f.write('				# partitioning rate (molecules/cm3.s)\n')
	#		f.write('				dydt_all = kimt[ibin, :]*(y[0:num_comp, 0]-Csit)\n')
	#		f.write('				dd[0:num_comp] -= dydt_all # gas-phase change\n')
	#		f.write('				# particle-phase change\n')
	#		f.write('				dd[num_comp*(ibin+1):num_comp*(ibin+2)] += dydt_all\n')
	#		f.write('		\n')
	#	# only write next section if gas-wall partitioning active
	#	if (self.wall_on==1):
	#		f.write('		if (Cw > 0.): # only consider if wall present\n')
	#		f.write('			# if wall consideration turned on, estimate gas-wall partitioning\n')
	#		f.write('			# concentration at wall (molecules/cm3 (air))\n')
	#		f.write('			Csit = y[num_comp*num_sb:num_comp*(num_sb+1), 0]\n')
	#		f.write('			Csit = (Psat[0, :]*(Csit/Cw)*act_coeff[0, :]) # with Raoult term\n')
	#		f.write('			dydt_all = (kw)*(y[0:num_comp, 0]-Csit)\n')
	#		f.write('			dd[0:num_comp] -= dydt_all # gas-phase change\n')
	#		f.write('			# wall concentration change \n')
	#		f.write('			dd[num_comp*num_sb:num_comp*(num_sb+1)] += dydt_all\n')
	#		f.write('			\n')
	f.write('		\n')
	
	f.write('		dd = (dd[:, 0]).reshape(num_sb+1, num_comp)\n')
	f.write('		# force all components in size bins with no particle to zero\n')
	f.write('		if (num_asb > 0):\n')
	f.write('			dd[1:num_asb+1, :][N_perbin[:, 0] == 0, :] = 0\n')
	f.write('		# return to array, note that consistent with the solve_ivp manual, this ensures dd is\n')
	f.write('		# a vector rather than matrix, since y0 is a vector\n')
	f.write('		dd = dd.flatten()\n')
	f.write('		return (dd)\n')
	f.write('\n')
	
	# set the Jacobian
	f.write('	def jac(t, y): # define the Jacobian\n')
	f.write('		\n')
	f.write('		# inputs: ----------------\n')
	f.write('		# y - concentrations (molecules/cm3), note when using scipy integrator solve_ivp, this should have shape (number of elements, 1)\n')
	f.write('		# t - time interval to integrate over (s)\n')
	f.write('		# ---------------------------------------------\n')
	f.write('		\n')
	f.write('		# ensure y is correct shape\n')
	f.write('		if (y.ndim == 2):\n')
	f.write('			if (y.shape[1] > 1):\n')
	f.write('				y = y[:, 0].reshape(-1, 1)\n')
	f.write('		if (y.ndim <= 1):\n')
	f.write('			y = y.reshape(-1, 1)\n')
	f.write('		\n')
	
	f.write('		# elements of sparse Jacobian matrix\n')
	if (num_asb > 0): # include any particle-phase modifiers
		f.write('		data = np.zeros((%s+jac_mod_len))\n' %len(rowvals))
	else: # don't include any particle-phase modifiers
		f.write('		data = np.zeros((%s))\n' %len(rowvals))
	f.write('		\n')
	
	if (eqn_num[0] > 0): # if gas-phase reactions present
		f.write('		for i in range(rindx.shape[0]): # gas-phase reaction loop\n')
		f.write('			# reaction rate (molecules/cm3/s)\n')
		f.write('			rr = rrc[i]*(y[rindx[i, 0:nreac[i]], 0].prod())\n')
		f.write('			# prepare Jacobian inputs\n')
		f.write('			jac_coeff = np.zeros((njac[i, 0]))\n')
		f.write('			# only fill Jacobian if reaction rate sufficient\n')
		f.write('			if (rr != 0.):\n')
		f.write('				jac_coeff = (rr*(jac_stoi[i, 0:njac[i, 0]])/\n')
		f.write('				(y[jac_den_indx[i, 0:njac[i, 0]], 0]))\n')
		f.write('			data[jac_indx[i, 0:njac[i, 0]]] += jac_coeff\n')
		f.write('		\n')
	
	if (eqn_num[1] > 0): # if particle-phase reactions present
		f.write('		n_aqr = nreac_aq.shape[0] # number of aqueous-phase reactions \n')
		f.write('		aqi = 0 # aqueous-phase reaction counter\n')
		f.write('		\n')
		f.write('		for i in range(rindx.shape[0], rrc.shape[0]): # aqueous-phase reaction loop\n')
		f.write('			# reaction rate (molecules/cm3/s)\n')
		f.write('			rr = rrc[i]*(y[rindx_aq[aqi::n_aqr, 0:nreac_aq[aqi]], 0].prod(axis=1))\n')
		f.write('			# spread along affected components\n')
		f.write('			rr = rr.reshape(-1, 1)\n')
		f.write('			rr = (np.tile(rr, int(njac_aq[aqi, 0]/(num_sb-self.wall_on)))).flatten(order=\'C\')\n')
		f.write('			# prepare Jacobian inputs\n')
		f.write('			jac_coeff = np.zeros((njac_aq[aqi, 0]))\n')
		f.write('			nzi = (rr != 0)\n')
		f.write('			jac_coeff[nzi] = (rr[nzi]*((jac_stoi_aq[aqi, 0:njac_aq[aqi, 0]])[nzi])/\n')
		f.write('				((y[jac_den_indx_aq[aqi, 0:njac_aq[aqi, 0]], 0])[nzi]))\n')
		f.write('			# stack size bins\n')
		f.write('			jac_coeff = jac_coeff.reshape(int(num_sb-self.wall_on), int(njac_aq[aqi, 0]/(num_sb-self.wall_on)), order=\'C\')\n')
		f.write('			data[jac_indx_aq[aqi::n_aqr, 0:(int(njac_aq[aqi, 0]/(num_sb-self.wall_on)))]] += jac_coeff\n')
		f.write('			\n')
		f.write('			aqi += 1 # keep count on aqueous-phase reactions \n')
	f.write('		\n')
	
	if (num_asb > 0): # include gas-particle partitioning in ode solver Jacobian
		f.write('		# gas-particle partitioning\n')
		f.write('		part_eff = np.zeros((%s))\n' %((num_comp)*(num_asb+1)+((num_comp)*(num_asb*2))))
		f.write('		if (sum(N_perbin[:, 0]) > 0.): # if any particles present \n')
		f.write('			part_eff[0:%s:%s] = -kimt.sum(axis=0) # effect of gas on gas\n' %(num_comp*(num_asb+1), (num_asb+1)))
		f.write('		\n')
		f.write('		# empty array for any particle-on-gas and particle-on-particle effects on water in the particle-phase for rows of Jacobian\n')
		f.write('		part_eff_rw = np.zeros((len(jac_part_hmf_indx)))\n')
		f.write('		# empty array for any particle-on-gas and particle-on-particle effects of water in the particle-phase on non-water components in the particle-phase for columns of Jacobian\n')
		f.write('		part_eff_cl = np.zeros((len(jac_part_H2O_indx)))\n')
		f.write('		# starting index for jacobian row inputs for effect on water\n')
		f.write('		sti_rw = 0 \n')
		f.write('		\n')
		f.write('		# transform particle phase concentrations into\n')
		f.write('		# size bins in rows, components in columns\n')
		f.write('		ymat = (y[num_comp:num_comp*(num_asb+1), 0]).reshape(num_asb, num_comp)\n')
		f.write('		ymat[N_perbin[:, 0] == 0, :] = 0 # ensure zero components where zero particles\n')
		f.write('		# total particle-phase concentration per size bin (molecules/cm3 (air))\n')
		f.write('		csum = ymat.sum(axis=1)-ymat[:, self.seedi].sum(axis=1)+(ymat[:, self.seedi]*core_diss).sum(axis=1)\n')
		f.write('		\n')
		f.write('		# effect of particle on gas\n')
		f.write('		for isb in range(int(num_asb)): # size bin loop\n')
		f.write('			if (csum[isb] > 0): # if components present in this size bin\n')
		f.write('				# effect of gas on particle\n')
		f.write('				part_eff[1+isb:num_comp*(num_asb+1):num_asb+1] = +kimt[isb, :]\n')
		f.write('				# start index\n')
		f.write('				sti = int((num_asb+1)*num_comp+isb*(num_comp*2))\n')
		f.write('				# diagonal index\n')
		f.write('				diag_indxg = sti+np.arange(0, num_comp*2, 2).astype(\'int\')\n')
		f.write('				diag_indxp = sti+np.arange(1, num_comp*2, 2).astype(\'int\')\n')
		f.write('				# prepare for diagonal (component effect on itself)\n')
		f.write('				diag = kimt[isb, :]*Psat[0, :]*act_coeff[0, :]*kelv_fac[isb, 0]*(-(csum[isb]-ymat[isb, :])/(csum[isb]**2.)) \n')
		f.write('				# implement to part_eff\n')
		f.write('				part_eff[diag_indxg] -= diag\n')
		f.write('				part_eff[diag_indxp] += diag\n')
		f.write('				\n')
		f.write('				if (rw_indx[isb] > -1): # if water in this size bin \n') 
		f.write('					# prepare for row(s) (particle-phase non-water component effects on water in particle phase)\n')
		f.write('					rw = kimt[isb, rw_indx[isb]]*Psat[0, rw_indx[isb]]*act_coeff[0, rw_indx[isb]]*kelv_fac[isb, 0]*(-(-ymat[isb, rw_indx[isb]])/(csum[isb]**2.)) \n')
		f.write('					# indices\n')
		f.write('					indxg = sti_rw+np.arange(0, ((num_comp-1)*2), 2).astype(\'int\')\n')
		f.write('					indxp = sti_rw+np.arange(1, ((num_comp-1)*2), 2).astype(\'int\')\n')
		f.write('					# implement to part_eff_rw\n')
		f.write('					part_eff_rw[indxg] -= rw\n')
		f.write('					part_eff_rw[indxp] += rw\n')
		f.write('					\n')
		f.write('					# prepare for column(s) (particle-phase water effect on non-water in particle phase)\n')
		f.write('					#cl = kimt[isb, :]*Psat[0, :]*act_coeff[0, :]*kelv_fac[isb, 0]*(-(-ymat[isb, :])/(csum[isb]**2.))\n')
		f.write('					#cl = np.zeros((num_comp))\n')
		f.write('					# remove water\n')
		f.write('					#cl = np.concatenate((cl[0:H2Oi], cl[H2Oi+1::]))\n')
		f.write('					#indxg = sti_rw+np.arange(0, (num_comp-1)).astype(\'int\')\n')
		f.write('					#indxp = sti_rw+np.arange((num_comp-1), (num_comp-1)*2).astype(\'int\')\n')
		f.write('					# implement to part_eff_cl\n')
		f.write('					#part_eff_cl[indxg] -= cl\n')
		f.write('					#part_eff_cl[indxp] += cl\n')
		f.write('					\n')
		f.write('					# starting index update\n')
		f.write('					sti_rw += (num_comp-1)*2\n')
		f.write('		\n')
		f.write('		data[jac_part_indx] += part_eff # diagonal\n')
		f.write('		data[jac_part_hmf_indx] += part_eff_rw # rows\n')
		f.write('		#data[jac_part_H2O_indx] += part_eff_cl # columns\n')
		f.write('		\n')
		
	if (self.wall_on > 0): # include gas-wall partitioning in ode solver Jacobian
		f.write('		if (Cw > 0.):\n')
		f.write('			wall_eff = np.zeros((%s))\n' %(num_comp*4))
		f.write('			wall_eff[0:%s:2] = -kw # effect of gas on gas \n' %(num_comp*2))
		f.write('			wall_eff[1:%s:2] = +kw # effect of gas on wall \n' %(num_comp*2))
		f.write('			# effect of wall on gas\n')
		f.write('			wall_eff[%s:%s:2] = +kw*(Psat[0,:]*act_coeff[0, :]/Cw) \n' %(num_comp*2, num_comp*4))
		f.write('			# effect of wall on wall\n')
		f.write('			wall_eff[%s+1:%s:2] = -kw*(Psat[0,:]*act_coeff[0, :]/Cw) \n' %(num_comp*2, num_comp*4))
		f.write('			data[jac_wall_indx] += wall_eff\n')
		f.write('		\n')
	if (self.dil_fac > 0): # include extraction of chamber air in ode solver Jacobian
		f.write('		data[jac_extr_indx] -= 1.*self.dil_fac\n')
		f.write('		\n')

	f.write('		# create Jacobian\n')
	f.write('		j = SP.csc_matrix((data, rowvals, colptrs))\n')
	f.write('		\n')
	f.write('		return(j)\n')
	f.write('	\n')
	f.write('	# set ODE solver tolerances\n')
	f.write('	atol = %s\n'%int_tol[0])
	f.write('	rtol = %s\n'%int_tol[1])
	f.write('	\n')
	f.write('	# check for underflow issues\n')
	f.write('	# reaction rate coefficient calculation\n')
	f.write('	#rrc_y = np.ones((rindx.shape[0]*rindx.shape[1]))\n')
	f.write('	#rrc_y[y_arr] = y[y_rind]\n')
	f.write('	#rrc_y = rrc_y.reshape(rindx.shape[0], rindx.shape[1], order = \'C\')\n')
	f.write('	# reaction rate coefficient zeroed wherever product of reactant concentrations is zero (including where underflow causes zero, thereby preventing underflows breaking the solver which appears to be an issue on less powerful machines such as HP Spectre Folio) (/s) \n')
	f.write('	#rrc[((rrc_y**rstoi).prod(axis=1)) == 0.0] = 0.\n')
	f.write('	\n')
	f.write('	# call on the ODE solver, note y contains the initial condition(s) (molecules/cm3 (air)) and must be 1D even though y in dydt and jac has shape (number of elements, 1)\n')
	f.write('	sol = solve_ivp(dydt, [0, integ_step], y, atol = atol, rtol = rtol, method = \'BDF\', t_eval = [integ_step], vectorized = True, jac = jac)\n')
	f.write('	\n')
	f.write('	# force all components in size bins with no particle to zero\n')
	f.write('	y = np.squeeze(sol.y)\n')
	f.write('	y = y.reshape(num_sb+1, num_comp)\n')
	f.write('	if (num_asb > 0):\n')
	f.write('		y[1:num_asb+1, :][N_perbin[:, 0] == 0, :] = 0\n')
	f.write('	# return to array\n')
	f.write('	y = y.flatten()\n')
	f.write('	\n')
	f.write('	# return concentration(s) and time(s) following integration\n')
	f.write('	return(y, sol.t)\n')
	f.close() # close file