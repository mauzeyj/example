###Installation
I used python 3.9.5 for this project

1. place code.tgx in folder you want to unpackage it in

   
In terminal
2. tar -xvf code.tgx
3. cd Users/jasonmauzey/PycharmProjects/circulo_test   
4. sudo apt-get install python3.9-venv
5. python3 -m venv env
    - env is the name you want to name your environment
6. source env/bin/activate
    - replace env with the name you chose in 3
7. pip install -r requirements.txt
 

###Use
in virtual environment
1. type      jupyter lab

2. select the local host link if the browser doesn't open
3. on left side select eda.ipynb
4. you shouldn't have to run the notebook as the previous results will be saved



###Parts of project
 - data_prep - data preparation sample
 - tests - testing sample
 - train_model - empty model that would normally be used
 - eda.ipynb - jupyter notebook used for the majority of project


     
###Results
More in depth notes are in the notebook. Overall I think the results
where ok put I wouldn't want to go with the results. There wasn't much
data to work with. For this case I suspect that having a higher recall
is more important. One of the models had a fairly high recall with a 20 
percent precision would be reasonable given the rest of the models.



####Approach notes
All the analysis notes are in the jupyter notebook. I will list high 
level notes here. 
 - Initial visualization was successful and offered insights. 
 - I used pandas dummies method for ease use, this would not be usable in a production 
setting
 - I only tried standard scaler. With MLflow, I would usually try different methods and record the
results
 -   


I wanted to go with the "throw stuff at the wall approach and see what sticks" method
due to the short timeframe. I applied a handful of models after initial data cleaning 








####Short on time notes
For this case with only 4-6 hours to work on it and with visualizations that
can be shared being an important part I went primarily with the jupyter notebook
as it is well-designed for that use case. I did create the data_prep and train_model
modules as I would usually use them as well as a prediction module that would pick
up the model and serve, generally behind an api. I put some code in the data_prep
and made a test for it as that is usually how I build projects. Something I usually
use for project like this is mlflow to track experiments and artifacts such as models.

####Notes of interest
- I followed the ml practice of X being in uppercase which is not pep8 standard
- Usually when starting a project like this I go down one of two paths.
    -   I know what I am attempting to do can be done, and I follow TDD coding
    principles
    -   I am not sure the approach will work, and I use a combination of notebook
    and project organization to address the problem. If the results are successful 
        I fully port the code into the project format
