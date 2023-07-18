

# AWS API gateway

REST APIs are a "front door" to external apps to access backend services (eg. code/aws lambda).

AWS API gateway is a fully managed service for APIs to:
- create
- publish
- maintain
- monitor
- secure
- scale

# Integrating AWS sageMaker with API gateway
Client app -> AWS API Gateway -> AWS Lambda function -> AWS SageMaker Endpoint


# DEMO
creating an API gateway for defining a REST service for triggering a lambda function, that invokes a sage maker end point, to run a model on input data.

1. Navigate to AWS console: API Gateway
2. Click on create API
3. choose protocol: "REST"
4. choose "new API"
5. fill in api name and description
6. endpoint type: "Regional"
7. click "Next"
8. In actions menu, click "Create Resource"
9. give resource a name and "click resource"
10. In actions menu, click "create method" and select "POST"
11. Choose Integration type: "Lambda"
12. Choose your own custom lambda function 
13. click "Save"

# If API takes in non-conventional media types such as images...
14. Click on "Settings"
15. Under heading "Binary Media types"
16. write: "application/x-image"

# Deploy API
17. Click on "actions"
18. Click "deploy API"
19. select deployment stage: [New Stage]
20. name the new stage + description ... click "Deploy!"

# Test
21. call POST on postman to new deployed API

