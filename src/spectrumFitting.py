from extract import *
import matplotlib.pyplot as plt
import time
import numpy as np
from sklearn.metrics import r2_score
import warnings
warnings.simplefilter('ignore', np.RankWarning)

# Spectrum (Ref. - Raw data & fitting data)
for t in a:
    path = os.path.basename(t)
    root = ET.parse(t).getroot()

    v = []
    for waveLengthSweep in root.findall('.//WavelengthSweep'):
        waveValues = []
        for child in waveLengthSweep:
            waveValues.append(list(map(float, child.text.split(','))))

        waveValues.append(waveLengthSweep.attrib['DCBias'])
        v.append(waveValues)

    plt.plot(v[6][0], v[6][1], color='black', label="Fit ref polynomial O3")

    handle = []
    start_time = time.process_time()

    x = v[6][0]
    y = v[6][1]
    degree = 7
    model = np.poly1d(np.polyfit(x, y, degree))

    print('Time for fitting degree ', '7', ': ', time.process_time()-start_time)

    #polyline = np.linspace(1530, 1580, 6065)
    y2 = model(x)
    l, = plt.plot(x, y2, '--', color='red', label='degree 7')

    handle.append(l)
    r_fitting = r2_score(y, y2)
    print('R_Square value for degree 7 :', r_fitting)
