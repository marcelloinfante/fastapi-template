#!/bin/sh

# Build the project
uv lock
docker build -t fastapi-app lambda.DockerFile

# Push image to ECR
aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
docker tag fastapi-app:latest aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest
docker push aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest

# Create AWS Lambda function
aws lambda create-function \
   --function-name myFunction \
   --package-type Image \
   --code ImageUri=aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest \
   --role arn:aws:iam::111122223333:role/my-lambda-role

# Update AWS Lambda function 
aws lambda update-function-code \
   --function-name myFunction \
   --image-uri aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest \
   --publish

