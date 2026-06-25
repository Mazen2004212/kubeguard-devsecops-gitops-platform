variable "aws_region" {
  description = "AWS region used for KubeGuard infrastructure."
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name."
  type        = string
  default     = "kubeguard"
}

variable "environment" {
  description = "Environment name."
  type        = string
  default     = "dev"
}

variable "cluster_name" {
  description = "EKS cluster name."
  type        = string
  default     = "kubeguard-eks"
}

variable "vpc_cidr" {
  description = "VPC CIDR block."
  type        = string
  default     = "10.40.0.0/16"
}

variable "node_instance_types" {
  description = "EKS managed node group instance types."
  type        = list(string)
  default     = ["t3.small"]
}

variable "node_capacity_type" {
  description = "EKS node capacity type. Use ON_DEMAND for stability or SPOT for lower cost demos."
  type        = string
  default     = "ON_DEMAND"
}

variable "node_desired_size" {
  description = "Desired number of worker nodes."
  type        = number
  default     = 2
}

variable "node_min_size" {
  description = "Minimum number of worker nodes."
  type        = number
  default     = 1
}

variable "node_max_size" {
  description = "Maximum number of worker nodes."
  type        = number
  default     = 3
}
