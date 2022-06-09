# ![Footer](https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=footer&text=Programming%20for%20Engineer%20II%20Group%20B2&fontSize=40&)

***

## Index
[Introduction](#Introduction)   
[Install](#Install)  
[Environment](#Environment)  
[Usage](#Usage)  
[Contributor](#Contributor)  
***

## Introduction
This tool is data analysis software using PyCharm. 

Put the data file in the folder and input a wafer name you want, 
this program stores analyzed Dataframes and graphs and shows xml data customer give.

For more information, see 'manual_report' and 'comparision_report' in the 'doc' folder.
You will be able to see the analyzed results for the sample data in the 'doc' folder.
You can also see an example of running the software in the 'ppt' folder as a video.
***

## Install
 ```
pip install -r requirements.txt
 ```
***

## Environment
* <span style="color:red">Python 3.8</span>
* Window 10

***

## Usage
1. **Wafer** : You can type the wafer number you want in the data folder.
2. **Coordinates** : You can type 'Row' and 'Column' from the wafer you choose.
   * You must use parentheses. ex) (0,0) 
   * Type "all" if you want to see the entire data.
3. **Device ID** : You can type device ID from the wafer you choose.
   * ex) LMZ, LMZC, LMZO ...
4. **Show Output** : You can see the result graphs one by one.
   * The graph is replaced every two seconds.
   * It is not recommended because it takes a long time and if you have a PyCharm professional, you can see it in a scientific view.
5. **Save Output** : You can save all of the graphs and csv file you choose.
6. **Results folder** : You can open 'res' folder and confirm the figure and Excel file you saved.
7. **OK** : You can save and execute the data you choose.
8. **Quit** : Exit
***

## Contributor
* Kim Jung Hun              dan05006@hanyang.ac.kr
* Kang Gyeong Don           kgd981013@hanyang.ac.kr  
* Kim Min Ju                minjukim12@hanyang.ac.kr  
* Nhat Dong                 nhatdong.tran@googlemail.com 
