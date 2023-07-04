provider "aws" {
  region = "eu-central-1"
}
module "jenkins" {
  source = "../../modules/jenkins"
  instance_type = "n5.4xlarge"
  env = "env"
}