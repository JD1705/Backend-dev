from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# loading environment
load_dotenv()

# getting environment variable
PG_URI = os.getenv('PG_URI')

# stablish connection
engine = create_engine(PG_URI)
