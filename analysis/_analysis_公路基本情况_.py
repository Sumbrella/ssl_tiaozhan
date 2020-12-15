#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar, Graph

# get_ipython().run_line_magic('timeit', '')


# In[2]:

data_dir = os.path.join("..", "data")
result_dir = os.path.join("..", 'results')

# In[3]:


def series2list(s):
    return s.to_list()


# In[4]:


df = pd.read_excel(os.path.join(data_dir, "2020公路路线明细表.xls"))

# In[5]:


df.head()

# In[6]:


df.describe()

# In[7]:


temp_df = df[10:20]
temp_df.head()

# In[8]:


c = Bar()
c.add_xaxis(series2list(temp_df.路线名称))

c.add_yaxis("已绿化", series2list(temp_df.已绿化), stack="stack1", color='gray')

c.add_yaxis("未绿化", series2list(temp_df.可绿化 - temp_df.已绿化), stack="stack1", color='green')

c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

c.set_global_opts(title_opts=opts.TitleOpts(title="绿化情况(部分)"), xaxis_opts=opts.AxisOpts(axislabel_opts={"interval": 0}),
                  legend_opts=opts.LegendOpts(type_='scroll'))

c.render_notebook()

# In[9]:


c = Bar()

c.add_xaxis(series2list(temp_df.路线名称))

c.add_yaxis("沥青混凝土", series2list(temp_df.沥青混凝土), stack="stack1")

c.add_yaxis("水泥混凝土", series2list(temp_df.水泥混凝土), stack="stack1")

c.add_yaxis("简易铺装", series2list(temp_df.简易铺装), stack="stack1")

c.add_yaxis("未铺装", series2list(temp_df.未铺装), stack="stack1")

c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

c.set_global_opts(title_opts=opts.TitleOpts(title="铺装情况(部分)"), xaxis_opts=opts.AxisOpts(axislabel_opts={"interval": 0}))
c.render(os.path.join(result_dir, "part_roads_status.html"))
c.render_notebook()

# In[10]:


c = Bar(opts.InitOpts(width="10000px"))

c.add_xaxis(series2list(df.路线名称))

c.add_yaxis("沥青混凝土", series2list(df.沥青混凝土), stack="stack1")

c.add_yaxis("水泥混凝土", series2list(df.水泥混凝土), stack="stack1")

c.add_yaxis("简易铺装", series2list(df.简易铺装), stack="stack1")

c.add_yaxis("未铺装", series2list(df.未铺装), stack="stack1")

c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

c.set_global_opts(title_opts=opts.TitleOpts(title="铺装情况(全部)"), legend_opts=opts.LegendOpts(type_='scroll'))
c.render(os.path.join(result_dir, "all_road_status.html"))
c.render_notebook()

# In[11]:


box_plot_x = ['里程总计\r\n（公里）', '重复里程\r\n（公里）',
              '断头路\r\n里程\r\n（公里）', '高速', '一级', '二级', '三级', '四级', '准四级', '等外公路',
              '沥青混凝土', '水泥混凝土', '简易铺装', '未铺装', '养护里程', '可绿化', '已绿化', '通车']

# In[12]:


from pyecharts.charts import Boxplot

c = (
    Boxplot(opts.InitOpts(width="1300px"))
        .add_xaxis(box_plot_x)
)
c.add_yaxis("", c.prepare_data(df[box_plot_x].T.values.tolist()), )
# c.set_global_opts(title_opts=opts.TitleOpts(title="分布情况"))
c.set_global_opts(
    title_opts=opts.TitleOpts(title="分布箱子形图"),
    xaxis_opts=opts.AxisOpts(axislabel_opts={"interval": 0}),
    legend_opts=opts.LegendOpts(type_='scroll')
)
c.render(os.path.join(result_dir, "boxplot.html"))
c.render_notebook()

# In[13]:


