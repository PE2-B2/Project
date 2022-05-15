import pandas as pd
from extract import root
from process import *  #우선 그냥 여기 원래 소스꺼 다 불러놓은느낌.

# pandas
element = root.find('.//TestSiteInfo')
Batch = element.attrib['Batch']
wafer = element.attrib['Wafer']
mask = element.attrib['Maskset']
testSite = element.attrib['TestSite']
row = element.attrib['DieRow']
column = element.attrib['DieColumn']
ScriptOwner = 'B2'

T = []
for child in root.find('.//DesignParameters'):
    T.append(list(map(float, child.text.split(','))))
AnalysisWavelength = (T[1][0])

element1 = root.find('.//Modulator')
name = element1.attrib['Name']

element2 = root.find('.//ModulatorSite')
operator = element2.attrib['Operator']

element3 = root.find('.//PortCombo')
date = element3.attrib['DateStamp']

rawValues = []
for child in root.find('./ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement'):
    rawValues.append(list(map(float, child.text.split(','))))

IatV1 = rawValues[1][12]
IatminV1 = rawValues[1][4]

data = []
pivot = 0
for key, value in sorted(rsq.items()):
    values = [Batch, wafer, mask, testSite, name, date, ScriptOwner, operator, row, column, AnalysisWavelength, key, value,
              variableValues[pivot][0], variableValues[pivot][1], variableValues[pivot][2], variableValues[pivot][3],
              IVlist[pivot], IatV1, IatminV1]
    data.append(values)

    for i in range(1,2):
        pivot += i


df = pd.DataFrame(data, columns=['Batch', 'Wafer', 'Mask', 'TestSite', 'Name', 'Date','ScriptOwner','operator', 'row', 'column',
                                 'AnalysisWavelength','Degree', 'Rsq for nth','MAX(X)', 'MAX(Y)', 'MIN(X)', 'MIN(Y)',
                                 'I-V Rsq for nth', 'I at 1V [A]', 'I at -1V [A]'])

print(df)

df.to_csv("AnalysisResult_B2.csv", index=False)