# #!/usr/bin/env python3
#
"""dfcbenchmarker is a package that compares different dynamic functoinal connectivity methods against eachother."""
#
__author__ = "William Hedley Thompson (wiheto)"
__version__ = "0.1" #Peer reviewed version becomes version 1.0
#
from dfcbenchmarker.get_data import gen_data_sim1,gen_data_sim2,gen_data_sim3,gen_data_sim4, load_data, gen_data
from dfcbenchmarker.dfc_calc import dfc_calc
from dfcbenchmarker.dfc_evaluate import bayes_model,save_bayes_model,load_bayes_model,calc_waic, model_dfc, trace_plot
from dfcbenchmarker.misc import check_params,standerdize, square_axis, autocorr, panel_letters, get_discrete_colormap, multiindex_preproc, load_params
from dfcbenchmarker.plot import plot_betadfc_distribution, plot_fluctuating_covariance, plot_method_correlation, plot_dfc_timeseries,plot_timeseries
from dfcbenchmarker.add_method import calc_new_method
from dfcbenchmarker.run import run_simulations
from dfcbenchmarker.send_method import send_method
