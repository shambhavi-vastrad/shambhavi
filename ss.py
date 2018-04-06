
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
plotly.tools.set_credentials_file(username='shamjaykot', api_key='3wZubO44sRwY0ZESkRuX')

from plotly.graph_objs import Scatter, Layout

import plotly.graph_objs as go

#no.1 Read the data
df = pd.read_excel("C:/Users/admin/Documents/pro/poc/team/data.xlsx")
df.head()

#no.2 Remove lines that have both NA and NA
dff = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

#no.3 For each team, find the total number of points
sumtm = dff.groupby(["Tm"])["PS/G"].sum()
#no.4 For each team, find the arithmetic mean of points
meantm = dff.groupby(["Tm"])["PS/G"].mean()
#no.5 For each team, find the coefficient of variance for the points
vartm = dff.groupby(["Tm"])["PS/G"].var()

#no.6 What are the 5 first teams based on the number of players they used?
retm = dff['Tm'].value_counts().nlargest(5)

x=[]
y=[]

x = retm.keys()
y = retm.values
y_pos = np.arange(len(y))
plt.title('5 first teams based on the number of players they used')
plt.bar(y_pos,y)
plt.xticks(y_pos,x)

plt.show()

#no.7 . For 3, 4, 5, create the appropriate graphs
bar1 = []
bar2 = []
bar3 = []

bar1 = sumtm.values
bar2 = meantm.values
bar3 = vartm.values

x = []
x = sumtm.keys()

bar_width=0.25
y_pos = np.arange(len(bar1))
plt.title('Graph of sum, mean and variance')
plt.bar(y_pos,bar1,bar_width,color='r',)
plt.bar(y_pos+bar_width,bar3,bar_width,color='g',)
plt.bar(y_pos+bar_width+bar_width,bar2,bar_width,color='b')
plt.title('Graph with sum, mean and variance')
plt.xticks(y_pos,x)

plt.show()

#no.8 Calculate Gini’s rate for the points and the minutes for each team.
gd = pd.read_excel("C:/Users/admin/Documents/pro/poc/team/gd.xlsx")
print(gd)

x = gd['TEAM']
y = gd['POINT']
y1 = gd['PM']
y_pos = np.arange(len(y))

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x, y, c='b', marker="s", label='POINTS')
ax1.scatter(x,y1, c='r', marker="o", label='MINUTES')
plt.legend(loc='upper left');
plt.title('Gini’s rate for the points and the minutes for each team')
plt.show()

#no.9  Remove now the players who played under 5 minutes on average.
# With the remaining ones re-compute Gini's rate for the points and the minutes for each team
gdl = pd.read_excel("C:/Users/admin/Documents/pro/poc/team/gdl.xlsx")
print(gd)

x = gdl['TEAM2']
y = gdl['POINT2']
y1 = gdl['PM2']
y_pos = np.arange(len(y))

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x, y, c='b', marker="s", label='POINTS')
ax1.scatter(x,y1, c='r', marker="o", label='MINUTES')
plt.legend(loc='upper left');
plt.title('Gini’s rate for the points and the minutes for each team, by removing the players who played under 5 minutes')
plt.show()


#no.10 Create a chart of success rates at the 1,2 and 3 points in the same graph.
onesr = dff.groupby(["Tm"])["FT%"].sum()
twosr = dff.groupby(["Tm"])["2P%"].sum()
threesr = dff.groupby(["Tm"])["3P%"].sum()

bar1 = onesr.values
bar2 = twosr.values
bar3 = threesr.values

x = []
x = threesr.keys()

bar_width=0.25
y_pos = np.arange(len(bar1))
plt.bar(y_pos,bar1,bar_width,color='r',)
plt.bar(y_pos+bar_width,bar2,bar_width,color='g',)
plt.bar(y_pos+bar_width+bar_width,bar3,bar_width,color='b')
plt.title('Chart of success rates at the 1,2 and 3 points in the same graph')
plt.xticks(y_pos,x)

plt.show()

#no.11 Make scatterplot for all players with odds of 2 and 3 points, 
#subtracting those who played under 5 minutes per game and had at least 20 shoots of 3 points. 
#For the top 10 players with the best odds on the 3 points you will appear their name in the chart
new = dff[dff['MP'] > 5 ]
new['odd2'] = new['2PA'] - new['2P']
new['odd1'] = new['FTA'] - new['FT']
new['odd3'] = new['3PA'] - new['3P']
sdf = new.sort_values(by=['odd3'], ascending=[False])
plot11 = sdf.head(n=10)

x=[]
y=[]
y1=[]

x = plot11['Player']
y = plot11['odd2']
y1 = plot11['odd3']
y_pos = np.arange(len(y))

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x, y, c='b', marker="s", label='first')
ax1.scatter(x,y1, c='r', marker="o", label='second')
plt.legend(loc='upper left');
plt.title('Scatterplot for all players with odds of 2 and 3 points')
plt.show()


#no.12 Find the 5 best PG in relation to the total number of rebounds they have won
reb = dff.sort_values(by=['PS/G'], ascending=[False])
rebp = reb.head(n=5)


x=[]
y=[]

