# o2pr-dental-panoramic-radiographs-dataset-preprocessing-for-instance-segmentation

If you find it helpful, please consider giving it a star🌟.

We mainly use the "Dataset and code" for the instance segmentation. 

But there are some problems in the `train.json` and `test.json` files. 
The main problem is that not all the images are included in the annotation files. 
So we decide to remove the images that not in the json.
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


    
    
