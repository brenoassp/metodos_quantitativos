import matplotlib
import matplotlib.pyplot as plt
import subprocess
from datetime import datetime, timedelta

import pandas as pd

from youtube_traces_from_campus_network.calc import min_value, normalize_value

users = {}

p1 = subprocess.Popen(['awk', '-f', 'get_flows_start_between_timestamp_ontime_rate.awk', 'flow.dat'],
                      stdout=subprocess.PIPE)

output = p1.communicate()[0]

file = open('ontime-rate-without-normalization.txt', 'w')
file.write(output.decode('utf-8'))
file.close()

df = pd.read_csv('ontime-rate-without-normalization.txt', sep=" ", header=None)

ontime_min = df.iloc[:,0].min()
ontime_max = df.iloc[:,0].max()
ontimes_normalized = df.iloc[:,0].apply(normalize_value, args=(ontime_min, ontime_max))

taxa_min = df.iloc[:,1].min()
taxa_max = df.iloc[:,1].max()
rates_normalized = df.iloc[:,1].apply(normalize_value, args=(taxa_min, taxa_max))

df2 = pd.concat([ontimes_normalized, rates_normalized], axis=1)

df2.to_csv('ontime-rate-normalized.csv', sep=' ', index=False, header=False)

axis_x = []
axis_y = []

# for line in output.decode("utf-8").split('\n'):
#     if len(line) > 0:
#         spl_line = line.split()
#         axis_x.append(spl_line[1])
#         axis_y.append(spl_line[0])
#
# i = 0
# # while i < len(axis_x):
# #     new_y =
# #     i += 1
#
plt.scatter(ontimes_normalized.values, rates_normalized.values)
plt.title('tempo de on x taxa')
plt.xlabel('tempo de on')
plt.ylabel('taxa')
plt.savefig('ontime-taxa-normalizado.png')
plt.show()
