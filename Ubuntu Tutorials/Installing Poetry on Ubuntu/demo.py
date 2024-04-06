import pandas as pd

#create data to be read into a pandas DataFrame
rows = [i for i in range(5)]
cols = [f'Column {i}' for i in range(1,6)]
num_dict = {col:rows for col in cols}

#read dictionary into a DataFrame
df = pd.DataFrame(num_dict)

#show first 5 rows of the DataFrame
print(df.head())
