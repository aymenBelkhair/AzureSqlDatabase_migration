from app.db import engine
import pandas as pd


# Chunked loading
chunk_size = 10000  
csv_file = "path to the csv files" # you can use os.listdir to list all of them thrn create a for loop on them
table_name = "Name"

total_inserted = 0
for chunk in pd.read_csv(csv_file, chunksize=chunk_size,dtype=str):
    chunk.to_sql(table_name, engine, if_exists='append', index=False)
    total_inserted += len(chunk)
    print(f"✅ Inserted {total_inserted} rows so far...")

print("✅ All data uploaded.")