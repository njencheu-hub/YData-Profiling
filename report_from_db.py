import pandas as pd
from os import getcwd, environ
from dotenv import load_dotenv
from sqlalchemy import create_engine
from ydata_profiling import ProfileReport

# Path to the .env file
env_file_path = getcwd() + "/.env"

# Load environment variables
load_dotenv(dotenv_path=env_file_path)

# Set up a PostgreSQL connection
postgres_host = environ.get('POSTGRES_HOST')
postgres_user = environ.get('POSTGRES_USER')
postgres_password = environ.get('POSTGRES_PASSWORD')
postgres_port = environ.get('POSTGRES_PORT')
postgres_db = environ.get('POSTGRES_DB')

# Setup the URL
postgres_url = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}'

# Create an engine
engine = create_engine(url=postgres_url)

# Setup a connection via SQLAlchemy via .connect()
cursor = engine.connect()

# Read a table related to spotify_streams
df = pd.read_sql_table(table_name='spotify_streams', con=cursor, schema='dea')

df.info()

# Profile Path
profile_path = getcwd() + "/data/profile_reports"

# Generate a profile
profile = ProfileReport(df=df, tsmode=True, explorative=True)

profile.to_file(output_file=f'{profile_path}/spotify_streams_report.html')

cursor.close()