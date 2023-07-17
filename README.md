# Exit Alert
The repository contains a POC of an HR application used to predict if an employee is about to quit.

Backend is written in Django, frontend is using HTML, CSS and JavaScript (template downloaded from [BBBootstrap](https://bbbootstrap.com/snippets/bootstrap-multi-step-survey-form-98749679), needed to be adjusted a bit).

Logo icon designed by Adrien Coquet.

Application is deployed on AWS Elastic Beanstalk: [link](http://hr-alert.eu-north-1.elasticbeanstalk.com/)

## About
- Prediction is done based on [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) dataset,
- EDA and model training is done in my Kaggle notebook: [Employee Attrition Rate](https://www.kaggle.com/code/kattat/employee-attrition-rate).

## The idea
- To use this application, an HR worker will fill in a survey about the given employee,
- There are 26 questions in total, and they are based on the mentioned IBM HR Analytics dataset,
- Different dataset will result in different set of survey questions, it all depends on the company's data,
- HR worker using the application is acknowledged with the questions, so I didn't attach any explanations of them (please see the IBM dataset description for more information about it).
- In the ideal world, this whole process of predicting employee atrrition would be synchronized with company's HR system. Once HR has all the necessary data about the worker (for example after a quarterly interview), ML model would be triggered and provide the prediction results back to the HR system.

## Technologies
<p align="left"> <a href="https://aws.amazon.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> </p>
