**# KubeGuard Incident Runbook: Application Target Down**



**## Objective**



**Simulate a production outage where the KubeGuard application becomes unavailable, then validate that Prometheus detects the issue through the KubeGuardTargetDown alert.**



**## Alert Rule**



**```promql**

**up{job="kubeguard-app", namespace="kubeguard"} == 0**

