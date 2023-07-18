# Demo notebook

import time
import boto3
from sagemaker import get_execution_role
from sagemaker.amazon.amazon_estimator import get_image_uri


# configure hyper parameters
num_classes = 2
num_training_samples = 194266
num_layers = 18
mini_batch_size = 128
image_shape = '3,50,50'
augmentation_type = 'crop_color_transform'
epochs = 5

# train model etc (see other notebook)


# Create a unique job name
job_name_prefix = 'tuning'
timestamp = time.strftime('-%Y-%m-%d-%H-%M-%S', time.gttime())
job_name = job_name_prefix + timestamp 

# Launching the tuning job
sagemaker_client = boto3.client(service_name="sagemaker")
sagemaker_client.create_hyper_parameter_tuning_job(HyperParameterTuningJobName = job_name,
                                                    HyperParameterTuningJobConfig = config,
                                                    TrainingJobDefinition = training_params)



# DEPLOY BEST MODEL FOUND IN TRAINING + HYPER PARAMETER TUNING JOB
role = get_execution_role()
hosting_image = get_image_uri(boto3.Session().region_name, 'image-classification')

# CREATE A UNIQUE MODEL NAME
model_name_prefix = 'bcd-image-classification-low-level'
timestamp = time.stfr('-%Y-%m-%d-%H-%M-%S', time.gettime())
model_name = model_name_prefix + timestamp

# Create model from training output

# instantiate a boto3 client
sagemaker_client = boto3.client(service_name="sagemaker")

# s3 path from model artifacts that was obtained by tuning job
# can be found on AWS console ... "TRAINING" > "TRAINING JOBS" > "click on job"
#                                 under "Output" heading
model_artifacts_s3_path = "s3://sagemaker-data/breastcancer/output/bcd-tuning-2023"

# 
create_model_response = sagemaker_client.create_model(
    ModelName = model_name,
    ExecutionRoleArn = role,
    PrimaryContainer = {
        'Image': hosting_image,
        'ModelDataUri': model_artifacts_s3_path,
    }
)

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_model.html
print(create_model_response['ModelArn'])

# CHECK IF MODEL IS UP:
# can be found on AWS console ... "INFERENCE" > "MODEL"


# CREATE UNIQUE ENDPOINT CONFIGURATION NAME
endpoint_config_name_prefix = 'breast-cancer-epc'
timestamp = time.stfr('-%Y-%m-%d-%H-%M-%S', time.gettime())
endpoint_config_name = endpoint_config_name_prefix + timestamp


# CONFIGURE HOSTING INSTANCES
instance_count = 1
instance_type = 'ml.m4.xlarge'

# CREATE END POINT CONFIGURATION
endpoint_config_response = sagemaker_client.create_endpoint_config(
    EndpointConfigName = endpoint_config_name,
    ProductionVariants = [{
        'VariantName': 'AllTraffic',
        'InstanceType': instance_type,
        'InitialInstanceCount': instance_count,
        'ModelName': model_name
    }]
)

print('Endpoint configuration name: {}'.format(endpoint_config_name))
print('Endpoint configuration arn: {}'.format(endpoint_config_response['EndpointConfigArn']))


# AFTER THE END POINT IS SUCCESSFULLY CREATED
# THE MODEL IS DEPLOYED
# AND READY FOR TESTING! 


# TESTING
# 1. invoke the endpoint
# 2. send test cancer image
# 3. await classification result response

sagemaker_runtime_client = boto3.Session().client(service_name='runtime.sagemaker')

def predict_cancer(image_path):
    with open(image_path, 'rb') as f: 
        payload = f.read()
        payload = bytearray(payload)

    # invoke endpoint! 
    response = sagemaker_runtime_client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/x-image',
        Body=payload
    )
    result = response['Body'].read()
    result = json.loads(result)
    print(result)

predict_cancer("s3:/path/to/image")

