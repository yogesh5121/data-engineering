import sys

import pandas as pd


print("arguments", sys.argv)

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")
df = pd. DataFrame({'Y':[5,1],'Z':[4,7]})
print(df.head())
df.to_parquet(f"output_day_{sys.argv[1]}.parquet")
print('hello pipline')