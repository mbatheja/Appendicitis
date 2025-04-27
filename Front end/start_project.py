import subprocess
import os


frontend_path = r"E:\CMU\HIS\final\Model-main\Model-main\Front end"
frontend_script = "login+form.py"


backend_path = r"E:\CMU\HIS\final\Model-main\Model-main\Front end"
flask_app = "app.py"


subprocess.Popen(["streamlit", "run", os.path.join(frontend_path, frontend_script)], shell=True)

env = os.environ.copy()
env["FLASK_APP"] = flask_app
subprocess.Popen(["flask", "run"], shell=True, cwd=backend_path, env=env)