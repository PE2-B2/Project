from extract import *
import matplotlib.pyplot as plt

# Spectrum (Raw data)
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

# Spectrum graph of raw data
    plots = []
    for i in range(len(v) - 1):
        line, = plt.plot(v[i][0], v[i][1], label="DCBias=\"" + str(v[i][2]) + "\"")
        plots.append(line)

    line, = plt.plot(v[6][0], v[6][1], color='black', label="REF")

    plt.gca().add_artist(plt.legend(handles=[line], loc='upper right'))
    plt.legend(handles=plots, ncol=2, loc="lower center")
    plt.title("Transmission spectra - as measured")
    plt.xlabel('Wavelength [nm]')
    plt.ylabel('Measured transmission [dB]')