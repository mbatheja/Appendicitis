"""Start the Streamlit front end and the Flask prediction API together."""
import os
import subprocess
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent

subprocess.Popen(["streamlit", "run", "Home.py"], cwd=APP_DIR)

env = os.environ.copy()
env["FLASK_APP"] = "app.py"
subprocess.Popen(["flask", "run"], cwd=APP_DIR, env=env)
