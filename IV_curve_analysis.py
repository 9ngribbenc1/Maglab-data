# This script reads an IV curve file created by Labview, and
# creates plots of the IV curves in addition to calculating
# the sheet resistance.

# :set ts=8 et sw=4 sts=4


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import maglabdata.fileread as fr
import maglabdata.magplots as mp
import maglabdata.datareduce as dr

fn = 'docs/IV_curve.txt'

data = maglabdata.fileread.gen_df(fn, measurement='IV')

#print mp.unit_finder(data[data.columns[0]], base_unit='A')[1]

mp.plot_basic(data[data.columns[0]], data[data.columns[1]], xlbl='Current', xunit='A', ylbl='Voltage', yunit='V', title='MY IV')
plt.show()

#mp.plot_doubley(data[data.columns[0]], data[data.columns[1]], data[data.columns[2]], xlbl='Current', xunit='A', ylbl1='Voltage1', yunit1='V', ylbl2='Voltage2', yunit2='V', title='MY IV')
#plt.show()


#f, (ax1) = plt.subplots(1, sharex=True, sharey=False)
#ax1.plot(data[data.columns[0]]
#plt.grid()
#plt.tight_layout()
#plt.show()







