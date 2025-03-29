import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Print to check if the keys are being loaded

print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")
print(f"SERPER_API_KEY: {os.getenv('SERPER_API_KEY')}")

# Retrieve API keys

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Validate that keys are available (optional but recommended)

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Add it to your .env file.")

if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY is not set. Add it to your .env file.")

