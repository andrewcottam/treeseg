import open3d as o3d
import numpy as np
import os

# Load the big PCD
pcd = o3d.io.read_point_cloud("/home/andrew/Downloads/Data/tahi/lidar/Tahi_Area2_LiDAR_Full.pcd")
points = np.asarray(pcd.points)

# Parameters
tile_size = 10  # meters
output_dir = "/home/andrew/Downloads/Data/tahi/lidar/pcd_tiles"
os.makedirs(output_dir, exist_ok=True)

# Get bounds
min_x, min_y = points[:, 0].min(), points[:, 1].min()
max_x, max_y = points[:, 0].max(), points[:, 1].max()

tile_id = 0
for x_start in np.arange(min_x, max_x, tile_size):
    for y_start in np.arange(min_y, max_y, tile_size):
        x_end = x_start + tile_size
        y_end = y_start + tile_size

        # Filter points in this tile
        mask = (
            (points[:, 0] >= x_start) & (points[:, 0] < x_end) &
            (points[:, 1] >= y_start) & (points[:, 1] < y_end)
        )
        tile_points = points[mask]

        if len(tile_points) > 0:
            tile_pcd = o3d.geometry.PointCloud()
            tile_pcd.points = o3d.utility.Vector3dVector(tile_points)
            out_path = os.path.join(output_dir, f"tile_{tile_id:04d}.pcd")
            o3d.io.write_point_cloud(out_path, tile_pcd)
            tile_id += 1
