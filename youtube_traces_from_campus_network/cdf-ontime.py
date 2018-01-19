import pandas as pd
import matplotlib.pyplot as plt

def to_min(value):
    return value/60


df = pd.read_csv('ontime-rate-without-normalization.txt', sep=" ", header=None)

ontimes = df.iloc[:,0].apply(to_min)
rates = df.iloc[:,1]

#ontimes.hist(cumulative=True, normed=1, bins=1000, histtype='step', grid=False)
#plt.show()

n = pd.np.arange(1,len(ontimes.values)+1) / pd.np.float(len(ontimes.values))
Xs = pd.np.sort(ontimes.values)
fig, ax = plt.subplots()
ax.step(Xs,n)
plt.xlabel('tempo de ON (minutos)')
plt.title('Cdf tempo de ON')
#plt.ylabel('')
plt.savefig('cdf-tempoON-minutos.png')
#plt.show()

n = pd.np.arange(1,len(rates.values)+1) / pd.np.float(len(rates.values))
Xs = pd.np.sort(rates.values)
fig, ax = plt.subplots()
ax.step(Xs,n)
plt.xlabel('taxa (kbits/s)')
plt.title('Cdf da taxa')
#plt.ylabel('')
plt.savefig('cdf-taxa-kbits-seg.png')
