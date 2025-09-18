---
id: f14bb9c2ba
question: Getting ERROR [internal] load metadata for public.ecr.aws/lambda/python:3.8
sort_order: 3100
---

This error is produced sometimes when building your Docker image from the Amazon Python base image.

### Solution Description:

The following could solve the problem:

- **Update Docker Desktop**: Ensure you have the latest version installed.
- **Restart Docker and Terminal**: Try restarting Docker Desktop and your terminal application, then build the image again.
- **Disable BuildKit**: If the above steps do not work, run the following command to disable Docker BuildKit and build your image:
  
  ```bash
  DOCKER_BUILDKIT=0 docker build .
  ```

<details>
  <summary>Additional Deployment Information (Optional)</summary>
  
  **Q: How can I deploy a machine learning model using AWS Lambda and API Gateway?**
  
  To deploy a machine learning model using AWS Lambda and API Gateway, follow these steps:
  
  1. **Prepare the Code for Lambda**: Develop and test your machine learning model (e.g., using TensorFlow Lite) locally. Ensure the model is optimized for serverless execution.
  
  2. **Use AWS Lambda**: AWS Lambda allows you to run code without provisioning or managing servers. Upload your code, which may include the model, dependencies, and necessary libraries.
  
  3. **Prepare a Docker Image (Optional)**: If custom dependencies or environments are required, package your application in a Docker image, upload it to Amazon Elastic Container Registry (ECR), and link it to AWS Lambda.
  
  4. **Create the Lambda Function**: After preparing your code or Docker image, create a Lambda function to process requests and return results.
  
  5. **Expose the Lambda Function using API Gateway**: Set up an API Gateway to expose the Lambda function as a RESTful endpoint, allowing interaction with your model via HTTP requests.

  By following these steps, you can deploy and expose your machine learning model in a scalable and efficient serverless architecture using AWS Lambda and API Gateway.
</details>