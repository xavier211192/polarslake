import polars as pl
from datetime import datetime

# Displays all columns
pl.Config().set_tbl_cols(-1)

data = {
    'product_code' : ['0001', '0002', '0003', '0004'],
    'color' : ['red', 'green','blue','yellow'],
    'size': ['small','medium','large','x-large']
}

df = pl.DataFrame(data).with_columns(
    [
        pl.lit(True).alias('is_current'),
        pl.lit(False).alias('is_deleted'),
        pl.lit(datetime(1900,1,1,0,0,0,0)).alias('valid_from'),
        pl.lit(datetime(9999,12,31,0,0,0,0)).alias('valid_to')
    ]
)
print(df)

table_path = "./data/deltalake/product"
# df.write_delta(table_path,mode="append")


