import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('SOCR-HeightWeight.csv')
df["BMI"]=df["Weight(Pounds)"]/(df["Height(Inches)"])**2
print(df)
