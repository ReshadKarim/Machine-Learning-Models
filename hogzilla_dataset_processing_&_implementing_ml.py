# -*- coding: utf-8 -*-
"""Hogzilla Dataset processing & implementing ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sRxRR8Apy6O72nkizQ2j6pnSAZ9xuO1Q
"""

# Commented out IPython magic to ensure Python compatibility.
#Importing important librarys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline 
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
le = LabelEncoder()
import warnings
warnings.filterwarnings('ignore')

#Importing csv dataset from personal google drive
from google.colab import drive
drive.mount('/content/drive')

#reading the csv file
df = pd.read_csv('/content/drive/MyDrive/datasets/merged.csv')
df.head()



#"""************** Pre-Processing **************"""

#dropping unnecessary columns
df = df.drop(['src',	'src_port','dst_port','dst','event_generator', 'event_signature', 'event_priority', "original_dataset","original_label", "C_packets_rst_avg"], axis = 1)
df.shape
#Dropping the null values
print("Shape of dataframe before dropping:", df.shape)
df = df.dropna(axis = 0, subset = ['Botnets_label'])
print("Shape after dropping:", df.shape)

# transforming the values
df['ndpi_detected_protocol'] = le.fit_transform(df['ndpi_detected_protocol'])
df['ndpi_risk'] = le.fit_transform(df['ndpi_risk'])
df['Botnets_label'] = le.fit_transform(df['Botnets_label'])
df['protocol'] = le.fit_transform(df['protocol'])
df.head()




#"""************ Train Test Split ************"""

from sklearn.model_selection import train_test_split
X=df[['ndpi_detected_protocol', 'payload_bytes_first', 'packet_pay_size-3', 'packet_pay_size-2', 'dst2src_packets_rate', 'C_packets_rst_min', 'C_packets_urg_avg', 'src2dst_packets_rate', 'C_packets_fin_avg', 'C_idletime_max', 'http_response_status_code', 'packet_header_size-4', 'dst2src_inter_time_std', 'packet_header_size-0', 'C_packets_rst_std', 'payload_bytes_max', 'src2dst_header_bytes_min', 'C_dst2src_packets_rate_max', 'packet_pay_size-8', 'dst2src_header_bytes_min', 'http_request_version', 'src2dst_header_bytes_max', 'dns_query_type', 'payload_bytes_avg', 'dst2src_header_bytes_std', 'C_dst2src_packets_rate_min', 'C_packets_syn_std', 'C_src2dst_packets_rate_max', 'packet_header_size-7', 'C_packets_syn_max', 'C_tcp_retransmissions_max', 'packets_fin', 'src2dst_pay_bytes', 'packet_header_size-6', 'dst2src_packets', 'inter_time-10', 'C_packets_ack_avg', 'src2dst_header_bytes', 'inter_time-9', 'C_idletime_std', 'C_dst2src_pay_bytes_rate_max', 'packet_direction-5', 'C_src2dst_pay_bytes_max', 'packet_direction-0', 'packet_direction-1', 'inter_time-7', 'packets_rst', 'C_packets_psh_min', 'C_src2dst_pay_bytes_rate_avg', 'src2dst_inter_time_std', 'C_src2dst_pay_bytes_avg', 'dns_num_answers', 'packet_pay_size-7', 'C_number_of_contacts', 'detection_completed', 'inter_time-6', 'src2dst_header_bytes_std', 'packets_ack', 'C_packets_rst_max', 'inter_time-3', 'dst2src_header_bytes_avg', 'C_duration_avg', 'C_packets_ack_min', 'dns_query_class', 'C_dst2src_pay_bytes_std', 'C_packets_syn_avg', 'C_packets_psh_max', 'C_src2dst_packets_rate_avg', 'dst2src_pay_bytes_min', 'C_dst2src_header_bytes_min', 'src2dst_inter_time_max', 'src2dst_pay_bytes_min', 'http_method', 'C_packets_psh_avg', 'C_dst2src_header_bytes_std', 'C_packets_ack_std', 'flow_use_time', 'inter_time-2', 'dst2src_inter_time_min', 'C_dst2src_packets_rate_std', 'packet_pay_size-4', 'C_packets_ack_max', 'C_dst2src_packets_max', 'C_src2dst_pay_bytes_min', 'dns_num_queries', 'inter_time-8', 'packet_header_size-8', 'src2dst_pay_bytes_max', 'protocol', 'dst2src_pay_bytes_max', 'C_src2dst_packets_avg', 'C_src2dst_pay_bytes_rate_std', 'response_rel_time', 'packet_pay_size-10', 'inter_time_min', 'packet_header_size-1', 'dns_reply_code', 'inter_time_avg', 'C_packets_psh_std', 'src2dst_header_bytes_avg', 'packet_direction-9', 'C_dst2src_packets_std', 'packet_header_size-9', 'src2dst_packets', 'payload_bytes', 'packet_pay_size-5', 'http_num_request_headers', 'packet_header_size-2', 'packet_direction-4', 'packet_direction-7', 'C_tcp_retransmissions_min', 'C_duration_min', 'C_dst2src_pay_bytes_avg', 'dst2src_pay_bytes_avg', 'C_dst2src_header_bytes_max', 'C_packets_syn_min', 'packet_direction-3', 'http_num_response_headers', 'C_packets_fin_std', 'C_duration_std', 'C_src2dst_header_bytes_max', 'packets_syn', 'C_dst2src_header_bytes_avg', 'C_src2dst_pay_bytes_rate_min', 'packets_psh', 'src2dst_pay_bytes_rate', 'C_tcp_retransmissions_std', 'C_idletime_avg', 'C_src2dst_packets_rate_min', 'C_src2dst_packets_max', 'C_duration_max', 'packet_direction-6', 'C_packets_fin_max', 'C_packets_urg_std', 'C_src2dst_packets_rate_std', 'dst2src_header_bytes', 'payload_bytes_std', 'C_dst2src_pay_bytes_rate_avg', 'src2dst_inter_time_min', 'flow_duration', 'C_src2dst_pay_bytes_std', 'C_src2dst_packets_min', 'C_packets_urg_min', 'inter_time-5', 'dst2src_header_bytes_max', 'packet_direction-10', 'dst2src_inter_time_max', 'packet_pay_size-0', 'packets', 'inter_time_max', 'inter_time_std', 'C_src2dst_packets_std', 'packets_urg', 'packet_direction-8', 'dst2src_pay_bytes_rate', 'src2dst_inter_time_avg', 'dns_rsp_type', 'flow_idle_time', 'packet_header_size-3', 'inter_time-0', 'C_dst2src_pay_bytes_min', 'dst2src_pay_bytes_std', 'C_src2dst_header_bytes_avg', 'C_dst2src_packets_avg', 'bytes', 'packets_without_payload', 'C_tcp_retransmissions_avg', 'inter_time-1', 'C_src2dst_pay_bytes_rate_max', 'inter_time-4', 'C_dst2src_pay_bytes_max', 'packet_pay_size-6', 'dst2src_pay_bytes', 'payload_bytes_min', 'tcp_retransmissions', 'C_packets_fin_min', 'C_dst2src_packets_rate_avg', 'dst2src_inter_time_avg', 'packet_header_size-5', 'packet_pay_size-1', 'packet_header_size-10', 'C_dst2src_pay_bytes_rate_std', 'src2dst_pay_bytes_std', 'C_idletime_min', 'C_src2dst_header_bytes_std', 'src2dst_pay_bytes_avg', 'packet_pay_size-9', 'packet_direction-2', 'C_src2dst_header_bytes_min', 'C_dst2src_packets_min', 'C_packets_urg_max', 'C_dst2src_pay_bytes_rate_min']]
y=df[['Botnets_label' ]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)
X.shape , y.shape




