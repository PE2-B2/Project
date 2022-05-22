from . import model
from . import extract
from . import IVAnalysis
from . import fitted_spectrum
from . import spectrumFitting


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

    model.printData()

    extract.makeCSV(0)

    IVAnalysis.showPara(0)

    spectrumFitting.specFitting(0)

    fitted_spectrum.fitSpec(0)
