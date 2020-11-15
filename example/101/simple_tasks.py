

# define a app
app = App() # load etq_settings in PYTHONPATH

# define a task
@app.task
def simple_task1():
    print('hello, take it easy')

# schedule a task

app.creat_task(Task(name='simple_task', code='simple_task.simple_task'))

# dispatch a task to a the queue
app.dispatch(queue='simple_task_queue')


# run the task (consume the task from queue)
# python bin/worker.py -q simple_task_queue