import pandas as pd
#data = [['mahesh',18,99],['abhi',18,90],['gaurav',18,85],['jay',18,75]]
df = pd.DataFrame(columns = ['name','age','precentage'])
df.loc[0] = ['mahesh', 18, 99]
df.loc[1] = ['jay', 18, 36]
df.loc[2] = ['abhi', 18, 90]
df.loc[3] = ['gaurav', 18, 85]
df.loc[4] = ['rupesh', 18, 35]
df.loc[5] = ['Atharva', 18, 40]
df.loc[6] = ['Monu', 18, 50]
df.loc[7] = ['sopan', 18, 99]
df.loc[8] = ['tejas', 18, 99]
print(df)

# print("Hello WorlD !")
