# Python Diagrams Method

Uses the `diagrams` Python library which renders professional architecture diagrams with real icons (AWS, GCP, on-prem, databases, queues, etc.) on a white background.

Best for: system architecture, infrastructure, service flows, data pipelines, deployment diagrams.

Reference script: `scripts/diagrams_event_driven.py`

## Script Template

Write a Python script to `data/articles/<YYMMDD_slug>/diagram_source.py`:

```python
from diagrams import Diagram, Cluster, Edge
# Import nodes from: diagrams.onprem.*, diagrams.aws.*, diagrams.gcp.*,
#   diagrams.programming.*, diagrams.generic.*, etc.

OUTPUT = "diagram"  # produces diagram.png in current directory

with Diagram("Diagram Title", filename=OUTPUT, show=False, direction="LR",
             graph_attr={"bgcolor": "white", "pad": "0.5", "dpi": "150"}):
    # Define nodes, clusters, and edges
    ...
```

## Common Node Imports

- **Clients**: `diagrams.onprem.client.Client`, `diagrams.onprem.client.User`
- **Web/API**: `diagrams.programming.framework.FastAPI`, `diagrams.onprem.network.Nginx`
- **Databases**: `diagrams.onprem.database.PostgreSQL`, `diagrams.onprem.database.MongoDB`
- **Queues**: `diagrams.onprem.queue.Kafka`, `diagrams.onprem.queue.RabbitMQ`
- **Monitoring**: `diagrams.onprem.monitoring.Prometheus`, `diagrams.onprem.monitoring.Grafana`
- **Compute**: `diagrams.generic.compute.Rack`, `diagrams.onprem.compute.Server`
- **Storage**: `diagrams.onprem.storage.StorageDevice`, `diagrams.gcp.storage.GCS`
- **AI/ML**: `diagrams.gcp.ml.AIHub`, `diagrams.aws.ml.Sagemaker`

## Render

```bash
cd data/articles/<slug> && python diagram_source.py
```

This produces `diagram.png` in the article directory.

## Branding

Add TadReamk branding (logo + "TadReamk.com") to the top-right:
```bash
python scripts/add_branding.py --image data/articles/<YYMMDD_slug>/diagram.png
```
