# This module contains functions for producing plots of the various maglab
# data and experiments. It requires the fileread module for reading the data
# and the datareduce module for extracting a signal. I also  have included
# my own preferences for plot settings such as text size.

# :set ts=8 et sw=4 sts=4


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define metric prefix dictionary
metricpre = {0: '',
        1: 'k',
        2: 'M',
        3: 'G',
        -1: 'm',
        -2: '$\mu$',
        -3: 'n'
        }

# Determine the appropriate units for plotting an array of data
def unit_finder(x, base_unit='Unit'):
    oom = np.log(np.mean(abs(x)))/np.log(10.)
    met_pre_num = (oom - oom%3)/3
    return metricpre[met_pre_num] + base_unit, 10**(3*met_pre_num)

# plot two arrays or lists against each other with matplotlib
def plot_basic(x, y, xlbl='x', xunit='U', ylbl='y', yunit='U', mc='b-', lbl='Some Data', title='Plot Title'):
    xup = unit_finder(x, xunit)
    yup = unit_finder(y, yunit) 
    f, (ax1) = plt.subplots(1, sharex=True, sharey=False)
    ax1.plot(x/xup[1], y/yup[1], mc, label=lbl)
    ax1.set_xlabel(xlbl+' ('+xup[0]+')', fontsize=25)
    ax1.set_ylabel(ylbl+' ('+yup[0]+')', fontsize=25)
    ax1.set_title(title, fontsize=30)
    ax1.tick_params(axis='both', which='major', labelsize=18)
    ax1.yaxis.grid(True, which='major')
    ax1.xaxis.grid(True, which='major')
    plt.tight_layout()

# plot two arrays against one and have the plot share an x axis and have two y axes.
def plot_doubley(x, y1, y2, mc1='b-', mc2='r-', xlbl='x', xunit='U', ylbl1='y1', yunit1='U', ylbl2='y2', yunit2='U', lbl1='Some Data', lbl2='Sum Data', title='Plot Title'):
    xup = unit_finder(x, xunit)
    yup1 = unit_finder(y1, yunit1)
    yup2 = unit_finder(y2, yunit2)
    f, (ax1) = plt.subplots(1, sharex=True, sharey=False)
    ax2 = ax1.twinx()
    ax1.plot(x/xup[1], y1/yup1[1], mc1, label=lbl1)
    ax2.plot(x/xup[1], y2/yup2[1], mc2, label=lbl2)
    ax1.set_xlabel(xlbl+' ('+xup[0]+')', fontsize=25)
    ax1.set_ylabel(ylbl1+' ('+yup1[0]+')', fontsize=25)
    ax2.set_ylabel(ylbl2+' ('+yup2[0]+')', fontsize=25)
    ax1.set_title(title, fontsize=30)
    ax1.tick_params(axis='both', which='major', labelsize=18)
    ax2.tick_params(axis='both', which='major', labelsize=18)
    ax1.yaxis.grid(True, which='major')
    ax2.yaxis.grid(True, which='major')
    ax1.xaxis.grid(True, which='major')
    plt.tight_layout()




