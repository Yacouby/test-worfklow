import mlrun
from kfp import dsl

@dsl.pipeline(name="remote_pipeline", description="tests remote pipeline")
def pipeline(context):
    op = dsl.ContainerOp(
        name="print-message",
        image="python:3.9",  # A simple Python image
        command=["echo", "Hello, Kubeflow!"]
    )
