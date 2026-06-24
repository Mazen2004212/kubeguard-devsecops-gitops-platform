terraform {
  backend "s3" {
    bucket       = "kubeguard-tf-state-766696030212-us-east-1"
    key          = "kubeguard/terraform.tfstate"
    region       = "us-east-1"
    encrypt      = true
    use_lockfile = true
  }
}
