import os

import pandas as pd


def sort_files(path):
    tab_files = os.listdir(path)
    result = [''] * len(tab_files)
    for file in tab_files:
        idx = int(file.split('_')[-1].split('.')[0])
        result[idx] = file
    return result


name_files = sort_files('data/result')

first_df = True
df_merged = pd.DataFrame

for idx, name_file in enumerate(name_files):
    path_file = 'data/result/' + name_file
    globals()[f'df_{idx}'] = pd.read_csv(path_file, sep=';').dropna(subset=['ean'])
    if first_df:
        first_df = False
        # print(globals()[f'df_{idx}'])# .merge(df_franprix, how='inner', on='ean'))
        df_merged = globals()[f'df_{idx}']
    else:
        globals()[f'df_{idx}'] = df_merged.merge(globals()[f'df_{idx}'], how='outer', indicator=True)
        globals()[f'df_{idx}'] = globals()[f'df_{idx}'].loc[lambda x: x['_merge'] == 'right_only'].drop('_merge', axis=1)
        df_merged = df_merged.merge(globals()[f'df_{idx}'], how='outer')

df_franprix = pd.read_csv('data/cleaned/produits_franprix_cleaned.csv', sep=';', usecols=['ean', 'product_name_final'])

for idx, _ in enumerate(name_files):
    globals()[f'df_{idx}'] = globals()[f'df_{idx}'].merge(df_franprix, how='inner', on='ean').\
        rename(columns={'product_name_final_x': 'libelle_uber_eats', 'product_name_final_y': 'libelle_franprix'})\
        .drop_duplicates(subset=['ean'])
    globals()[f'df_{idx}']['ean'] = globals()[f'df_{idx}']['ean'].astype(int)
    globals()[f'df_{idx}'][['ean', 'libelle_uber_eats', 'libelle_franprix']].\
        to_csv(path_or_buf=f'data/visualise/visualise_lev_distance_{idx}.csv', sep=';', index=False)
