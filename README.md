# Squirrel Detector 
## Dataset Preparation Steps
We followed advice for how the dataset is structured [here.](https://forums.developer.nvidia.com/t/dusty-nv-jetson-training-custom-data-sets-generating-labels/175008)
1. Annotate images in PASCAL VOC format. In this case, we used [CVAT.ai.](https://github.com/cvat-ai/cvat)
2. After exporting from CVAT, generate test, train, and validation subsets.