# ssl_tiaozhan
  本代码库为挑战杯项目代码库, 
  
  // TODO: 增加描述
## 项目结构
```
ssl_tiaozhan
├── __init__.py
├── analysis        #  分析文件夹
│   ├── __init__.py
│   ├── _analysis_公路基本情况_.py  
│   └── _analysis_地质灾害风险_.py
├── data            #  数据文件夹
│   ├── 2020公路路线明细表.xls
│   ├── 农村公路汛前洪涝地质灾害风险隐患排查统计表.xls
│   ├── 合计.xls
│   └── 市B-1公路基本情况统计表.xlsx
├── html2pic.py     # html转化为图片
├── pre_analysis.ipynb
├── results        # 结果文件夹
│   ├── all_road_status.html
│   ├── boxplot.html
│   ├── figures
│   ├── fluid_green.html
│   ├── graph_with_edge_options.html
│   └── part_roads_status.html
└── routes.py
```

## 基于
`pyecharts`, `pandas`, `numpy`, `matplotlib`, `statsmodels`, `sklearn`
