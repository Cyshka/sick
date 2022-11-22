from mysite.celery import app

@app.task()
def summ(x,y):
    res = x+y
    print(res,'результат сложения')
    return res