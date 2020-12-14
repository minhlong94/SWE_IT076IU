import sys

from streamlit import cli

from wms.demo import demo

filename = demo.__file__
sys.argv = ["streamlit", "run", filename]
sys.exit(cli.main())
