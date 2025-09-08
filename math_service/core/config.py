import os
from dotenv import load_dotenv

# load variables from .env file if present
load_dotenv()

API_KEY = os.getenv("API_KEY", "this_is_backup")  # fallback default

# ... DB URLs, feature flags, etc.
