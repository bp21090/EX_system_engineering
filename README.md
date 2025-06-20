# EX_system_engineering ディレクトリ構成（2025/06/20時点）

```
EX_system_engineering/
├── region/                # 各都市ごとの人流データ（CSV）を格納
│   ├── atami/
│   │   ├── 2018_atami.csv
│   │   ├── 2021_atami.csv
│   │   └── 2024_atami.csv
│   ├── enoshima/
│   │   ├── 2018_enoshima.csv
│   │   ├── 2021_enoshima.csv
│   │   └── 2024_enoshima.csv
│   ├── hakone/
│   │   ├── 2018_hakone.csv
│   │   ├── 2021_hakone.csv
│   │   └── 2024_hakone.csv
│   ├── kamakura/
│   │   ├── 2018_kamakura.csv
│   │   ├── 2021_kamakura.csv
│   │   └── 2024_kamakura.csv
│   ├── miura/
│   │   ├── 2018_miura.csv
│   │   ├── 2021_miura.csv
│   │   └── 2024_miura.csv
│   └── yokosuka/
│       ├── 2018_yokosuka.csv
│       ├── 2021_yokosuka.csv
│       └── 2024_yokosuka.csv
│
├── output/                # 集計・分析結果の出力先
│   ├── {発都市}_trend.csv   # 発都市ごとの年×着都市の人数推移データ
│   ├── {発都市}_trend.png   # 発都市ごとの人数推移グラフ
│   └── ...
│
├── analysis_script.py     # 人流データ集計・可視化スクリプト
├── analyze_trends.py      # output内の傾向分析スクリプト
├── convert_to_utf8.py     # CSVの文字コード変換スクリプト
└── README.md              # このファイル
```

## 補足
- region/配下のディレクトリ・ファイルは都市や年が増減しても自動対応できる設計です。
- output/配下には自動生成された集計CSV・グラフ画像が格納されます。
- analysis_script.py：region/配下のデータを集計・グラフ化
- analyze_trends.py：output/配下の集計結果から傾向を抽出
- convert_to_utf8.py：CSVの文字コード（Shift_JIS→UTF-8）変換
