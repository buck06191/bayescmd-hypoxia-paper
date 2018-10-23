"""Create BayesCMD configuration file for PLOS simulated data."""
import pandas as pd
import json
from pathlib import Path
import os.path as op
p = Path(op.abspath(__file__))
from bayescmd.abc import priors_creator

current_file = Path(op.abspath(__file__))

param_df = pd.read_csv(op.join(current_file.parents[2],
                                    'pdist_files',
                                    'pdists_BS_PLOS_wide.csv'
                                    ),
                       header=None,
                       names=['Parameter', 'Dist. Type',
                              'Min', 'Max', 'Default'],
                       index_col=0)

# chosen_params = ['sigma_coll',
#                  'R_auto',
#                  'n_h',
#                  'r_t',
#                  'mu_max',
#                  'n_m',
#                  'r_m',
#                  'P_v',
#                  'phi',
#                  'Xtot']

# experimental_params = [
#     'P_ic',
#     'v_on',
#     'n_m',
#     'T_max0',
#     'E_2',
#     'h_0',
#     'K_sigma',
#     'v_un',
#     'R_autc',
#     'v_cn'
#     ]

filtered_params = ['n_m',
                   'r_m',
                   'K_sigma',
                   'p_tot',
                   'k_aut',
                   'v_cn',
                   'sigma_e0',
                   'k2_n',
                   'Xtot',
                   'R_autc']

prior_dict = priors_creator(param_df.loc[filtered_params, 'Default'].to_dict(),
                            0.5)



config_dict = {"model_name": "BS1-1",
               "inputs": ["SaO2sup", "P_a", "Pa_CO2"],
               "create_params": False,
               "priors": prior_dict,
               "targets": ["TOI", "CCO", "HbT", "HbD"],
               "zero_flag": {
                   "TOI": False,
                   "CCO": True,
                   "HbD": True,
                   "HbT": True
               },
               "batch_debug": False,
               "store_simulations": False
               }

with open(op.join(current_file.parents[2],
                       'configuration_files',
                       'filtered_hypoxia_config.json'
                       ),
                       'w') as f:
    json.dump(config_dict, f)