para_plot_x = ['里程总计\r\n（公里）', '重复里程\r\n（公里）',
               '断头路\r\n里程\r\n（公里）', '沥青混凝土', '水泥混凝土', '简易铺装', '未铺装', '养护里程']

# In[14]:


prepare_dict = [
    {"dim": i, "name": para_plot_x[i]}
    for i in range(len(para_plot_x))
]

# In[15]:


import pyecharts.options as opts
from pyecharts.charts import Parallel

parallel_axis = prepare_dict
new_df = df.head(100)

data = new_df[para_plot_x].values.tolist()

(
    Parallel(init_opts=opts.InitOpts(width="1400px", height="800px"))
        .add_schema(schema=parallel_axis)
        .add(
        series_name="",
        data=data,
        linestyle_opts=opts.LineStyleOpts(width=4, opacity=0.5),
    )
        .set_global_opts(title_opts=opts.TitleOpts("各属性平行坐标图"))
        #     .render(os.path.join(result_dir,"para.html"))
        .render_notebook()
)

# In[16]:


total_df = pd.read_excel(os.path.join(data_dir, "合计.xls"))
radar_cols = ['里程总计', '重复历程', '断头路', '沥青混泥土', '水泥混泥土', '简易铺装', '未铺装', '已绿化', ]
radar_data = total_df[radar_cols].values.tolist()

# In[17]:


total_df

# In[18]:


total_df[radar_cols].describe()

# In[19]:


import pyecharts.options as opts
from pyecharts.charts import Radar

v1 = radar_data[0]
v2 = radar_data[1]
v3 = radar_data[2]
v4 = radar_data[3]
max_list = [int(float(val) * 1.2) + 1 for val in
            "1928.311000	51.931000	1.654000	136.213000	1270.456000	229.142000	292.500	260.688000".split()]
(
    Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC"))
        .add_schema(
        schema=[
            opts.RadarIndicatorItem(name=radar_cols[0], max_=max_list[0]),
            opts.RadarIndicatorItem(name=radar_cols[1], max_=max_list[1]),
            opts.RadarIndicatorItem(name=radar_cols[2], max_=max_list[2]),
            opts.RadarIndicatorItem(name=radar_cols[3], max_=max_list[3]),
            opts.RadarIndicatorItem(name=radar_cols[4], max_=max_list[4]),
            opts.RadarIndicatorItem(name=radar_cols[5], max_=max_list[5]),
            opts.RadarIndicatorItem(name=radar_cols[6], max_=max_list[6]),
            opts.RadarIndicatorItem(name=radar_cols[7], max_=max_list[7]),
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="#fff"),
    )
        .add(
        series_name="省道合计",
        data=[v1],
        linestyle_opts=opts.LineStyleOpts(color="#CD0000"),
    )
        .add(
        series_name="县道合计",
        data=[v2],
        linestyle_opts=opts.LineStyleOpts(color="#5CACEE"),
    )
        .add(
        series_name="乡道合计",
        data=[v3],
        linestyle_opts=opts.LineStyleOpts(color="yellow"),
    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        title_opts=opts.TitleOpts(title="基础雷达图"), legend_opts=opts.LegendOpts()
    )
        .render_notebook()
    #     .render("os.path.join(result_dir, radar.html"))
)


# In[21]:


all_places = set(df.起点地名.unique().tolist())
all_places = all_places.union(set(df.迄点地名.unique().tolist()))

# In[22]:


ndf = df.pivot_table(index=['起点地名', '迄点地名'], values=['里程总计\r\n（公里）'])

nodes = [{"name": place, "symbolSize": np.random.randint(10, 20)} for place in all_places]
links = []

for i, (start, end) in enumerate(ndf.index):
    links.append(
        {'source': start, 'target': end, 'value': ndf.values[i].tolist()[0]}
    )
