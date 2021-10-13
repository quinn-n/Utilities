#!/usr/bin/env python3
# Appends a string to a file a given number of times
# Written by Quinn Neufeld
# Oct. 12 2021 - Rewritten to use click for CLI

import multiprocessing as mp
from io import TextIOBase

import click


def append_worker(file: TextIOBase, s: str, times: int, worker_id: int, n_workers: int) -> None:
    """Worker function to append string to a file object a given number of times

    Args:
        file (TextIOBase): file object to write to
        string (str): string to write to the file object
        times (int): number of times
        worker_id (int): id of the specific worker
        n_workers (int): total number of workers
    """
    for _ in range(worker_id, times, n_workers):
        file.write(s)
    file.close()

@click.command()
@click.argument("path", type=str, required=True)
@click.argument("times", type=int, required=True)
@click.argument("string", type=str, required=True)
def mass_append(path: str, times: int, string: str) -> None:
    """Appends string to path a given number of times
    """
    n_workers = mp.cpu_count()
    workers = []
    fi = open(path, "a")
    for i in range(n_workers):
        workers.append(mp.Process(target=append_worker, args=(fi, string, times, i, n_workers)))
        workers[-1].start()

    [worker.join() for worker in workers]

if __name__ == "__main__":
    mass_append(None, None, None)
