from config.celery import app


@app.task(bind=True, ignore_result=True)
def get_task(*args, **kwargs):
    print('Hello!')
