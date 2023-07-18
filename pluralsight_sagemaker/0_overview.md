# Source of info:
https://app.pluralsight.com/course-player?courseId=6be37733-52e3-44f5-8c5c-f8fd9ca94677

# SageMaker overview
Allows developers to:
1. Build
2. Train
3. Deploy (to RestAPI) a ML model

# Sage Maker Advantage 
1. we don't have to waste time doing this manually + installing tools
2. Built in high performance algos, ready optimised for production

# Pre-built algos vs Custom algos
Built in algos: 
- ready to be used
- optimised for production
- sage maker can automate hyper-parameter optimization

Own algos:
- flexible and customizable 
- can use any language + any frameworks
- usable as long as code is packed in docker image
- AWS provides ready made TensorFlow and ApacheMXNet docker containers


# Deploying model on AWS sage maker
1. create end points
2. monitor end points
3. autoscale end points which automatically adjust machine fleets to demand for model usage




# Example workflow

### 1. Infrastructure
- create IAM role for user
- create S3 bucket to store INPUT DATA and OUTPUT DATA.
- 

### 3. Deployment 
- once a model is deployed on sage maker, it has a URL
- you can use postman to test POST/GET requests
- For example, we can have an image classification model on sageMaker, we can post an image to the restAPI and the API will return a string to indicate the classification result