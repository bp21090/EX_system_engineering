import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib  # これをmatplotlib.pyplotのimport直後に追加

REGION_DIR = 'region'
OUTPUT_DIR = 'output'
# YEARS = ['2018', '2021', '2024']  # 拡張性のため自動取得も可
# region配下のディレクトリから年を自動取得
YEARS = set()
for city in os.listdir(REGION_DIR):
    city_path = os.path.join(REGION_DIR, city)
    if not os.path.isdir(city_path):
        continue
    for fname in os.listdir(city_path):
        if fname.endswith('.csv'):
            # ファイル名例: 2018_atami.csv
            year = fname.split('_')[0]
            YEARS.add(year)
YEARS = sorted(list(YEARS))

# 1. region配下の着都市ディレクトリ一覧
city_dirs = [d for d in glob.glob(os.path.join(REGION_DIR, '*')) if os.path.isdir(d)]
city_names = [os.path.basename(d) for d in city_dirs]

# 2. 2018年miuraの発都市ごとの人数集計
miura_2018 = os.path.join(REGION_DIR, 'miura', '2018_miura.csv')
df_miura = pd.read_csv(miura_2018, encoding='utf-8')
df_miura = df_miura[['市区町村名', '人数']].copy()
df_miura = df_miura.sort_values('人数', ascending=False)
df_miura['累積'] = df_miura['人数'].cumsum()
total = df_miura['人数'].sum()
df_miura['累積比率'] = df_miura['累積'] / total
発都市リスト = df_miura[df_miura['累積比率'] <= 0.9]['市区町村名'].tolist()

# 3. 発都市×着都市×年の人数データ集計
data = []
for 発都市 in 発都市リスト:
    for 着都市 in city_names:
        for year in YEARS:
            csv_path = os.path.join(REGION_DIR, 着都市, f'{year}_{着都市}.csv')
            if not os.path.exists(csv_path):
                continue
            df = pd.read_csv(csv_path, encoding='utf-8')
            row = df[df['市区町村名'] == 発都市]
            if not row.empty:
                n = int(row.iloc[0]['人数'])
            else:
                n = 0
            data.append({'発都市': 発都市, '着都市': 着都市, '年': year, '人数': n})
集計df = pd.DataFrame(data)

# 4. outputディレクトリ作成
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 5. 発都市ごとにグラフ・CSV出力
for 発都市 in 発都市リスト:
    df_pivot = 集計df[集計df['発都市'] == 発都市].pivot(index='年', columns='着都市', values='人数').fillna(0)
    df_pivot.to_csv(os.path.join(OUTPUT_DIR, f'{発都市}_trend.csv'), encoding='utf-8')
    plt.figure(figsize=(8,5))
    for 着都市 in city_names:
        plt.plot(df_pivot.index, df_pivot[着都市], marker='o', label=着都市)
    plt.title(f'{発都市} → 各都市 人数推移')
    plt.xlabel('年')
    plt.ylabel('人数')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f'{発都市}_trend.png'))
    plt.close()

print('完了')
