import pandas as pd
import os



employee_data = {
    ("Alice", "HR", 2019),
    ("Bob", "Engineering", 2020),
    ("Charlie", "Marketing", 2018),
    ("Diana", "Engineering", 2021),
    ("Eva", "HR", 2020)
}

df = pd.DataFrame(employee_data, columns=["Name", "Department", "Year"])

data_dir = os.path.join(os.getcwd(), "data")
os.makedirs(data_dir,exist_ok=True)

data_file = os.path.join(data_dir,'data.csv')

df.to_csv(data_file,index= False)

