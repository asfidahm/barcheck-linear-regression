import csv
import matplotlib.pyplot as plt
import numpy as np

#membaca data csv
with open('data.csv') as csvfile:
    data = csv.reader(csvfile, delimiter = ',', quotechar = '|')
    next(data)
    dfx = []
    dy = []
    n = 0
    for row in data:
        dfx.append(int(row[0]))
        dy.append(float(row[1]))
        n += 1

x = np.array(dfx) #variabel terikat
y = np.array(dy) #variabel bebas

#sigma x, y, x2, y2, dan xy
s_x = np.sum(x)
s_y = np.sum(y)
s_xx = np.sum(x*x)
s_xy = np.sum(x*y)

#menghitung xbar, ybar
x_bar = (1/n)*s_x
y_bar = (1/n)*s_y
print("xbar : {}, ybar : {}".format(x_bar, y_bar))

#menghitung koefisien regresi b1 dan b0
b_1 = (n*s_xy - s_x*s_y) / (n*s_xx - s_x*s_x)
b_0 = y_bar - b_1*x_bar
print("B1 : {}, B2 : {}".format(b_1, b_0))

#scatter plot data
plt.scatter(x, y, color = "m", marker = "o", s = 30)

#menghitung persamaan regresi linear
y_pred = b_0 + b_1*x

#mengatur plot regresi linear
plt.plot(x, y_pred, color = "g")

#menampilkan plot
plt.xlabel('Measurement Depth (du) (m)')
plt.ylabel('True Depth (dt) (m)')
plt.show()

#true depth of 3.75 6.24 7.4 dan 12.65
soal = [3.75, 6.24, 7.4, 12.65]
for i in soal:
    y_true = b_0 + b_1*i
    print("{} : {}".format(i, y_true))
