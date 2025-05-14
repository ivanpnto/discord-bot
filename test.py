from dotenv import load_dotenv
import os

load_dotenv(override=True)

token = os.getenv("TOKEN")
print(f"TOKEN: {token}")
