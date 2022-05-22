# Model Default Values
waferId = []
waferNumber = 0
waferDirList = []

xyCoordinate = []
xyCoordinateNumber = 0

deviceName = ''
optSaveFig = False
optShowFig = False


def storeWaferId(waferArr):
    global waferId, waferNumber

    for pivot in waferArr:
        waferNumber += 1
        waferId.append(pivot)


def storexyCoordinate(xyCoordinateArr):
    global xyCoordinate, xyCoordinateNumber

    for pivot in xyCoordinateArr:
        xyCoordinateNumber += 1
        xyCoordinate.append(pivot)


def storeDeviceName(device):
    global deviceName

    deviceName = device


def storeOptSaveFig(optSave):
    global optSaveFig

    if optSave == 'True':
        optSaveFig = True
    elif optSave == 'False':
        optSaveFig = False
    # Err Catch (True나 False가 입력안되면 에러처리하기)


def storeOptShowFig(optShow):
    global optShowFig

    if optShow == 'True':
        optShowFig = True
    elif optShow == 'False':
        optShowFig = False
    # Err Catch (True나 False가 입력안되면 에러처리하기)


def printData():
    global waferId, waferNumber, xyCoordinate, xyCoordinateNumber, deviceName, optSaveFig, optShowFig

    print(waferId)
    print(xyCoordinate)
    print(deviceName)
    print(optSaveFig)
    print(optShowFig)
