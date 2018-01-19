import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('numberOfClustersXintraCv.txt', sep=" ", header=None)

x = df[0].values
y1 = df[1].values
y2 = df[2].values
y3 = [y1[index]/y2[index] for index in range(len(y1))]

plt.plot(x, y1, 'r--', label='intra cluster cv')
plt.plot(x, y2, '-', label='inter cluster cv')
plt.plot(x, y3, ':', label='intra cluster cv / inter cluster cv')
legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#00FFCC')

plt.savefig('beta-cv.png')
plt.show()
