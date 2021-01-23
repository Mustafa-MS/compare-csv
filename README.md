# compare-csv
this simple code to compare 2 csv files and do something if similarity found
I made it to help me when dealing with LUNA16 database.
LUNA16 have 2 csv files, one called annotations (1187 line) and the other is candidates v2 (754976 line).

annotations.head()
| seriesuid  	| coordX 	| coordY  	| coordZ  	| diameter_mm |
|:---: |:---: |:---: |:---: |:---:| 
|1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860 |-128.699421 	|-175.319272| 	-298.387506| 	5.651471|
|1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860 |103.783651 	|-211.925149| 	-227.121250| 	4.224708|
|1.3.6.1.4.1.14519.5.2.1.6279.6001.100398138793540579077826395208 |69.639017 	|-140.944586| 	876.374496| 	5.786348|
|1.3.6.1.4.1.14519.5.2.1.6279.6001.100621383016233746780170740405 |-24.013824 	|192.102405| 	-391.081276| 	8.143262|
|1.3.6.1.4.1.14519.5.2.1.6279.6001.100621383016233746780170740405 |2.441547 	|172.464881| 	-405.493732| 	18.545150|

candidates.head()
|seriesuid|	coordX |	coordY |	coordZ| 	class|
|:---: |:---: |:---: |:---: |:---:| 
|1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860|	68.42	|-74.48	|-288.7	|0|
|1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860	|-95.20936148|	-91.80940617|	-377.4263503|	0|
|1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860	|-24.76675476	|-120.3792939	|-273.3615387	|0|
|1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860	|-63.08	|-65.74	|-344.24|	0|
|1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860|	52.94668794	|-92.68887262|	-241.067872|	0|

I needed a new csv file that have the unique patient ID and the class only (patient count 888 only).
first I created a csv file named (names.csv) that contain the patient ID only by using the following linux command


> dir$ find . -type f -name "*.mhd" -execdir basename {} \; > names.csv


then I run the python code to search and compare between names.csv and candidatesv2.csv.
the code search for patient name in candidate if exist that mean the patient have cancer and add 1 to the status
if the name is not found in candidate that mean the patient does not have cancer and add 0 to the status.

names.head()
|Patient_ID	|status|
|:---: |:---: |
|1.3.6.1.4.1.14519.5.2.1.6279.6001.944888107209008719031293531091	|1|
|1.3.6.1.4.1.14519.5.2.1.6279.6001.170825539570536865106681134236	|0|
|1.3.6.1.4.1.14519.5.2.1.6279.6001.900182736599353600185270496549	|1|
|1.3.6.1.4.1.14519.5.2.1.6279.6001.897279226481700053115245043064	|0|
|1.3.6.1.4.1.14519.5.2.1.6279.6001.230675342744370103160629638194	|1|

It's maybe not the best implemmantation but it did the job!
