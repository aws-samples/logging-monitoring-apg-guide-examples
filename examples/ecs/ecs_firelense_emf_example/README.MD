# Using the FireLens fluent bit agent to send CloudWatch logs in Embedded Metric Format - Demo

You can deploy a sample python application that demonstrates how you can use Firelens with the Embedded Metric Format.  This will enable you to capture custom CloudWatch metrics for your container based workloads running on ECS.  This example uses the [aws-embedded-metrics library for python](https://github.com/awslabs/aws-embedded-metrics-python).


## Deploy  
You will need to build and push a docker image for the application using the provided [Dockerfile](./Dockerfile)  The image is based on the public python 3 image and simply copies the python code to the image and installs the aws-embedded-metrics python library.

### Create a docker image and push it to your docker image repository

1.  Clone this directory and then build the docker image:
         
         docker build -t ecs-firelens-python-emf-demo
         
2.  Tag the image so it can be pushed to your docker image repository, for example, for an ECR repo named ecs-firelens-python-emf-demo, your command will look like:
                  
        docker tag ecs-firelens-python-emf-demo:latest <your account number>.dkr.ecr.<region>.amazonaws.com/ecs-firelens-python-emf-demo:latest
        
3.  Push the image to the repository:

        docker push <account number>.dkr.ecr.<region>.amazonaws.com/ecs-firelens-python-emf-demo:latest
        
### Create an ECS task definition

You can use the AWS CLI to create a task definition for an ECS cluster with EC2 container instances.

1.  Use the AWS CLI with your AWS account credentials applied and run the following command:

        aws ecs register-task-definition --cli-input-json file://ecs-task-python-firelens-emf.json --region <your aws region>

### Launch a new ECS task using the created ECS task definition

Launch a new task into an existing ECS cluster using the task definition you created.  The task definition that is provided is compatible with ECS clusters with EC2 container instances.  You can modify it to work with FARGATE by specifying an **awsvpc** for the **networkMode**.

