import pandas as pd
from pymavlink import mavutil

class RobotClient:
    def __init__(self, **robot_cfg):
        self.url = robot_cfg["url"]
        self.mavcar = mavutil.mavlink_connection(self.url)
        self.closed = False
        self.gps_log = pd.DataFrame(columns=["lat", "lon"])

    def get_gps(self):
        while not self.closed:
            coords = self.mavcar.location()
            print(coords)

if __name__ == "__main__":
    url = "tcp:127.0.0.1:5760"
    robot = RobotClient(url)
    robot.get_gps()
