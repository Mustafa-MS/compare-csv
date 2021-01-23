# import pandas library to deal with the csv files
import pandas

# the path of folder that contain all needed csv files
luna_csv_path = "/content/"

# read csv files into dataframe
positive_nodules = pandas.read_csv(luna_csv_path + "annotations.csv")
patient_names = pandas.read_csv(luna_csv_path + "names.csv")

#positive_nodules.head()
#patient_names.head()


for i in range(len(patient_names)):
  #if the patient id from names.csv is available in annotations.csv then write 1 in his status
  if patient_names.at[i, 'Patient_ID'] in positive_nodules.values:
    patient_names.at[i,'status'] = 1
    # print for debug
    #print (patient_names.at[i, 'Patient_ID'] ,i, ' is positive!')
  else:
    # if patient ID is not available write 0 in his status
    patient_names.at[i,'status'] = 0
    # print for debug
    #print (patient_names.at[i, 'Patient_ID'] , i, ' is negative!')
    
# write the changes to the csv files, because the changes in a dataframe.    
patient_names.to_csv('truth_table.csv', index=False)

#patient_names.head()
