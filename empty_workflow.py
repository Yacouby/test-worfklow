import mlrun

@kfp.dsl.pipeline(name="remote_pipeline", description="tests remote pipeline")
def pipeline(context):
    context.logger.info("Basic remote workflow executed successfully.")
