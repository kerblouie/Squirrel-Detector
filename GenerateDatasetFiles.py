import os
import sys
import math
import random

def get_dataset_files(dataset_folder):
    annotations_folder = os.path.join(dataset_folder, "Annotations")
    images_folder = os.path.join(dataset_folder, "JPEGImages")
    if not os.path.isdir(annotations_folder) or not os.path.isdir(images_folder):
        print("ERROR: No images or annotations could be found")
        return[]
    annotation_file_names = []
    image_file_names = []
    for file_name in os.listdir(annotations_folder):
        file_name_noext = os.path.splitext(file_name)[0]
        annotation_file_names.append(file_name_noext)
    for file_name in os.listdir(images_folder):
        file_name_noext = os.path.splitext(file_name)[0]
        image_file_names.append(file_name_noext)
    image_file_names = set(image_file_names)
    annotation_file_names = set(annotation_file_names)
    images_no_annotations = image_file_names.difference(annotation_file_names)
    if len(images_no_annotations) > 0:
        print("WARNING: The images and annotations are not identical. Some images may not have annotations")
        print(list(sorted(images_no_annotations)))
        image_file_names = list(sorted(set(annotation_file_names).intersection(image_file_names)))
    return list(sorted(image_file_names))

def main(test_percent = 10, val_percent = 10):
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} DETECTION_DATASET_FOLDER")
        return
    dataset_folder = sys.argv[1]
    dataset_files = get_dataset_files(dataset_folder)
    test_set_target_length = int(math.ceil(len(dataset_files) * test_percent/100))
    val_set_target_length = int(math.ceil(len(dataset_files) * val_percent/100))
    train_set_target_length =  len(dataset_files) - test_set_target_length - val_set_target_length
    if train_set_target_length <= 0:
        print("ERROR: No training images left for training subset")
        return
    random.shuffle(dataset_files)
    test_set = dataset_files[:test_set_target_length]
    val_set = dataset_files[test_set_target_length:val_set_target_length + test_set_target_length]
    train_set = dataset_files[val_set_target_length + test_set_target_length:]
    if len(test_set) != test_set_target_length:
        print("An error occured with randomly selecting the test set")
        return
    if len(val_set) != val_set_target_length:
        print("An error occured with randomly selecting the validation set")
        return
    if len(train_set) != train_set_target_length:
        print("An error occured with randomly selecting the train set")
        return
    if any(set(test_set).intersection(train_set)) or any(set(test_set).intersection(val_set)):
        print("ERROR: The test set elements are not unique from the train or validation sets")
        return
    if any(set(val_set).intersection(train_set)):
        print("ERROR: The validation set elements are not unique from the train set")
        return
    set_files = {
        "test":test_set,
        "train":train_set,
        "val":val_set,
        "trainval":train_set + val_set
    }
    for file_name, subset in set_files.items():
        with open(os.path.join(dataset_folder, "ImageSets", "Main", f"{file_name}.txt"), "wt") as output_file:
            for dataset_file in sorted(subset):
                output_file.write(f"{dataset_file}\n")


if __name__ == "__main__":
    main()