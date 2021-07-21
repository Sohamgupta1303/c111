import csv 
import plotly.graph_objects as go
import plotly.figure_factory as pf
import pandas as pd
import statistics as s
import random as r

df = pd.read_csv('studentMarks.csv')

data = ['Math_score'].tolist()

figure = pf.create_distplot([data], ['Math_score'], show_hist= False)

figure.show()

mean = s.mean(data)
stdv = s.stdev(data)

def randomsetofmean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = r.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = s.mean(dataset)
    return mean

meanlist = []
for i in range (0,1000):
    setofMean = randomsetofmean(100)
    meanlist.append(setofMean)

mean = s.mean(meanlist)
stdv = s.stdev(meanlist)

print(mean)
print(stdv)
