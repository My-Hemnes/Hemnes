# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
import os
import click
from apps.configs.constants import AppsConf


@click.group()
def cli_start():
    pass


@click.command()
@click.option("--pid", required=True, type=str)
def start_pid_file(pid):
    out_path = "/".join([AppsConf.APPS_HOME, "tests/profile.svg"])
    if os.path.exists(out_path):
        os.remove(out_path)
    os.system(f"sudo py-spy record -o {out_path} --pid {pid}")
    # click.echo(f"py-spy record -o {out_path} --pid {pid}")


def main():
    start_pid_file()


if __name__ == '__main__':
    main()
