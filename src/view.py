from . import model
from . import filter as df  # Directory Filter
from . import extract
from . import IVAnalysis
from . import fitted_spectrum
from . import spectrumFitting
from . import spectrumAnalysis
import matplotlib.pyplot as plt


def initMainView():
    print('Wafer : ')
    waferArr = list(map(str, input().split()))
    print('xy : ')
    xyCoordinateArr = list(map(str, input().split()))
    print('device name : ')
    deviceName = str(input())
    print('optsave? : ')
    optSaveFig = str(input())
    print('opt show? : ')
    optShowFig = str(input())

    model.storeWaferId(waferArr)
    model.storexyCoordinate(xyCoordinateArr)
    model.storeDeviceName(deviceName)
    model.storeOptSaveFig(optSaveFig)
    model.storeOptShowFig(optShowFig)

    """
    waferIndex = 0
    while True:
        print ('What Wafer? : ')
        wafer = str(input())
        waferIndex = chkExist (waferArr, wafer)
        if waferIndex == -1:
            print ('Wrong Input!')
            continue
        break

    coordinateIndex = 0
    while True:
        print ('What Coordiante? :')
        coordinate = str(input())
        coordinateIndex = chkExist (xyCoordinateArr, coordinate)
        if coordinateIndex == -1:
            print ('Wrong Input!')
            continue
        break

    model.storeInput(waferIndex, coordinateIndex)
    """
    # input Test Part
    # model.printData()

    # Directory Search
    targetDirectory = []  # 디렉토리는 여기 추가하면 됨
    """
    targetWafer = model.waferId[model.inputIDIndex]
    targetCoordinate = model.xyCoordinate[model.inputCoordinateIndex]
    targetDevice = model.deviceName
    targetDirectory.append(df.call_dir(targetWafer, targetDevice, targetCoordinate)) #일단 하나인 경우 처리
    """

    targetDevice = deviceName
    for waferPivot in waferArr:
        if xyCoordinateArr[0] == 'all':
            waferAllDir = df.call_all_dir(waferPivot, targetDevice)
            for waferEntirePivot in waferAllDir:
                targetDirectory.append(waferEntirePivot)
        else:
            for coordinatePivot in xyCoordinateArr:
                targetDirectory.append(df.call_dir(waferPivot, targetDevice, coordinatePivot))

    # extract.makeCSV(targetDirectory)
    # extract.makeCSV(targetDirectory)
    extract.makeCSV(targetDirectory)
    hashTable = {}
    for pivot in targetDirectory:
        IVAnalysis.showPara(pivot)
        spectrumFitting.specFitting(pivot, model.inputIDIndex)
        fitted_spectrum.fitSpec(pivot, model.inputCoordinateIndex)
        spectrumAnalysis.specAnaly(pivot)

        if optSaveFig == 'True':
            wafer, coordinate = df.fileSplicer(pivot)
            device = deviceName
            key = str(wafer + coordinate + device)
            if key in hashTable:
                hashTable[key] += 1
                version = '(' + str(hashTable[key]) + ')'
                plt.savefig('.\\res\\figureRes\\' + wafer + ' ' + coordinate + ' ' + device + ' ' + version + '.png')
            else:
                plt.savefig('.\\res\\figureRes\\' + wafer + ' ' + coordinate + ' ' + device + '.png')
                hashTable[key] = 1

        if optShowFig == 'True':
             plt.show()
        else:
            plt.clf()


def chkExist(targetArr, target):
    index = 0

    for pivot in targetArr:
        if pivot == target:
            return index
        index += 1

    return -1
