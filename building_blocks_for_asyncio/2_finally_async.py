import time
from typing import Any, Dict, Generator, Iterable, List


def async_await(tasks: Iterable[Generator]) -> List[Any]:
    pending_tasks = set(tasks)
    saved_task_results: Dict[Generator, Any] = {task: None for task in pending_tasks}

    print('\n' + "=" * 60)
    print('Starting the event loop')
    start = time.perf_counter()
    while pending_tasks:
        for pending_task in list(pending_tasks):
            try:
                print(f'***Running task: {pending_task.__name__}***')
                curr_result = pending_task.send(saved_task_results[pending_task])
                saved_task_results[pending_task] = curr_result
                print(
                    f'Current result of task: {pending_task.__name__} is {curr_result}'
                )
                print()
            except StopIteration as e:
                saved_task_results[pending_task] = e.args[0]
                pending_tasks.remove(pending_task)
                print(f'Stopped iteration for task: {pending_task}')
                print()
    print('Completed running the event loop')
    print('\n' + "=" * 60)
    end = time.perf_counter()
    print(f'Total time taken to run all the tasks: {end - start:.2f}(s)')
    print('\n' + "=" * 60)
    return list(saved_task_results.values())


def sleep(duration: float):
    print('>>> Entering sleep')
    now = time.time()
    threshold = now + duration
    print('Now time is: ', now)
    print('Set threshold is: ', threshold)
    while now < threshold:
        print('Now is less than threshold, so just yielding from sleep')
        yield
        print('Yielded from sleep')
        now = time.time()
        print('Updating now in sleep after yield')
    print('>>> Exiting sleep')


def bar():
    print('>>> Entering bar task')
    print('Yielding sleep() from bar')
    yield from sleep(0.01)
    print('Yielded sleep from bar')
    print('>>> Exiting from bar')
    return 123


def foo():
    print('>>> Entering foo task')
    print('Yielding bar() from foo')
    value = yield from bar()
    print('Yielded bar from foo with value: ', value)
    print(f'Returning value of: {value} from foo')
    print('>>> Exiting foo task')
    return value


if __name__ == '__main__':
    tasks = [foo(), foo()]
    results = async_await(tasks)
