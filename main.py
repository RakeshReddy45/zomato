import pandas as pd
from sqlalchemy import create_engine

# Database configuration
from sqlalchemy import create_engine

db_username = 'root'
db_password = 'root'
db_host = 'localhost'
db_port = '3306'
db_name = 'zomato_db'

engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')



# Load Country-Code.xls
country_df = pd.read_excel('archive (3)/Country-Code.xlsx')

# Load JSON files
file1_df = pd.read_json('archive (3)/file1.json')
file2_df = pd.read_json('archive (3)/file2.json')
file3_df = pd.read_json('archive (3)/file3.json')
file4_df = pd.read_json('archive (3)/file4.json')
file4_df = pd.read_json('archive (3)/file5.json')

# Combine JSON data
json_df = pd.concat([file1_df, file2_df, file3_df, file4_df])

# Load Zomato.csv
# zomato_df = pd.read_csv('archive (3)/zomato.csv')

import pandas as pd

# Attempt to read with different encodings
try:
    zomato_df = pd.read_csv('archive (3)/zomato.csv', encoding='utf-8')
except UnicodeDecodeError:
    try:
        zomato_df = pd.read_csv('archive (3)/zomato.csv', encoding='latin-1')
    except UnicodeDecodeError:
        zomato_df = pd.read_csv('archive (3)/zomato.csv', encoding='iso-8859-1')

# Now zomato_df should contain your dataframe if read successfully


# Merge country codes with zomato data
zomato_df = zomato_df.merge(country_df, on='Country Code', how='left')

# Save dataframes to the database
zomato_df.to_sql('restaurants', con=engine, if_exists='replace', index=False)
