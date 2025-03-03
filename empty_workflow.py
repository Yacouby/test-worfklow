import mlrun

@mlrun.handler()
def log_message(context):
    context.logger.info("Basic remote workflow executed successfully.")
