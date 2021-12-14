import glob
import argparse
import pandas as pd
import os

def append_sheet(region):
    if region.lower() == "all":
        xlsx_files = glob.glob("*.xlsx")
    else:
        xlsx_files = glob.glob(f"{region}*.xlsx")

    xlsx_files.sort()
    print(xlsx_files)

    excel_list = []
    ## store excel contents to dataframe
    for file in xlsx_files:
        excel_list.append(pd.read_excel(file))
    
    ## dataframe to store merged xlsx
    excel_merged = pd.DataFrame()

    for excel_file in excel_list:
        ## append data to merged dataframe
        excel_merged = excel_merged.append(excel_file, ignore_index=True)

    merged_folder = "merged_sheets"
    if not os.path.exists(merged_folder):
        os.mkdir(merged_folder)

    merged_file = os.path.join(merged_folder, f"{region}_merged.xlsx")
    ## delete merged file if already exists
    if os.path.exists(merged_file):
        os.remove(merged_file)

    print(f"Writing merged sheet [{merged_file}]")    
    ## export merged dataframe to xls
    excel_merged.to_excel(merged_file, index=False)

if __name__ == "__main__":    
    ## handle cli arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--region', dest='region', type=str, help='region')
    args = argparser.parse_args()

    append_sheet(args.region)

