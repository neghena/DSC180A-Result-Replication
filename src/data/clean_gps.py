import pandas as pd 


def clean_gps(**config) -> pd.DataFrame:
    """Clean raw gps data and transform into datafram with columns latitude and 
    longitude.
    """
    df_gps = pd.read_csv(config["gps_raw_data"])
    df_gps.columns = ["lat", "lon", "alt"]
    df_gps.lat = df_gps.lat.str.replace("lat=", "").astype(float)
    df_gps.lon = df_gps.lon.str.replace("lon=", "").astype(float)
    df_gps.alt = df_gps.alt.str.replace("alt=", "").astype(float)

    cleaned_path = config["gps_raw_data"].replace("raw", "temp").replace("log", "csv")
    print(cleaned_path)
    df_gps.to_csv(cleaned_path, index=False)
