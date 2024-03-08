# o2pr-dental-panoramic-radiographs-dataset-preprocessing-for-instance-segmentation

If you find it helpful, please consider giving it a star🌟.

We mainly use the "Dataset and code" for the instance segmentation. 

In the original dataset, there are differences in the annotation formats between `test.json` and `train.json`. `test.json` is in the format of `list[list[float]]`, while `train.json` is in the format of `dict`.
The differences in format could be related to the [Detectron2 Standard Dataset Dicts](https://detectron2.readthedocs.io/en/latest/tutorials/datasets.html#standard-dataset-dicts).
>[!NOTE]
>The format of `dict` in `train.json` is the uncompressed RLE.

This repository means to convert the `train.json` uncompressed RLE annotation to a coco polygon annotation format `list[list[float]]` by our `rle_convert_2_polygon.py`.

There may be some issues with the original `train.json` and `test.json` files. The primary concern is that not all images are included in the annotation files.
You can eliminate the images not present in the JSON files using our `remove_imgs_not_in_json.py` script. However, it's alright if you don't need to do that.



- ## 1. Dataset source
These datasets come from the paper ["Children’s dental panoramic radiographs dataset"](https://www.nature.com/articles/s41597-023-02237-5)[1]. They claim that the "dataset and code" are from [2].
You can obtain these datasets from the publication references.
- ## 2. dataset structure
  ```
  |--Dental dataset
      |-- Adult tooth segmentation dataset
          |-- Archive
          |-- Dataset and code
              |-- test
                  |-- annotations
                      |-- test.json
                  |-- images
                  |-- masks
                  |-- masks_supplementary
              |-- train
                  |-- annotations
                        |-- train.json
                  |-- images
                  |-- masks
          |-- Panoramic radiography database
      |-- Children's dental caries segmentation dataset
      |-- Pediatric dental disease detection dataset

  ```

- ## reference
[1] Zhang, Yifan, et al. "Children’s dental panoramic radiographs dataset for caries segmentation and dental disease detection." Scientific Data 10.1 (2023): 380.

[2] Silva, Gil, Luciano Oliveira, and Matheus Pithon. "Automatic segmenting teeth in X-ray images: Trends, a novel data set, benchmarking and future perspectives." Expert Systems with Applications 107 (2018): 15-31.


    
    
