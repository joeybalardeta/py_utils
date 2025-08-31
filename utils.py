# ==============================================================================
#   utils.property
#
#   General utilities for Python projects.
#
#   Maintained by Joey Balardeta
#
# ==============================================================================



# ==============================================================================
# version
__version__ = "0.1.0"



# ==============================================================================
# imports

# standard imports
import os, sys, socket, json


# local imports



# third-party imports



# ==============================================================================
# standalone functions

# ================================================
# path utilities
def get_parent_dir(path: str) -> str:
    """Get the parent directory of a given path.
    
    Returns:
        str: The absolute path to the parent directory.
    
    Example:
        >>> get_parent_dir("C:/Users/joey/python-project/") = "C:/Users/joey/"
    """
    return os.path.dirname(path)


def get_project_root() -> str:
    """Get the project root directory.

    Uses this module's location to infer the project root reliably instead
    of relying on sys.argv, which can vary depending on how the program is
    launched (e.g., tests, REPL, different entry points).

    Returns:
        str: The absolute path to the project root.
    """
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    )


def get_project_relative_path(path: str) -> str:
    """Get the relative path to the project root.
    
    Returns:
        str: The relative path to the project root.
    
    Example:
        >>> get_project_relative_path("data/") = "data/"
    """
    return os.path.join(get_project_root(), path)


def create_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def build_path(*args: str) -> str:
    full_path = ""
    for i in range(len(args)):
        full_path += args[i].strip("/")

        if i != len(args) - 1:
            full_path += "/"
    
    return full_path



# ================================================
# system (OS) utilities
def get_machine_name() -> str:
    return socket.gethostname()


def get_username() -> str:
    return os.getlogin()


def create_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def delete_dir(path: str) -> None:
    os.removedirs(path)


def delete_file(path: str) -> None:
    os.remove(path)


# ================================================
# JSON utilities
def json_file_to_dict(path: str) -> dict:
    """Load a JSON file into a dictionary with clear error messages.

    Args:
        path: Path to the JSON file.

    Returns:
        dict: Parsed JSON content.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty or contains invalid JSON.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"JSON file not found: {path}")

    if os.path.getsize(path) == 0:
        raise ValueError(f"JSON file is empty: {path}")

    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Invalid JSON in {path}: {exc}"
                ) from exc
    except UnicodeDecodeError:
        raise Exception(
            f"Warning: File '{path}' could not be decoded as UTF-8. "
            "Please ensure the file is UTF-8 encoded."
        )