# DEPLOYMENT

Steps:
1. Create a model in sage maker
   + provide path of model in SageMaker
   + provide path of model artifacts
2. Create an END POINT CONFIGURATION
   for HTTPS END POINT
   + specify name of model
   + specify number and type of ML compute instances
   + if you specify two or more instances, AWS will deploy them in multiple availability zones
3. create an HTTPS end point

note. once a model is deployed, we can validate it by sending sample requests and get inferences from juputer notebook






