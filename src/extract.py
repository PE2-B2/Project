from . import filter as f
from . import model
import os
import xml.etree.ElementTree as ET
import csv


def makeCSV(directory):
    errormsg = ['No Error', 'Rsq. IV. Error']

    # csv path
    f_output = open('./res/csvRes/analyzedResult.csv', 'w', newline='')
    csv_writer = csv.writer(f_output)
    csv_writer.writerow(
        ['Lot', 'Wafer', 'Mask', 'TestSite', 'Name', 'Date', 'Script ID', 'Script Owner', 'Operator', 'Row', 'Column',
         'ErrorFlag', 'Error description', 'Analysis Wavelength', 'Rsq of Ref. spectrum', 'Max transmission of Ref. spec. (dB)',
         'Rsq of IV', 'I at -2V', 'I at -1V', 'I at 1V'])

    dirCounter = 0
    for t in directory:
        path = os.path.basename(t)
        root = ET.parse(t).getroot()

        scriptID = 'process LMZ'
        scriptOwner = 'B2'

        element1 = root.find('.//Modulator')
        name = element1.attrib['Name']

        element2 = root.find('.//ModulatorSite')
        operator = element2.attrib['Operator']

        element3 = root.find('.//PortCombo')
        date = element3.attrib['DateStamp']

        element4 = root.find('.//TestSiteInfo')
        WaferID = element4.attrib['Wafer']
        batch = element4.attrib['Batch']
        testsite = element4.attrib['TestSite']
        maskset = element4.attrib['Maskset']
        dierow = element4.attrib['DieRow']
        diecolumn = element4.attrib['DieColumn']

        T = []
        for child in root.find('.//DesignParameters'):
            T.append(list(map(float, child.text.split(','))))
        AnalysisWavelength = (T[1][0])

        rawValues = []
        for child in root.find('./ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement'):
            rawValues.append(list(map(float, child.text.split(','))))

        IatV1 = rawValues[1][12]
        IatminV1 = rawValues[1][4]
        IatminV2 = rawValues[1][0]

        nowRsqIV = model.rsqIV[dirCounter]
        if nowRsqIV >= 0.99:
            errorcode = 0
        else:
            errorcode = 1
        rsqSpec = model.resSpectrum[dirCounter]
        MaxRef = model.maxRef[dirCounter]


        csv_writer.writerow(
            [batch, WaferID, maskset, testsite, name, date, scriptID, scriptOwner, operator, dierow, diecolumn,
             errorcode, errormsg[errorcode], AnalysisWavelength, rsqSpec, MaxRef,
             nowRsqIV, IatminV2, IatminV1, IatV1])
        dirCounter += 1

    f_output.close()
