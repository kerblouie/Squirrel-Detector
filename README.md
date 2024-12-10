# Squirrel Detector 

 This project uses an object detection network to detect wether a squirrel is present in a given image or video. The project uses a retrained version of ssd-mobilenet. 

![add image descrition here](direct image link here)

## The Algorithm

### Models Used
 This project uses a retrained object detection network. The ssd-mobilenet was retrained using the ipython notebook included in this repository (Train_Object_Detection.ipynb).

### Dataset Preparation Steps
We followed advice for how the dataset is structured [here.](https://forums.developer.nvidia.com/t/dusty-nv-jetson-training-custom-data-sets-generating-labels/175008)
1. Annotate images in PASCAL VOC format. In this case, we used [CVAT.ai.](https://github.com/cvat-ai/cvat)
2. After exporting from CVAT, generate test, train, trainval, and validation subsets using the python script GenerateDatasetFiles.py
3. For the dataset, make sure to start your dataset's labels.txt file with "BACKGROUND" as the first class.

## Running this project

1. Set up the jetson-inference project and its requirements as outlined [here.](https://github.com/dusty-nv/jetson-inference/tree/master)
2. Clone this repository.
3. Run the script using the following command and use --help to view arguments: `python3 squirrelnet.py --help`

[View a video demonstration here.](./squirrel_slideshow_output.mp4)