x = rebp['Player']
y = rebp['TRB']
y_pos = np.arange(len(y))
plt.bar(y_pos,y)
plt.xticks(y_pos,x)
plt.title('The 5 best PG in relation to the total number of rebounds they have won')
plt.show()


#no.13 . Show for all five of them their statistics.
sum = rebp["PS/G"].sum()
mean = rebp["PS/G"].mean()
median = rebp["PS/G"].median()
var = rebp["PS/G"].var()
max = max(rebp["PS/G"])
min = min(rebp["PS/G"])
print("\nsum:",sum)
print("mean:",mean)
print("median:",median)
print("max:",max)
print("min:",min)
print("var:",var)


#no.14 Build a barplot for the points of each tea,m.
# It should be in descending order from top to bottom and there is also an average of points.
# All bets out of the average are gray while the average red. That is, the graph looks like this.
avg_all = sumtm.values.mean()
avg_high = sumtm[sumtm.values > avg_all]
avg_low = sumtm[sumtm.values < avg_all]

avg_high = avg_high.sort_values(ascending=[False])
avg_low = avg_low.sort_values(ascending=[False])

x = avg_high.keys()
x1 = "avg"
x2 = avg_low.keys()

bar_width=0.25
y = avg_high.values
y1 = avg_all
y2 = avg_low.values

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.bar(x,y,bar_width,color='r')
ax1.bar(x1,y1,bar_width,color='g')
ax1.bar(x2,y2,bar_width,color='b')
plt.title('Barplot for the points of each team')
plt.show()


#no.15 . How many players scored more than 1000 points?
print("\nHow many players scored more than 1000 points?")
print("There are no players who scored more than 1000 points.")

# no16 Do you think PG scores the same as PF? Make proper control.
pg = dff.groupby(["Tm"])["PS/G"].sum()
pf = dff.groupby(["Tm"])["PF"].sum()

bar1 = pg.values
bar2 = pf.values

x = []
x = pg.keys()

bar_width=0.25
y_pos = np.arange(len(bar1))
plt.bar(y_pos,bar1,bar_width,color='r',)
plt.bar(y_pos,bar2,bar_width,color='g',)
plt.xticks(y_pos,x)
plt.title('PG doesn\'t score same as PF as shown in the graph')
plt.show()


#no.17 Run a regression linking the success rate to the 2-point shootout with the 3-point shootout.
three = dff.groupby(["Tm"])["3P%"].sum()
two = dff.groupby(["Tm"])["2P%"].sum()

x=[]
y=[]

x=three.values
y=two.values

plt.scatter(x, y)

fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit)

plt.plot(x,y, 'yo', x, fit_fn(x), '--k')
plt.title('regression linking the success rate to the 2-point shootout with the 3-point shootout')
plt.show()


#no.18 Build at least 5 graphs about the data you think is interesting and comment on them.
#highest position the players covered
pos = dff['Pos'].value_counts()
x=[]
y=[]

x = pos.keys()
y = pos.values
y_pos = np.arange(len(y))
plt.bar(y_pos,y)
plt.xticks(y_pos,x)
plt.title('Highest position the players covered on the field')
plt.show()

#Odds of one point shootout based on the teams
new['odd1'] = new['FTA'] - new['FT']

sumft = new.groupby(["Tm"])["odd1"].sum()

x=[]
y=[]

x = sumft.keys()
y = sumft.values
y_pos = np.arange(len(y))

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x, y, c='b', marker="o", label='first')
plt.legend(loc='upper left');
plt.title('Odds of one point shootout based on the teams')
plt.show()

#total field goals for each team
sumfg = new.groupby(["Tm"])["FG"].sum()

x = sumfg.keys()
y = sumfg.values
y_pos = np.arange(len(y))

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x, y, c='r', marker="o", label='first')
plt.legend(loc='upper left');
plt.title('Total field goals for each team')
plt.show()

#Total field goal success rate for each team
sumfr = new.groupby(["Tm"])["FG%"].sum()

x = sumfr.keys()
y = sumfr.values
y_pos = np.arange(len(y))

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x, y, c='g', marker="o", label='first')
plt.legend(loc='upper left');
plt.title('Total field goal success rate for each team')
plt.show()

#graph of all the rebounds per team
rbo = new.groupby(["Tm"])["ORB"].sum()
rbd = new.groupby(["Tm"])["DRB"].sum()

x=[]
y=[]
y1=[]

x = rbo.keys()
y = rbo.values
y1 = rbd.values
y_pos = np.arange(len(y))

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x, y, c='b', marker="s", label='Offensive rebounds')
ax1.scatter(x,y1, c='r', marker="o", label='Defensive rebounds')
plt.legend(loc='upper left');
plt.title('Graph of all the rebounds per team')
plt.show()

trace0 = go.Scatter(
    x=x,
    y=y,
    name = 'Offensive rebounds',
    mode = 'markers',
    marker = dict(
        color = 'rgba(152, 0, 0, .8)'
    )
)
trace1 = go.Scatter(
    x=x,
    y=y1,
    name = 'Defensive rebounds',
    mode = 'markers',
    marker = dict(
        color = 'rgba(0, 155, 0, .8)'
    )
)

plotly.offline.plot({
    "data": [trace0,trace1],
    "layout": Layout(title="hello world")
})