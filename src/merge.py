import polars as pl

table_path = "src/data/deltalake/product"

data = {
    'product_code' : ['0001', '0002', '0003', '0004','0005'],
    'color' : ['red', 'green','blue','yellow','purple'],
    'size': ['small','medium','large','x-large','xxl'],
    'is_current':[False,False,False,False,True]
}

#Updated data all is_current set to false & add new record
df_src = pl.DataFrame(data)
print(df_src)

#Using Polars implementation
## When matched update
## When not matched delete
#https://docs.pola.rs/api/python/dev/reference/api/polars.DataFrame.write_delta.html
# (df_src.write_delta(
#     table_path,
#     mode="merge",
#     delta_merge_options={
#         "source_alias":"s",
#         "target_alias":"t",
#         "predicate":"s.product_code==t.product_code"
#     }
#     )
#     .when_matched_update_all()
#     .when_not_matched_insert_all()
#     .execute()
# )


df = pl.read_delta(table_path)
print(df)