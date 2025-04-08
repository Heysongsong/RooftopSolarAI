import logging
from model_training import train_and_predict
from clustering import run_clustering

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("系统启动：光伏潜力智能评估系统")

    train_and_predict()
    run_clustering()

    logging.info("系统运行完毕。")
