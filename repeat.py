#!/usr/bin/env python3

import click


@click.command()
@click.argument("text", type=str, required=True, nargs=-1)
@click.argument("times", type=int, required=True)
def repeat(text: list[str], times: int):
    """Repeatedly echos text to the terminal
    """
    outstr = " ".join(text)
    for _ in range(times):
        click.echo(outstr)
    
if __name__ == "__main__":
    repeat(None, None)
