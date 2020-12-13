import argparse
import os
import subprocess
import sys


def _colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='wms', description='Application with Streamlit.')
    parser.add_argument("action", type=str, nargs='?', help="Run demo app")
    args = parser.parse_args()

    if args.action == "demo":
        dirname = os.path.dirname(__file__)
        os.chdir(dirname)

        import pkg_resources

        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = {'pipenv'} - installed

        if missing:
            prompt = input("Install pipenv (Y/n): ")
            if prompt.upper() == 'Y':
                subprocess.check_call([sys.executable, "m", "pip", "install", "--user", "pipenv"])
                try:
                    subprocess.check_call([sys.executable, "m", "pipenv", "install", "--ignore-pipfile"])
                except subprocess.CalledProcessError:
                    subprocess.check_call([sys.executable, "m", "pipenv", "install"])

        print(f"\n{_colored(0, 128, 0, 'Running demo...')}\n")
        subprocess.run([sys.executable, "-m", "pipenv", "run", "python", "run_demo.py"])

    else:
        print(f"\nNothing happened.\n")
