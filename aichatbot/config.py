from email import message
from pathlib import Path
from loguru import logger
import sys
import os

logger.configure(
    handlers=[
        dict(sink=sys.stderr, format="<white>[{time:HH:mm:ss}]</white><level>[{level:^8}]</level> {message}", level="TRACE",colorize=True),
    ],
)

logger.level("TRACE", color="<b><white>")
logger.level("INFO", color="<b><blue>")
logger.level("DEBUG", color="<magenta>")

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

if not os.path.exists(PROCESSED_DATA_DIR):
    os.makedirs(PROCESSED_DATA_DIR)