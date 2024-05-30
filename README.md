# ChatApp Deployment to Amazon EKS 

This GitHub Actions workflow automates the deployment of the ChatApp application to an Amazon EKS (Elastic Kubernetes Service) cluster. The ChatApp is a simple chat web application built with Flask, allowing users to communicate in real-time.

## Workflow Description

The workflow is triggered on every push to the `main` branch and on pull requests targeting the `main` branch. It consists of the following steps:

### 1. Checkout code
Retrieves the source code of the ChatApp from the repository using the `actions/checkout` action.

### 2. Install kubectl
Sets up `kubectl`, the Kubernetes command-line tool, for interacting with the Amazon EKS cluster using the `azure/setup-kubectl` action.

### 3. Configure AWS Credentials
Configures AWS credentials for authentication and authorization using the `aws-actions/configure-aws-credentials` action. It retrieves the necessary AWS access key ID and secret access key from GitHub Secrets.

### 4. Login to Amazon ECR
Logs in to Amazon Elastic Container Registry (ECR) to authenticate Docker and push the Docker image of the ChatApp using the `aws-actions/amazon-ecr-login` action.

### 5. Build, tag, and push Docker image to Amazon ECR
Builds the Docker image of the ChatApp, tags it with the latest version, and pushes it to the Amazon ECR repository.

### 6. Install AWS CLI
Installs the AWS Command Line Interface (CLI) for managing Amazon EKS using the `unfor19/install-aws-cli-action` action.

### 7. Update kube config + deploy app with updated image and svc
Updates the Kubernetes configuration to access the Amazon EKS cluster and deploys the ChatApp using the updated Docker image and service configuration. It scales down the deployment to zero replicas, waits for 5 seconds, and scales it back up to one replica to trigger the rollout of the updated image.

## ChatApp Deployment

The deployment includes:

- **Deployment YAML**: Defines the deployment configuration for the ChatApp, specifying the pod template, image, ports, and other settings.

- **Service YAML**: Defines the Kubernetes service configuration for the ChatApp, exposing it internally within the cluster.

## Usage

To use this workflow:

1. Ensure that your AWS credentials (access key ID and secret access key)  are stored securely in GitHub Secrets.

2. Update the deployment YAML (`deployment.yml`) and service YAML (`service.yml`) files with your specific configuration and settings.

3. Push your changes to the `main` branch or create a pull request targeting the `main` branch to trigger the workflow.

4. Monitor the workflow execution and verify the successful deployment of the ChatApp to the Amazon EKS cluster.

## Additional Information

- **Author**: [Your Name or Organization]
- **License**: [Specify License]

For more information on Amazon EKS and Kubernetes, refer to the [Amazon EKS Documentation](https://docs.aws.amazon.com/eks/) and [Kubernetes Documentation](https://kubernetes.io/docs/).
