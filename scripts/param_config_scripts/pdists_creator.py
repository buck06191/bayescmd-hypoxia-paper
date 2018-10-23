"""Create BayesCMD pdists csv file with wider priors."""

import pandas as pd
import copy
import sys
import os.path as op
from pathlib import Path

current_file = Path(op.abspath(__file__))

param_df = pd.read_csv(op.join(current_file.parents[2],
                               'pdist_files',
                               'pdists_BS_PLOS.csv'),
                       header=None,
                       names=['Parameter', 'Dist. Type',
                              'Min', 'Max', 'Default'],
                       index_col=0)

delta = abs(param_df.loc[:, 'Default']*0.5)
new_max = param_df.loc[:, 'Default'].values + delta
new_min = param_df.loc[:, 'Default'].values - delta

# for idx, v_min in enumerate(new_min):
#     v_max = copy.deepcopy(new_max[idx])
#     if v_min > v_max:
#         new_max[idx] = v_min
#         new_min[idx] = v_max


new_df = param_df.copy()
new_df['Min'] = new_min
new_df['Max'] = new_max

new_df.to_csv(op.join(current_file.parents[2],
                      'pdist_files',
                      'pdists_BS_PLOS_wide.csv'),
              header=False)
