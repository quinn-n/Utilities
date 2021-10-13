#!/usr/bin/env python3
# Echos the number of times per second a delay will happen - eg. .05 will echo 20.
# Oct. 11 2021 - Moved CLI to click

import click


@click.command()
@click.argument("delay", type=float, required=True)
def counter(delay: float) -> None:
    """Gets the number of times per second a delay will happen - ex. .05 will return 20.
    """
    click.echo(1 / delay)

if __name__ == "__main__":
    counter(None)
