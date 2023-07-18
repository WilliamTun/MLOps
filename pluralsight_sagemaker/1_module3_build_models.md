

# Option 1: Notebook instances
- sageMaker has fully managed jupyter notebooks, including pre-installed ML related packages & infra storage volumes. 
- option to deploy models to "sagemaker hosting"

# Workflow 1: set up infrastructure
- 1. create a new notebook
- 2. Use bash scripts in notebook to create relevant folders and chmod
```
%%bash

mkdir /home/ec2-user/my_folder
mv <file> /home/ec2-user/my_folder
chmod 600 /home/ec2-user/my_folder/<file>
```

- 3. If using tensorflow for classification, make a folder and within that folder, make a subdirectory to store data from each class
- 4. copy train and test datasets to s3

```
%%bash

aws s3 cp <training_data> s3://<bucket>/<input>/<train_data>


aws s3 cp <testing_data> s3://<bucket>/<input>/<test_data>
```

# Workflow 2: set up notebook code to take in data

### Path 1: Custom manual approach
- 1. put model hyperparameters in variable
- 2. put a unique job name in a variable. Using time stamps may help with creating the unique job name
- 3. specify the path of the training and test datasets in the S3 buckets
- 4. specify the path of the S3 bucket to hold the outputs
- 5. put training instance parameters such as instance count, machine type and volume size into variables
- 6. Create a dictionary that holds all the variables defined above. See: 
https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html

### Path 2: High level sage maker python library
- repeat up to step 5 from above
- then call the sagemaker library:
```

sagemaker_session = sagemaker.Session() 
estimator = sagemaker.estimator.Estimator(
        training_image,
        role,
        training_instance_count=training_instance_count,
        training_instance_type=training_instance_type,
        train_volume_size=train_volume_gb,
        train_max_run=train_timeout,
        output_path=output_path,
        sagemaker_session=sagemaker_sesession)
)

estimator.set_hyperparameters(
    num_classes=num_classes,
    num_training_samples=num_training_samples,
    num_layers=num_layers,
    mini_batch_size=mini_batch_size,
    image_shape=image_shape,
    augmentation_type=augmentation_type,
    epochs=epochs,
    learning_rate=learning_rate,
    use_pretrained_model=use_pretrained_model
)
```

### Regardless of option 1 or 2, we next make a tensorflow model in sage maker

1. transform input images as appropriate for task
2. write training script
3. build model using tensorflow estimator
4. sage maker gives training script access to pre-configuted environment variables:
- SML_MODEL_DIR :: local path where training job can write intermediate files and training artifacts to
- SM_NUM_GPUS :: number of gpus available to host
- SM_OUTPUT_DATA_DIR :: path to the directory to write output artifacts to eg. checkpoints &  graphs
- SM_CHANNEL_<XXXX> :: path to input data. We can define several variants of this env variable


### Tensorflow scripts

point 1. we can parse arguments from env variables

```
def _parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--model-dir', type=str)

    parser.add_argument('--sm-model-dir', type=str, default = os.environ.get('<ENV_VARIABLE>')
    
    parser.add_argument('--epochs', type=int, default = 100)
    )
```



