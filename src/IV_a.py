import matplotlib.pyplot as plt
import numpy as np
from extract import *
from sklearn.metrics import r2_score
from lmfit import Parameters, minimize, fit_report

v = []
for child in root.find('.//IVMeasurement'):
    v.append(list(map(float, child.text.split(','))))

V1 = np.array(v[0][0:9])
I1 = np.array(np.abs(v[1])[0:9])
V2 = np.array(v[0][10:])
I2 = np.array(np.abs(v[1][10:]))

# IV fitting by polyfit
model1 = np.poly1d(np.polyfit(V1, I1, 4))
polyline = np.linspace(-2.0, 0.25, 10)

print(model1(polyline))

# IV fitting by lmfit
def mod(params, V2, I2):
    I_S = params['I_S']
    VT = params['VT']
    model = I_S * (np.exp(V2 / VT) - 1)
    return model - I2

params = Parameters()
params.add('I_S', value=1e-15)
params.add('VT', value=0.026)

fitted_params = minimize(mod, params, args=(V2, I2,), method='leastsq')

VT = fitted_params.params['VT'].value
I_S = fitted_params.params['I_S'].value

print(fit_report(fitted_params))
fittedDiagram = np.abs(I_S * (np.exp(V2 / VT) - 1))
