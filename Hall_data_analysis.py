# This script reads Hall data created by Labview, and 
# creates plots of the Hall data in addition to calculating
# the carrier density and mobility

# :set ts=8 et sw=4 sts=4

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import maglabdata.fileread as fr
import maglabdata.datareduce as dr
import maglabdata.magplots as mp

fniv = 'docs/IV_curve.txt'
fnh = 'docs/hall_data.txt'

current = float(fr.mtdata_rd(fnh, '#DC Current (A):'))
rsq = float(fr.mtdata_rd(fnh, '#Sheet Resistance (Ohm/sq):'))

data = fr.gen_df(fnh, measurement='Hall')

voltH = dr.evenadd_time(data.iloc[:,0], data.iloc[:,4], data.iloc[:,0], data.iloc[:,5]) 
bfldH = dr.evenadd_time(data.iloc[:,0], data.iloc[:,2], data.iloc[:,0], data.iloc[:,3])


RH = dr.hall_coefficient(bfldH, voltH/current, rsq)
mp.plot_basic(bfldH, voltH)
plt.show()
print RH


