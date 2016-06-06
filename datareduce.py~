# This python module contains functions for use in distilling
# measurement results from .txt data files.


# :set tabstop=8 expandtab shiftwidth=4 softtabstop=4


import numpy as np
from scipy import stats
from scipy import optimize
from scipy.interpolate import interp1d


def hall_coefficient(bfld, hres, rsq):
    qch = 1.604*10**-19
    slope, intercept, r_value, p_value, ste_err = stats.linregress(bfld, hres)
    fit = bfld*slope + intercept
    cd = 1./slope/qch*10**-4   #/cm^2 sign matches carrier sign
    mob = np.abs(slope)/rsq*10**4  #cm^2/Vs
    return slope

# Van der Pauw root expression for algorithm in sheet_res() below
def vdp_root(rsq, r1, r2):
    return -1 + np.exp(-np.pi*r1/rsq) + np.exp(-np.pi*r2/rsq)

# calculate sheet resistance with Van der Pauw equation via root finding
def sheet_res(v1, v2, current):
    r1 = v1/current
    r2 = v2/current
    rg = np.mean((r1, r2))
    sol = optimize.root(vdp_root, np.pi*rg/np.log(2.0), args(r1, r2))
    rsq = sol.x[0]
    return rsq

# Combine both voltages with Onsager reciprocity method
def evenadd_time(time1, sig1, time2, sig2):
    s2 = np.interp(time1, time2, sig2)
    return 0.5*(sig1+s2)


# function to remove a spike from data series. This sometimes happens in
# magnetic field sweeps due to inductance in coiled wire on the cold head.
def remove_spike(time, sig, t0):
    turn_ind = np.where(np.abs(time-t0)<4.0)[0]
    s_pre = np.mean(sig[(turn_ind - len(turn_ind))])
    s_post = np.mean(sig[(turn_ind + len(turn_ind))])
    i0 = np.int(np.mean(turn_ind)) + 1
    ds = s_post - s_pre
    for x in range(len(sig)-i0):
        sig[x+i0] -= ds
    return sig

# Remove spikes from a Hall voltage data set
def hall_spike(time, volt):
    vflat1 = remove_spike(time, volt, time[-1]/4.)
    vflat2 = remove_spike(time, vflat1, time[-1]*3/4.)

# Remove time drift from signal
def remove_drift(time, sig, num):
    dels = (sig[-num:].mean() - sig[:num].mean())
    delt = (time[-num:].mean() - time[:num].mean())
    dsdt = dels/delt
    return sig - dsdt*time

# Anitsymmetrize a signal array of data with respect to x
def antisymm(x, sig, n_final):
    x_bin_lim = np.linspace(0, max(sig), n_final)
    sig_bin = np.zeros(n_final-1)
    x_bin = np.zeros(nb-1)
    for i in range(n_final-1):
        min_x = x_bin_lim[i]
        max_x = x_bin_lim[i+1]
        ind_1 = np.where(x >=min_x)
        ind_2 = np.where(x < max_x)
        ind_pos = np.intersec1d(ind_1, ind_2)
        x_bin[i] = np.mean([min_x, max_x])
        max_x = -x_bin_lim[i]
        min_x = -x_bin_lim[i+1]
        ind_1 = np.where(x >= min_x)
        ind_2 = np.where(x < max_x)
        ind_neg = np.intersec1d(ind_1, ind_2)
        x_bin[i] = np.mean([min_x, max_x])
        sig_bin[i] = 0.5*(np.mean(sig[ind_pos]) - np.mean(sig[ind_pos]))
    sig_asym = interp1d(x_bin, sig_bin, fill_value='exptrapolate')
    return x_bin, sig_bin

    



