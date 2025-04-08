# 光伏潜力智能评估系统 🌞

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)

<!-- Chinese Version -->
<details>
<summary><b>中文版 / Chinese Version</b></summary>

## 项目概述
使用机器学习方法预测城市屋顶面积，评估分布式光伏安装潜力。包含：
- 基于XGBoost和LightGBM的集成学习模型
- 结合预测数据的谱聚类区域分析
- 自动化评估流程

## 快速开始
### 环境安装
```bash
git clone git@github.com:Heysongsong/ml-pv-potential.git
conda env create -f environment.yml
```
### 准备数据
```bash
tar -xzvf data.tar.gz
```

### 运行示例
```bash
python main.py
```

## 项目结构
```
├── config.py           # 参数配置
├── main.py             # 主入口
├── data_preprocessing.py # 数据清洗
├── model_training.py   # 模型训练
├── clustering.py       # 聚类分析
├── utils.py            # 工具函数
└── README.md           # 说明文档
```

## 详细说明
### 配置修改
在`config.py`中可调整：
```python
XGB_PARAMS = {
    'n_estimators': 2000,
    'learning_rate': 0.1,
    # ...其他参数
}
```

### 输出结果
程序将生成：
- `ensemble_results.csv`：预测结果
- `spectral_cluster_visual.png`：聚类可视化

</details>

<!-- English Version -->
<details open>
<summary><b>English Version</b></summary>

## Project Overview
A machine learning system for urban rooftop area prediction and distributed photovoltaic potential assessment. Key features:
- Ensemble learning model (XGBoost + LightGBM)
- Spectral clustering with climate data
- Automated evaluation pipeline

## Quick Start
### Installation
```bash
git clone https://github.com/yourusername/rooftop-pv-estimation.git
cd rooftop-pv-estimation
pip install -r requirements.txt
```

### Data Preparation
```bash
tar -xzvf data.tar.gz
```

### Run Demo
```bash
python main.py
```

## Project Structure
```
├── config.py           # Configuration
├── main.py             # Main entry
├── data_preprocessing.py # Data cleaning
├── model_training.py   # Model training
├── clustering.py       # Cluster analysis
├── utils.py            # Utility functions
└── README.md           # Documentation
```


### Configuration
Modify parameters in `config.py`:
```python
XGB_PARAMS = {
    'n_estimators': 2000,
    'learning_rate': 0.1,
    # ...other parameters
}
```

### Output Files
The system will generate:
- `ensemble_results.csv`: Prediction results
- `spectral_cluster_visual.png`: Cluster visualization



## License
[MIT License](LICENSE) © 2023 YourName
```

Key features of this combined version:
1. **Bilingual Toggle**: Uses HTML `<details>` tags to create expandable sections
2. **Consistent Structure**: Maintains identical section ordering in both languages
3. **Shared Elements**: License and badges appear outside language sections
4. **Visual Separation**: Clear headers mark each language version
5. **Default Open**: English version set to open by default (change `open` attribute if needed)

To use this:
1. Copy the entire content
2. Replace placeholders (`yourusername`, year, name)
3. Ensure your `spectral_cluster_visual.png` exists in root directory
4. The expandable sections will work automatically on GitHub
