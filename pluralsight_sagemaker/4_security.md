# Main Topics:

1. Authentication & Access control with IAM
2. Monitor and troubleshoot endpoints with Cloudwatch
3. Configure automatic scaling for end points

# Monitoring
Once deployed, sagemaker end points can be monitored with cloudwatch.

End point invocation metrics:
1. Invocation4XXErrors
   number of 400 http response code returned 
2. Invocation5XXErrors
   number of 500 http response code returned 
3. Invocations
   total number of invoked end point requests sent to model end point
4. InvocationsPerInstance
   useful metric if we deploy model to several end points
5. ModelLatency
   interval of time (microseconds), taken by model, to respond to sage maker
6. Overhead Latency
   interval of time (microseconds), time taken to respond to a client request


Endpoint hosting metrics:
1. CPUUtilization
2. MemoryUtilization
3. GPUUtilization
4. GPUMemoryUtilization
5. DiskUtilization


# Automatic scaling for sagemaker endpoints
Automatic scaling dynamically adjusts number of instances provisioned 
for a production variant... in response to changes in workload

How?
1. define a scaling policy

define: 

1. target metric - to determine what metric to look at to see how much to scale. 
2. Min - max capacity 
3. Cool down period ... amount of time lag between one scale in/out activity and another scale in/out activity

