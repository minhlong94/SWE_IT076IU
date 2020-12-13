import sys

from streamlit import cli


if __name__ == '__main__':
    from src.demo import app

    filename = app.__file__
    sys.argv = ["streamlit", "run", filename]
    sys.exit(cli.main())
