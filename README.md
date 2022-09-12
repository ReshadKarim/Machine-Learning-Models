# Mechine-Learning-Models
Pre-processing and transforming a dataset and applying machine learning models i.e. Logistic Regression,  Decision Tree, Linear Regression, Random Forest, NNC and SVC


We have chosen the Hogzilla Dataset which is created by combining the network traffic behavioral characteristics from the CTU-13 Botnet and the ISCX 2012 IDS datasets. Each flow of this dataset contains the information of legitimate traffic and 13 network traces of 7 distinct botnet malwares from the ISCX 2012 IDS dataset and CTU-13 botnet combined. 

192 subset of flow features are selected from the dataset which are sufficient enough to accurately detect the characteristics of the botnets. 
The features mainly consist of - 
Flow Duration
Maximum and minimum expire time of the flow
Protocol type
Bytes count (Source to destination and vice-versa)
Packets
Source to destination packets
Destination to source packets
Maximum and minimum flow idle time 


After applying the mechine learning models we get the accuracy of-

Accuracy of Neural Network Classifier     :   72.22 %
Accuracy of Linear Regression             :   73.88 %
Accuracy of Logistic Regression           :   80.38 %
Accuracy of Decision Tree                 :   96.62%
Accuracy of Random Forest Classifier      :   96.84 %
