from spectrumAnalysis import *
import warnings
import time
import numpy as np
from sklearn.metrics import r2_score


# Spectrum (Ref. - Raw data & fitting data)
plt.subplot(232)
plt.plot(v[6][0], v[6][1], color='black', label="Fit ref polynomial O3")

rsq = {}
handle = []
color = ['red', 'green', 'blue', 'limegreen', 'orange', 'purple', 'blue']
for i in range(2, 8):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        start_time = time.process_time()

        x = v[6][0]
        y = v[6][1]
        degree = i
        model = np.poly1d(np.polyfit(x, y, degree))

        print('Time for fitting degree ', i, ': ', time.process_time()-start_time)

        #polyline = np.linspace(1530, 1580, 6065)
        y2 = model(x)
        l, = plt.plot(x, y2, '--', color=color[i - 2], label='degree ' + str(i))

        handle.append(l)
        rsq[str(i)] = r2_score(y, y2)
        print('R_Square value for degree ', i, ': ', r2_score(y, y2))

print(rsq)