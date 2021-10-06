#!/usr/bin/env python
import click

from mylib import hello

@click.command()
@click.option(
    "--name",
    help="What is your name?"
)
def hellocli(name):
    """This prints your name, it is very boring"""

    click.echo(click.style(f"HI! {name}:", fg="red"))

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    hellocli()