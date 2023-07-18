# Key features

1. Problem definition
2. Data sourcing. 
   E.g. pull in data from external provider
3. Data preparing
   - check for Nas
   - what is the data distribution 
   - format data such that it is appropraite for ML framework
4. ML
    - training
    - testing 
    - monitory ...
      the time used while running execution
5. ML model deployment
    - deployment style
    - monitoring
    - model explainability
      (to built trust)
6. Iteration 
    - results of test feed back to model to improve performance


# Version data
Why?
1. Traceability - to maintain all the data that was used
2. Compliance - in some scenarios you must be legally required to explain why a model made a prediction
3. compare and contrast diff datasets


# MLOps ecosystem

Overaching Tools that manages the whole set of eco system tools:
a) Jira
b) GitLab/GitHub

1. Data sourcing:
- Apache Airflow
- Basin
- Chronos

2. Data preprocessing:
- Bokeh
- Feature Tools
- PyOD

3. Model training and evaluation
- Sklearn / tensorflow
- FairLearn

4. Model deployment
- TensorFlow serving
- ForestFlow

5. Model monitoring
- MLWatcher
- Cubonacci


# Example system
a) Data storage
   - local data file
   - cloud hosted dataset
   - public URL

b) preprocess and store data
   - eg. s3 / dynamoDB

c) model training 
   
d) monitor data drift to feedback to dataset section. 



# From Dev to Production

1. data scientists sketch out code in a notebook
2. prepare pipeline infrastructure eg. sagemaker / azure devOps 
3. write python code on visual studio code 
4. upload python code to github / gitlab 

# ML infrastructure

- we need a code repo
- we need pipelines to pull in data from specific sources eg. s3
- we need pipelines to build + train model
- we need pipelines to release ML model to specific cloud resources

- we need to think about cloud resources... to run all the pipelines.


# Example workflow
- 1. Create infrastructure
     bonus points: infrastructure as code. We can configure components of the infrastructure, eg. machine type, as a variable parameter. 
- 2. ssh into machine
- 3. git clone the project
- 4. Run code ... build + release. 




