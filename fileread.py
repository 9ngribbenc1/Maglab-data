# This file is a python module storing functions that read in data
# from .txt files generate by labview. They were originally developed 
# in Spyder for individual types of experiments. 

# :set ts=8 et sw=4 sts=4


import numpy as np
import pandas as pd


# Read in a metadata flexibly
def mtdata_rd(fn, strng):
    with open(fn, 'r') as input_data:
        # Below reads through the file lines until one matches the
	# chosen metadata header line. The lines are read in sequentially.
        for line in input_data:
            if line.strip() == strng:
                break
        # Read the desired metadatum
        for line in input_data: # this line continues reading lines
            if line.strip() != '\x00\x00\x00' and line.strip() != '':
                mtdatum = line.strip()
                break
    return mtdatum

# Find the line number at which a certain string resides in a .txt file
def find_line(fn, strng):
    ln = 0
    with open(fn, 'r') as input_data:
        for line in input_data:
            ln = ln+1
            if line.strip() == strng:
                break
    return ln-1

# Create a pandas dataframe from the specified .txt file
def gen_df(fn, measurement):
    if measurement == 'IV':
        header = 'Current (A)	Voltage Vertical (V)	Voltage Horizontal (V)'
    if measurement == 'Hall':
        header = 'Time Hall 1 (s)	Time Hall 2 (s)	Magnetic Field 1 (T)	Magnetic Field 2 (T)	Hall Voltage 1 (V)	Hall Voltage 2 (V)	Time VdP (s)	Magnetic Field VdP (T)	Temperature VdP (K)	Temperature VdP (K)	Temperature VdP (K)'
    hln = find_line(fn, header)
    # The line below reads the file and creates the dataframe
    data = pd.read_csv(fn, sep='\t+', header=hln, skiprows=0, engine='python')
    # The lines below zero all the times for computational ease

    if measurement == 'Hall':
        data.iloc[:,0] -= data.iloc[0,0]
        data.iloc[:,1] -= data.iloc[0,1]
        data.iloc[:,6] -= data.iloc[0,6]
	meas = ['Time', 'Time', 'Magnetic Field', 'Magnetic Field', 'Hall Voltage', 'Hall Voltage', 'Time', 'Magnetic Field', 'Temperature', 'Voltage', 'Voltage']
        unit = ['Seconds', 'Seconds', 'Tesla', 'Tesla', 'Volts', 'Volts', 'Seconds', 'Tesla', 'Kelvin', 'Volts', 'Volts']
        purp = ['Hall 1', 'Hall 2', 'Hall 1', 'Hall 2', 'Hall 1', 'Hall 2', 'MR', 'MR', 'Temperature', 'MR', 'MR']

    if measurement == 'IV':
        meas = ['Current', 'Voltage', 'Voltage']
        unit = ['Amps', 'Volts', 'Volts']
        purp = ['Source', 'Vertical', 'Horizontal']
    
    data.columns = pd.MultiIndex.from_arrays([meas, unit, purp], names=['Measurement', 'Unit', 'Purpose'])
    return data


