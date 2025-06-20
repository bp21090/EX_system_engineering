import os
import glob

region_dir = 'region'

# region配下の全CSVファイルを再帰的に取得
csv_files = glob.glob(os.path.join(region_dir, '**', '*.csv'), recursive=True)

for file in csv_files:
    try:
        with open(file, 'r', encoding='shift_jis') as f:
            content = f.read()
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'変換完了: {file}')
    except Exception as e:
        print(f'変換失敗: {file} ({e})')