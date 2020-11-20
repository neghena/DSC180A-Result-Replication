# import pandas as pd 


# def clean_gps(**config) -> pd.DataFrame:
#     """Clean raw gps data and transform into datafram with columns latitude and 
#     longitude.
#     """
#     df_gps = pd.read_csv(config["gps_raw_data"])
#     df_gps.columns = ["lat", "lon", "alt"]
#     df_gps.lat = df_gps.lat.str.replace("lat=", "").astype(float)
#     df_gps.lon = df_gps.lon.str.replace("lon=", "").astype(float)
#     df_gps.alt = df_gps.alt.str.replace("alt=", "").astype(float)

#     cleaned_path = config["gps_raw_data"].replace("raw", "temp").replace("log", "csv")
#     print(cleaned_path)
#     df_gps.to_csv(cleaned_path, index=False)


import pandas as pd 
import glob
import os

#cleans in batches
#assuming our the path to our raw data looks 
#something like this: '../data/raw/first_fix/'

def clean_gps(path):  
    # make a new folder inside temp to hold cleaned data 
    # for each batch
    new_folder = path.split("../data/raw/",1)[1]
    os.mkdir("../data/temp/"+new_folder)
    all_raw_files = glob.glob(path + "/*.log")

    for file in all_raw_files:
        print("Cleaning raw data at", file)
        
        df_gps = pd.read_csv(file, index_col=None, header=None, names=['lat', 'lon', 'alt'])
        df_gps.lat = df_gps.lat.str.replace("lat=", "").astype(float)
        df_gps.lon = df_gps.lon.str.replace("lon=", "").astype(float)
        df_gps.alt = df_gps.alt.str.replace("alt=", "").astype(float)
        
        cleaned_file_path = file.replace(".log", "_cleaned.csv").replace("../data/raw", "../data/temp")
        df_gps.to_csv(cleaned_file_path, index=False)
    print("Cleaned csv for all raw data inside", new_folder, " at ", "../data/temp/"+new_folder)
