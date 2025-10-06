import time
from typing import Any, Iterable, List, Set


class Task:
    """Interface for creating tasks."""

    def __init__(self) -> None:
        self.ready = False
        self.result = None

    def run(self) -> None:
        """Runs the task."""
        raise NotImplementedError


class Sleep(Task):
    """Sleeps for a defined duration."""

    def __init__(self, duration: int) -> None:
        super().__init__()
        self.duration = duration
        self.threshold = time.time() + duration

    def run(self) -> None:
        now = time.time()
        if now > self.threshold:
            self.ready = True
            self.result = True
            print(
                f'Setting results for task:{self.__class__.__name__} with value: {self.duration}'
            )


def wait(tasks: Iterable[Task]) -> List[Any]:
    """Event loop that runs the tasks."""
    print('Running the event loop')
    completed_tasks: List[Task] = []
    pending_tasks: Set[Task] = set(tasks)
    start = time.perf_counter()

    while pending_tasks:
        for task in list(pending_tasks):
            task.run()

            if task.ready:
                pending_tasks.remove(task)
                completed_tasks.append(task)

    end_time = time.perf_counter()
    msg = f'Completed all the tasks in {end_time - start:.2f}(s)'
    print(msg)
    return [completed_task.result for completed_task in completed_tasks]


if __name__ == '__main__':
    task1 = Sleep(1)
    task2 = Sleep(5)
    task3 = Sleep(3)

    result = wait([task1, task2, task3])
    print('Result of the tasks:')
    print(result)
