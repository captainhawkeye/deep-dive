terraform {
  backend "s3" {
    bucket = "anuragpoc-s3"
    key = "Jenkins/terraform.tfstate"
    region = "ap-southeast-2"
  }
}