import polars as pl
from datetime import datetime
from deltalake import DeltaTable
# Displays all columns
pl.Config().set_tbl_cols(-1)

##Read delta using polars
table_path = "src/data/deltalake/product"
df = pl.read_delta(table_path)
print(df)

# print history returns a list of transactions on the table
# turn this into a dataframe using polars
dt = DeltaTable(table_path)
hist = pl.DataFrame(dt.history())
print(hist)

# VACUUM
## Default is 7 days
## By default runs only dry run and returns a list of files that will be deleted 
## pass dry_run=False to actually delete the files
print(dt.vacuum())
# dt.vacuum(dry_run=False)

# ##Optimize 
# dt.optimize.compact()