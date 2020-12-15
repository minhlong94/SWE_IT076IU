"""This is a script which is run when the WMS package is executed."""

import click
import streamlit.cli as stcli

from wms.hello import demo


@click.group()
@click.option("--set-password", is_flag=True)
@click.pass_context
def main(ctx, set_password):
    """Try out a demo with:

        $ wms hello
    """
    from wms import encryption

    _need_new_password = demo.create_output_dir()
    if _need_new_password and not set_password:
        if click.confirm("This is the first time you run this demo, do you want to set a new password?"):
            set_password = True
        else:
            click.secho("\nApp will be launched with the default password [python].", fg="green")

    if set_password:
        password = click.prompt("\nPassword", default="python", hide_input=True, confirmation_prompt=True)
        if password == "python":
            if click.confirm("Continue with the default password?", default=True, abort=True):
                pass
        encryption.hash_password(password, encryption_file=demo.ENCRYPTION_KEY)


@main.command("hello")
@click.pass_context
def main_hello(ctx):
    import sys

    filename = demo.__file__
    sys.argv = ["streamlit", "run", filename]
    sys.exit(stcli.main())
