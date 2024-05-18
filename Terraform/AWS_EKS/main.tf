data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type = "Service"
      identifiers = [ "eks.amazonaws.com" ]
    }

    actions = [ "sts:AssumeRole" ]
  }
}

resource "aws_iam_role" "example" {
  name = "anuragpoc-eks-role"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_iam_role_policy_attachment" "example-AWSEKSClusterPolicy" {
  policy_arn = "arn:aws:iam:aws:policy/AmazonEKSClusterPolicy"
  role = aws_iam_role.example.name
}

data "aws_vpc" "default" {
  default = true
}

data "aws_subnets" "public" {
  filter {
    name = "vpc-id"
    values = [ data.aws_vpc.default.id ]
  }
}

resource "aws_eks_cluster" "example" {
  name = "anuragpoc-eks"
  role_arn = aws_iam_role.example.arn

  vpc_config {
    subnet_ids = data.aws_subnets.public.ids
  }

  depends_on = [
    aws_iam_role_policy_attachment.example-AWSEKSClusterPolicy,
  ]
}

resource "aws_iam_role" "example1" {
  name = "anuragpoc-eks-nodegroup-role"

  assume_role_policy = jsonencode({
    Statement = [{
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
            Service = "ec2.amazonaws.com"
        }
    }]
    Version = "2012-10-17"
  })
}

resource "aws_iam_role_policy_attachment" "example-AmazonEKSWorkerNodePolicy" {
  policy_arn = "arn:aws:iam:aws:policy/AmazonEKSWorkerNodePolicy"
  role = aws_iam_role.example1.name
}

resource "aws_iam_role_policy_attachment" "example-AmazonEKS_CNI_Policy" {
  policy_arn = "arn:aws:iam:aws:policy/AmazonEKS_CNI_Policy"
  role = aws_iam_role.example1.name
}

resource "aws_iam_role_policy_attachment" "example-AmazonEC2ContainerRegistryReadOnly" {
  policy_arn = "arn:aws:iam:aws:policy/AmazonEC2ContainerRegistryReadOnly"
  role = aws_iam_role.example1.name
}

resource "aws_eks_node_group" "example" {
  cluster_name = aws_eks_cluster.example.name
  node_group_name = "anuragpoc-eks-nodegroup"
  node_role_arn = aws_iam_role.example1.arn
  subnet_ids = data.aws_subnets.public.ids

  scaling_config {
    desired_size = 1
    max_size = 2
    min_size = 1
  }

  instance_types = [ "t2.medium" ]

  depends_on = [
    aws_iam_role_policy_attachment.example-AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.example-AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.example-AmazonEC2ContainerRegistryReadOnly,
  ]
}