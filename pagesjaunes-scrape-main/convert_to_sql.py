import glob
import argparse
import pandas as pd
import sqlalchemy

## mysql
host = "localhost"
password = "root"
username = "root"

def convert_to_sql(input_file, dbname):
    if not dbname:
        dbname = 'PagesJaunesData'
    if not input_file:
        input_file = 'all'
    
    engine = sqlalchemy.create_engine(f"mysql://{password}:{username}@{host}")
    engine.execute(f"create database if not exists {dbname}")
    engine.dispose()

    conn = sqlalchemy.create_engine(f"mysql://{password}:{username}@{host}/{dbname}?charset=utf8mb4", encoding='utf8')
        

    if input_file.lower() == "all":
        xlsx_files = glob.glob("*.xlsx")
    else:
        xlsx_files = glob.glob(input_file)
    
    xlsx_files.sort()

    excel_list = []
    ## store excel contents to dataframe
    for file in xlsx_files:
        excel_list.append(pd.read_excel(file))
    
    ## dataframe to store merged xlsx
    excel_merged = pd.DataFrame()

    for excel_file in excel_list:
        ## append data to merged dataframe
        excel_merged = excel_merged.append(excel_file, ignore_index=True)
    print("Finished reading input sheets")

    ## write to sql
    excel_merged.to_sql(name="table1", con=conn, chunksize=10000, if_exists='append')

    print("Finished writing sql")
    
if __name__ == "__main__":    
    ## handle cli arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--input', dest='input', type=str, help='name of xlsx sheet to convert')
    argparser.add_argument('--dbname', dest='dbname', type=str, help='name of database file to write to')
    args = argparser.parse_args()

    convert_to_sql(args.input, args.dbname)