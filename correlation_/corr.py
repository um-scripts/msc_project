import numpy as np
import matplotlib.pyplot as plt

f1 = open('ORF_Rep1Rep2_common.txt', 'r')
f1.readline()
x1 = []
x2 = []
for line in f1.readlines():
    c = line.strip('\n').split('\t')
    x1.append(int(c[3]))
    x2.append(int(c[5]))

f1.close()

plt.title('ORF Plot')
plt.xlabel('Rep1 reads unique')
plt.ylabel('Rep2 reads unique')
plt.scatter(np.log2(x1), np.log2(x2), s = 0.5)
plt.show()


r = np.corrcoef(np.array(x1), np.array(x2))
print('Correlation Coefficient: {r}'.format(r=r))
