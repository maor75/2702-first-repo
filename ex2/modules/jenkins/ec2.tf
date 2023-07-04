resource "aws_instance" "web" {
  count = var.create_ec2 ? 1 : 0
  ami = "ami-04a0ae173da5807d3"
  instance_type = var.instance_type
  tags = {
    Name = "blabla"
    Environment = var.env
  }
}