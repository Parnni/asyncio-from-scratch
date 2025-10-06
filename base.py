from datetime import datetime


def print_log(message: str):
    """Standardized logging with timestamp."""
    now = datetime.now().strftime('%H:%M:%S.%f')[:-3]
    print(f'[{now}] {message}')
