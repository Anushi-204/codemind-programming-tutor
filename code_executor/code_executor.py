import subprocess
import tempfile

def run_code(code):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
        f.write(code.encode())
        filename = f.name

    try:
        result = subprocess.run(
            ["python", filename],
            capture_output=True,
            text=True,
            timeout=5
        )

        output = result.stdout + result.stderr

    except Exception as e:
        output = str(e)

    return output