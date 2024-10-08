import redis, os
from flask.cli import load_dotenv
from flask_mail import Mail

load_dotenv()

redis_client = redis.StrictRedis(
    unix_socket_path=os.getenv("REDIS_SOCKET"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
)

mail = Mail()
