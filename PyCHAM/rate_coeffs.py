'''module for calculating reaction rate coefficients (automatically generated)'''
# module to hold expressions for calculating rate coefficients # 
# created at 2021-08-03 11:40:25.902690

import numpy
import photolysisRates

def evaluate_rates(RO2, H2O, TEMP, lightm, time, lat, lon, act_flux_path, DayOfYear, M, N2, O2, photo_par_file, Jlen, tf, NO, HO2, NO3):

	# inputs: ------------------------------------------------------------------
	# RO2 - names of components included in peroxy radical list
	# M - third body concentration (molecules/cc (air))
	# N2 - nitrogen concentration (molecules/cc (air))
	# O2 - oxygen concentration (molecules/cc (air))
	# H2O, TEMP: given by the user
	# lightm: given by the user and is 0 for lights off and 1 for on
	# reaction rate coefficients and their names parsed in eqn_parser.py 
	# Jlen - number of photolysis reactions
	# tf - sunlight transmission factor
	# NO - NO concentration (molecules/cc (air))
	# HO2 - HO2 concentration (molecules/cc (air))
	# NO3 - NO3 concentration (molecules/cc (air))
	# ------------------------------------------------------------------------

	erf = 0; err_mess = '' # begin assuming no errors
	# calculate generic reaction rate coefficients given by chemical scheme
	try:
		KRO2NO=2.7e-12*numpy.exp(360/TEMP) 
		KRO2HO2=2.91e-13*numpy.exp(1300/TEMP) 
		KAPHO2=5.2e-13*numpy.exp(980/TEMP) 
		KAPNO=7.5e-12*numpy.exp(290/TEMP) 
		KRO2NO3=2.3e-12 
		KNO3AL=1.44e-12*numpy.exp(-1862/TEMP) 
		KDEC=1.00e+06 
		KROPRIM=2.50e-14*numpy.exp(-300/TEMP) 
		KROSEC=2.50e-14*numpy.exp(-300/TEMP) 
		KCH3O2=1.03e-13*numpy.exp(365/TEMP) 
		K298CH3O2=3.5e-13 
		K14ISOM1=3.00e7*numpy.exp(-5300/TEMP) 
		KD0=1.10e-05*M*numpy.exp(-10100/TEMP) 
		KDI=1.90e17*numpy.exp(-14100/TEMP) 
		KRD=KD0/KDI 
		FCD=0.30 
		NCD=0.75-1.27*(numpy.log10(FCD)) 
		FD=10**(numpy.log10(FCD)/(1+(numpy.log10(KRD)/NCD)**2)) 
		KBPAN=(KD0*KDI)*FD/(KD0+KDI) 
		KC0=3.28e-28*M*(TEMP/300)**-6.87 
		KCI=1.125e-11*(TEMP/300)**-1.105 
		KRC=KC0/KCI 
		FCC=0.30 
		NC=0.75-1.27*(numpy.log10(FCC)) 
		FC=10**(numpy.log10(FCC)/(1+(numpy.log10(KRC)/NC)**2)) 
		KFPAN=(KC0*KCI)*FC/(KC0+KCI) 
		K10=1.0e-31*M*(TEMP/300)**-1.6 
		K1I=5.0e-11*(TEMP/300)**-0.3 
		KR1=K10/K1I 
		FC1=0.85 
		NC1=0.75-1.27*(numpy.log10(FC1)) 
		F1=10**(numpy.log10(FC1)/(1+(numpy.log10(KR1)/NC1)**2)) 
		KMT01=(K10*K1I)*F1/(K10+K1I) 
		K20=1.3e-31*M*(TEMP/300)**-1.5 
		K2I=2.3e-11*(TEMP/300)**0.24 
		KR2=K20/K2I 
		FC2=0.6 
		NC2=0.75-1.27*(numpy.log10(FC2)) 
		F2=10**(numpy.log10(FC2)/(1+(numpy.log10(KR2)/NC2)**2)) 
		KMT02=(K20*K2I)*F2/(K20+K2I) 
		K30=3.6e-30*M*(TEMP/300)**-4.1 
		K3I=1.9e-12*(TEMP/300)**0.2 
		KR3=K30/K3I 
		FC3=0.35 
		NC3=0.75-1.27*(numpy.log10(FC3)) 
		F3=10**(numpy.log10(FC3)/(1+(numpy.log10(KR3)/NC3)**2)) 
		KMT03=(K30*K3I)*F3/(K30+K3I) 
		K40=1.3e-3*M*(TEMP/300)**-3.5*numpy.exp(-11000/TEMP) 
		K4I=9.7e+14*(TEMP/300)**0.1*numpy.exp(-11080/TEMP) 
		KR4=K40/K4I 
		FC4=0.35 
		NC4=0.75-1.27*(numpy.log10(FC4)) 
		F4=10**(numpy.log10(FC4)/(1+(numpy.log10(KR4)/NC4)**2)) 
		KMT04=(K40*K4I)*F4/(K40+K4I) 
		KMT05=1.44e-13*(1+(M/4.2e+19)) 
		KMT06=1+(1.40e-21*numpy.exp(2200/TEMP)*H2O) 
		K70=7.4e-31*M*(TEMP/300)**-2.4 
		K7I=3.3e-11*(TEMP/300)**-0.3 
		KR7=K70/K7I 
		FC7=0.81 
		NC7=0.75-1.27*(numpy.log10(FC7)) 
		F7=10**(numpy.log10(FC7)/(1+(numpy.log10(KR7)/NC7)**2)) 
		KMT07=(K70*K7I)*F7/(K70+K7I) 
		K80=3.2e-30*M*(TEMP/300)**-4.5 
		K8I=3.0e-11 
		KR8=K80/K8I 
		FC8=0.41 
		NC8=0.75-1.27*(numpy.log10(FC8)) 
		F8=10**(numpy.log10(FC8)/(1+(numpy.log10(KR8)/NC8)**2)) 
		KMT08=(K80*K8I)*F8/(K80+K8I) 
		K90=1.4e-31*M*(TEMP/300)**-3.1 
		K9I=4.0e-12 
		KR9=K90/K9I 
		FC9=0.4 
		NC9=0.75-1.27*(numpy.log10(FC9)) 
		F9=10**(numpy.log10(FC9)/(1+(numpy.log10(KR9)/NC9)**2)) 
		KMT09=(K90*K9I)*F9/(K90+K9I) 
		K100=4.10e-05*M*numpy.exp(-10650/TEMP) 
		K10I=6.0e+15*numpy.exp(-11170/TEMP) 
		KR10=K100/K10I 
		FC10=0.4 
		NC10=0.75-1.27*(numpy.log10(FC10)) 
		F10=10**(numpy.log10(FC10)/(1+(numpy.log10(KR10)/NC10)**2)) 
		KMT10=(K100*K10I)*F10/(K100+K10I) 
		K1=2.40e-14*numpy.exp(460/TEMP) 
		K3=6.50e-34*numpy.exp(1335/TEMP) 
		K4=2.70e-17*numpy.exp(2199/TEMP) 
		K2=(K3*M)/(1+(K3*M/K4)) 
		KMT11=K1+K2 
		K120=2.5e-31*M*(TEMP/300)**-2.6 
		K12I=2.0e-12 
		KR12=K120/K12I 
		FC12=0.53 
		NC12=0.75-1.27*(numpy.log10(FC12)) 
		F12=10**(numpy.log10(FC12)/(1.0+(numpy.log10(KR12)/NC12)**2)) 
		KMT12=(K120*K12I*F12)/(K120+K12I) 
		K130=2.5e-30*M*(TEMP/300)**-5.5 
		K13I=1.8e-11 
		KR13=K130/K13I 
		FC13=0.36 
		NC13=0.75-1.27*(numpy.log10(FC13)) 
		F13=10**(numpy.log10(FC13)/(1+(numpy.log10(KR13)/NC13)**2)) 
		KMT13=(K130*K13I)*F13/(K130+K13I) 
		K140=9.0e-5*numpy.exp(-9690/TEMP)*M 
		K14I=1.1e+16*numpy.exp(-10560/TEMP) 
		KR14=K140/K14I 
		FC14=0.36 
		NC14=0.75-1.27*(numpy.log10(FC14)) 
		F14=10**(numpy.log10(FC14)/(1+(numpy.log10(KR14)/NC14)**2)) 
		KMT14=(K140*K14I)*F14/(K140+K14I) 
		K150=8.6e-29*M*(TEMP/300)**-3.1 
		K15I=9.0e-12*(TEMP/300)**-0.85 
		KR15=K150/K15I 
		FC15=0.48 
		NC15=0.75-1.27*(numpy.log10(FC15)) 
		F15=10**(numpy.log10(FC15)/(1+(numpy.log10(KR15)/NC15)**2)) 
		KMT15=(K150*K15I)*F15/(K150+K15I) 
		K160=8e-27*M*(TEMP/300)**-3.5 
		K16I=3.0e-11*(TEMP/300)**-1 
		KR16=K160/K16I 
		FC16=0.5 
		NC16=0.75-1.27*(numpy.log10(FC16)) 
		F16=10**(numpy.log10(FC16)/(1+(numpy.log10(KR16)/NC16)**2)) 
		KMT16=(K160*K16I)*F16/(K160+K16I) 
		K170=5.0e-30*M*(TEMP/300)**-1.5 
		K17I=1.0e-12 
		KR17=K170/K17I 
		FC17=0.17*numpy.exp(-51/TEMP)+numpy.exp(-TEMP/204) 
		NC17=0.75-1.27*(numpy.log10(FC17)) 
		F17=10**(numpy.log10(FC17)/(1.0+(numpy.log10(KR17)/NC17)**2)) 
		KMT17=(K170*K17I*F17)/(K170+K17I) 
		KMT18=9.5e-39*O2*numpy.exp(5270/TEMP)/(1+7.5e-29*O2*numpy.exp(5610/TEMP)) 
		KPPN0=1.7e-03*numpy.exp(-11280/TEMP)*M 
		KPPNI=8.3e+16*numpy.exp(-13940/TEMP) 
		KRPPN=KPPN0/KPPNI 
		FCPPN=0.36 
		NCPPN=0.75-1.27*(numpy.log10(FCPPN)) 
		FPPN=10**(numpy.log10(FCPPN)/(1+(numpy.log10(KRPPN)/NCPPN)**2)) 
		KBPPN=(KPPN0*KPPNI)*FCPPN/(KPPN0+KPPNI) 
		KNO=KRO2NO*NO 
		KHO2=KRO2HO2*HO2*0.706 
		KRO2=1.26e-12*RO2 
		KNO3=KRO2NO3*NO3 
		KTR=KNO+KHO2+KRO2+KNO3 
		K16ISOM=(KTR*5.18e-04*numpy.exp(1308/TEMP))+(2.76e07*numpy.exp(-6759/TEMP)) 

	except:
		erf = 1 # flag error
		err_mess = 'Error: reaction rates failed to be calculated, please check chemical scheme and associated chemical scheme markers, which are stated in the model variables input file' # error message

	# estimate and append photolysis rates
	J = photolysisRates.PhotolysisCalculation(time, lat, lon, TEMP, act_flux_path, DayOfYear, photo_par_file, Jlen, tf)

	if (lightm == 0):
		J = [0]*len(J)
	rate_values = numpy.zeros((881))
	
	# reac_coef has been formatted so that python can recognize it
	# gas-phase reactions
	rate_values[0] = 5.6e-34*N2*(TEMP/300)**-2.6*O2+6.0e-34*O2*(TEMP/300)**-2.6*O2
	rate_values[1] = 8.0e-12*numpy.exp(-2060/TEMP)
	rate_values[2] = KMT01
	rate_values[3] = 5.5e-12*numpy.exp(188/TEMP)
	rate_values[4] = KMT02
	rate_values[5] = 3.2e-11*numpy.exp(67/TEMP)*O2+2.0e-11*numpy.exp(130/TEMP)*N2
	rate_values[6] = 1.4e-12*numpy.exp(-1310/TEMP)
	rate_values[7] = 1.4e-13*numpy.exp(-2470/TEMP)
	rate_values[8] = 3.3e-39*numpy.exp(530/TEMP)*O2
	rate_values[9] = 1.8e-11*numpy.exp(110/TEMP)
	rate_values[10] = 4.50e-14*numpy.exp(-1260/TEMP)
	rate_values[11] = KMT03
	rate_values[12] = 2.14e-10*H2O
	rate_values[13] = 1.70e-12*numpy.exp(-940/TEMP)
	rate_values[14] = 7.7e-12*numpy.exp(-2100/TEMP)
	rate_values[15] = KMT05
	rate_values[16] = 2.9e-12*numpy.exp(-160/TEMP)
	rate_values[17] = 2.03e-16*(TEMP/300)**4.57*numpy.exp(693/TEMP)
	rate_values[18] = 4.8e-11*numpy.exp(250/TEMP)
	rate_values[19] = 2.20e-13*KMT06*numpy.exp(600/TEMP)+1.90e-33*M*KMT06*numpy.exp(980/TEMP)
	rate_values[20] = KMT07
	rate_values[21] = KMT08
	rate_values[22] = 2.0e-11
	rate_values[23] = 3.45e-12*numpy.exp(270/TEMP)
	rate_values[24] = KMT09
	rate_values[25] = 3.2e-13*numpy.exp(690/TEMP)*1.0
	rate_values[26] = 4.0e-12
	rate_values[27] = 2.5e-12*numpy.exp(260/TEMP)
	rate_values[28] = KMT11
	rate_values[29] = 4.0e-32*numpy.exp(-1000/TEMP)*M
	rate_values[30] = KMT12
	rate_values[31] = 1.3e-12*numpy.exp(-330/TEMP)*O2
	rate_values[32] = 6.00e-06
	rate_values[33] = 4.00e-04
	rate_values[34] = 1.20e-15*H2O
	rate_values[35] = J[1]
	rate_values[36] = J[2]
	rate_values[37] = J[3]
	rate_values[38] = J[4]
	rate_values[39] = J[5]
	rate_values[40] = J[6]
	rate_values[41] = J[7]
	rate_values[42] = J[8]
	rate_values[43] = KMT04
	rate_values[44] = KMT10
	rate_values[45] = 1.2e-12*numpy.exp(490/TEMP)*0.65
	rate_values[46] = 1.2e-12*numpy.exp(490/TEMP)*0.35
	rate_values[47] = 8.05e-16*numpy.exp(-640/TEMP)*0.6
	rate_values[48] = 8.05e-16*numpy.exp(-640/TEMP)*0.4
	rate_values[49] = 1.2e-11*numpy.exp(440/TEMP)*0.572
	rate_values[50] = 1.2e-11*numpy.exp(440/TEMP)*0.353
	rate_values[51] = 1.2e-11*numpy.exp(440/TEMP)*0.075
	rate_values[52] = KRO2HO2*0.914
	rate_values[53] = KRO2NO
	rate_values[54] = KRO2NO3
	rate_values[55] = 6.70e-15*0.1*RO2
	rate_values[56] = 6.70e-15*0.9*RO2
	rate_values[57] = KRO2HO2*0.914
	rate_values[58] = KRO2NO
	rate_values[59] = KRO2NO3
	rate_values[60] = 2.50e-13*0.1*RO2
	rate_values[61] = 2.50e-13*0.8*RO2
	rate_values[62] = 2.50e-13*0.1*RO2
	rate_values[63] = KDEC*0.55
	rate_values[64] = KDEC*0.45
	rate_values[65] = KDEC*0.50
	rate_values[66] = KDEC*0.50
	rate_values[67] = KRO2HO2*0.914
	rate_values[68] = KRO2NO*0.230
	rate_values[69] = KRO2NO*0.770
	rate_values[70] = KRO2NO3
	rate_values[71] = 9.20e-14*RO2*0.7
	rate_values[72] = 9.20e-14*RO2*0.3
	rate_values[73] = KRO2HO2*0.914
	rate_values[74] = KRO2NO*0.230
	rate_values[75] = KRO2NO*0.770
	rate_values[76] = KRO2NO3
	rate_values[77] = 8.80e-13*RO2*0.2
	rate_values[78] = 8.80e-13*RO2*0.6
	rate_values[79] = 8.80e-13*RO2*0.2
	rate_values[80] = KRO2HO2*0.914
	rate_values[81] = KRO2NO*0.125
	rate_values[82] = KRO2NO*0.875
	rate_values[83] = KRO2NO3
	rate_values[84] = 6.70e-15*RO2*0.7
	rate_values[85] = 6.70e-15*RO2*0.3
	rate_values[86] = 6.87e-12
	rate_values[87] = J[41]
	rate_values[88] = KDEC
	rate_values[89] = 3.64e-12
	rate_values[90] = 1.90e-12*numpy.exp(190/TEMP)
	rate_values[91] = 1.23e-11
	rate_values[92] = J[41]
	rate_values[93] = KROSEC*O2
	rate_values[94] = 4.00e+05
	rate_values[95] = 5.50e-12
	rate_values[96] = 5.55e-12
	rate_values[97] = J[55]
	rate_values[98] = KRO2HO2*0.914
	rate_values[99] = KRO2NO
	rate_values[100] = KRO2NO3
	rate_values[101] = 9.20e-14*0.7*RO2
	rate_values[102] = 9.20e-14*0.3*RO2
	rate_values[103] = KRO2HO2*0.914
	rate_values[104] = KRO2NO
	rate_values[105] = KRO2NO3
	rate_values[106] = 2.00e-12*RO2*0.05
	rate_values[107] = 2.00e-12*RO2*0.90
	rate_values[108] = 2.00e-12*RO2*0.05
	rate_values[109] = 1.20e-15
	rate_values[110] = 1.00e-14
	rate_values[111] = 1.00e-15
	rate_values[112] = 7.00e-14
	rate_values[113] = 1.40e-17*H2O
	rate_values[114] = 2.00e-18*H2O
	rate_values[115] = KRO2HO2*0.890
	rate_values[116] = KRO2NO*0.157
	rate_values[117] = KRO2NO*0.843
	rate_values[118] = KRO2NO3
	rate_values[119] = 1.30e-12*0.6*RO2
	rate_values[120] = 1.30e-12*0.2*RO2
	rate_values[121] = 1.30e-12*0.2*RO2
	rate_values[122] = 1.83e-11
	rate_values[123] = J[41]
	rate_values[124] = KDEC
	rate_values[125] = 1.49e-11
	rate_values[126] = 3.28e-11
	rate_values[127] = J[41]
	rate_values[128] = KDEC
	rate_values[129] = 8.18e-12
	rate_values[130] = 1.03e-10
	rate_values[131] = J[41]
	rate_values[132] = 9.87e-11
	rate_values[133] = J[55]
	rate_values[134] = KDEC
	rate_values[135] = 9.91e-11
	rate_values[136] = 2.0e-14
	rate_values[137] = 5.2e-12*numpy.exp(600/TEMP)*0.772
	rate_values[138] = 5.2e-12*numpy.exp(600/TEMP)*0.228
	rate_values[139] = J[15]
	rate_values[140] = KRO2HO2*0.914
	rate_values[141] = KRO2NO
	rate_values[142] = KRO2NO3
	rate_values[143] = 6.70e-15*RO2
	rate_values[144] = KAPHO2*0.44
	rate_values[145] = KAPHO2*0.41
	rate_values[146] = KAPHO2*0.15
	rate_values[147] = KAPNO
	rate_values[148] = KFPAN
	rate_values[149] = KRO2NO3*1.74
	rate_values[150] = 1.00e-11*0.7*RO2
	rate_values[151] = 1.00e-11*0.3*RO2
	rate_values[152] = 3.01e-11
	rate_values[153] = J[41]+J[15]
	rate_values[154] = KDEC
	rate_values[155] = 2.66e-11
	rate_values[156] = J[15]
	rate_values[157] = 5.47e-11
	rate_values[158] = J[41]+J[15]
	rate_values[159] = J[22]
	rate_values[160] = KDEC*0.80
	rate_values[161] = KDEC*0.20
	rate_values[162] = 5.47e-11
	rate_values[163] = J[34]+J[15]
	rate_values[164] = 4.45e-11
	rate_values[165] = J[22]
	rate_values[166] = J[15]
	rate_values[167] = 6.65e-12
	rate_values[168] = J[22]
	rate_values[169] = 1.90e-12*numpy.exp(190/TEMP)
	rate_values[170] = 1.30e-11
	rate_values[171] = J[41]+J[22]
	rate_values[172] = 2.88e-12
	rate_values[173] = J[53]+J[22]
	rate_values[174] = 4.20e+10*numpy.exp(-3523/TEMP)
	rate_values[175] = 7.67e-12
	rate_values[176] = J[22]
	rate_values[177] = KNO3AL*8.5
	rate_values[178] = 2.64e-11
	rate_values[179] = J[15]
	rate_values[180] = 8.8e-12*numpy.exp(-1320/TEMP) + 1.7e-14*numpy.exp(423/TEMP)
	rate_values[181] = J[21]
	rate_values[182] = 1.19e-10
	rate_values[183] = KRO2HO2*0.820
	rate_values[184] = KRO2NO*0.278
	rate_values[185] = KRO2NO*0.722
	rate_values[186] = KRO2NO3
	rate_values[187] = 2.50e-13*RO2*0.6
	rate_values[188] = 2.50e-13*RO2*0.2
	rate_values[189] = 2.50e-13*RO2*0.2
	rate_values[190] = KRO2HO2*0.914
	rate_values[191] = KRO2NO*0.050
	rate_values[192] = KRO2NO*0.950
	rate_values[193] = KRO2NO3
	rate_values[194] = 6.70e-15*0.7*RO2
	rate_values[195] = 6.70e-15*0.3*RO2
	rate_values[196] = 5.94e-12
	rate_values[197] = J[41]
	rate_values[198] = KDEC
	rate_values[199] = 9.73e-12
	rate_values[200] = J[41]+J[22]
	rate_values[201] = 3.66e-12
	rate_values[202] = KBPAN
	rate_values[203] = KRO2HO2*0.914
	rate_values[204] = KRO2NO*0.125
	rate_values[205] = KRO2NO*0.875
	rate_values[206] = KRO2NO3
	rate_values[207] = 6.70e-15*0.7*RO2
	rate_values[208] = 6.70e-15*0.3*RO2
	rate_values[209] = KAPHO2*0.44
	rate_values[210] = KAPHO2*0.15
	rate_values[211] = KAPHO2*0.41
	rate_values[212] = KAPNO
	rate_values[213] = KFPAN
	rate_values[214] = KRO2NO3*1.74
	rate_values[215] = 1.00e-11*RO2*0.7
	rate_values[216] = 1.00e-11*RO2*0.3
	rate_values[217] = J[11]
	rate_values[218] = J[12]
	rate_values[219] = 5.5e-16
	rate_values[220] = 5.4e-12*numpy.exp(135/TEMP)
	rate_values[221] = KAPHO2*0.41
	rate_values[222] = KAPHO2*0.44
	rate_values[223] = KAPHO2*0.15
	rate_values[224] = KAPNO
	rate_values[225] = KFPAN
	rate_values[226] = KRO2NO3*1.74
	rate_values[227] = 1.00e-11*RO2*0.7
	rate_values[228] = 1.00e-11*RO2*0.3
	rate_values[229] = KRO2HO2*0.890
	rate_values[230] = KRO2NO
	rate_values[231] = KRO2NO3
	rate_values[232] = 1.30e-12*RO2
	rate_values[233] = KRO2HO2*0.890
	rate_values[234] = KRO2NO
	rate_values[235] = KRO2NO3
	rate_values[236] = 6.70e-15*0.7*RO2
	rate_values[237] = 6.70e-15*0.3*RO2
	rate_values[238] = KAPHO2*0.56
	rate_values[239] = KAPHO2*0.44
	rate_values[240] = KAPNO
	rate_values[241] = KFPAN
	rate_values[242] = KRO2NO3*1.74
	rate_values[243] = 1.00e-11*RO2
	rate_values[244] = KRO2HO2*0.859
	rate_values[245] = KRO2NO
	rate_values[246] = KRO2NO3
	rate_values[247] = 6.70e-15*RO2
	rate_values[248] = 1.36e-13*numpy.exp(1250/TEMP)*0.15
	rate_values[249] = 1.36e-13*numpy.exp(1250/TEMP)*0.85
	rate_values[250] = KRO2NO
	rate_values[251] = KRO2NO3
	rate_values[252] = 2*(K298CH3O2*8.0e-12)**0.5*RO2*0.2
	rate_values[253] = 2*(K298CH3O2*8.0e-12)**0.5*RO2*0.6
	rate_values[254] = 2*(K298CH3O2*8.0e-12)**0.5*RO2*0.2
	rate_values[255] = KAPHO2*0.15
	rate_values[256] = KAPHO2*0.41
	rate_values[257] = KAPHO2*0.44
	rate_values[258] = 7.5e-12*numpy.exp(290/TEMP)
	rate_values[259] = KFPAN
	rate_values[260] = 4.0e-12
	rate_values[261] = 1.00e-11*0.3*RO2
	rate_values[262] = 1.00e-11*0.7*RO2
	rate_values[263] = 3.8e-13*numpy.exp(780/TEMP)*(1-1/(1+498*numpy.exp(-1160/TEMP)))
	rate_values[264] = 3.8e-13*numpy.exp(780/TEMP)*(1/(1+498*numpy.exp(-1160/TEMP)))
	rate_values[265] = 2.3e-12*numpy.exp(360/TEMP)*0.001
	rate_values[266] = 2.3e-12*numpy.exp(360/TEMP)*0.999
	rate_values[267] = KMT13
	rate_values[268] = 1.2e-12
	rate_values[269] = 2*KCH3O2*RO2*7.18*numpy.exp(-885/TEMP)
	rate_values[270] = 2*KCH3O2*RO2*0.5*(1-7.18*numpy.exp(-885/TEMP))
	rate_values[271] = 2*KCH3O2*RO2*0.5*(1-7.18*numpy.exp(-885/TEMP))
	rate_values[272] = KRO2HO2*0.820
	rate_values[273] = KRO2NO*0.042
	rate_values[274] = KRO2NO*0.958
	rate_values[275] = KRO2NO3
	rate_values[276] = 9.20e-14*RO2*0.7
	rate_values[277] = 9.20e-14*RO2*0.3
	rate_values[278] = 1.27e-10
	rate_values[279] = J[41]
	rate_values[280] = 9.60e-11
	rate_values[281] = J[54]
	rate_values[282] = KROSEC*O2
	rate_values[283] = 1.09e-10
	rate_values[284] = 2.75e-11
	rate_values[285] = J[41]+J[15]
	rate_values[286] = 2.25e-11
	rate_values[287] = J[55]+J[15]
	rate_values[288] = KDEC
	rate_values[289] = 2.41e-11
	rate_values[290] = J[22]
	rate_values[291] = KRO2HO2*0.914
	rate_values[292] = KRO2NO
	rate_values[293] = KRO2NO3
	rate_values[294] = 6.70e-15*RO2
	rate_values[295] = 6.28e-11
	rate_values[296] = J[41]+J[35]
	rate_values[297] = 2.85e-11
	rate_values[298] = J[55]+J[35]
	rate_values[299] = KDEC
	rate_values[300] = 5.93e-11
	rate_values[301] = J[35]
	rate_values[302] = KDEC*0.80
	rate_values[303] = KDEC*0.20
	rate_values[304] = 2.69e-11
	rate_values[305] = J[15]
	rate_values[306] = 3.00e-11
	rate_values[307] = J[41]+J[15]
	rate_values[308] = 2.52e-11
	rate_values[309] = KBPAN
	rate_values[310] = 9.16e-12
	rate_values[311] = J[41]+J[22]
	rate_values[312] = 5.70e-12
	rate_values[313] = J[22]
	rate_values[314] = 5.56e-12
	rate_values[315] = KBPAN
	rate_values[316] = 2.36e-11
	rate_values[317] = J[41]+J[22]
	rate_values[318] = 4.20e+10*numpy.exp(-3523/TEMP)
	rate_values[319] = 1.05e-11
	rate_values[320] = J[41]+J[22]
	rate_values[321] = KDEC
	rate_values[322] = 7.20e-12
	rate_values[323] = J[22]
	rate_values[324] = 1.02e-11
	rate_values[325] = J[41]+J[22]
	rate_values[326] = 6.60e-12
	rate_values[327] = KBPAN
	rate_values[328] = 1.29e-11
	rate_values[329] = J[41]+J[22]
	rate_values[330] = KDEC
	rate_values[331] = KDEC
	rate_values[332] = 1.90e-12*numpy.exp(190/TEMP)
	rate_values[333] = 8.39e-12
	rate_values[334] = J[22]
	rate_values[335] = J[41]
	rate_values[336] = 1.6e-12*numpy.exp(305/TEMP)
	rate_values[337] = J[22]
	rate_values[338] = J[34]
	rate_values[339] = KNO3AL*2.4
	rate_values[340] = 1.9e-12*numpy.exp(575/TEMP)
	rate_values[341] = 8.00e-13
	rate_values[342] = 3.70e-12
	rate_values[343] = J[41]
	rate_values[344] = 3e-14
	rate_values[345] = KBPAN
	rate_values[346] = J[41]
	rate_values[347] = 5.3e-12*numpy.exp(190/TEMP)*0.6
	rate_values[348] = 5.3e-12*numpy.exp(190/TEMP)*0.4
	rate_values[349] = J[51]
	rate_values[350] = 4.0e-13*numpy.exp(-845/TEMP)
	rate_values[351] = 7.2e-14*numpy.exp(-1080/TEMP)*O2
	rate_values[352] = KMT14
	rate_values[353] = 2.85e-12*numpy.exp(-345/TEMP)
	rate_values[354] = 7.06e-11
	rate_values[355] = J[41]
	rate_values[356] = 1.26e-11
	rate_values[357] = KDEC
	rate_values[358] = 6.72e-11
	rate_values[359] = KNO3AL*5.5
	rate_values[360] = 6.70e-11
	rate_values[361] = J[35]
	rate_values[362] = KRO2HO2*0.914
	rate_values[363] = KRO2NO*0.125
	rate_values[364] = KRO2NO*0.875
	rate_values[365] = KRO2NO3
	rate_values[366] = 6.70e-15*0.7*RO2
	rate_values[367] = 6.70e-15*0.3*RO2
	rate_values[368] = 8.03e-12
	rate_values[369] = J[41]
	rate_values[370] = KDEC
	rate_values[371] = KRO2HO2*0.820
	rate_values[372] = KRO2NO*0.278
	rate_values[373] = KRO2NO*0.722
	rate_values[374] = KRO2NO3
	rate_values[375] = 2.50e-13*0.6*RO2
	rate_values[376] = 2.50e-13*0.2*RO2
	rate_values[377] = 2.50e-13*0.2*RO2
	rate_values[378] = KAPHO2*0.41
	rate_values[379] = KAPHO2*0.44
	rate_values[380] = KAPHO2*0.15
	rate_values[381] = KAPNO
	rate_values[382] = KFPAN
	rate_values[383] = KRO2NO3*1.74
	rate_values[384] = 1.00e-11*RO2*0.7
	rate_values[385] = 1.00e-11*RO2*0.3
	rate_values[386] = KRO2HO2*0.859
	rate_values[387] = KRO2NO*0.104
	rate_values[388] = KRO2NO*0.896
	rate_values[389] = KRO2NO3
	rate_values[390] = 6.70e-15*RO2*0.7
	rate_values[391] = 6.70e-15*RO2*0.3
	rate_values[392] = 2*KNO3AL*5.5
	rate_values[393] = 1.33e-10
	rate_values[394] = J[15]*2
	rate_values[395] = KRO2HO2*0.890
	rate_values[396] = KRO2NO
	rate_values[397] = KRO2NO3
	rate_values[398] = 6.70e-15*RO2
	rate_values[399] = KRO2HO2*0.890
	rate_values[400] = KRO2NO*0.118
	rate_values[401] = KRO2NO*0.882
	rate_values[402] = KRO2NO3
	rate_values[403] = 6.70e-15*0.7*RO2
	rate_values[404] = 6.70e-15*0.3*RO2
	rate_values[405] = KRO2HO2*0.859
	rate_values[406] = KRO2NO
	rate_values[407] = KRO2NO3
	rate_values[408] = 6.70e-15*RO2
	rate_values[409] = KNO3AL*5.5
	rate_values[410] = 8.92e-11*0.232
	rate_values[411] = 8.92e-11*0.768
	rate_values[412] = J[15]
	rate_values[413] = KAPHO2*0.56
	rate_values[414] = KAPHO2*0.44
	rate_values[415] = KAPNO
	rate_values[416] = KFPAN
	rate_values[417] = KRO2NO3*1.74
	rate_values[418] = 1.00e-11*RO2
	rate_values[419] = KAPHO2*0.44
	rate_values[420] = KAPHO2*0.56
	rate_values[421] = KAPNO
	rate_values[422] = KFPAN
	rate_values[423] = KRO2NO3*1.74
	rate_values[424] = 1.00e-11*RO2
	rate_values[425] = 8.01e-11
	rate_values[426] = J[41]+J[15]
	rate_values[427] = 7.03e-11
	rate_values[428] = J[55]+J[15]
	rate_values[429] = KDEC
	rate_values[430] = 7.66e-11
	rate_values[431] = J[15]
	rate_values[432] = KRO2HO2*0.820
	rate_values[433] = KRO2NO
	rate_values[434] = KRO2NO3
	rate_values[435] = 2.50e-13*RO2
	rate_values[436] = 2.00e-10
	rate_values[437] = J[41]+J[35]
	rate_values[438] = 2.23e-11
	rate_values[439] = J[54]+J[35]
	rate_values[440] = KROSEC*O2
	rate_values[441] = 1.26e-10
	rate_values[442] = J[35]
	rate_values[443] = 1.04e-11
	rate_values[444] = J[41]
	rate_values[445] = KRO2HO2*0.859
	rate_values[446] = KRO2NO*0.138
	rate_values[447] = KRO2NO*0.862
	rate_values[448] = KRO2NO3
	rate_values[449] = 1.30e-12*RO2*0.2
	rate_values[450] = 1.30e-12*RO2*0.6
	rate_values[451] = 1.30e-12*RO2*0.2
	rate_values[452] = 7.29e-12
	rate_values[453] = 6.77e-12
	rate_values[454] = KBPAN
	rate_values[455] = 3.61e-11
	rate_values[456] = J[41]+J[15]
	rate_values[457] = 2.56e-11
	rate_values[458] = J[55]+J[15]
	rate_values[459] = 2.70e+14*numpy.exp(-6643/TEMP)
	rate_values[460] = 2.86e-11
	rate_values[461] = J[15]
	rate_values[462] = KRO2HO2*0.625
	rate_values[463] = KRO2NO
	rate_values[464] = KRO2NO3
	rate_values[465] = 2.00e-12*RO2
	rate_values[466] = 1.29e-11
	rate_values[467] = J[41]+J[22]
	rate_values[468] = KDEC
	rate_values[469] = 2.05e-11
	rate_values[470] = J[41]+J[35]
	rate_values[471] = 5.37e-12
	rate_values[472] = J[55]+J[35]
	rate_values[473] = KDEC
	rate_values[474] = 1.69e-11
	rate_values[475] = J[35]
	rate_values[476] = 3.45e-11
	rate_values[477] = J[41]+J[15]
	rate_values[478] = KDEC
	rate_values[479] = KAPHO2*0.44
	rate_values[480] = KAPHO2*0.15
	rate_values[481] = KAPHO2*0.41
	rate_values[482] = KAPNO
	rate_values[483] = KFPAN
	rate_values[484] = KRO2NO3*1.74
	rate_values[485] = 1.00e-11*RO2*0.7
	rate_values[486] = 1.00e-11*RO2*0.3
	rate_values[487] = KRO2HO2*0.770
	rate_values[488] = KRO2NO
	rate_values[489] = KRO2NO3
	rate_values[490] = 2.00e-12*RO2*0.2
	rate_values[491] = 2.00e-12*RO2*0.6
	rate_values[492] = 2.00e-12*RO2*0.2
	rate_values[493] = 4.75e-12
	rate_values[494] = J[41]+J[35]
	rate_values[495] = KRO2HO2*0.770
	rate_values[496] = KRO2NO
	rate_values[497] = KRO2NO3
	rate_values[498] = 2.00e-12*RO2
	rate_values[499] = 8.83e-13
	rate_values[500] = KBPAN
	rate_values[501] = 7.55e-11
	rate_values[502] = J[41]+J[22]+J[15]
	rate_values[503] = 7.19e-11
	rate_values[504] = KBPAN
	rate_values[505] = KRO2HO2*0.820
	rate_values[506] = KRO2NO
	rate_values[507] = KRO2NO3
	rate_values[508] = 8.80e-13*0.6*RO2
	rate_values[509] = 8.80e-13*0.2*RO2
	rate_values[510] = 8.80e-13*0.2*RO2
	rate_values[511] = 3.25e-11
	rate_values[512] = J[41]
	rate_values[513] = 4.00e+04
	rate_values[514] = KROSEC*O2
	rate_values[515] = 1.70e-11
	rate_values[516] = J[41]
	rate_values[517] = 3.29e-12
	rate_values[518] = J[53]
	rate_values[519] = KDEC
	rate_values[520] = KNO3AL*8.5
	rate_values[521] = 2.63e-11
	rate_values[522] = J[15]
	rate_values[523] = 7.89e-12
	rate_values[524] = KRO2HO2*0.914
	rate_values[525] = KRO2NO*0.104
	rate_values[526] = KRO2NO*0.896
	rate_values[527] = KRO2NO3
	rate_values[528] = 6.70e-15*RO2*0.7
	rate_values[529] = 6.70e-15*RO2*0.3
	rate_values[530] = 8.33e-11
	rate_values[531] = J[41]+J[22]+J[15]
	rate_values[532] = KDEC
	rate_values[533] = KRO2HO2*0.890
	rate_values[534] = KRO2NO
	rate_values[535] = KRO2NO3
	rate_values[536] = 6.70e-15*RO2
	rate_values[537] = 3.22e-12
	rate_values[538] = J[22]
	rate_values[539] = KRO2HO2*0.770
	rate_values[540] = KRO2NO*0.098
	rate_values[541] = KRO2NO*0.902
	rate_values[542] = KRO2NO3
	rate_values[543] = 8.80e-13*0.2*RO2
	rate_values[544] = 8.80e-13*0.6*RO2
	rate_values[545] = 8.80e-13*0.2*RO2
	rate_values[546] = KRO2HO2*0.706
	rate_values[547] = KRO2NO
	rate_values[548] = KRO2NO3
	rate_values[549] = 8.80e-13*RO2
	rate_values[550] = 2.39e-11
	rate_values[551] = J[22]*2
	rate_values[552] = 2.70e-11
	rate_values[553] = J[41]+J[22]*2
	rate_values[554] = 2.29e-11
	rate_values[555] = KBPAN
	rate_values[556] = 3.23e-11
	rate_values[557] = J[41]+J[22]*2
	rate_values[558] = KDEC
	rate_values[559] = 3.55e-11
	rate_values[560] = J[34]
	rate_values[561] = 2.54e-11*0.890
	rate_values[562] = 2.54e-11*0.110
	rate_values[563] = J[22]*2
	rate_values[564] = 1.01e-11
	rate_values[565] = J[41]+J[35]
	rate_values[566] = KDEC
	rate_values[567] = KNO3AL*5.5
	rate_values[568] = 1.33e-11
	rate_values[569] = J[34]
	rate_values[570] = 2*KNO3AL*4.0
	rate_values[571] = 3.39e-11
	rate_values[572] = J[15]
	rate_values[573] = J[34]
	rate_values[574] = 1.20e-10
	rate_values[575] = J[41]+J[15]
	rate_values[576] = KDEC
	rate_values[577] = 1.25e-12
	rate_values[578] = J[55]
	rate_values[579] = KRO2HO2*0.859
	rate_values[580] = KRO2NO
	rate_values[581] = KRO2NO3
	rate_values[582] = 9.20e-14*RO2*0.7
	rate_values[583] = 9.20e-14*RO2*0.3
	rate_values[584] = KAPHO2*0.41
	rate_values[585] = KAPHO2*0.44
	rate_values[586] = KAPHO2*0.15
	rate_values[587] = KAPNO
	rate_values[588] = KFPAN
	rate_values[589] = KRO2NO3*1.74
	rate_values[590] = 1.00e-11*RO2*0.7
	rate_values[591] = 1.00e-11*RO2*0.3
	rate_values[592] = KRO2HO2*0.820
	rate_values[593] = KRO2NO
	rate_values[594] = KRO2NO3
	rate_values[595] = 1.30e-12*RO2
	rate_values[596] = 8.35e-11
	rate_values[597] = J[41]+J[15]
	rate_values[598] = 4.96e-11
	rate_values[599] = J[55]+J[15]
	rate_values[600] = 2.70e+14*numpy.exp(-6643/TEMP)
	rate_values[601] = 8.00e-11
	rate_values[602] = J[15]
	rate_values[603] = KAPHO2*0.15
	rate_values[604] = KAPHO2*0.41
	rate_values[605] = KAPHO2*0.44
	rate_values[606] = KAPNO
	rate_values[607] = KFPAN
	rate_values[608] = KRO2NO3*1.74
	rate_values[609] = 1.00e-11*0.3*RO2
	rate_values[610] = 1.00e-11*0.7*RO2
	rate_values[611] = 1.51e-11
	rate_values[612] = J[41]+J[22]
	rate_values[613] = KDEC
	rate_values[614] = KRO2HO2*0.625
	rate_values[615] = KRO2NO
	rate_values[616] = KRO2NO3
	rate_values[617] = 2.00e-12*0.6*RO2
	rate_values[618] = 2.00e-12*0.2*RO2
	rate_values[619] = 2.00e-12*0.2*RO2
	rate_values[620] = KAPHO2*0.44
	rate_values[621] = KAPHO2*0.15
	rate_values[622] = KAPHO2*0.41
	rate_values[623] = KAPNO
	rate_values[624] = KFPAN
	rate_values[625] = KRO2NO3*1.74
	rate_values[626] = 1.00e-11*0.7*RO2
	rate_values[627] = 1.00e-11*0.3*RO2
	rate_values[628] = 8.69e-11
	rate_values[629] = J[41]+J[35]
	rate_values[630] = 71.11e-12
	rate_values[631] = J[35]
	rate_values[632] = KDEC
	rate_values[633] = 3.78e-11
	rate_values[634] = J[35]
	rate_values[635] = 7.49e-11
	rate_values[636] = J[41]+J[15]
	rate_values[637] = KDEC
	rate_values[638] = KAPHO2*0.15
	rate_values[639] = KAPHO2*0.41
	rate_values[640] = KAPHO2*0.44
	rate_values[641] = KAPNO
	rate_values[642] = KFPAN
	rate_values[643] = KRO2NO3*1.74
	rate_values[644] = 1.00e-11*RO2*0.3
	rate_values[645] = 1.00e-11*RO2*0.7
	rate_values[646] = KRO2HO2*0.625
	rate_values[647] = KRO2NO*0.017
	rate_values[648] = KRO2NO*0.983
	rate_values[649] = KRO2NO3
	rate_values[650] = 2.00e-12*0.2*RO2
	rate_values[651] = 2.00e-12*0.6*RO2
	rate_values[652] = 2.00e-12*0.2*RO2
	rate_values[653] = KAPHO2*0.44
	rate_values[654] = KAPHO2*0.56
	rate_values[655] = KAPNO
	rate_values[656] = KFPAN
	rate_values[657] = KRO2NO3*1.74
	rate_values[658] = 1.00e-11*RO2
	rate_values[659] = KAPHO2*0.56
	rate_values[660] = KAPHO2*0.44
	rate_values[661] = KAPNO
	rate_values[662] = KFPAN
	rate_values[663] = KRO2NO3*1.74
	rate_values[664] = 1.00e-11*RO2
	rate_values[665] = KRO2HO2*0.520
	rate_values[666] = KRO2NO
	rate_values[667] = KRO2NO3
	rate_values[668] = 2.00e-12*RO2
	rate_values[669] = KRO2HO2*0.820
	rate_values[670] = KRO2NO
	rate_values[671] = KRO2NO3
	rate_values[672] = 8.80e-13*RO2
	rate_values[673] = 1.09e-11
	rate_values[674] = J[41]
	rate_values[675] = KDEC
	rate_values[676] = 7.42e-12
	rate_values[677] = 9.65e-12
	rate_values[678] = J[41]
	rate_values[679] = 6.57e-12
	rate_values[680] = 2.96e-12
	rate_values[681] = KBPAN
	rate_values[682] = 1.27e-11
	rate_values[683] = J[41]
	rate_values[684] = KDEC
	rate_values[685] = KRO2HO2*0.706
	rate_values[686] = KRO2NO*0.129
	rate_values[687] = KRO2NO*0.871
	rate_values[688] = KRO2NO3
	rate_values[689] = 2.50e-13*RO2*0.6
	rate_values[690] = 2.50e-13*RO2*0.2
	rate_values[691] = 2.50e-13*RO2*0.2
	rate_values[692] = J[15]
	rate_values[693] = 2.14e-11
	rate_values[694] = J[41]+J[15]
	rate_values[695] = 2.49e-11
	rate_values[696] = KRO2HO2*0.387
	rate_values[697] = KRO2NO
	rate_values[698] = KRO2NO3
	rate_values[699] = 2.00e-12*0.2*RO2
	rate_values[700] = 2.00e-12*0.6*RO2
	rate_values[701] = 2.00e-12*0.2*RO2
	rate_values[702] = KBPAN
	rate_values[703] = 2.10e-11
	rate_values[704] = KRO2HO2*0.770
	rate_values[705] = KRO2NO
	rate_values[706] = KRO2NO3
	rate_values[707] = 8.80e-13*RO2
	rate_values[708] = J[41]+J[35]
	rate_values[709] = 1.90e-12*numpy.exp(190/TEMP)
	rate_values[710] = 5.99e-12
	rate_values[711] = KDEC
	rate_values[712] = J[35]
	rate_values[713] = 2.69e-12
	rate_values[714] = J[34]
	rate_values[715] = J[35]
	rate_values[716] = KNO3AL*4.0
	rate_values[717] = 1.23e-11
	rate_values[718] = 2.73e-12
	rate_values[719] = 6.19e-12
	rate_values[720] = J[41]
	rate_values[721] = 1.12e-12
	rate_values[722] = KBPAN
	rate_values[723] = J[15]
	rate_values[724] = J[35]
	rate_values[725] = KNO3AL*5.5
	rate_values[726] = 6.65e-11
	rate_values[727] = J[15]*2
	rate_values[728] = 2*KNO3AL*2.4
	rate_values[729] = 4.29e-11
	rate_values[730] = 2.34e-11
	rate_values[731] = J[22]
	rate_values[732] = 2.65e-11
	rate_values[733] = J[41]+J[22]
	rate_values[734] = 7.60e-12
	rate_values[735] = KBPAN
	rate_values[736] = J[41]
	rate_values[737] = 5.77e-11
	rate_values[738] = J[56]*0.91
	rate_values[739] = 2.23e-12
	rate_values[740] = KDEC
	rate_values[741] = J[15]
	rate_values[742] = KNO3AL*4.0
	rate_values[743] = 2.45e-11
	rate_values[744] = J[22]
	rate_values[745] = 1.88e-11
	rate_values[746] = J[41]+J[15]
	rate_values[747] = 4.23e-12
	rate_values[748] = KBPAN
	rate_values[749] = 3.12e-13
	rate_values[750] = 1.63e-11
	rate_values[751] = J[41]+J[34]
	rate_values[752] = 1.27e-11
	rate_values[753] = KBPAN
	rate_values[754] = 2.41e-11
	rate_values[755] = J[41]+J[34]
	rate_values[756] = KDEC
	rate_values[757] = 1.85e-11
	rate_values[758] = J[41]
	rate_values[759] = KDEC
	rate_values[760] = KRO2HO2*0.859
	rate_values[761] = KRO2NO*0.104
	rate_values[762] = KRO2NO*0.896
	rate_values[763] = KRO2NO3
	rate_values[764] = 6.70e-15*RO2*0.7
	rate_values[765] = 6.70e-15*RO2*0.3
	rate_values[766] = KRO2HO2*0.820
	rate_values[767] = KRO2NO
	rate_values[768] = KRO2NO3
	rate_values[769] = 6.70e-15*RO2
	rate_values[770] = 1.10e-10
	rate_values[771] = J[41]+J[15]*2
	rate_values[772] = 4.33e-11
	rate_values[773] = J[54]+J[15]*2
	rate_values[774] = 1.80e-14*numpy.exp(-260/TEMP)*O2
	rate_values[775] = 6.99e-11
	rate_values[776] = J[15]*2
	rate_values[777] = 2.91e-11
	rate_values[778] = 1.90e-12*numpy.exp(190/TEMP)
	rate_values[779] = J[41]
	rate_values[780] = J[15]
	rate_values[781] = KDEC
	rate_values[782] = J[31]
	rate_values[783] = J[33]
	rate_values[784] = J[32]
	rate_values[785] = KNO3AL
	rate_values[786] = 3.1e-12*numpy.exp(340/TEMP)
	rate_values[787] = KNO3AL
	rate_values[788] = 1.00e-11*0.200
	rate_values[789] = 1.00e-11*0.800
	rate_values[790] = J[15]
	rate_values[791] = 1.00e-10
	rate_values[792] = J[41]+J[22]
	rate_values[793] = KDEC
	rate_values[794] = 7.00e11*numpy.exp(-3160/TEMP)+5.00e-12*O2
	rate_values[795] = 5.00e-12*O2*3.2*(1-numpy.exp(-550/TEMP))
	rate_values[796] = 5.00e-12*O2*3.2*numpy.exp(-550/TEMP)
	rate_values[797] = KAPHO2*0.56
	rate_values[798] = KAPHO2*0.44
	rate_values[799] = KAPNO
	rate_values[800] = KFPAN
	rate_values[801] = KRO2NO3*1.74
	rate_values[802] = 1.00e-11*RO2
	rate_values[803] = 5.77e-11
	rate_values[804] = J[15]*2
	rate_values[805] = KAPHO2*0.44
	rate_values[806] = KAPHO2*0.56
	rate_values[807] = KAPNO
	rate_values[808] = KFPAN
	rate_values[809] = KRO2NO3*1.74
	rate_values[810] = 1.00e-11*RO2
	rate_values[811] = 1.86e-11
	rate_values[812] = J[41]+J[34]
	rate_values[813] = 7.82e-12
	rate_values[814] = J[55]+J[34]
	rate_values[815] = KDEC
	rate_values[816] = 1.75e-11
	rate_values[817] = J[34]
	rate_values[818] = 3.31e-11
	rate_values[819] = J[41]
	rate_values[820] = KDEC
	rate_values[821] = KNO3AL*5.5
	rate_values[822] = 2.37e-11
	rate_values[823] = J[15]
	rate_values[824] = J[35]
	rate_values[825] = KAPHO2*0.15
	rate_values[826] = KAPHO2*0.41
	rate_values[827] = KAPHO2*0.44
	rate_values[828] = KAPNO
	rate_values[829] = KFPAN
	rate_values[830] = KRO2NO3*1.74
	rate_values[831] = 1.00e-11*0.7*RO2
	rate_values[832] = 1.00e-11*0.3*RO2
	rate_values[833] = J[22]
	rate_values[834] = J[41]
	rate_values[835] = 7.34e-12
	rate_values[836] = KBPAN
	rate_values[837] = 3.74e-12
	rate_values[838] = 1.68e-11
	rate_values[839] = J[41]
	rate_values[840] = 1.32e-11
	rate_values[841] = KBPAN
	rate_values[842] = 6.69e-11
	rate_values[843] = J[34]+J[15]
	rate_values[844] = KRO2HO2*0.706
	rate_values[845] = KRO2NO
	rate_values[846] = KRO2NO3
	rate_values[847] = 8.8e-13*RO2
	rate_values[848] = KRO2HO2*0.625
	rate_values[849] = KRO2NO
	rate_values[850] = KRO2NO3
	rate_values[851] = 8.80e-13*RO2
	rate_values[852] = KAPHO2*0.44
	rate_values[853] = KAPHO2*0.56
	rate_values[854] = KAPNO
	rate_values[855] = KFPAN
	rate_values[856] = KRO2NO3*1.74
	rate_values[857] = 1.00e-11*RO2
	rate_values[858] = KRO2HO2*0.625
	rate_values[859] = KRO2NO
	rate_values[860] = KRO2NO3
	rate_values[861] = 2.00e-12*RO2
	rate_values[862] = J[34]
	rate_values[863] = 1.23e-11
	rate_values[864] = J[41]+J[15]
	rate_values[865] = 1.58e-11
	rate_values[866] = J[22]+J[41]
	rate_values[867] = 3.38e-11
	rate_values[868] = KDEC
	rate_values[869] = 7.46e-11
	rate_values[870] = J[41]
	rate_values[871] = KDEC
	rate_values[872] = 6.55e-12
	rate_values[873] = J[41]+J[35]
	rate_values[874] = 2.92e-12
	rate_values[875] = KBPAN
	rate_values[876] = 9.61e-12
	rate_values[877] = J[41]+J[35]
	rate_values[878] = KDEC
	rate_values[879] = 1.44e-11
	rate_values[880] = J[34]+J[35]
	
	# aqueous-phase reactions
	
	return(rate_values, erf, err_mess)
