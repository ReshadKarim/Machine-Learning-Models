# Machine-Learning-Models
Pre-processing and transforming a dataset and applying machine learning models i.e. Logistic Regression,  Decision Tree, Linear Regression, Random Forest, NNC and SVC


We have chosen the Hogzilla Dataset which is created by combining the network traffic behavioral characteristics from the CTU-13 Botnet and the ISCX 2012 IDS datasets. Each flow of this dataset contains the information of legitimate traffic and 13 network traces of 7 distinct botnet malwares from the ISCX 2012 IDS dataset and CTU-13 botnet combined. 

192 subset of flow features are selected from the dataset which are sufficient enough to accurately detect the characteristics of the botnets. 
The features mainly consist of - 
Flow Duration,
Maximum and minimum expire time of the flow,
Protocol type,
Bytes count (Source to destination and vice-versa),
Packets,
Source to destination packets,
Destination to source packets,
Maximum and minimum flow idle time. 

For running the dataset on our machine Learning models we preprocessed the dataset by removing all the noises and missing values, removed all unwanted rows and columns and transformed all the sting values to num values. This Feature Scaling is used in order to remove biases or deviance. The Min-Max Scaler method is used for this pre-processing. After the preprocessing phase, the Train-Test-Split method is used to split the dataset into two sectors, one for training and other for testing. The splitting is done with a ratio which is gradually increased and decreased for better accuracy results of the machine learning models. The most efficient result was with a ratio of 75:25. Where 75% is for training and 25% is for testing. The training portion of the dataset is trained under the Machine Learning models. The  Train-Test-Split method uses the X_train and y_train for training the models where X_train are the network flow features of the dataset and y_train is the Botnet itself. After the training is completed by the ML models, it is tested in the test portion of the dataset where X_test and y_test are the same features as the training ones. Each Machine learning model has a different execution time which is very distinctive from each other and mostly depending on the complexity of the models and the hardware it executes on. The accuracy and execution-time results of the ML models are stated below:

After applying the mechine learning models we get the accuracy of-

Accuracy of Linear Regression             :    62.64 %    execution time:     16.32 sec
Accuracy of Neural Network Classifier  :   71.97 %     execution time:     435.51 sec
Accuracy of Logistic Regression           :   78.52 %     execution time:      141.3 sec
Accuracy of Decision Tree                    :    96.61%      execution time:     23.92 sec
Accuracy of Random Forest Classifier  :   96.81 %     execution time:  85.43 sec

