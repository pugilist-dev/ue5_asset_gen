import os
from pathlib import Path
import sys
from glob import glob

#Data loader related imports
from src.config import (
    RAW_DATA_DIR, render_config
)
from src.inference import Inference

if __name__ == "__main__":
    # read data from raw data 
    raw_txt_file = os.path.join(RAW_DATA_DIR, "prompts.txt")
    infer = Inference(device="cuda")

    if os.path.exists(raw_txt_file):
        with open(raw_txt_file, "r") as file:
            for line in file:
                prompt = line.strip()
                if prompt:
                    print(f"Generating the asset for: {prompt}")
                    infer.inference(prompt, render_config=render_config)
                    