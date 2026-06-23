**# KubeGuard Incident Runbook: High Error Rate**



**## Objective**



**Simulate HTTP 5xx application errors and validate that Prometheus detects the issue using the KubeGuardHighErrorRate alert.**



**## Alert Rule**



**```promql**

**sum(rate(kubeguard\_http\_requests\_total{namespace="kubeguard", status=\~"5.."}\[1m])) > 0.1**

