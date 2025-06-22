import os
from dotenv import load_dotenv

env_missing = not os.getenv("API_KEY") or not os.getenv("KAFKA_BOOTSTRAP_SERVERS") or not os.getenv("KAFKA_TOPIC")

# Load from .env file only if required variables are not already set
if env_missing:
    load_dotenv()

# Read values (either from existing env or .env file)
API_KEY = os.getenv("API_KEY", "super-secret-key")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "security-events")
