#!/usr/bin/env python3

import json
from typing import Any

import click

def load_json(path: str) -> dict[Any, Any]:
    """Loads a json file at `path`"""
    with open(path, "r") as fi:
        j = json.load(fi)
    return j


def save_json(path: str, j: dict[Any, Any]) -> None:
    """Writes a json dict to a file at `path`"""
    with open(path, "w") as fi:
        json.dump(j, fi, indent=4)


@click.command()
@click.argument("files", type=click.Path(exists=True, readable=True, writable=True), required=True, nargs=-1)
def prettify_json(files: tuple[str]) -> None:
    for file in files:
        j = load_json(file)
        save_json(file, j)


if __name__ == "__main__":
    prettify_json()
