import asyncio
import time

from colorama import Fore, Style, init

from base import print_log

init(autoreset=True)


def check_event_loop_is_running(context: str):
    """Checks and logs if the event loop is running with colored output."""
    print_log(f'{context} - Checking if event loop is running...')
    try:
        loop = asyncio.get_event_loop()
        running = loop.is_running()

        status = (
            f"{Fore.GREEN}***RUNNING***" if running else f"{Fore.RED}***NOT RUNNING***"
        )
        print_log(f'{context} - Event loop status: {status}{Style.RESET_ALL}')
        return running
    except RuntimeError:
        status = f"{Fore.RED}***NO LOOP FOUND***"
        print_log(f'{context} - Event loop status: {status}{Style.RESET_ALL}')
        return False


def sync_function() -> None:
    """Synchronous function."""
    print_log('>>> ENTERING sync_function()')
    check_event_loop_is_running('sync_function: BEFORE sleep')
    print_log('Sleeping for 1 second (blocking)...')
    time.sleep(1)
    check_event_loop_is_running('sync_function: AFTER sleep')
    print_log('<<< EXITING sync_function()')


async def async_function() -> None:
    """Asynchronous wrapper that calls a sync function."""
    print_log('>>> ENTERING async_function()')
    check_event_loop_is_running('async_function: BEFORE sync_function')
    print_log('--> Calling sync_function() from async_function()')
    sync_function()
    check_event_loop_is_running('async_function: AFTER sync_function')
    print_log('<<< EXITING async_function()')


async def low_level() -> None:
    """Low-level asyncio function using futures."""
    print_log('>>> ENTERING low_level()')
    check_event_loop_is_running('low_level: BEFORE future')
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    print_log(f'Created empty future: {future}')
    future.set_result('This is the result')
    result = await future
    check_event_loop_is_running('low_level: AFTER future')
    print_log(f'Result of awaited future: {result}')
    print_log('<<< EXITING low_level()')


if __name__ == '__main__':
    print('\n' + '=' * 60)
    print('1️⃣  Running async_function() via asyncio.run()')
    print('=' * 60)
    asyncio.run(async_function())
    print()

    print('=' * 60)
    print('2️⃣  Running sync_function() in standalone mode')
    print('=' * 60)
    check_event_loop_is_running('Main: BEFORE sync_function')
    sync_function()
    check_event_loop_is_running('Main: AFTER sync_function')
    print()

    print('=' * 60)
    print('3️⃣  Running low_level() async function')
    print('=' * 60)
    check_event_loop_is_running('Main: BEFORE low_level')
    asyncio.run(low_level())
    check_event_loop_is_running('Main: AFTER low_level')
    print()
