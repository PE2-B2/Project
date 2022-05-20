from extract import *
import numpy as np
import matplotlib.pyplot as plt
from lmfit import Parameters, minimize, fit_report
from sklearn.metrics import r2_score

for t in a:                     # t랑 a에 해당하는 변수를 미리 모델에 해당하는 파이썬 모듈에 저장하기
    path = os.path.basename(t)
    root = ET.parse(t).getroot()

    # extract IV raw data from xml files
    v = []
    for child in root.find('.//IVMeasurement'):
        v.append(list(map(float, child.text.split(','))))

    V1 = np.array(v[0][0:9])
    I1 = np.array(np.abs(v[1])[0:9])
    V2 = np.array(v[0][10:])
    I2 = np.array(np.abs(v[1][10:]))

    # fitting IV data at Voltage -2 ~ 0.25 used polyfit
    model1 = np.poly1d(np.polyfit(V1, I1, 4))
    polyline = np.linspace(-2.0, 0.25, 10)

    # fitting IV data at voltage 0.25 ~ 1 used lmfit
    def ivFit(params, V2, I2):
        I_S = params['I_S']
        VT = params['VT']
        model = I_S * (np.exp(V2 / VT) - 1)
        return model - I2

    params = Parameters()
    params.add('I_S', value=1e-15)
    params.add('VT', value=0.026)

    fitted_params = minimize(ivFit, params, args=(V2, I2,), method='leastsq')

    VT = fitted_params.params['VT'].value
    I_S = fitted_params.params['I_S'].value

    print(fit_report(fitted_params))
    fittedDiagram = np.abs(I_S * (np.exp(V2 / VT) - 1))

    RI = np.concatenate((model1(polyline), np.abs(I_S * (np.exp(V2 / VT) - 1))))
    R2 = r2_score(np.abs(v[1]), RI)

    # plot IV raw data & fitted data
    plt.subplot(121)
    line1, = plt.plot(polyline, model1(polyline), color='red')
    plt.scatter(v[0], np.abs(v[1]), s=70, c='red', lw=2, label="IV data")
    plt.plot(v[0][9:11], np.abs(v[1][9:11]), c='red', lw=2, label="fitted graph")
    plt.plot(V2, fittedDiagram, c='red', lw=2, label=R2)

    plt.title("IV-Analysis", size=15)
    plt.xlabel('Voltage [V]', size=15)
    plt.ylabel('Current [A]', size=15)
    plt.yscale('logit')
    plt.legend()
    plt.grid(True)
    plt.show()
