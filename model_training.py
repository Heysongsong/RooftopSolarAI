import pandas as pd
import xgboost as xgb
import lightgbm as lgb
from sklearn.model_selection import train_test_split
import config
import logging
from utils import evaluate
from data_preprocessing import load_and_prepare_data

def train_and_predict():
    logging.info("加载并预处理数据...")
    X_scaled, df = load_and_prepare_data()
    X = X_scaled[df["flag"] == 1]
    y = df[df["flag"] == 1]["Rooftop_area"].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1212)

    logging.info("训练XGBoost模型...")
    xgb_model = xgb.XGBRegressor(**config.XGB_PARAMS)
    xgb_model.fit(X_train, y_train)

    logging.info("训练LightGBM模型...")
    lgb_model = lgb.LGBMRegressor(**config.LGB_PARAMS)
    lgb_model.fit(X_train, y_train)

    # 预测融合
    xgb_pred_test = xgb_model.predict(X_test)
    lgb_pred_test = lgb_model.predict(X_test)
    ensemble_pred_test = 0.5 * xgb_pred_test + 0.5 * lgb_pred_test

    xgb_pred_train = xgb_model.predict(X_train)
    lgb_pred_train = lgb_model.predict(X_train)
    ensemble_pred_train = 0.5 * xgb_pred_train + 0.5 * lgb_pred_train

    evaluate(y_train, xgb_pred_train, "XGBoost_train")
    evaluate(y_test, xgb_pred_test, "XGBoost_test")
    evaluate(y_train, lgb_pred_train, "LightGBM_train")
    evaluate(y_test, lgb_pred_test, "LightGBM_test")
    evaluate(y_train, ensemble_pred_train, "Ensemble_train")
    evaluate(y_test, ensemble_pred_test, "Ensemble_test")

    # Inference
    logging.info("进行全量预测...")
    inference_xgb = xgb_model.predict(X_scaled)
    inference_lgb = lgb_model.predict(X_scaled)
    df["inference"] = 0.5 * inference_xgb + 0.5 * inference_lgb
    df.to_csv("ensemble_results.csv", index=False)
    logging.info(f"总预测面积: {df['inference'].sum():.2f} m²")
