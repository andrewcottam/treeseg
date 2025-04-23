import pdal
import json

# To use:
# python /home/andrew/GitHub/treeseg/tools/las_to_pcd.py
pipeline = [
    {
        "type": "readers.las",
        "filename": "/home/andrew/Downloads/Data/tahi/lidar/Tahi_Area2_LiDAR_Full.las"
    },
    {
        "type": "writers.pcd",
        "filename": "/home/andrew/Downloads/Data/tahi/lidar/Tahi_Area2_LiDAR_Full.pcd"
    }
]

pipeline_json = json.dumps(pipeline)
p = pdal.Pipeline(pipeline_json)
p.execute()
