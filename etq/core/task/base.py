from enum import Enum


class TaskState(Enum):
    NEW = 0
    DISPATCHED = 1
    RUNNING = 2
    FINISHED = 3
    FAILED = 4
    WAIT_FOR_RETRY = 5
    HALTED = 6


class Task:

    def __init__(self, task_id: int,  name: str, code_name: str, scheduled_at, state=TaskState.NEW):
        self.task_id = task_id
        self.name = name
        self.code_name = code_name
        self.state = state
        self.scheduled_at = scheduled_at
        self.retry_count = 3


