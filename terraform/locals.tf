locals {
  name_prefix = "${var.project_name}-${var.environment}"

  tags = {
    Project     = "KubeGuard"
    Environment = var.environment
    ManagedBy   = "Terraform"
    Owner       = "Mazen"
  }
}
