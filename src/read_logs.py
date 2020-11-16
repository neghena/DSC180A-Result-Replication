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


def filter_coordinates(gps_lst):
    '''
    Filters the coordinates that come out of the read function so that its only x, y, z.

    trying to change this into becoming a csv file not too sure yet though.

    gps_lst should be a list of text gps coordinates
    '''

    #csv_file = [["X", "Y", "Z"]]




    return
