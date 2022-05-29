from . import model
from . import filter as df  # Directory Filter
from . import extract
from . import IVAnalysis
from . import fitted_spectrum
from . import spectrumFitting
from . import spectrumAnalysis
import matplotlib.pyplot as plt


def initMainView(wafer, xy, device, save, show):
    progressPivot = 10

    waferArr = list(map(str, wafer.split()))
    xyCoordinateArr = list(map(str, xy.split()))
    deviceName = str(device)
    optSaveFig = str(save)
    optShowFig = str(show)

    model.storeWaferId(waferArr)
    model.storexyCoordinate(xyCoordinateArr)
    model.storeDeviceName(deviceName)
    model.storeOptSaveFig(optSaveFig)
    model.storeOptShowFig(optShowFig)


    # Directory Search
    targetDirectory = []  # 디렉토리는 여기 추가하면 됨

    targetDevice = deviceName
    for waferPivot in waferArr:
        if xyCoordinateArr[0] == 'all':
            waferAllDir = df.call_all_dir(waferPivot, targetDevice)
            for waferEntirePivot in waferAllDir:
                targetDirectory.append(waferEntirePivot)
        else:
            for coordinatePivot in xyCoordinateArr:
                targetDirectory.append(df.call_dir(waferPivot, targetDevice, coordinatePivot))

    hashTable = {}
    numDat = len(targetDirectory)
    counter = 0
    nowPrg = progressPivot
    for pivot in targetDirectory:
        if counter / numDat * 100 > nowPrg:
            print('[Progress ' + str(nowPrg) + '% Complete]')
            nowPrg += progressPivot

        IVAnalysis.showPara(pivot)
        spectrumFitting.specFitting(pivot, model.inputIDIndex)
        fitted_spectrum.fitSpec(pivot, model.inputCoordinateIndex)
        spectrumAnalysis.specAnaly(pivot)

        if optSaveFig == 'True':
            wafer, coordinate = df.fileSplicer(pivot)
            device = deviceName
            key = str(wafer + coordinate + device)
            figure = plt.gcf()
            figure.set_size_inches(16, 10)
            if key in hashTable:
                hashTable[key] += 1
                version = '(' + str(hashTable[key]) + ')'
                plt.savefig('.\\res\\figureRes\\' + wafer + ' ' + coordinate + ' ' + device + ' ' + version + '.png')
            else:
                plt.savefig('.\\res\\figureRes\\' + wafer + ' ' + coordinate + ' ' + device + '.png')
                hashTable[key] = 1

        if optShowFig == 'True':
            plt.show()
            plt.pause(2)  # This part takes a lot of time. It is recommended that this part be omitted.
            plt.close()
        else:
            plt.clf()
        counter += 1
    print('[Process Complete!]')

    print('[Data Storing]')
    extract.makeCSV(targetDirectory)
    print('[Storing Complete!]')


def chkExist(targetArr, target):
    index = 0

    for pivot in targetArr:
        if pivot == target:
            return index
        index += 1

    return -1
