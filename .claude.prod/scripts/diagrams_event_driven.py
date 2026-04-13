"""diagrams library - Example 2: Event-Driven Microservices"""
import os
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Client
from diagrams.onprem.network import Nginx
from diagrams.programming.framework import FastAPI
from diagrams.onprem.database import PostgreSQL, MongoDB
from diagrams.onprem.queue import Kafka
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.generic.compute import Rack

OUTPUT = os.path.join(os.path.dirname(__file__), "..", "data", "images", "diagrams_event_driven")

with Diagram("Event-Driven Microservices", filename=OUTPUT, show=False, direction="LR",
             graph_attr={"bgcolor": "white", "pad": "0.5", "dpi": "150"}):
    client = Client("Mobile App")
    gateway = Nginx("API Gateway")

    with Cluster("Message Broker"):
        kafka = Kafka("Kafka")

    with Cluster("Order Service"):
        order_api = FastAPI("Order API")
        order_db = PostgreSQL("Orders DB")

    with Cluster("Inventory Service"):
        inv_api = Rack("Inventory API")
        inv_db = MongoDB("Inventory DB")

    with Cluster("Notification Service"):
        notif_api = Rack("Notification API")

    with Cluster("Observability"):
        prom = Prometheus("Prometheus")
        graf = Grafana("Grafana")

    client >> gateway >> order_api
    order_api >> order_db
    order_api >> Edge(label="order.created") >> kafka
    kafka >> Edge(label="consume") >> inv_api
    kafka >> Edge(label="consume") >> notif_api
    inv_api >> inv_db
    order_api >> Edge(style="dashed") >> prom
    inv_api >> Edge(style="dashed") >> prom
    prom >> graf
