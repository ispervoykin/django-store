import os

from dotenv import load_dotenv

load_dotenv(override=True)

HOST = os.environ.get("DB_HOST")
PORT = os.environ.get("DB_PORT")
NAME = os.environ.get("DB_NAME")
USER = os.environ.get("DB_USER")
PASSWORD = os.environ.get("DB_PASS")
