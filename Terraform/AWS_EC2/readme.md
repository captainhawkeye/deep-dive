## Description ##

- This Terraform Script will provision an AWS EC2 instance along with required roles/permissions. It will also install the following softwares/packages in the instance along with the provisioning.
    - Jenkins
    - Docker
    - Trivy
    - Terraform
    - Kubectl
    - AWS CLI

## Steps ##

- terraform init
- terraform --version
- terraform validate
- aws --version
- terraform plan
- terraform apply / terraform apply --auto-approve