import boto3
import json
import base64 

sagemaker_runtime_client = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    image = base64.b64decode(event['image'])
    return _predict_breast_cancer(image)

def _predict_breast_cancer(image):
    response = sagemaker_runtime_client.invoke_endpoint(
        EndpointName='endpoint_name_2023_05_07',
        ContentType='application/x-image',
        Body=image
    )
    result = response['Body'].read()
    result = json.loads(result)
    predicted_class = 0 if result[0] > result[1] else 1
    if predicted_class == 0:
        return "Negative result"
    else:
        return "Positive result"
