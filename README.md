## loan-machine-learning-project
### project explanation
- The data set collect from kaggle
- The csv file is loaded with the help of read_csv method in pandas library
- The data consists of 614 rows and 12 features
#### Data Understanding
- Gender : Applicant Gender
- Married: Applicant Married or not
- Dependents : How many people became dependent on the person
- Education : Applicant is Graduate or not
- Self_Employed : Applicant is self employed or not
- Applicant_Income :person anuval income
- Coapplicant_Income : coapplicant income if it is mutual loan 
- Loan_Amount : amount of loan
- Term : How many terms amount will repay
- Credit_History:1-yes/ 0-no
- Area: where the person is living ( Urban/Rural/Semiurban)
- Status: Y-loan approved / N-loan declined
#### Data preprocessing
- divide continous variables and descrite variables
- applied count plot on descrite variables with the help of countplot() method in seaborn library
- applied boxplot on continous variables with the help of boxplot() method in seaborn library
- applied pairplot on continous variables with the help of pairplot() method in seaborn library
###### Data cleaning && Data wrangling
- missing values are filled by using mode with the help of fillna() method in pandas library
- in continous variables converted skewness to normal distribution with the help of nth room transformation
- converting descrete catagorical into descrete numerical with the help of labelencoder() method in sklearn library
- divided input feature and output features and divided train test
- we applied standardscaler to input feature train and test 
- we applied the classification algorithms like logistic regression,knn,svm,decision tree,random forest etc..
- finaly logistic regression model is the best model
- save as picke file
- We have built a Logistic Regression which performs having the Training accuracy of 80.04% and Testing accuracy of 84.55%.
- deployed the python script to load trained model with the help of flask,htmlfile,cssfile and spyder
