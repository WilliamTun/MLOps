
# Key components
1. URL of s3 bucket with training data & output data
2. config of compute resources
3. elastic contain registry with training code in docker

# Monitor and analyze the training job
1. use AWS cloudwatch to collect raw monitoring data in real time and preprocess it into readable metrics
2. Cloudwatch writes various metrics to logs & visualise as graphs
3. training jobs report:
   - CPU / Memory utilization
   - GPU / GPUMemory utilization
   - Disk Utilization
4. stdout and stderr output by ML algo container is also sent to CloudWatch Logs:
   - log group name: /aws/sagemaker/TrainingJobs 
   - log stream name: [train_job_name]/algo-[instance_num]-[epoch_time_stamp]
   

# Workflow

1. Define the training parameters in a dictionary:
   https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html

2. create the training job
```
sagemaker_client = boto3.client(service_name='sagemaker')
sagemaker_client.create_training_job(**training_parameters)
```

3. check if training job has started
```
status = sagemaker_client.describe_training_job(TrainingJobName=job_name)["TrainingJobStatus"]

print(status)
```

4. Create a "Waiter" that waits until a job finishes and report the status of the training job after it completes/fails

```
try:
    sagemaker_client.get_waiter('training_job_completed_or_stopped').wait(TrainingJobName=job_name)
    status = training_info['TrainingJobStatus']
    print(status)
else:
    status = sagemaker_client.describe_training_job(TrainingJobName=job_name)['FailureReason']
    print(status)
```

5. Go to SageMaker in AWS console and to check training progress, go to tab: "Training" > "TrainingJobs"


