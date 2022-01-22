from matplotlib import style
import numpy as np
import csv
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#X_Axis = [1,2,3,4,5,6,7,8]
#Y_Axis = [2,5,3,5,1,6,7,8]

slices = [60, 40]
#labels = ['Males', 'Females']

#plt.pie(slices, labels=labels)

#plt.plot(X_Axis, Y_Axis, Label="X and Y")
#plt.legend()
#plt.show()
plt.style.use("fivethirtyeight")

x = []
y = []

with open('confirmedCases.csv', 'r') as csvfile:
    plts = csv.reader(csvfile, delimiter=':')
    for row in plts:
        x.append(row[1])
        y.append(row[0])

#plt.plot(x,y)
plt.barh(x,y)
#plt.bar(x,y)
plt.tight_layout()
plt.show()


#plt.plot(languages, popularity)
#print(programmingLanguage_counter.most_common(15))
#plt.legend()

#plt.xticks(ticks=x_indexes, labels=ages_x)
