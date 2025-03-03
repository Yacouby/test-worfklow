import mlrun
from kfp import dsl

@dsl.pipeline(name="remote_pipeline", description="tests remote pipeline")
def pipeline(context):
    project = mlrun.get_or_create_project("proj", "./")
    print("Basic remote workflow executed successfully.")
