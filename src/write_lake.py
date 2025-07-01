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
    ]
)
print(df)
table_path = "src/data/deltalake/product"
##1.31.0 is not working 
df.write_delta(table_path,mode='append')


