"""
In the previous module `0_getting_a_feel_of_async` we saw that
- One thread is required to run all the tasks.
- If you increase the number of tasks, the total time of execution will be closer to
the task with highest execution time.

Issues with our crude async code:
- Each task has to keep track of its progress. i.e result, ready, etc.
- Each task always start from the beginning.

What we can do?
- What if there is something that can start from where it was left?
    THE GENERATORS!!!
- Once it is exhausted or completed, the send will have no effect even if you satisfy a
condition inside it.
- Before exhausting, you can move the condition back-and-forth,
see `generators_with_send`
"""

from typing import Any, Dict, Generator, Iterable, List, Literal


def normal_generators() -> Generator[int, Any, None]:
    """A normal generator which generates data from 1 to 5."""
    start = 1
    end = 6

    while start < end:
        yield start  # Yields the value
        # After performing next, the next line of code runs and the loop repeats until
        # hitting yield again.
        start += 1


def generators_with_send() -> Generator[int, Any, None]:
    """A generator which accepts start values from outside."""
    start = 1
    end = 6

    while start < end:
        temp_start = start
        print(f'Yielding {start} from send generator')
        start = yield start  # Yields the value
        # After performing next, the next line of code runs and the loop repeats until
        # hitting yield again.
        msg = f'Received value for start: {start} from outside but inside it is {temp_start}!!!'
        print(msg)
        start += 1


def counter() -> Generator[Any | Literal[0], Any, None]:
    """Congratulations!!! You just invented COROUTINE!!!"""
    start = 0
    limit = 5
    value_start = start

    while value_start < limit:
        # Expects `.send` method to be called after each yield.
        value_start += yield value_start
    yield value_start




def mock_api():
    print('Making request')
    
    
if __name__ == '__main__':
    print('\n' + '=' * 60)
    print('Normal generator')
    print('=' * 60)
    gen = normal_generators()
    for value in gen:
        print('Generated: ', value)

    print('\n' + '=' * 60)
    print('Send generator')
    print('=' * 60)
    send_gen = generators_with_send()
    value = next(send_gen)
    print('Generated: ', value)

    try:
        print('Sending start value of 4 \n')
        send_gen.send(4)

        print('Sending start value of 1 \n')
        send_gen.send(1)

        print('Sending start value of 5 \n')
        send_gen.send(5)

        print('Sending start value of 10 \n')
        send_gen.send(10)

        print('Sending start value of 1 \n')
        send_gen.send(1)
    except StopIteration:
        print('Exhausted the send generator!')
