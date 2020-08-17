### Lambda
Stored in `lambda/`

#### Updating VirtualEnv
  $ source aotd-lambda/bin/activate
  $ pip install <library_name>
  $ rm function.zip # if zip already exists
  $ cd aotd-lambda/lib/python3.8/site-packages
  $ zip -r9 ~/Developer/personal/aotd-lambda/lambda/function.zip .

#### Updating Code (Must run for each file after updating VirtualEnv)
  $ zip -g function.zip <file_name>

#### Uploading to AWS Manually (Note must delete function in AWS if exists)
  $ ./create-lambda.sh

### AWS Infrastructure
Configured using Terraform. Runs in us-west-1. Stored in `terraform/`

#### Build Infrastructure

$ terraform fmt
$ terraform validate
$ terraform apply

#### Check Infrastructure

$ terraform show

#### Teardown Infrastructure

$ terraform destroy