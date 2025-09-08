import logging
from pathlib import Path

# check logs/ if exists
Path("logs").mkdir(exist_ok=True)

# configure
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",  # e.g. 2025-07-21 13:45:12 + WARNING + MSG_error
    handlers=[
        logging.FileHandler("logs/app.log"),  # to file
        logging.StreamHandler(),  # print in terminal
    ],
)

logger = logging.getLogger(
    __name__
)  # __name__: if in routes.py, logger is named "api.routes"
# else for math_ops.py, it's "services.math_ops"
