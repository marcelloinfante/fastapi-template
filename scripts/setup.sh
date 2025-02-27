#!/bin/sh


REGION="us-east-1"
AWS_ACCOUNT_ID="111111111111"
PROJECT_NAME="fastapi-template"

ROLE_ARN="arn:aws:iam::$AWS_ACCOUNT_ID:role/$PROJECT_NAME"
IMAGE_URI="$AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$PROJECT_NAME:latest"


echo ========== Create ECR repository ==========

aws ecr create-repository \
   --repository-name $PROJECT_NAME

echo ========== Create ECR repository ==========


echo ========== Build the project ==========

uv lock
docker build -t $PROJECT_NAME -f ./lambda.Dockerfile .

echo ========== Build the project ==========


echo ========== Push image to ECR ==========

aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $IMAGE_URI
docker tag $PROJECT_NAME:latest $IMAGE_URI
docker push $IMAGE_URI

echo ========== Push image to ECR ==========


echo ========== Create IAM role ==========

aws iam create-role \
  --role-name $PROJECT_NAME \
  --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'

echo ========== Create IAM role ==========


echo ========== Create AWS Lambda function ==========

sleep 10

aws lambda create-function \
   --function-name $PROJECT_NAME \
   --package-type Image \
   --code ImageUri=$IMAGE_URI \
   --role $ROLE_ARN

echo ========== Create AWS Lambda function ==========


echo ========== Create AWS Lambda function URL ==========

aws lambda create-function-url-config \
    --function-name $PROJECT_NAME \
    --auth-type NONE

echo ========== Create AWS Lambda function URL ==========
