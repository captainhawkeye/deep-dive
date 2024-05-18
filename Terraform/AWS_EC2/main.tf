resource "aws_iam_role" "example_role" {
  name = "anuragpoc-iamrole"

  assume_role_policy = <<EOF
{
    "version": "2012-10-17",
    "statement": [
        {
            "Effect": "Allow",
            "Pricipal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "example_attachment" {
  role = aws_iam_role.example_role.name
  policy_arn = "arn:aws:iam:aws:policy/AdministratorAccess"
}

resource "aws_iam_instance_profile" "example_profile" {
  name = "anuragpoc-profile"
  role = aws_iam_role.example_role.name
}

resource "aws_security_group" "anurag-sg" {
  name = "anuragpoc-sg123"
  description = "Open 22, 443, 80, 8080, 9000"

  ingress = [
    for port in [22, 80, 443, 8080, 9000, 3000] : {
        description      = "TLS from VPC"
        from_port        = port
        to_port          = port
        protocol         = "tcp"
        cidr_blocks      = ["0.0.0.0/0"]
        ipv6_cidr_blocks = []
        prefix_list_ids  = []
        security_groups  = []
        self             = false
    }
  ]

  egress = {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "anuragpoc-sg"
  }
}

resource "aws_instance" "anuragpoc-instance" {
  ami                    = "ami-0f5ee92e2d63afc18"
  instance_type          = "t2.large"
  key_name               = "AnuragPOC"
  vpc_security_group_ids = [aws_security_group.anurag-sg.id]
  user_data              = templatefile("./install.sh", {})
  iam_instance_profile   = aws_iam_instance_profile.example_profile.name

  tags = {
    Name = "anuragpoc-ec2-machine"
  }

  root_block_device {
    volume_size = 30
  }
}