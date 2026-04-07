import subprocess

def execute_script(script_path: str):
    result = subprocess.run(
        ["python", script_path],
        capture_output=True,
        text=True
    )

    return {
        "return_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    }