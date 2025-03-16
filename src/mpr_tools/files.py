"""Tools for file elements"""

from pathlib import Path


def get_extension(filename: Path | str) -> str:
    """returns the file extension"""

    if isinstance(filename, str):
        filename = Path(filename)

    suffixes = filename.suffixes
    if suffixes:
        suffixes[0] = suffixes[0].replace(".", "")
    return "".join(suffixes)
