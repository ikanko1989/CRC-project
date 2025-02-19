# AWS CLOUD RESUME CHALLENGE

![AWS_CRC_picture](https://github.com/ikanko1989/CRC-project/assets/139227790/ef67abb9-296b-4cb4-be0f-b07b597835b3)

## Description
Before starting this project I have managed to complete [AWS Cloud Practitioner certification](https://aws.amazon.com/certification/certified-cloud-practitioner/) exam.  
I [successfully passed](https://www.credly.com/badges/a0318fce-8d31-49c3-8a02-803d7c082def/public_url) the exam on 19.01.2024.   
After completing this project did [AWS Certified Solutions Architect - Associate certification](https://aws.amazon.com/certification/certified-solutions-architect-associate/) exam.  
I [successfully passed](https://www.credly.com/earner/earned/badge/472e26b2-bbcb-4c07-84ed-3be5ca93d35e) the exam on 12.01.2025.

The [AWS Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/) involves creating a static resume website (in my case it is my CV) that is hosted on AWS and integrated with various AWS services to provide dynamic functionality, such as a visitor counter. 

Here’s a detailed explanation of how it works, broken down into its main components:
------------------------------------------------------------------------------------
__1. Frontend: Static Website(my personal CV)__  
•	_HTML/CSS/JavaScript_: Created a static website using HTML, CSS, and JavaScript to display website(CV).    
•	_Hosting on S3_: The static files are uploaded to an Amazon S3 bucket, which is configured to host the website. S3 provides a cost-effective, highly available solution for serving static content.


__2. Custom Domain and HTTPS__    
•	_Domain Name_: Used Amazon Route 53 to manage domain name. If you don’t have a domain, you can register one through Route 53 or another registrar.    
•	_CloudFront Distribution_: Set up an AWS CloudFront distribution to cache and serve my website content globally with low latency. CloudFront also provides HTTPS support.  
•	_SSL/TLS Certificate_: Used AWS Certificate Manager (ACM) to provision an SSL/TLS certificate for my domain, enabling HTTPS to secure the site.


__3. Backend: Visitor Counter__   
•	_API Gateway_: AWS API Gateway is used to create a RESTful API that handles requests from my website. This API interacts with the backend to update and retrieve the visitor count.  
•	_Lambda Function_: AWS Lambda, a serverless compute service, is used to execute code in response to the API requests. The Lambda function interacts with a DynamoDB table to increment and retrieve the visitor count.  
•	_DynamoDB_: AWS DynamoDB is a fully managed NoSQL database service used to store the visitor count. The Lambda function will read from and write to this database.

__4. CI/CD Pipeline__   
•	_GitHub Repository_: Hosted my code in a GitHub repository. The repository contains static website files, and Lambda function code.  
•	_GitHub Actions_: Set up GitHub Actions to create a CI/CD pipeline. This pipeline automates the process of building, testing, and deploying your code. For example, it can automatically deploy updates to your S3 bucket and Lambda function when changes are pushed to the repository.

__5. Infrastructure as Code (IaC) –> Planning to do to as a future improvement__    
•	_AWS CloudFormation or Terraform_: Use IaC tools to define and deploy your AWS resources. This ensures your infrastructure is reproducible and manageable.  
•	_CloudFormation Template/Terraform Configuration_: Write a CloudFormation template or Terraform configuration file that defines all the necessary AWS resources, including S3, CloudFront, API Gateway, Lambda, DynamoDB, and Route 53.


__Workflow and Interaction__    
1.	_User Visits Website_: When a user visits my website, their browser requests the static content (HTML, CSS, JavaScript) from CloudFront, which caches the content from the S3 bucket.
2.	_JavaScript Makes API Call_: The JavaScript on my website makes a call to the API Gateway endpoint to get the current visitor count.
3.	_API Gateway Triggers Lambda_: API Gateway receives the request and triggers the Lambda function.
4.	_Lambda Interacts with DynamoDB_: The Lambda function executes, incrementing the visitor count in the DynamoDB table and retrieving the updated count.
5.	_Response Sent Back_: The Lambda function sends the updated visitor count back through API Gateway to the frontend.
6.	_Update Counter on Website_: The JavaScript on my website updates the visitor counter displayed to the user.


