import os.path
import subprocess
import sys
from pathlib import Path

import neatest


def git_push():
    cwd = Path(__file__).parent
    if "* dev" not in subprocess.check_output(["git", "branch"],
                                              cwd=cwd).decode():
        raise ValueError(f"Unexpected current GIT branch.")
    subprocess.check_call(["git", "add", "."], cwd=cwd)
    subprocess.check_call(["git", "commit", "-m",
                           f"Autocommit from {os.path.basename(__file__)}. "
                           f"All tests passed"],
                          cwd=cwd)
    subprocess.check_call(["git", "push"], cwd=cwd)


def run():
    a = sys.argv[1] if len(sys.argv) >= 2 else None

    if a == "lint" or not a:
        print("Running mypy...")
        package_dir_path = 'commie'
        subprocess.check_call([sys.executable, '-m', 'mypy', package_dir_path,
                               '--pretty'])

    if a == "unit" or not a:
        neatest.run(verbosity=neatest.Verbosity.normal,
                    buffer=True)

    if not a:
        git_push()


if __name__ == "__main__":
    run()
