import asyncio
import time

from base import print_log


async def async_function(sleep_time):
    """An async function."""
    print()
    print_log('>>> Entering async function')
    print_log(f'Sleeping for time: {sleep_time}')
    await asyncio.sleep(sleep_time)
    print_log(f'Slept with time: {sleep_time}')
    print_log('<<< Exiting async function')
    return sleep_time


async def coroutine_main():
    """Runs async tasks with coroutines."""
    print_log('Running async tasks with coroutines')
    coroutine_obj1 = async_function(1)
    coroutine_obj2 = async_function(2)
    print('Tasks created are of the type: ', type(coroutine_obj1))

    result1 = await coroutine_obj1  # Run till completed and not scheduled or queued.
    print('Got the result of task1: ', result1)

    result2 = await coroutine_obj2  # Run till completed and not scheduled or queued.
    print('Got the result of task2: ', result2)
    print_log('Completed running async tasks with coroutines')
    return sum([result1, result2])


async def asyncio_main():
    """Run async tasks with asyncio's create task."""
    print_log('Running async tasks with asyncio"s create task')
    task1 = asyncio.create_task(async_function(2))  # Scheduled
    task2 = asyncio.create_task(async_function(1))  # Scheduled
    print('Tasks created are of the type: ', type(task1))
    print('Task details: \n')
    print(task1)

    result1 = await task1  # Run till completed.
    print('Got the result of task1: ', result1)

    result2 = await task2  # Run till completed.
    print('Got the result of task2: ', result2)
    print_log('Completed running async tasks with asyncio"s create task')
    return sum([result1, result2])


if __name__ == '__main__':
    # Coroutine task run
    print('\n' + '=' * 60)
    print('Started running the Event loop for coroutines')
    print('=' * 60)

    start = time.perf_counter()
    asyncio.run(coroutine_main())
    end = time.perf_counter()

    print('\n' + '=' * 60)
    print(f'Completed running the Event loop for coroutines in {end - start:.2f}(s)')
    print('=' * 60)

    # Create task run
    print('\n' + '=' * 60)
    print('Started running the Event loop for create task')
    print('=' * 60)

    start = time.perf_counter()
    asyncio_main_coroutine = asyncio_main()  # This is a coroutine.
    asyncio.run(asyncio_main_coroutine)
    end = time.perf_counter()

    print('\n' + '=' * 60)
    print(f'Completed running the Event loop for create task in {end - start:.2f}(s)')
    print('=' * 60)
