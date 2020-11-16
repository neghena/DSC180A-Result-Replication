def read(x):
    '''
    Reads the log file and filters out just the GPS coordinates from the log

    x should be the path to a singular log file
    returns a list of all logs that have the word GPS_POS in them
    '''
    with open(x) as f:
        f = f.readlines()

    gps_coords = []

    for line in f:
        if 'GPS_POS' in line:
            gps_coords.append(line)

    return gps_coords
