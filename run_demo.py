import sys

from streamlit import cli

from src.demo import app

if __name__ == '__main__':
    filename = app.__file__
    sys.argv = ["streamlit", "run", filename]
    sys.exit(cli.main())
