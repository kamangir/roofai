# AIRS

Aerial Imagery for Roof Segmentation, from [kaggle](https://www.kaggle.com/datasets/atilol/aerialimageryforroofsegmentation), 457 km2, orthorectified, 220,000 buildings, gsd: 7.5 cm, 19.36 GB, + ground truth.

## Content

For `subset` in `[test, train, val]`,

- `{subset}/image` contains `.tif`s, RGB.
- `{subset}/label` contains `.tif`s and `_vis.tif`, binary, RGB.
- `{subset}.txt`, `test.txt` missing.

more: [AIRS.ipynb](../../../notebooks/dataset/custom/AIRS.ipynb).

## Ingest

```bash
roofai dataset ingest \
    source=AIRS - \
    --test_count 250 \
    --train_count 350 \
    --val_count 100
```

## Review

```bash
roofai dataset review - \
    $ROOFAI_AIRS_CACHE_OBJECT_NAME \
    --index 2
```

![image](https://github.com/kamangir/assets/blob/main/roofAI/AIRS-cache-v45--review-index-2.png?raw=true)

```bash
roofai dataset review - \
    roofAI_ingest_AIRS_2025-01-13-sg1kjj
```

![image](https://github.com/kamangir/assets/blob/main/roofAI/christchurch_1011-00000-02400.png?raw=true)
