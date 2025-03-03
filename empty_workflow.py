import mlrun
from kfp import dsl

@dsl.pipeline(name="remote_pipeline", description="tests remote pipeline")
def pipeline(context):
    print("Basic remote workflow executed successfully.")
