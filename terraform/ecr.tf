resource "aws_ecr_repository" "kubeguard_app" {
  name = "kubeguard-demo-app"

  image_scanning_configuration {
    scan_on_push = true
  }

  lifecycle {
    prevent_destroy = true
  }

  tags = {
    Name = "kubeguard-demo-app"
  }
}
