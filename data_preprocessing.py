import pandas as pd
from utils import max_min_scale
import config

def load_and_prepare_data():
    df = pd.read_csv(config.TRAIN_DATA_PATH)
    drop_cols = ['code', 'flag', 'Lon', 'Lat', 'Rooftop_area',
                 'City', 'Partition', 'Level', 'Bare_ratio',
                 'Dem_average', 'Dem_difference', 'Slope_average',
                 'Snow_ratio', 'Trees_ratio', 'Water_ratio']
    X = df.drop(columns=drop_cols)
    mins = X.min()
    maxs = X.max()
    X_scaled = max_min_scale(X, mins, maxs)
    return X_scaled, df
