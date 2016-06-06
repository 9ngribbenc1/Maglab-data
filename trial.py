# This script is for running trials of functions developed in modules.

# :set ts=8 et sw=4 sts=4


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import maglabdata.magplots as mp
import maglabdata.fileread as fr


fn = 'docs/IV_curve.txt'
data = fr.gen_df(fn, 'IV')
print data.head(2)