c = (
    Graph()
        .add(
        "",
        nodes,
        links,
        repulsion=4000,
        edge_label=opts.LabelOpts(
            is_show=True, position="middle", formatter="{c}"
        ),
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Graph-GraphNode-GraphLink-WithEdgeLabel")
    )
        .render(os.path.join(result_dir, "graph_with_edge_options.html"))
)

# In[23]:

total_df['已绿化'] / total_df['可绿化']

# In[24]:


from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode

l1 = (
    Liquid()
        .add("lq", [0.4943], center=["50%", "50%"], color=['green'], is_outline_show=True,
             outline_itemstyle_opts=opts.ItemStyleOpts(border_color='white'),
             label_opts=opts.LabelOpts(
                 font_size=50,
                 formatter=JsCode(
                     """function (param) {
                             return (Math.floor(param.value * 10000) / 100) + '%';
                         }"""
                 ),
                 position="inside",
                 color='green'
             ), )
        .set_global_opts(title_opts=opts.TitleOpts(title="绿化程度"))
)

l2 = Liquid().add(
    "lq",
    [0.6229],
    color=['green'],
    center=["20%", "50%"],
    outline_itemstyle_opts=opts.ItemStyleOpts(border_color='white'),
    label_opts=opts.LabelOpts(
        font_size=50,
        formatter=JsCode(
            """function (param) {
                    return (Math.floor(param.value * 10000) / 100) + '%';
                }"""
        ),
        position="inside",
        color='green'
    ),
)
l3 = Liquid().add(
    "乡",
    [0.3885],
    outline_itemstyle_opts=opts.ItemStyleOpts(border_color='white'),
    color=['green'],
    center=["80%", "50%"],
    label_opts=opts.LabelOpts(
        font_size=50,
        formatter=JsCode(
            """function (param) {
                    return (Math.floor(param.value * 10000) / 100) + '%';
                }"""
        ),
        position="inside",
        color='green'
    ),
)

grid = Grid().add(l1, grid_opts=opts.GridOpts()).add(l2, grid_opts=opts.GridOpts()).add(l3, grid_opts=opts.GridOpts())
grid.render(os.path.join(result_dir, "fluid_green.html"))
grid.render_notebook()

# In[25]:


import random

from pyecharts import options as opts
from pyecharts.charts import HeatMap
from pyecharts.faker import Faker

value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
c = (
    HeatMap()
        .add_xaxis(Faker.clock)
        .add_yaxis("series0", Faker.week, value)
        .set_global_opts(
        title_opts=opts.TitleOpts(title="HeatMap-基本示例"),
        visualmap_opts=opts.VisualMapOpts(),
    )
        .render_notebook()
    #     .render(os.path.join(result_dir,"heatmap_base.html"))
)

# In[26]:


df.columns
heat_columns = ['里程总计\r\n（公里）', '重复里程\r\n（公里）',
                '断头路\r\n里程\r\n（公里）', '沥青混凝土', '水泥混凝土', '简易铺装', '未铺装', '养护里程', '可绿化', '已绿化', '通车']

# In[27]:


from pyecharts import options as opts
from pyecharts.charts import HeatMap

from sklearn import preprocessing

value = df[heat_columns].values.tolist()

min_max_scale = preprocessing.MinMaxScaler()

value = min_max_scale.fit_transform(value)

value = [[i, j, value[i][j] * 100] for i in range(len(value)) for j in range(len(heat_columns))]
c = (
    HeatMap(opts.InitOpts(width="2000px"))
        .add_xaxis(df.路线名称.values.tolist())
        .add_yaxis("", heat_columns, value)
        .set_global_opts(
        title_opts=opts.TitleOpts(title="HeatMap"),
        visualmap_opts=opts.VisualMapOpts(
            orient="vertial",
            pos_right='right',
            pos_top='middle'
        ),
        yaxis_opts=opts.AxisOpts(axislabel_opts={"interval": 0}))
        .render_notebook()
    #     .render(os.path.join(result_dir, "heatmap_base.html"))
)

# In[28]:

from html2pic import main
main()

main()



