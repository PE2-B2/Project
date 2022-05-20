from . import filter as f
import os
import xml.etree.ElementTree as ET
import pandas as pd
import csv
from . import model


def makeCSV():
    # Wafer = str(input("Input wafer name : "))
    # a = f.call_dir(Wafer, 'LMZ')
    Wafer = model.waferId[0]
    a = f.call_dir(Wafer, model.deviceName)

    f_output = open('test_1.csv', 'w', newline='')
    csv_writer = csv.writer(f_output)
    csv_writer.writerow(
        ['Name', 'Operator', 'Date', 'Testsite', 'Maskset', 'DieRow', 'DieColumn', 'AnalysisWavelength', 'I at 1V [A]',
         'I at -1V [A]'])

    for t in a:
        path = os.path.basename(t)
        root = ET.parse(t).getroot()
        print(path)

        element1 = root.find('.//Modulator')
        name = element1.attrib['Name']

        element2 = root.find('.//ModulatorSite')
        operator = element2.attrib['Operator']

        element3 = root.find('.//PortCombo')
        date = element3.attrib['DateStamp']

        element4 = root.find('.//TestSiteInfo')
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

        print(name)
        print(operator)
        print(date)
        print(batch)
        print(testsite)
        print(maskset)
        print(dierow)
        print(diecolumn)
        print(AnalysisWavelength)
        print(IatV1)
        print(IatminV1)

        # data = {'Name': name, 'Operator' : operator, 'Date' : date, 'Testsite' : testsite, 'Maskset' : maskset, 'DieRow' : dierow, 'DieColumn' : diecolumn, 'AnalysisWavelength' : AnalysisWavelength, 'I at 1V [A]' : IatV1, 'I at -1V [A]' : IatminV1}
        csv_writer.writerow(
            [name, operator, date, testsite, maskset, dierow, diecolumn, AnalysisWavelength, IatV1, IatminV1])

    # df = pd.DataFrame(data, index=['a'])
    # df.to_csv("test_1.csv", index=False)

    # print(data)

    # df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])

    # print(df)
    f_output.close()
