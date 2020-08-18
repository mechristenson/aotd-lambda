### Lambda
Stored in `lambda/`

#### Updating VirtualEnv

- $ source aotd-lambda/bin/activate
- $ pip install <library_name>
- $ deactivate

#### Update Payload

- $ ./create-payload.sh

#### Uploading to AWS Manually (Note must delete function in AWS if exists)

- $ ./create-lambda.sh

### AWS Infrastructure
Configured using Terraform. Runs in us-west-1. Stored in `terraform/`

#### Build Infrastructure

- $ terraform fmt
- $ terraform validate
- $ terraform apply

#### Check Infrastructure

- $ terraform show

#### Teardown Infrastructure

- $ terraform destroy