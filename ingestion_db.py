import pandas as pd
import os
from sqlalchemy import create_engine
import logging

logging.basicConfig(
    filename="logs/.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

datapath = r"C:\Users\K Ravi K Aruna\Desktop\project files failed\project 2\data"

def ingest_db(file,engine):
    '''set chunksize and ingest the dataframe into database table'''
    chunksize = 100000
    file_path = os.path.join(datapath,file)
    for chunk in pd.read_csv(file_path,chunksize=chunksize,low_memory=True):
        chunk.to_sql(file[:-4],con=engine,if_exists='append',index=False)
        print(f"inserted {len(chunk)} rows from {file}")

def load_raw_data():
    '''this function will load csv as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir(datapath):
        if file.endswith('.csv'):
            print(f'processing{file}...')
            logging.info(f"ingesting {file} in db")
            ingest_db(file,engine)
    end = time.time()
    total_time = (end=start)/60
    logging.info("-------------------ingestion complete-----------------------")
    logging.info("total time taken: {total_time} minutes")


if __name__ == '__main__':
    load_raw_data()
    