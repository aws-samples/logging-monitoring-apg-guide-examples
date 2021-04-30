## AWS Logging & Monitoring Example Resources
The CloudFormation templates included in this repository are intended to assist you in configuring and installing Amazon CloudWatch and AWS X-Ray for on premises servers, Amazon EC2, Amazon ECS, and Amazon EKS. Templates are also provided for deploying ECS and EKS clusters and services with Amazon CloudWatch preconfigured.

This repository supports guidance provided in the **Designing and implementing logging and monitoring with Amazon CloudWatch** APG guide.

## Resources Summary
Example templates and code are described here by the use case that they are intended to support.  A summary is provided of how the resource can be used to support you in implementing the use case.

### Demo Resources
These resources are provided for you so that you can setup prerequisites and configuration files to demo the Amazon CloudWatch agent, Amazon X-Ray, and the Embedded Metric Format.

* [Sample VPC](./create_vpc_example.yaml) - This template can be used to deploy a sample Amazon VPC with a single public subnet.  It deploys an internet gateway, with a default route on the public subnet.  You need a VPC in order to deploy an Amazon EC2 instance.  The Amazon EC2 instance needs to access the public CloudWatch service endpoints.

* [Amazon S3 bucket for centralized CloudWatch agent configuration storage accessible by AWS Organization accounts](./cloudwatch-config-s3-bucket.yaml) - This CloudFormation template deploys an Amazon S3 bucket that can be made accessible to an entire AWS Organization or Organization Unit.  You can use this sample S3 bucket CloudFormation template to create an S3 bucket accessible by multiple accounts.  The template includes a parameter named OrganizationID that you can use to grant read access to all accounts within an AWS organization.

  Once you have created the S3 bucket, you can create a key / folder prefix structure to store your CloudWatch configuration files.  You can use a folder structure such as this:

    * */config/standard/windows/ec2*:  You can store your standard Windows CloudWatch platform configuration file here for EC2.  You may further categorize your standard platform configurations for different windows versions, EC2 instance types, and environments.
    * */config/standard/windows/onpremises*:  You can store your standard Windows CloudWatch platform configuration file here for on premises servers.  You may further categorize your standard platform configurations for different windows versions, EC2 instance types, and environments.
    * */config/standard/linux/ec2*:  You can store your standard Linux CloudWatch platform configuration file here for EC2.  You may further categorize your standard platform configuration for different linux distributions, EC2 instance types, and environments.
    * */config/standard/linux/onpremises*:  You can store your standard Linux CloudWatch platform configuration file here for on premises servers.  You may further categorize your standard platform configuration for different linux distributions, EC2 instance types, and environments.
    * */config/<application_name>*:  You can store your application specific CloudWatch configuration files here.  You may further categorize your applications with additional folders / prefixes for environments, etc

  This template is intended to be used by [AWS Systems Manager Setup with AWS CloudFormation](./custom_ssm_setup/) and [AWS Systems Manager Document to install /update the Amazon CloudWatch agent - configure from central S3 bucket](dev/builder/logging-monitoring-apg-guide-examples/custom_ssm_setup/InstallAndManageCloudWatchDocument.yaml)

* [AWS Systems Manager Setup with AWS CloudFormation](./custom_ssm_setup/) - This CloudFormation template provides a customized deployment of the [AWS Systems Manager Quick Setup process](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html) via CloudFormation.  This template includes customized SSM documents for deploying and updating your CloudWatch agents from a centralized S3 bucket.

* [IAM Instance Profile for Amazon CloudWatch and AWS Systems Manager](./ssm-cloudwatch-instance-role.yaml) - This instance profile and role includes the AWS managed policy named **AmazonSSMManagedInstanceCore** for Systems Manager as well as the **CloudWatchAgentServerPolicy** for CloudWatch.  This can be deployed at a StackSet to each account.  Since IAM resources are global, it should only be deployed to a single region even in a multi-region configuration.

* [AWS Systems Manager Document to install /update the Amazon CloudWatch agent - configure from central S3 bucket](dev/builder/logging-monitoring-apg-guide-examples/custom_ssm_setup/InstallAndManageCloudWatchDocument.yaml) - This CloudFormation template creates a customized AWS Systems Manager document with steps for Windows and Linux to install and update the Amazon CloudWatch agent.  It also downloads CloudWatch agent configuration files from an S3 bucket accessible by AWS Organizations accounts to the CloudWatch configuration directory and then start / stop the agent on the instance in order to apply configuration changes.  It can be deployed as a StackSet to multiple accounts and regions to centrally maintain and update your CloudWatch agent management.

* [Sample CloudWatch Agent Configuration Files](./cloudwatch_agent_configs) - These CloudWatch agent json configuration files provide the CloudWatch agent predefined metric sets.  You can use them as a starting point for custom CloudWatch agent configuration.

* [Amazon ECS Example Resources](./examples/ecs) - This directory contains sample logging and monitoring resources for Amazon ECS.

* [Amazon EKS Resources](./examples/eks) - This directory contains sample logging and monitoring resources for Amazon EKS.