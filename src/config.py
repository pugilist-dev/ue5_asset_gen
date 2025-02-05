from pathlib import Path
import os
import sys

from dotenv import load_dotenv
from loguru import logger
import platform
load_dotenv()

# System configuration

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]

# Local data storage location
if PROJ_ROOT:
    os.makedirs(PROJ_ROOT/"data", exist_ok=True)
    DATA_DIR = PROJ_ROOT / "data"
else:
    logger.error("PROJ_ROOT is not defined")
    sys.exit(1)

# Local repo data storage location
RAW_DATA_DIR = DATA_DIR / "raw"
os.makedirs(RAW_DATA_DIR, exist_ok=True)
INTERIM_DATA_DIR = DATA_DIR / "interim"
os.makedirs(INTERIM_DATA_DIR, exist_ok=True)
PROCESSED_DATA_DIR = DATA_DIR / "processed"
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

# Trained model storage location
MODELS_DIR = PROJ_ROOT / "models"

# Analysis and reports
REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

render_config = {
    'render_mode': 'nerf',
    'size': 64
}