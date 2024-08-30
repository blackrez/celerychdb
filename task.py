import chdb
from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')


app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'

@app.task
def query():
    print("query start")
    result = chdb.query("SELECT version()")
    print("query end")
    data = result.data()
    print(data)
    return data
