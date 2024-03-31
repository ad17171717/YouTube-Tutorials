#Author: Adrian Dolinay

#Description: Python script that will generate multiple csv files for the "PySpark! Reading CSV files into a DataFrame" tutorial
#Please note the overall size of the files generated will be approximately 8 GB

import pandas as pd

cols = [f'Column {num}' for num in range(1,6)]

row_write = [num for num in range(1500000,40000000,1500000)]

for row in row_write:
    d = {col:[num for num in range(row)] for col in cols}
    df = pd.DataFrame(d)
    df.to_csv(f'{str(row)}.csv')