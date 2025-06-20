import os
import pandas as pd

OUTPUT_DIR = 'output'
TREND_SUFFIX = '_trend.csv'

miura_decrease = []
miura_increase = []
other_increase = []
miura_decrease_data = []
miura_increase_data = []
trend_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(TREND_SUFFIX)]

for fname in trend_files:
    path = os.path.join(OUTPUT_DIR, fname)
    df = pd.read_csv(path, index_col=0)
    発都市 = fname.replace(TREND_SUFFIX, '')
    if 'miura' in df.columns:
        miura_2018 = df.loc[2018, 'miura']
        miura_2024 = df.loc[2024, 'miura']
        if miura_2024 < miura_2018:
            miura_decrease.append(発都市)
            miura_decrease_data.append((発都市, miura_2018, miura_2024, miura_2018 - miura_2024))
            # 他都市で増加しているものを記録
            for col in df.columns:
                if col != 'miura' and df.loc[2024, col] > df.loc[2018, col]:
                    other_increase.append((発都市, col, df.loc[2018, col], df.loc[2024, col]))
        elif miura_2024 > miura_2018:
            miura_increase.append(発都市)
            miura_increase_data.append((発都市, miura_2018, miura_2024, miura_2024 - miura_2018))

print('miuraへの流入が減少している発都市（ランキング・人数）:')
miura_decrease_data_sorted = sorted(miura_decrease_data, key=lambda x: x[3], reverse=True)
for i, (city, n2018, n2024, diff) in enumerate(miura_decrease_data_sorted, 1):
    print(f"{i}. {city}: 2018年={n2018}, 2024年={n2024}, 減少数={diff}")

print('\nmiuraへの流入が増加している発都市（ランキング・人数）:')
miura_increase_data_sorted = sorted(miura_increase_data, key=lambda x: x[3], reverse=True)
for i, (city, n2018, n2024, diff) in enumerate(miura_increase_data_sorted, 1):
    print(f"{i}. {city}: 2018年={n2018}, 2024年={n2024}, 増加数={diff}")

print('\n他都市への流入が増加している発都市と都市名:')
for item in other_increase:
    print(f"{item[0]} → {item[1]}: {item[2]}→{item[3]}")
