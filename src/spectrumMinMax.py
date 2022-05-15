from spectrumFitting import warnings
from spectrumFitting import np
from spectrumAnalysis import v
from IV_graph import plt

# min, max
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    y_values = np.asarray(np.poly1d(np.polyfit(v[6][0], v[6][1], 6))(v[6][0]))

variableValues = []
for i in range(2, 8, 1):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        values = np.asarray(np.poly1d(np.polyfit(v[6][0], v[6][1], i))(v[6][0]))
    tempValue = []
    tempValue.append(v[6][0][values.argmax()])
    tempValue.append(v[6][1][values.argmax()])
    tempValue.append(v[6][0][values.argmin()])
    tempValue.append(v[6][1][values.argmin()])
    variableValues.append(tempValue)


print(variableValues)

print('Max value: ', v[6][0][y_values.argmax()], v[6][1][y_values.argmax()])
print('Min value: ', v[6][0][y_values.argmin()], v[6][1][y_values.argmin()])
plt.scatter([v[6][0][y_values.argmax()], v[6][0][y_values.argmin()]],
         [v[6][1][y_values.argmax()], v[6][1][y_values.argmin()]], s=100)

y_values_new = v[6][1] - y_values

plt.legend(handles=handle, ncol=2, loc="lower center")
plt.title("REF fitting")
plt.xlabel('Wavelength [nm]')
plt.ylabel('Measured transmission [dB]')