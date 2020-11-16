import subprocess

class Robot:
    def __init__(self, **robot_cfg):
        subprocess.run([robot_cfg["command"], robot_cfg["vehicle_type"]])
