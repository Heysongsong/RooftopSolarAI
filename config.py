XGB_PARAMS = {
    'n_estimators': 2000,
    'learning_rate': 0.1,
    'max_depth': 10,
    'min_child_weight':10,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'reg_lambda': 300,
    'gamma': 1,
    'random_state': 1212
}

LGB_PARAMS = {
    'n_estimators': 2000,
    'learning_rate': 0.05,
    'max_depth': 10,
    'num_leaves': 64,
    'verbosity': -1,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'reg_lambda': 100,
    'random_state': 1212
}

TRAIN_DATA_PATH = "./grid_data.csv"
CLUSTER_DATA_PATH = "./cluster_data.csv"
