![AWS_CRC_picture](https://github.com/ikanko1989/CRC-project/assets/139227790/ef67abb9-296b-4cb4-be0f-b07b597835b3)

Before starting this project I have managed to complete AWS Cloud Practitioner certification exam.
I successfully passed the exam on 19.01.2024.

The AWS Cloud Resume Challenge involves creating a static resume website (in my case it is my CV) that is hosted on AWS and integrated with various AWS services to provide dynamic functionality, such as a visitor counter. 

Here’s a detailed explanation of how it works, broken down into its main components:
1. Frontend: Static Website(my personal CV)
•	HTML/CSS/JavaScript: Created a static website using HTML, CSS, and JavaScript to display website(CV).
•	Hosting on S3: The static files are uploaded to an Amazon S3 bucket, which is configured to host the website. S3 provides a cost-effective, highly available solution for serving static content.


2. Custom Domain and HTTPS
•	Domain Name: Used Amazon Route 53 to manage domain name. If you don’t have a domain, you can register one through Route 53 or another registrar.
•	CloudFront Distribution: Set up an AWS CloudFront distribution to cache and serve my website content globally with low latency. CloudFront also provides HTTPS support.
•	SSL/TLS Certificate: Used AWS Certificate Manager (ACM) to provision an SSL/TLS certificate for my domain, enabling HTTPS to secure the site.


3. Backend: Visitor Counter
•	API Gateway: AWS API Gateway is used to create a RESTful API that handles requests from my website. This API interacts with the backend to update and retrieve the visitor count.
•	Lambda Function: AWS Lambda, a serverless compute service, is used to execute code in response to the API requests. The Lambda function interacts with a DynamoDB table to increment and retrieve the visitor count.
•	DynamoDB: AWS DynamoDB is a fully managed NoSQL database service used to store the visitor count. The Lambda function will read from and write to this database.

4. CI/CD Pipeline
•	GitHub Repository: Hosted my code in a GitHub repository. The repository contains your static website files, and Lambda function code.
•	GitHub Actions: Set up GitHub Actions to create a CI/CD pipeline. This pipeline automates the process of building, testing, and deploying your code. For example, it can automatically deploy updates to your S3 bucket and Lambda function when changes are pushed to the repository.

5. Infrastructure as Code (IaC) –Planning to do to as a future improvement
•	AWS CloudFormation or Terraform: Use IaC tools to define and deploy your AWS resources. This ensures your infrastructure is reproducible and manageable.
•	CloudFormation Template/Terraform Configuration: Write a CloudFormation template or Terraform configuration file that defines all the necessary AWS resources, including S3, CloudFront, API Gateway, Lambda, DynamoDB, and Route 53.


Workflow and Interaction
1.	User Visits Website: When a user visits my website, their browser requests the static content (HTML, CSS, JavaScript) from CloudFront, which caches the content from the S3 bucket.
2.	JavaScript Makes API Call: The JavaScript on my website makes a call to the API Gateway endpoint to get the current visitor count.
3.	API Gateway Triggers Lambda: API Gateway receives the request and triggers the Lambda function.
4.	Lambda Interacts with DynamoDB: The Lambda function executes, incrementing the visitor count in the DynamoDB table and retrieving the updated count.
5.	Response Sent Back: The Lambda function sends the updated visitor count back through API Gateway to the frontend.
6.	Update Counter on Website: The JavaScript on my website updates the visitor counter displayed to the user.


