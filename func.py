import subprocess
from subprocess import CompletedProcess


def get_remote_branches(dir_name: str) -> CompletedProcess:
    result: CompletedProcess = subprocess.run(["git", "branch", "-r"], cwd=dir_name, capture_output=True, text=True)
    return result


def set_branch(dir_name: str, branch: str) -> None:
    print(type(branch), branch)
    subprocess.run(["git", "switch", branch], cwd=dir_name, capture_output=True, text=True)
    return None
