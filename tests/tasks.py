from django_atomic_celery import task


@task
def returning_task(sentinel):
    return sentinel


@task
def task(*arg, **kwargs):
    pass
