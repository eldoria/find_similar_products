import Levenshtein


def add_ean(data_franprix, data_uber_eats):
    if 'ean' not in data_uber_eats:
        data_uber_eats['ean'] = ''
    for label_uber_eats_idx, label_uber_eats_value in enumerate(data_uber_eats['product_name_final']):
        if data_uber_eats['ean'].iloc[label_uber_eats_idx] != '':
            continue
        for label_franprix_idx, label_franprix_value in enumerate(data_franprix['product_name_final']):
            if label_franprix_value == label_uber_eats_value:
                data_uber_eats['ean'].iloc[label_uber_eats_idx] = data_franprix['ean'].iloc[label_franprix_idx]
                break
    data_uber_eats['ean'].astype(int)
    data_uber_eats.to_csv(path_or_buf='data/result/produits_uber_eats_with_ean.csv', sep=';', index=False)


# supporte la distance de Levenshtein
def add_ean_v2(data_franprix, data_uber_eats):
    if 'ean' not in data_uber_eats:
        data_uber_eats['ean'] = ''
    for label_uber_eats_idx, label_uber_eats_value in enumerate(data_uber_eats['product_name_final']):
        if data_uber_eats['ean'].iloc[label_uber_eats_idx] != '':
            continue
        for label_franprix_idx, label_franprix_value in enumerate(data_franprix['product_name_final']):
            if Levenshtein.distance(label_franprix_value, label_uber_eats_value) <= 3:
                data_uber_eats['ean'].iloc[label_uber_eats_idx] = data_franprix['ean'].iloc[label_franprix_idx]
                break
    data_uber_eats['ean'].astype(int)
    data_uber_eats.to_csv(path_or_buf='data/result/produits_uber_eats_with_ean.csv', sep=';', index=False)


# prend le minimum des distances de Levenshtein pour chaque libéllé -> meilleure accuracy mais temps de calcul plus long
def add_ean_v3(data_franprix, data_uber_eats, dist_levenshtein):
    if 'ean' not in data_uber_eats:
        data_uber_eats['ean'] = ''
    for label_uber_eats_idx, label_uber_eats_value in enumerate(data_uber_eats['product_name_final']):
        '''
        if data_uber_eats['ean'].iloc[label_uber_eats_idx] != '':
            continue
        '''
        distance_min = 999999
        for label_franprix_idx, label_franprix_value in enumerate(data_franprix['product_name_final']):
            dist = Levenshtein.distance(label_franprix_value, label_uber_eats_value)
            if dist <= dist_levenshtein and dist < distance_min:
                distance_min = dist
                data_uber_eats['ean'].iloc[label_uber_eats_idx] = data_franprix['ean'].iloc[label_franprix_idx]
                if dist == 0:
                    break
    data_uber_eats.to_csv(path_or_buf=f'data/result/produits_uber_eats_with_ean_dist_lev_{dist_levenshtein}.csv', sep=';', index=False)