#"""************** Min-Max Scaling *************"""

# Scaling our data in order to remove biasness or deviance - Feature Scaling
# Method - Min Max Scaling Method
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X_train)

# Transforming
x_train_temp = scaler.transform(X_train)




#"""********** Logistic Regression **********"""

from sklearn.linear_model import LogisticRegression
model_conduct = LogisticRegression()
model_conduct.fit(X_train, y_train) #Training the model
predictions = model_conduct.predict(X_test)
print(predictions)# printing predictions

# Logistic Regression Accuracy Test
LogisticRegressionAccuracy = accuracy_score(y_test, predictions)
print("Accuracy of Logistic Regression : ",LogisticRegressionAccuracy*100,'%') #Logistic Regression Accuracy




#"""****************Decision Tree ****************"""

from sklearn.tree import DecisionTreeClassifier
conduct = DecisionTreeClassifier(criterion='entropy',random_state=20)
conduct.fit(X_train, y_train)
y_prediction = conduct.predict(X_test)
DecisionTreeAccuracy = accuracy_score(y_prediction,y_test)
print("Accuracy of Decision Tree : ",DecisionTreeAccuracy*100,'%') #Decision Tree Accuracy




#"""** ********Linear Regression******** **"""

#LinearRegression 
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
LinearRegression  = regressor.score(X_test,y_test)
print("Accuracy of Linear Regression  : ", LinearRegression*100,'%' ) #Linear Regression Accuracy




#"""** ******** Random Forest Classifier **********"""

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=50)
rfc.fit(X_train, y_train)
rfc.predict(X_test)
rfc.score(X_test,y_test)
accuracy_train_05=rfc.score(X_train, y_train)
accyracy_test_05=rfc.score(X_test, y_test)
print("Accuracy of Random Forest Classifier  : ", accyracy_test_05*100,'%' ) #Random Forest Classifier Accuracy




#"""********** Neural Network Classifier **********"""

from sklearn.neural_network import MLPClassifier
nnc=MLPClassifier(hidden_layer_sizes=(7), activation="relu", max_iter=10000)

nnc.fit(X_train, y_train)

accuracy_train_03=nnc.score(X_train, y_train)
accuracy_test_03=nnc.score(X_test, y_test)

predictions = nnc.predict(X_test)
print("Accuracy of Neural Network Classifier  : ", accuracy_test_03*100,'%' ) #Neural Network Classifier Accuracy




#"""********** SVC (Takes too much time) **********"""

from sklearn.svm import SVC
svc = SVC(kernel="linear")
svc.fit(X_train, y_train)
accuracy_train_04=svc.score(X_train, y_train)
accuracy_test_04=svc.score(X_test, y_test)
print("Accuracy of SVC  : ", accuracy_test_04*100,'%' ) #SVC Accuracy




#"""********** Comparing Graph **********"""

fig, ax = plt.subplots()
names = ['NeuralNetwork','LinearRegre','LogisticRegre','DecisionTree', 'RandomForest' ]
plt.tight_layout()
plt.subplots_adjust(wspace = 1, hspace = 1)
acc =[ accuracy_test_03*100, LinearRegression*100, LogisticRegressionAccuracy*100, DecisionTreeAccuracy*100, accyracy_test_05*100 ]
position = [1,2,3,4,5]
ax.bar(position,acc, width=0.5, color="red", bottom=None, align='center')
plt.xticks(position,names )
plt.subplots_adjust(wspace = 1, hspace = 1)
ax.set_title('Accuracy Comparision of Logistic Regression,  Decision Tree, Linear Regression, Random Forest and NNC')
ax.set_xlabel('Classification')
ax.set_ylabel('Accuracy')
