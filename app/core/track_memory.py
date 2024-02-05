import time
import os
import psutil
from loguru import logger


def elapsed_since(start):
    return time.strftime("%H:%M:%S", time.gmtime(time.time() - start))


def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss


def track(func):
    def wrapper(*args, **kwargs):
        mem_before = get_process_memory()
        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = elapsed_since(start)
        mem_after = get_process_memory()
        logger.info("'{name}': pid '{pid}': memory before: '{mem_before}', after: '{mem_after}', consumed: '{"
                    "consumed}'; exec time: '{elapsed_time}'",
                    name=func.__name__,
                    pid=os.getpid(),
                    mem_before=mem_before,
                    mem_after=mem_after,
                    consumed=mem_after - mem_before,
                    elapsed_time=elapsed_time)
        return result

    return wrapper
