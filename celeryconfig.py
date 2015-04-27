BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'amqp'

CELERY_IMPORTS = ('tasks',)
CELERY_ANNOTATIONS = {'tasks.add':{'rate_limit':'1000/s'}}
