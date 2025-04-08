# 光伏潜力智能评估系统 🌞

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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
git clone https://github.com/yourusername/rooftop-pv-estimation.git
cd rooftop-pv-estimation
pip install -r requirements.txt
```
### 准备数据
1. 训练数据：`grid_data.csv`（需包含屋顶面积等字段）
2. 聚类数据：`cluster_data.csv`（需包含太阳辐射等字段）

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
### 数据要求
训练数据应包含以下字段（示例）：
```csv
code,flag,Lon,Lat,Rooftop_area,City,...,Dem_average
```

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

## 示例输出
### 模型性能
```
INFO - Ensemble_test - MAE: 11.28, R²: 0.91
```

### 聚类效果
![聚类可视化](./spectral_cluster_visual.png)

## 常见问题
**Q：如何更换自己的数据集？**  
A：保持字段名称一致或修改`data_preprocessing.py`中的列名映射

**Q：如何调整聚类数量？**  
A：修改`clustering.py`中的`n_clusters`参数

## 后续计划
- [ ] 增加Web可视化界面
- [ ] 支持更多聚类算法
- [ ] 添加API接口
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
1. Training data: `grid_data.csv` (should contain rooftop area fields)
2. Clustering data: `cluster_data.csv` (should contain solar radiation fields)

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

## Detailed Instructions
### Data Requirements
Training data should include these fields (example):
```csv
code,flag,Lon,Lat,Rooftop_area,City,...,Dem_average
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

## Sample Output
### Model Performance
```
INFO - Ensemble_test - MAE: 11.28, R²: 0.91
```

### Cluster Visualization
![Cluster Visualization](./spectral_cluster_visual.png)

## FAQ
**Q: How to use custom datasets?**  
A: Either keep the same field names or modify column mapping in `data_preprocessing.py`

**Q: How to adjust cluster count?**  
A: Modify the `n_clusters` parameter in `clustering.py`

## Roadmap
- [ ] Add web visualization interface
- [ ] Support more clustering algorithms
- [ ] Implement API endpoints
</details>

## License 许可
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
