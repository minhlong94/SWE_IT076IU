from typing import Iterable

def _colored_text(r: int, g: int, b: int, text) -> str:
    # Returns colored text to print to stdout.
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def _check_package_installed(package: Iterable[str]):
    import pkg_resources

    required = set(package)
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    return missing
