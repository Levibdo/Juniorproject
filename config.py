import os
from dotenv import load_dotenv


if os.path.exists(".env"):
    load_dotenv(".env")

PASSWORD = os.getenv("PASSWORD")
VERSION = "0.1.0"
