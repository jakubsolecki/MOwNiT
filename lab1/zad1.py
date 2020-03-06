import numpy as np
from tabulate import tabulate

table = tabulate([['float64', np.finfo(np.float64).precision,
                   f'{np.finfo(np.float64).min} to {np.finfo(np.float64).max}'],
                  ['float32', np.finfo(np.float32).precision,
                   f'{np.finfo(np.float32).min} to {np.finfo(np.float32).max}'],
                  ['float16', np.finfo(np.float16).precision,
                   f'{np.finfo(np.float16).min} to {np.finfo(np.float16).max}']],
                 headers=['Type', 'Precision', 'Range'])
print(table)