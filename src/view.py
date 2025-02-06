import os
from pathlib import Path
import sys
from glob import glob

#Data loader related imports
from src.config import (
    PROCESSED_DATA_DIR
)

import open3d as o3d

mesh = o3d.io.read_triangle_mesh("/mnt/sdb/experimental/ue5_asset_gen/data/processed/helmet/3D/7.ply")
# Visualize the mesh
o3d.visualization.draw_geometries([mesh])