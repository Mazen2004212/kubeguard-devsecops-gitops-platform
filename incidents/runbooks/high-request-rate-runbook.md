**# KubeGuard Incident Runbook: High Request Rate**



**## Objective**



**Simulate high application traffic and validate that Prometheus detects increased request rate using the KubeGuardHighRequestRateDemo alert.**



**## Alert Rule**



**```promql**

**sum(rate(kubeguard\_http\_requests\_total{namespace="kubeguard"}\[1m])) > 1**

