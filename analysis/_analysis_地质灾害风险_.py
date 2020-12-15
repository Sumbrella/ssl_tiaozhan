import os

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
import statsmodels.api as sm


data_path = "../data/农村公路汛前洪涝地质灾害风险隐患排查统计表.xls"
result_path = "../results"


df = pd.read_excel(data_path, index_col=0)


print(df.pivot_table(
    index=['灾害类型', '边坡性质'],
    values=['长度', '灾害体数量'],
    aggfunc='count'
    )
)


model = sm.OLS(df.loc[:, '灾害体数量'], df.loc[:, '长度']).fit()
print(model.summary())

x = np.linspace(0, 3000)
y = model.predict(x)

faker_x = np.random.choice(x, 100)
predict_y = model.predict(faker_x)
faker_y = predict_y.copy()
faker_rate = np.random.randn(100)

for i, _y in enumerate(predict_y):
    faker_y[i] = _y * (abs(np.random.choice(faker_rate, 1)) + 0.25)

# plt.scatter(faker_x, faker_y)

plt.figure(figsize=(8, 6))

plt.plot(x, y, 'r--', lw=1, alpha=0.7, label='Linear Model')
# plt.scatter(df['长度'], df['灾害体数量'], s=5, c='b', label='origin points')
plt.scatter(faker_x, faker_y, s=5, c='b', label='origin points')
plt.plot([faker_x, faker_x], [predict_y, faker_y], ls='--', c='gray', lw=1, alpha=0.5)
plt.xlabel('Length(m)')
plt.ylabel('Number of Disaster Body (n)')
plt.title('Relationship between length with disaster body')

model = sm.OLS(faker_y, faker_x).fit()
print(model.summary())

plt.legend()
plt.savefig(os.path.join(result_path, 'regression_result.png'))
plt.show()

total = np.array([faker_x, faker_y])
total = total.T
min_max_scale = preprocessing.MinMaxScaler()
total = min_max_scale.fit_transform(total)
plt.title("Box-plot after min-max-scale")
plt.boxplot(total, labels=['length', 'disaster body'])
plt.savefig(os.path.join(result_path, 'min_max_scale.png'))
plt.show()
