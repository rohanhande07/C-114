import pandas as pd
import plotly.express as px

df = pd.read_csv("main.csv")

GRE_Score = df["GRE Score"].tolist()
Chances_of_admit = df["Chance of Admit "].tolist()

fig = px.scatter(x=GRE_Score, y=Chances_of_admit)
fig.show()

m = 0.01
c = -2.5
y = []
for x in GRE_Score:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=GRE_Score, y=Chances_of_admit)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(GRE_Score), x1= max(GRE_Score)
    )
])
fig.show()

x = 600
y = m * x + c
print(f"Chances of admit of someone based on their GRE Score {x} is {y}")

import numpy as np
GRE_Score_array = np.array(GRE_Score)
Chance_of_admit_array = np.array(Chances_of_admit)

#Slope and intercept using pre-built function of Numpy
m, c = np.polyfit(GRE_Score_array,Chance_of_admit_array,1)

y = []
for x in GRE_Score_array:
  y_value = m*x + c
  y.append(y_value)

#plotting the graph
fig = px.scatter(x=GRE_Score_array, y=Chance_of_admit_array)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(GRE_Score_array), x1= max(GRE_Score_array)
    )
])
fig.show()