import polars as pl
from datetime import datetime
from deltalake import DeltaTable
# Displays all columns
pl.Config().set_tbl_cols(-1)

table_path = "./data/deltalake/product"
df = pl.read_delta(table_path)
print(df)

dt = DeltaTable(table_path)
hist = pl.DataFrame(dt.history())
print(hist)