from sklearn.metrics import mean_absolute_error, r2_score
import logging

def evaluate(y_true, y_pred, name=""):
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    logging.info(f"{name} - MAE: {mae:.4f}, R²: {r2:.4f}")

def max_min_scale(X, mins=None, maxs=None):
    return (X - mins) / (maxs - mins)

