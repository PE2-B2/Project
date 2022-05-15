import filter as f
import xml.etree.ElementTree as ET

a = f.call_dir('D07', 'LMZ')

for t in a:
    print (t)

# 안에 있는 정보들을 추출해보자.


#
# root = ET.parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml').getroot()  # 기존 xml 파일이 없기 때문에 실행은 불가능함.

