provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"  # Example AMI, replace with a valid one
  instance_type = "t2.micro"

  tags = {
    Name = "DevOpsMegaProject"
  }
}
