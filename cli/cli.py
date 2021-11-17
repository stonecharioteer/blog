"""rmdir clone to demonstrate how to use Oso inside a command line tool."""
import argparse
from enum import Enum

parser = argparse.ArgumentParser(
        description="Simple rmdir clone command-line-tool to demonstrate Oso's usage.")
parser.add_argument("path", metavar="P", type=str, help="Path to remove")


class PathAttributes(Enum):
    """A bunch of enums to help understand the path attributes"""
    # path isn't a directory
    NOTADIRECTORY = 1
    # path is a writable directory
    WRITABLEDIRECTORY = 2
    # path is a read only directory (current user doesn't have write access)
    READONLYDIRECTORY = 3
    # path does not exist
    NONEXISTENTDIRECTORY = 4


def get_path_attributes(path):
    """Returns a tuple of path attributes"""
    import pathlib
    import os

    path = pathlib.Path(path)
    if not path.exists():
        return PathAttributes.NONEXISTENTDIRECTORY
    elif not path.is_dir():
        return PathAttributes.NOTADIRECTORY
    else:
        # this is a directory. We need to determine whether it's
        # writable, readable or accessible.
        if os.access(path, os.W_OK):
            return PathAttributes.WRITABLEDIRECTORY
        else:
            return PathAttributes.READONLYDIRECTORY


def rmdir(path):
    import shutil
    import getpass
    from oso import Oso
    oso = Oso()
    oso.register_class(PathAttributes)
    oso.load_files(["rmdir.polar"])
    path_attributes = get_path_attributes(path)
    user_id = getpass.getuser()
    if oso.is_allowed(user_id, "can_remove", path_attributes):
        shutil.rmtree(path)
    else:
        raise PermissionError(f"You cannot delete {path}")

if __name__ == "__main__":
    args = parser.parse_args()
    print(f"Attempting to remove directory: {args.path}.")
    rmdir(args.path)
