**# KubeGuard Incident Runbook: High Latency**



**## Objective**



**Simulate slow application responses and validate that Prometheus detects high P95 latency using the KubeGuardHighLatencyP95 alert.**



**## Alert Rule**



**```promql**

**histogram\_quantile(0.95, sum by (le, exported\_endpoint) (rate(kubeguard\_http\_request\_duration\_seconds\_bucket{namespace="kubeguard"}\[2m]))) > 0.3**

