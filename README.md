# KubeGuard — DevSecOps GitOps Monitoring Platform

![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?style=for-the-badge\&logo=kubernetes\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-Package_Manager-0F1689?style=for-the-badge\&logo=helm\&logoColor=white)
![Argo CD](https://img.shields.io/badge/Argo_CD-GitOps-EF7B4D?style=for-the-badge\&logo=argo\&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EKS_Cloud-FF9900?style=for-the-badge\&logo=amazonaws\&logoColor=white)
![Amazon EKS](https://img.shields.io/badge/Amazon_EKS-Kubernetes-FF9900?style=for-the-badge\&logo=amazoneks\&logoColor=white)
![Amazon ECR](https://img.shields.io/badge/Amazon_ECR-Container_Registry-FF9900?style=for-the-badge\&logo=amazonaws\&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-Infrastructure_as_Code-7B42BC?style=for-the-badge\&logo=terraform\&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?style=for-the-badge\&logo=prometheus\&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-Dashboards-F46800?style=for-the-badge\&logo=grafana\&logoColor=white)
![Loki](https://img.shields.io/badge/Loki-Logging-F46800?style=for-the-badge\&logo=grafana\&logoColor=white)
![Kyverno](https://img.shields.io/badge/Kyverno-Policy_Enforcement-326CE5?style=for-the-badge\&logo=kubernetes\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI_Quality_Gates-2088FF?style=for-the-badge\&logo=githubactions\&logoColor=white)
![Trivy](https://img.shields.io/badge/Trivy-Security_Scanning-1904DA?style=for-the-badge\&logo=aqua\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Demo_App-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![Python](https://img.shields.io/badge/Python-Backend-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

KubeGuard is a production-style DevSecOps and GitOps Kubernetes platform built with FastAPI, Docker, Helm, Kubernetes, Argo CD, Prometheus, Grafana, Loki, Promtail, Kyverno, GitHub Actions, Trivy, Terraform, Amazon ECR, and Amazon EKS.

The project demonstrates the complete operational lifecycle of a Kubernetes workload: containerization, Helm packaging, GitOps deployment, AWS EKS cloud deployment, immutable container image publishing, custom Prometheus metrics, Grafana dashboards, centralized logging, alerting, incident simulation, policy enforcement, HPA autoscaling, Terraform infrastructure provisioning, and CI quality gates.

---

## Table of Contents

* [Project Highlights](#project-highlights)
* [Architecture](#architecture)
* [Tech Stack](#tech-stack)
* [Tools and Technologies](#tools-and-technologies)
* [Screenshots](#screenshots)
* [Application Features](#application-features)
* [Application Endpoints](#application-endpoints)
* [Docker Setup](#docker-setup)
* [Helm Deployment](#helm-deployment)
* [AWS EKS Cloud Deployment](#aws-eks-cloud-deployment)
* [Horizontal Pod Autoscaling](#horizontal-pod-autoscaling)
* [Prometheus Monitoring](#prometheus-monitoring)
* [Grafana Dashboards](#grafana-dashboards)
* [Prometheus Alerting](#prometheus-alerting)
* [Incident Simulation Runbooks](#incident-simulation-runbooks)
* [Kyverno Security Policies](#kyverno-security-policies)
* [Argo CD GitOps](#argo-cd-gitops)
* [Loki and Promtail Logging](#loki-and-promtail-logging)
* [GitHub Actions CI Quality Gates](#github-actions-ci-quality-gates)
* [Terraform Infrastructure](#terraform-infrastructure)
* [Project Structure](#project-structure)
* [What This Project Demonstrates](#what-this-project-demonstrates)
* [Production Roadmap](#production-roadmap)
* [Security Notes](#security-notes)
* [Useful Commands](#useful-commands)
* [Cost Control](#cost-control)
* [CV Summary](#cv-summary)

---

## Project Highlights

* Built a Kubernetes-ready FastAPI application with health, readiness, config, stress, random-error, and metrics endpoints.
* Containerized the application using Docker.
* Created a reusable Helm chart for Kubernetes deployment.
* Deployed the application locally on Docker Desktop Kubernetes.
* Added liveness and readiness probes for workload reliability.
* Configured CPU and memory requests and limits.
* Configured Horizontal Pod Autoscaler with 2 minimum replicas and 6 maximum replicas.
* Exposed custom Prometheus metrics from the application.
* Installed kube-prometheus-stack for Prometheus, Grafana, Alertmanager, kube-state-metrics, and Prometheus Operator.
* Created a ServiceMonitor to scrape KubeGuard custom metrics.
* Built a Grafana observability dashboard as code.
* Added Prometheus alert rules for downtime, high request rate, high error rate, and high latency.
* Simulated real incidents and documented recovery steps with runbooks.
* Installed Kyverno and enforced Kubernetes security policies.
* Blocked insecure pods using Kyverno admission control.
* Installed Argo CD and configured GitOps deployment from GitHub.
* Verified Argo CD sync, health, and self-healing behavior.
* Installed Loki and Promtail for centralized Kubernetes logs.
* Added a Grafana logs dashboard for KubeGuard application logs.
* Added GitHub Actions CI workflow for Helm linting, template rendering, Docker build, and Trivy scans.
* Created an Amazon ECR repository for the KubeGuard application image.
* Built and pushed the Docker image to Amazon ECR using an immutable Git commit SHA tag.
* Provisioned AWS infrastructure using Terraform.
* Created an Amazon EKS cluster using Terraform.
* Created an EKS managed node group using Free Tier eligible worker nodes.
* Deployed KubeGuard to Amazon EKS using Helm and the ECR image.
* Exposed KubeGuard publicly using an AWS LoadBalancer service.
* Verified health, readiness, config, metrics, HPA, pods, services, and nodes on EKS.
* Added proof screenshots for local Kubernetes, AWS EKS, ECR, Terraform, monitoring, alerting, logging, GitOps, security policies, CI quality gates, and Kubernetes operations.

---

## Architecture

### DevSecOps GitOps Architecture

```text
GitHub Repository
    |
    | Push / Pull Request
    v
GitHub Actions
    |
    |-- Helm lint
    |-- Helm template
    |-- Docker build
    |-- Trivy filesystem scan
    |-- Trivy image scan
    v
Validated Source Code
    |
    | GitOps Sync
    v
Argo CD
    |
    | Watches helm/kubeguard-app
    | Sync + Self-Heal
    v
Kubernetes Cluster
    |
    |-- KubeGuard FastAPI Application
    |-- Kubernetes Service
    |-- HPA
    |-- Liveness Probe
    |-- Readiness Probe
    |
    |-- Prometheus ServiceMonitor
    |-- PrometheusRule Alerts
    |
    |-- Grafana Metrics Dashboard
    |-- Loki Logs Dashboard
    |
    |-- Kyverno Security Policies
```

### AWS Cloud Deployment Architecture

```text
Developer Workstation
    |
    | docker build
    | docker tag
    | docker push
    v
Amazon ECR
    |
    | kubeguard-demo-app:<git-sha>
    v
Amazon EKS
    |
    |-- KubeGuard Namespace
    |-- KubeGuard Deployment
    |-- KubeGuard Service - LoadBalancer
    |-- HPA
    |-- Worker Nodes
    |
    v
AWS LoadBalancer
    |
    v
Public HTTP Access
    |
    |-- /health
    |-- /ready
    |-- /config
    |-- /metrics
```

### Terraform AWS Infrastructure Architecture

```text
Terraform
    |
    | Remote backend
    v
S3 Terraform State Bucket
    |
    v
AWS Infrastructure
    |
    |-- VPC
    |-- Public Subnets
    |-- Internet Gateway
    |-- Route Table
    |-- IAM Role for EKS Cluster
    |-- IAM Role for EKS Worker Nodes
    |-- Amazon ECR Repository
    |-- Amazon EKS Cluster
    |-- EKS Managed Node Group
```

### Observability Architecture

```text
KubeGuard Application
    |
    | /metrics
    v
Prometheus
    |
    | PromQL
    v
Grafana Metrics Dashboard
    |
    | Alert Rules
    v
Alertmanager


Kubernetes Pod Logs
    |
    v
Promtail
    |
    | Push logs
    v
Loki
    |
    | LogQL
    v
Grafana Logs Dashboard
```

### Security and Policy Architecture

```text
Developer / kubectl / Argo CD
    |
    | Creates or updates Kubernetes resources
    v
Kubernetes API Server
    |
    | Admission Review
    v
Kyverno
    |
    |-- Require app and project labels
    |-- Require CPU and memory requests/limits
    |-- Disallow latest image tag
    |-- Disallow privileged containers
    v
Allowed or Denied Workload
```

---

## Tech Stack

| Layer                  | Technology                                             |
| ---------------------- | ------------------------------------------------------ |
| Demo Application       | Python, FastAPI, Uvicorn                               |
| Metrics                | prometheus-client                                      |
| Containerization       | Docker                                                 |
| Container Registry     | Amazon ECR                                             |
| Kubernetes Packaging   | Helm                                                   |
| Local Orchestration    | Docker Desktop Kubernetes                              |
| Cloud Orchestration    | Amazon EKS                                             |
| Infrastructure as Code | Terraform                                              |
| Terraform State        | Amazon S3 remote backend                               |
| Autoscaling            | Horizontal Pod Autoscaler                              |
| GitOps                 | Argo CD                                                |
| Monitoring             | Prometheus, Prometheus Operator, kube-prometheus-stack |
| Dashboards             | Grafana                                                |
| Logging                | Loki, Promtail                                         |
| Alerting               | PrometheusRule, Alertmanager                           |
| Policy Enforcement     | Kyverno                                                |
| CI Quality Gates       | GitHub Actions                                         |
| Security Scanning      | Trivy                                                  |
| Version Control        | Git, GitHub                                            |

---

## Tools and Technologies

| Category               | Tools                                              |
| ---------------------- | -------------------------------------------------- |
| Application Runtime    | Python, FastAPI, Uvicorn                           |
| Containerization       | Docker                                             |
| Container Registry     | Amazon ECR                                         |
| Kubernetes             | Deployments, Services, HPA, Probes, Namespaces     |
| Cloud Kubernetes       | Amazon EKS                                         |
| Package Management     | Helm                                               |
| Infrastructure as Code | Terraform                                          |
| Remote State           | Amazon S3                                          |
| GitOps Delivery        | Argo CD                                            |
| Metrics Collection     | Prometheus, ServiceMonitor                         |
| Metrics Dashboarding   | Grafana                                            |
| Centralized Logging    | Loki, Promtail                                     |
| Log Querying           | LogQL                                              |
| Alerting               | PrometheusRule, Alertmanager                       |
| Kubernetes Security    | Kyverno ClusterPolicy                              |
| CI/CD                  | GitHub Actions                                     |
| Security Scanning      | Trivy                                              |
| Local Cluster          | Docker Desktop Kubernetes                          |
| CLI Tools              | kubectl, helm, docker, git, AWS CLI, Terraform CLI |

---

## Screenshots

### Kubernetes and Helm Deployment

#### Helm Lint Success

![Helm Lint Success](screenshots/helm-lint-success.png)

#### Helm Release Installed

![Helm Release Installed](screenshots/helm-release-installed.png)

#### KubeGuard Kubernetes Resources

![KubeGuard Kubernetes Resources](screenshots/kubeguard-k8s-resources.png)

#### KubeGuard HPA Running

![KubeGuard HPA Running](screenshots/kubeguard-hpa-running.png)

#### KubeGuard Pods Recovered After Incident

![KubeGuard Pods Recovered](screenshots/kubeguard-pods-recovered.png)

---

### AWS EKS Cloud Deployment

#### Amazon ECR Image Pushed

![ECR KubeGuard Image Pushed](screenshots/ecr-kubeguard-image-pushed.png)

#### AWS Free Tier Instance Types

![AWS Free Tier Instance Types](screenshots/aws-free-tier-instance-types.png)

#### Terraform EKS Apply Success

![Terraform EKS Apply Success](screenshots/terraform-eks-apply-success.png)

#### Terraform State Resources

![Terraform State Resources](screenshots/terraform-state-resources.png)

#### EKS Cluster Active

![EKS Cluster Active](screenshots/eks-cluster-active.png)

#### EKS Node Group Active

![EKS Node Group Active](screenshots/eks-nodegroup-active.png)

#### EKS Nodes Ready

![EKS Nodes Ready](screenshots/eks-nodes-ready.png)

#### KubeGuard Helm Deployment on EKS

![EKS KubeGuard Helm Deploy](screenshots/eks-kubeguard-helm-deploy.png)

#### KubeGuard Pods Running on EKS

![EKS KubeGuard Pods Running](screenshots/eks-kubeguard-pods-running.png)

#### AWS LoadBalancer Service

![EKS LoadBalancer Service](screenshots/eks-loadbalancer-service.png)

#### KubeGuard Health Check through LoadBalancer

![EKS KubeGuard App Health LoadBalancer](screenshots/eks-kubeguard-app-health-loadbalancer.png)

#### KubeGuard Resources Running on EKS

![EKS KubeGuard Resources Running](screenshots/eks-kubeguard-resources-running.png)

#### KubeGuard HPA Metrics on EKS

![EKS KubeGuard HPA Metrics](screenshots/eks-kubeguard-hpa-metrics.png)

#### Live LoadBalancer Test

![EKS KubeGuard Live LoadBalancer Test](screenshots/eks-kubeguard-live-loadbalancer-test.png)

---

### Prometheus and Grafana Monitoring

#### Monitoring Stack Running

![Monitoring Stack Running](screenshots/monitoring-stack-running.png)

#### KubeGuard ServiceMonitor Created

![KubeGuard ServiceMonitor Created](screenshots/kubeguard-servicemonitor-created.png)

#### Prometheus Custom Metrics

![Prometheus KubeGuard Custom Metrics](screenshots/prometheus-kubeguard-custom-metrics.png)

#### Prometheus Health Metric

![Prometheus KubeGuard Health Metric](screenshots/prometheus-kubeguard-health-metric.png)

#### Grafana Observability Dashboard

![Grafana KubeGuard Observability Dashboard](screenshots/grafana-kubeguard-observability-dashboard.png)

---

### Prometheus Alerting

#### Alert Rules Created

![Prometheus KubeGuard Alert Rules](screenshots/prometheus-kubeguard-alert-rules.png)

#### Alert Pending

![Prometheus KubeGuard Alert Pending](screenshots/prometheus-kubeguard-alert-pending.png)

#### Alert Firing

![Prometheus KubeGuard Alert Firing](screenshots/prometheus-kubeguard-alert-firing.png)

#### Error Rate Alert Pending

![Prometheus KubeGuard Error Rate Pending](screenshots/prometheus-kubeguard-error-rate-pending.png)

#### Latency Alert Pending

![Prometheus KubeGuard Latency Alert Pending](screenshots/prometheus-kubeguard-latency-alert-pending.png)

#### Latency Alert Firing

![Prometheus KubeGuard Latency Alert Firing](screenshots/prometheus-kubeguard-latency-alert-firing.png)

---

### Loki and Promtail Logging

#### Loki and Promtail Running

![Loki Promtail Running](screenshots/loki-promtail-running.png)

#### Grafana Loki Explore Logs

![Grafana Loki KubeGuard Logs](screenshots/grafana-loki-kubeguard-logs.png)

#### Grafana Logs Dashboard

![Grafana KubeGuard Logs Dashboard](screenshots/grafana-kubeguard-logs-dashboard.png)

---

### Kyverno Security Policies

#### Kyverno Pods Running

![Kyverno Pods Running](screenshots/kyverno-pods-running.png)

#### Kyverno Cluster Policies Created

![Kyverno Cluster Policies Created](screenshots/kyverno-cluster-policies-created.png)

#### Deny Pod Without Standards

![Kyverno Deny Pod Without Standards](screenshots/kyverno-deny-pod-without-standards.png)

#### Deny Latest Image Tag

![Kyverno Deny Latest Image](screenshots/kyverno-deny-latest-image.png)

#### Deny Privileged Container

![Kyverno Deny Privileged Container](screenshots/kyverno-deny-privileged-container.png)

#### KubeGuard App Compliant with Kyverno

![KubeGuard App Compliant with Kyverno](screenshots/kubeguard-app-compliant-with-kyverno.png)

---

### Argo CD GitOps

#### Argo CD UI Login Success

![Argo CD UI Login Success](screenshots/argocd-ui-login-success.png)

#### Argo CD KubeGuard App Synced and Healthy

![Argo CD KubeGuard App Synced Healthy](screenshots/argocd-kubeguard-app-synced-healthy.png)

#### Argo CD Self-Healing Restored Replicas

![Argo CD Self Healing Restored Replicas](screenshots/argocd-self-healing-restored-replicas.png)

---

### GitHub Actions CI Quality Gates

#### GitHub Actions CI Success

![GitHub Actions KubeGuard CI Success](screenshots/github-actions-kubeguard-ci-success.png)

---

## Application Features

KubeGuard provides a lightweight application designed for DevOps, SRE, DevSecOps, GitOps, Kubernetes, and observability demonstrations.

| Feature               | Description                                              |
| --------------------- | -------------------------------------------------------- |
| Health check          | Confirms the application is alive                        |
| Readiness check       | Confirms the application is ready to receive traffic     |
| Runtime config        | Displays environment and version values                  |
| Metrics endpoint      | Exposes Prometheus-compatible application metrics        |
| Stress endpoint       | Generates CPU work and latency for incident simulation   |
| Random error endpoint | Simulates HTTP 500 responses for error-rate alerts       |
| Request metrics       | Tracks request count, status code, endpoint, and latency |
| Kubernetes probes     | Uses liveness and readiness probes                       |
| Autoscaling           | HPA scales pods based on CPU utilization                 |
| Cloud deployment      | Runs on Amazon EKS using an image pulled from Amazon ECR |

---

## Application Endpoints

| Endpoint        | Method | Description                      |
| --------------- | ------ | -------------------------------- |
| `/`             | GET    | Application information          |
| `/health`       | GET    | Liveness health check            |
| `/ready`        | GET    | Readiness check                  |
| `/config`       | GET    | Runtime environment and version  |
| `/metrics`      | GET    | Prometheus metrics endpoint      |
| `/stress`       | GET    | Simulates CPU load and latency   |
| `/random-error` | GET    | Simulates random HTTP 500 errors |

---

## Docker Setup

### Build Docker Image Locally

```powershell
docker build -t kubeguard-demo-app:local ./app
```

### Run Container Locally

```powershell
docker run -d --name kubeguard-demo-app -p 8000:8000 kubeguard-demo-app:local
```

### Test Endpoints

```powershell
curl.exe http://localhost:8000/health
curl.exe http://localhost:8000/ready
curl.exe http://localhost:8000/config
curl.exe http://localhost:8000/metrics
```

---

## Helm Deployment

KubeGuard is packaged using Helm.

### Validate Helm Chart

```powershell
helm lint helm\kubeguard-app
```

### Render Kubernetes Manifests

```powershell
helm template kubeguard-app helm\kubeguard-app
```

### Deploy KubeGuard Locally

```powershell
helm upgrade --install kubeguard-app helm\kubeguard-app -n kubeguard --create-namespace
```

### Verify Workloads

```powershell
kubectl get all -n kubeguard
```

---

## AWS EKS Cloud Deployment

KubeGuard was deployed to **Amazon EKS** using Terraform-managed AWS infrastructure and a real container image hosted on **Amazon ECR**.

This upgrade moves the project from a local-only Kubernetes demo to a cloud-ready DevSecOps platform.

### Cloud Deployment Highlights

* Provisioned AWS infrastructure using Terraform.
* Created an Amazon EKS cluster.
* Created an EKS managed node group.
* Used Free Tier eligible EC2 instance types for worker nodes.
* Created and used an Amazon ECR repository.
* Built and pushed the KubeGuard Docker image to ECR.
* Tagged the image using an immutable Git commit SHA.
* Deployed KubeGuard to EKS using Helm.
* Pulled the application image from Amazon ECR.
* Exposed the application publicly using an AWS LoadBalancer service.
* Verified application health, readiness, config, and metrics through the LoadBalancer.
* Verified Kubernetes nodes, pods, services, HPA, and Terraform state.

### ECR Image Registry

The KubeGuard application image was built locally, tagged with the Git commit SHA, and pushed to Amazon ECR.

```text
766696030212.dkr.ecr.us-east-1.amazonaws.com/kubeguard-demo-app:bddda69
```

Separate Helm values files are used for different environments:

```text
helm/kubeguard-app/values.yaml
helm/kubeguard-app/values-ecr.yaml
helm/kubeguard-app/values-eks.yaml
```

This keeps the local Docker Desktop Kubernetes configuration separate from the AWS EKS deployment configuration.

### Build, Tag, and Push to ECR

```powershell
$REGION="us-east-1"
$ACCOUNT_ID=(aws sts get-caller-identity --query Account --output text).Trim()
$ECR_REPO="kubeguard-demo-app"
$IMAGE_TAG=(git rev-parse --short HEAD).Trim()
$ECR_URI="$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$ECR_REPO"

aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin "$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com"

docker build -t kubeguard-demo-app:$IMAGE_TAG ./app

docker tag kubeguard-demo-app:$IMAGE_TAG "${ECR_URI}:$IMAGE_TAG"
docker tag kubeguard-demo-app:$IMAGE_TAG "${ECR_URI}:latest"

docker push "${ECR_URI}:$IMAGE_TAG"
docker push "${ECR_URI}:latest"
```

### Configure kubectl for EKS

```powershell
aws eks update-kubeconfig --region us-east-1 --name kubeguard-eks
kubectl get nodes
```

### Deploy KubeGuard to EKS

```powershell
helm upgrade --install kubeguard-app helm\kubeguard-app `
  -n kubeguard `
  --create-namespace `
  -f helm\kubeguard-app\values-eks.yaml
```

### Verify EKS Deployment

```powershell
kubectl get nodes
kubectl get pods -n kubeguard
kubectl get svc -n kubeguard
kubectl get hpa -n kubeguard
```

### Access KubeGuard through AWS LoadBalancer

```powershell
$LB = kubectl get svc kubeguard-app -n kubeguard -o jsonpath="{.status.loadBalancer.ingress[0].hostname}"

curl.exe http://$LB/health
curl.exe http://$LB/ready
curl.exe http://$LB/config
curl.exe http://$LB/metrics
```

---

## Horizontal Pod Autoscaling

KubeGuard uses Kubernetes HPA to keep at least 2 replicas available and scale up to 6 replicas under CPU load.

| Setting           | Value           |
| ----------------- | --------------- |
| Target deployment | `kubeguard-app` |
| Minimum replicas  | 2               |
| Maximum replicas  | 6               |
| CPU target        | 50%             |

Check HPA:

```powershell
kubectl get hpa -n kubeguard
```

Generate load:

```powershell
for ($i=1; $i -le 50; $i++) {
  curl.exe -s http://localhost:8000/stress | Out-Null
  Start-Sleep -Milliseconds 100
}
```

For EKS LoadBalancer traffic:

```powershell
$LB = kubectl get svc kubeguard-app -n kubeguard -o jsonpath="{.status.loadBalancer.ingress[0].hostname}"

for ($i=1; $i -le 100; $i++) {
  curl.exe -s http://$LB/health | Out-Null
  curl.exe -s http://$LB/ready | Out-Null
  curl.exe -s http://$LB/config | Out-Null
  Start-Sleep -Milliseconds 100
}
```

---

## Prometheus Monitoring

KubeGuard exposes custom Prometheus metrics from the `/metrics` endpoint.

Important metrics:

```text
kubeguard_http_requests_total
kubeguard_http_request_duration_seconds
kubeguard_app_health_status
```

Prometheus scrapes the application using a ServiceMonitor.

### Apply ServiceMonitor

```powershell
kubectl apply -f monitoring\kubeguard-servicemonitor.yaml
```

### Verify ServiceMonitor

```powershell
kubectl get servicemonitor -n monitoring
```

### Open Prometheus

```powershell
kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090 -n monitoring
```

Open:

```text
http://localhost:9090
```

Example PromQL queries:

```promql
kubeguard_http_requests_total
```

```promql
kubeguard_app_health_status
```

```promql
histogram_quantile(0.95, sum by (le, exported_endpoint) (rate(kubeguard_http_request_duration_seconds_bucket[5m])))
```

---

## Grafana Dashboards

KubeGuard includes two Grafana dashboards as code.

| Dashboard                       | Purpose                                       |
| ------------------------------- | --------------------------------------------- |
| `kubeguard-dashboard.json`      | Application metrics and health observability  |
| `kubeguard-logs-dashboard.json` | Application logs and log volume observability |

Dashboard folder:

```text
monitoring/grafana-dashboards/
```

### Apply Metrics Dashboard

```powershell
kubectl create configmap kubeguard-grafana-dashboard `
  --from-file=kubeguard-dashboard.json=monitoring\grafana-dashboards\kubeguard-dashboard.json `
  -n monitoring `
  --dry-run=client -o yaml | kubectl apply -f -

kubectl label configmap kubeguard-grafana-dashboard grafana_dashboard=1 -n monitoring --overwrite
```

### Apply Logs Dashboard

```powershell
kubectl create configmap kubeguard-logs-grafana-dashboard `
  --from-file=kubeguard-logs-dashboard.json=monitoring\grafana-dashboards\kubeguard-logs-dashboard.json `
  -n monitoring `
  --dry-run=client -o yaml | kubectl apply -f -

kubectl label configmap kubeguard-logs-grafana-dashboard grafana_dashboard=1 -n monitoring --overwrite
```

### Restart Grafana

```powershell
kubectl rollout restart deployment monitoring-grafana -n monitoring
kubectl rollout status deployment monitoring-grafana -n monitoring
```

### Open Grafana

```powershell
kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring
```

Open:

```text
http://localhost:3000
```

---

## Prometheus Alerting

KubeGuard includes Prometheus alert rules using the PrometheusRule CRD.

Alert rules file:

```text
monitoring/kubeguard-prometheus-rules.yaml
```

### Alerts

| Alert                          | Purpose                                         |
| ------------------------------ | ----------------------------------------------- |
| `KubeGuardTargetDown`          | Detects when Prometheus cannot scrape KubeGuard |
| `KubeGuardHighRequestRateDemo` | Demonstrates high request-rate alerting         |
| `KubeGuardHighErrorRate`       | Detects HTTP 5xx error spikes                   |
| `KubeGuardHighLatencyP95`      | Detects high P95 latency                        |

### Apply Alert Rules

```powershell
kubectl apply -f monitoring\kubeguard-prometheus-rules.yaml
```

### Check Prometheus Rules

```powershell
kubectl get prometheusrule -n monitoring
```

### Open Prometheus Alerts

```text
http://localhost:9090/alerts
```

---

## Incident Simulation Runbooks

KubeGuard includes runbooks for simulating and recovering from common production incidents.

| Runbook                        | Scenario                     |
| ------------------------------ | ---------------------------- |
| `target-down-runbook.md`       | Application outage           |
| `high-request-rate-runbook.md` | High traffic spike           |
| `high-error-rate-runbook.md`   | HTTP 5xx errors              |
| `high-latency-runbook.md`      | High latency using `/stress` |

Runbook folder:

```text
incidents/runbooks/
```

### Target Down Simulation

```powershell
kubectl scale deployment kubeguard-app -n kubeguard --replicas=0
```

Recovery:

```powershell
kubectl scale deployment kubeguard-app -n kubeguard --replicas=2
```

### High Request Rate Simulation

```powershell
for ($i=1; $i -le 120; $i++) {
  curl.exe -s http://localhost:8000/health | Out-Null
  curl.exe -s http://localhost:8000/ready | Out-Null
  curl.exe -s http://localhost:8000/config | Out-Null
  curl.exe -s http://localhost:8000/metrics | Out-Null
  Start-Sleep -Milliseconds 100
}
```

### High Error Rate Simulation

```powershell
for ($i=1; $i -le 80; $i++) {
  curl.exe -s http://localhost:8000/random-error | Out-Null
  Start-Sleep -Milliseconds 100
}
```

### High Latency Simulation

```powershell
for ($i=1; $i -le 50; $i++) {
  curl.exe -s http://localhost:8000/stress | Out-Null
  Start-Sleep -Milliseconds 100
}
```

---

## Kyverno Security Policies

Kyverno is used to enforce Kubernetes security and best-practice controls in the `kubeguard` namespace.

Policy folder:

```text
security/kyverno-policies/
```

### Policies

| Policy                                     | Purpose                                        |
| ------------------------------------------ | ---------------------------------------------- |
| `kubeguard-require-labels`                 | Requires `app` and `project` labels            |
| `kubeguard-require-resource-limits`        | Requires CPU and memory requests/limits        |
| `kubeguard-disallow-latest-image-tag`      | Blocks containers using the `latest` image tag |
| `kubeguard-disallow-privileged-containers` | Blocks privileged containers                   |

### Install Kyverno

```powershell
helm repo add kyverno https://kyverno.github.io/kyverno/
helm repo update

helm upgrade --install kyverno kyverno/kyverno -n kyverno --create-namespace
```

### Apply Policies

```powershell
kubectl apply -f security\kyverno-policies\
```

### Verify Policies

```powershell
kubectl get clusterpolicy
```

### Test Deny Pod Without Standards

```powershell
kubectl run bad-pod-no-standards -n kubeguard --image=nginx:1.27 --restart=Never
```

### Test Deny Latest Image

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: bad-latest-image
  namespace: kubeguard
  labels:
    app: bad-latest
    project: kubeguard
spec:
  containers:
    - name: nginx
      image: nginx:latest
      resources:
        requests:
          cpu: 50m
          memory: 64Mi
        limits:
          cpu: 100m
          memory: 128Mi
```

### Test Deny Privileged Container

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: bad-privileged-pod
  namespace: kubeguard
  labels:
    app: bad-privileged
    project: kubeguard
spec:
  containers:
    - name: nginx
      image: nginx:1.27
      securityContext:
        privileged: true
      resources:
        requests:
          cpu: 50m
          memory: 64Mi
        limits:
          cpu: 100m
          memory: 128Mi
```

---

## Argo CD GitOps

KubeGuard is managed declaratively using Argo CD.

Argo CD watches the GitHub repository and syncs the Helm chart from:

```text
helm/kubeguard-app
```

Application manifest:

```text
argocd/kubeguard-application.yaml
```

### Install Argo CD

```powershell
kubectl create namespace argocd
kubectl apply -n argocd --server-side --force-conflicts -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### Open Argo CD UI

```powershell
kubectl port-forward svc/argocd-server 8080:443 -n argocd
```

Open:

```text
https://localhost:8080
```

### Apply Argo CD Application

```powershell
kubectl apply -f argocd\kubeguard-application.yaml
```

### Check Application Status

```powershell
kubectl get applications -n argocd
```

Expected output:

```text
kubeguard-app   Synced   Healthy
```

### Self-Healing Demo

Manually change replicas:

```powershell
kubectl scale deployment kubeguard-app -n kubeguard --replicas=1
```

Argo CD automatically restores the desired state from Git.

---

## Loki and Promtail Logging

KubeGuard uses Loki and Promtail for centralized Kubernetes logging.

Logging files:

```text
logging/loki-stack-values.yaml
logging/loki-grafana-datasource.yaml
```

### Install Loki Stack

```powershell
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm upgrade --install logging grafana/loki-stack `
  -n logging `
  --create-namespace `
  -f logging\loki-stack-values.yaml
```

### Verify Logging Stack

```powershell
kubectl get pods -n logging
kubectl get svc -n logging
```

### Add Loki Datasource to Grafana

```powershell
kubectl apply -f logging\loki-grafana-datasource.yaml

kubectl rollout restart deployment monitoring-grafana -n monitoring
kubectl rollout status deployment monitoring-grafana -n monitoring
```

### Example LogQL Queries

```logql
{namespace="kubeguard"}
```

```logql
{namespace="kubeguard"} |= "GET"
```

```logql
{namespace="kubeguard"} |= "random-error"
```

---

## GitHub Actions CI Quality Gates

KubeGuard includes a GitHub Actions workflow that validates the project before changes are merged.

Workflow file:

```text
.github/workflows/kubeguard-ci.yml
```

### Pipeline Stages

* Checkout repository
* Set up Helm
* Run Helm lint
* Render Helm templates
* Build Docker image
* Run Trivy filesystem scan
* Run Trivy container image scan

The pipeline provides CI quality gates for both Kubernetes manifests and container security.

---

## Terraform Infrastructure

Terraform is used to provision the AWS infrastructure required for the EKS deployment.

Terraform files are stored in:

```text
terraform/
```

### Terraform Components

| File           | Purpose                                                                      |
| -------------- | ---------------------------------------------------------------------------- |
| `backend.tf`   | Configures the S3 remote backend and native state locking                    |
| `versions.tf`  | Defines Terraform and provider versions                                      |
| `provider.tf`  | Configures the AWS provider                                                  |
| `variables.tf` | Stores reusable input variables                                              |
| `locals.tf`    | Stores naming and tagging logic                                              |
| `vpc.tf`       | Creates VPC, public subnets, internet gateway, route table, and associations |
| `iam.tf`       | Creates IAM roles and policy attachments for EKS                             |
| `ecr.tf`       | Manages the KubeGuard ECR repository                                         |
| `eks.tf`       | Creates the EKS cluster and managed node group                               |
| `outputs.tf`   | Exposes useful infrastructure outputs                                        |
| `.gitignore`   | Excludes Terraform state files and local artifacts                           |

### Terraform Remote State

Terraform uses an encrypted Amazon S3 backend for remote state storage.

The backend includes:

* S3 bucket for Terraform state storage
* Encryption enabled
* Versioning enabled
* Public access blocked
* Native Terraform S3 lockfile support

### Terraform Workflow

```powershell
cd terraform

terraform init
terraform fmt
terraform validate
terraform plan -out=tfplan
terraform apply tfplan
```

### Terraform Outputs

After applying the infrastructure, Terraform outputs:

* AWS region
* EKS cluster name
* EKS cluster endpoint
* ECR repository URL
* kubectl update-kubeconfig command
* EKS node IAM role name

### Configure kubectl for EKS

```powershell
aws eks update-kubeconfig --region us-east-1 --name kubeguard-eks
kubectl get nodes
```

---

## Project Structure

```text
kubeguard-devsecops-gitops-platform/
│
├── .github/
│   └── workflows/
│       └── kubeguard-ci.yml
│
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── src/
│       └── main.py
│
├── helm/
│   └── kubeguard-app/
│       ├── Chart.yaml
│       ├── values.yaml
│       ├── values-ecr.yaml
│       ├── values-eks.yaml
│       └── templates/
│           ├── deployment.yaml
│           ├── service.yaml
│           └── hpa.yaml
│
├── argocd/
│   └── kubeguard-application.yaml
│
├── monitoring/
│   ├── kubeguard-servicemonitor.yaml
│   ├── kubeguard-prometheus-rules.yaml
│   └── grafana-dashboards/
│       ├── kubeguard-dashboard.json
│       └── kubeguard-logs-dashboard.json
│
├── logging/
│   ├── loki-stack-values.yaml
│   └── loki-grafana-datasource.yaml
│
├── security/
│   └── kyverno-policies/
│       ├── disallow-latest-image-tag.yaml
│       ├── disallow-privileged-containers.yaml
│       ├── require-kubeguard-labels.yaml
│       └── require-resource-limits.yaml
│
├── incidents/
│   └── runbooks/
│       ├── target-down-runbook.md
│       ├── high-request-rate-runbook.md
│       ├── high-error-rate-runbook.md
│       └── high-latency-runbook.md
│
├── terraform/
│   ├── backend.tf
│   ├── versions.tf
│   ├── provider.tf
│   ├── variables.tf
│   ├── locals.tf
│   ├── vpc.tf
│   ├── iam.tf
│   ├── ecr.tf
│   ├── eks.tf
│   ├── outputs.tf
│   ├── .terraform.lock.hcl
│   └── .gitignore
│
├── screenshots/
│   ├── argocd-kubeguard-app-synced-healthy.png
│   ├── argocd-self-healing-restored-replicas.png
│   ├── argocd-ui-login-success.png
│   ├── aws-free-tier-instance-types.png
│   ├── ecr-kubeguard-image-pushed.png
│   ├── eks-cluster-active.png
│   ├── eks-kubeguard-app-health-loadbalancer.png
│   ├── eks-kubeguard-helm-deploy.png
│   ├── eks-kubeguard-hpa-metrics.png
│   ├── eks-kubeguard-live-loadbalancer-test.png
│   ├── eks-kubeguard-pods-running.png
│   ├── eks-kubeguard-resources-running.png
│   ├── eks-loadbalancer-service.png
│   ├── eks-nodegroup-active.png
│   ├── eks-nodes-ready.png
│   ├── github-actions-kubeguard-ci-success.png
│   ├── grafana-kubeguard-logs-dashboard.png
│   ├── grafana-kubeguard-observability-dashboard.png
│   ├── grafana-loki-kubeguard-logs.png
│   ├── helm-lint-success.png
│   ├── helm-release-installed.png
│   ├── kubeguard-app-compliant-with-kyverno.png
│   ├── kubeguard-hpa-running.png
│   ├── kubeguard-k8s-resources.png
│   ├── kubeguard-pods-recovered.png
│   ├── kubeguard-servicemonitor-created.png
│   ├── kyverno-cluster-policies-created.png
│   ├── kyverno-deny-latest-image.png
│   ├── kyverno-deny-pod-without-standards.png
│   ├── kyverno-deny-privileged-container.png
│   ├── kyverno-pods-running.png
│   ├── loki-promtail-running.png
│   ├── monitoring-stack-running.png
│   ├── prometheus-kubeguard-alert-firing.png
│   ├── prometheus-kubeguard-alert-pending.png
│   ├── prometheus-kubeguard-alert-rules.png
│   ├── prometheus-kubeguard-custom-metrics.png
│   ├── prometheus-kubeguard-error-rate-pending.png
│   ├── prometheus-kubeguard-health-metric.png
│   ├── prometheus-kubeguard-latency-alert-firing.png
│   ├── prometheus-kubeguard-latency-alert-pending.png
│   ├── terraform-eks-apply-success.png
│   └── terraform-state-resources.png
│
├── video-script.txt
├── README.md
└── .gitignore
```

---

## What This Project Demonstrates

This project demonstrates hands-on DevOps, DevSecOps, GitOps, SRE, cloud, and Kubernetes operations skills, including:

* Building a containerized FastAPI application.
* Creating production-style Docker images.
* Packaging Kubernetes workloads using Helm.
* Deploying and managing workloads on Kubernetes.
* Deploying workloads to Amazon EKS.
* Publishing application images to Amazon ECR.
* Using immutable Git commit SHA image tags.
* Exposing cloud workloads through an AWS LoadBalancer.
* Creating AWS infrastructure using Terraform.
* Managing Terraform state remotely with Amazon S3.
* Configuring liveness and readiness probes.
* Defining CPU and memory requests and limits.
* Configuring HPA autoscaling.
* Exposing application-level Prometheus metrics.
* Installing and configuring kube-prometheus-stack.
* Creating ServiceMonitor resources.
* Building Grafana dashboards as code.
* Creating Prometheus alert rules.
* Simulating production incidents.
* Writing incident runbooks.
* Enforcing Kubernetes security policies with Kyverno.
* Blocking insecure pods using admission control.
* Managing deployments using Argo CD GitOps.
* Demonstrating self-healing and declarative sync.
* Installing Loki and Promtail for centralized logging.
* Querying logs using LogQL.
* Automating validation with GitHub Actions.
* Scanning code and container images with Trivy.

---

## Production Roadmap

KubeGuard already demonstrates local Kubernetes operations, GitOps, observability, logging, security policies, CI quality gates, Amazon ECR image publishing, Terraform infrastructure, and Amazon EKS deployment.

Future production improvements include:

* Add AWS Load Balancer Controller for ALB-based ingress.
* Add Route53 DNS and ACM TLS certificates.
* Add HTTPS termination.
* Add external Alertmanager notification channels such as Slack, email, or Microsoft Teams.
* Add sealed secrets or external secret management.
* Add image signing with Cosign.
* Add SBOM generation.
* Add OpenTelemetry tracing.
* Add resource dashboards for node and namespace-level usage.
* Add backup and restore procedures.
* Add Kubernetes NetworkPolicies.
* Add Pod Security Standards.
* Add multi-environment GitOps structure for dev, staging, and production.
* Add automated EKS deployment workflow through GitHub Actions.
* Add pytest unit tests and CI test stages.
* Add policy-as-code tests for Kubernetes manifests.

---

## Security Notes

* Kyverno enforces Kubernetes admission policies in the `kubeguard` namespace.
* Containers using the `latest` image tag are blocked in the Kyverno policy demo.
* Privileged containers are blocked.
* Pods missing required labels are blocked.
* Containers without CPU and memory requests and limits are blocked.
* GitHub Actions uses automated security scanning.
* Trivy scans both the filesystem and the container image.
* No secrets should be committed to the repository.
* Test manifests used only for policy validation should not be committed as production manifests.
* AWS root credentials should not be used for daily operations.
* For production usage, IAM users or IAM roles with least-privilege permissions should be used.
* Terraform state files should not be committed to the repository.
* AWS access keys must never be committed.

---

## Useful Commands

### Check KubeGuard

```powershell
kubectl get pods -n kubeguard
kubectl get svc -n kubeguard
kubectl get hpa -n kubeguard
```

### Check EKS

```powershell
aws eks describe-cluster --name kubeguard-eks --region us-east-1 --query "cluster.status" --output text

aws eks describe-nodegroup `
  --cluster-name kubeguard-eks `
  --nodegroup-name kubeguard-dev-node-group `
  --region us-east-1 `
  --query "nodegroup.{status:status,health:health.issues}" `
  --output json
```

### Configure kubectl for EKS

```powershell
aws eks update-kubeconfig --region us-east-1 --name kubeguard-eks
kubectl get nodes
```

### Check Monitoring

```powershell
kubectl get pods -n monitoring
kubectl get servicemonitor -n monitoring
kubectl get prometheusrule -n monitoring
```

### Check Logging

```powershell
kubectl get pods -n logging
kubectl get svc -n logging
```

### Check Kyverno

```powershell
kubectl get pods -n kyverno
kubectl get clusterpolicy
```

### Check Argo CD

```powershell
kubectl get pods -n argocd
kubectl get applications -n argocd
```

### Port Forward KubeGuard App

```powershell
kubectl port-forward svc/kubeguard-app 8000:80 -n kubeguard
```

### Port Forward Grafana

```powershell
kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring
```

### Port Forward Prometheus

```powershell
kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090 -n monitoring
```

### Port Forward Argo CD

```powershell
kubectl port-forward svc/argocd-server 8080:443 -n argocd
```

### Port Forward Loki

```powershell
kubectl port-forward svc/logging-loki 3100:3100 -n logging
```

### Check Terraform State

```powershell
cd terraform
terraform state list
terraform output
```

---

## Cost Control

This project includes both a local Kubernetes environment and an AWS EKS cloud deployment.

Local Docker Desktop Kubernetes does not require paid cloud resources.

The AWS EKS environment can generate ongoing AWS charges while running.

Resources that may generate cost include:

* Amazon EKS cluster
* EC2 worker nodes
* AWS LoadBalancer
* S3 Terraform state bucket
* ECR image storage

To stop AWS costs after the demo, destroy the Terraform-managed infrastructure:

```powershell
cd terraform
terraform destroy
```

Before destroying, make sure all required screenshots and documentation have been captured.

---

## CV Summary

KubeGuard is a production-style DevSecOps and GitOps Kubernetes platform demonstrating Docker, Helm, Kubernetes, Amazon ECR, Amazon EKS, Terraform, Argo CD, Prometheus, Grafana, Loki, Promtail, Kyverno, GitHub Actions, and Trivy.

The project proves hands-on experience with Kubernetes workload deployment, Helm packaging, GitOps synchronization, self-healing, AWS EKS cloud deployment, ECR image publishing, Terraform infrastructure provisioning, custom Prometheus metrics, Grafana dashboards, centralized logging, Prometheus alerting, incident simulation, Kyverno policy enforcement, HPA autoscaling, CI quality gates, and container security scanning.

---

## Resume Bullet Points

* Built a production-style DevSecOps Kubernetes platform using FastAPI, Docker, Helm, Amazon EKS, Amazon ECR, Terraform, Argo CD, Prometheus, Grafana, Loki, Kyverno, and GitHub Actions.
* Provisioned AWS infrastructure with Terraform, including VPC, public subnets, IAM roles, Amazon EKS cluster, EKS managed node group, Amazon ECR repository, and S3 remote state backend.
* Published the application Docker image to Amazon ECR using immutable Git commit SHA tags and deployed it to Amazon EKS using Helm.
* Exposed the EKS-hosted application publicly through an AWS LoadBalancer and verified health, readiness, config, and metrics endpoints.
* Implemented GitOps deployment with Argo CD and Helm, enabling declarative synchronization and self-healing from a GitHub repository.
* Exposed custom Prometheus metrics for request count, latency, and application health, then visualized them using Grafana dashboards.
* Configured Loki and Promtail for centralized Kubernetes log collection and created a Grafana logs dashboard for application log analysis.
* Created Prometheus alert rules for target downtime, high error rate, high latency, and high request rate scenarios.
* Wrote incident simulation runbooks for application outage, traffic spike, HTTP 5xx errors, and latency incidents.
* Enforced Kubernetes security standards with Kyverno policies blocking latest image tags, privileged containers, missing labels, and missing resource limits.
* Added GitHub Actions CI quality gates for Helm linting, Helm template rendering, Docker image build, and Trivy security scanning.

---

## Author

**Mazen Ibrahim Abdelrazek**

GitHub: [Mazen2004212](https://github.com/Mazen2004212)

Project Repository:
https://github.com/Mazen2004212/kubeguard-devsecops-gitops-platform
