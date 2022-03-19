import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('star_data.csv')

distance=pd.to_numeric(df['Distance (ly)'],errors='coerce').dropna()

gravity=df['Surface Gravity (m/s²)']

df=df[(distance<=100) & ((gravity>=150) & (gravity<=350))]

print("Solar systems of" , len(df), "stars are habitable")

df.to_csv("habitable.csv" ,index=False)
