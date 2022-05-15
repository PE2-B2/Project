from spectrumFitting import plt
from spectrumAnalysis import v
from spectrumFitting import np
from spectrumMinMax import y_values

# Spectrum (Processed interference spectrum)
plt.subplot(233)

plots = []
for i in range(len(v) - 1):

    array1 = np.array(v[i][1])
    array2 = np.array(y_values)
    if len(array1) == len(array2):
        subtracted_array = np.subtract(array1, array2)
        subtracted = list(subtracted_array)
        x_new = v[i][0]
    else:
        n = len(array1) - len(array2) if len(array1) > len(array2) else len(array2) - len(array1)
        x_new = v[i][0][:-n]
        array1 = np.array(v[i][1][:-n])
        subtracted_array = np.subtract(array1, array2)
        subtracted = list(subtracted_array)

    # plot values
    line, = plt.plot(x_new, subtracted, label="DCBias=\"" + str(v[i][2]) + "\"")
    plots.append(line)


# plt.legend(handles=plots, ncol=2, loc="lower center")
plt.title("Transmission spectra - as measured")
plt.xlabel('Wavelength [nm]')
plt.ylabel('Measured transmission [dB]')