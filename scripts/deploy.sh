#!/bin/sh


REGION="us-east-1"
AWS_ACCOUNT_ID="111111111111"
PROJECT_NAME="fastapi-template"

IMAGE_URI="$AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$PROJECT_NAME:latest"


echo ========== Build the project ==========

uv lock
docker build -t $PROJECT_NAME -f ./lambda.Dockerfile .

echo ========== Build the project ==========


echo ========== Push image to ECR ==========

aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $IMAGE_URI
docker tag $PROJECT_NAME:latest $IMAGE_URI
docker push $IMAGE_URI

echo ========== Push image to ECR ==========


echo ========== Update AWS Lambda function  ==========

aws lambda update-function-code \
   --function-name $PROJECT_NAME \
   --image-uri $IMAGE_URI \
   --publish


echo ========== Update AWS Lambda function  ==========
