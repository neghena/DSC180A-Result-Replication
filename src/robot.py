from pymavlink import mavutil

class Robot:
    def __init__(self, url):
        self.url = url
        self.mavcar = mavutil.mavlink_connection(url)
        self.closed = False

    def get_gps(self):
        while not self.closed:
            coords = self.mavcar.location()
            print(coords)

if __name__ == "__main__":
    url = "udp:127.0.0.1:14551"
    robot = Robot(url)
    robot.get_gps()
