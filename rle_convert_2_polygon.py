import json
import pycocotools
import numpy as np
import pycocotools.mask
import pycocotools.mask as mask_util
import cv2

def polygonFromMask(maskedArr):
  # adapted from https://github.com/hazirbas/coco-json-converter/blob/master/generate_coco_json.py
  contours, _ = cv2.findContours(maskedArr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  segmentation = []
  valid_poly = 0
  for contour in contours:
  # Valid polygons have >= 6 coordinates (3 points)
     if contour.size >= 6:
        segmentation.append(contour.astype(float).flatten().tolist())
        valid_poly += 1
  if valid_poly == 0:
     return 0
    #  raise ValueError
  return segmentation


json_name = 'O2PR/train/annotations/train.json'

with open(json_name) as json_file:
    labelbox_data = json.load(json_file)

new_json = labelbox_data.copy()
len_anno = len(labelbox_data["annotations"])
print(len_anno)

new_json["annotations"] = []
img_size =[1127,1991] # h w


ann0_id = 0
# image_id = 0
for i in range(len_anno):
# for i in range(3):
    seg = labelbox_data["annotations"][i]["segmentation"]
    compressed_rle = mask_util.frPyObjects(seg, seg.get('size')[0], seg.get('size')[1])
    # compressed_rle['counts'] = compressed_rle['counts'].decode('ascii')
    rle_2_mask = mask_util.decode(compressed_rle) # mask
    # print(rle_2_mask.shape)
    poly_lists_coco = polygonFromMask(rle_2_mask) # polygon lists [[x1,y1,x2,y2,x3,y3,,,],[],[]]

    # new_anno["image_id"] = image_id
    for j in range(len(poly_lists_coco)):
    # for j in range(9):
    #  print(poly_lists_coco[j])
      poly = poly_lists_coco[j]
      com_rle = mask_util.frPyObjects([poly],img_size[0], img_size[1])
      d_mask = mask_util.decode(com_rle) # mask
      poly_lists = polygonFromMask(d_mask)
      if poly_lists ==0:
        continue
      new_anno = {
                  "category_id": 1,
                  "width": 1991,
                  "height": 1127,
                  "iscrowd": 0,
              }
      new_anno["segmentation"] = poly_lists
      area_new = mask_util.area(com_rle)[0]
      # print("area:",area_new)
      new_anno["area"] = int(area_new)
      # print(mask_util.area(com_rle))
      bbox = mask_util.toBbox(com_rle)[0]
      bbox = bbox.astype(int)
      bbox = bbox.tolist()
      print("bbox:",bbox)
      new_anno["bbox"] = bbox
      new_anno["id"] = ann0_id
      image_id = labelbox_data["annotations"][i]["image_id"]
      new_anno["image_id"] = image_id
      new_json["annotations"].append(new_anno)

      ann0_id +=1
      
    # image_id += 1

path_newjson = "rle_convert_2_polygon.json"
with open(path_newjson, 'w') as outfile:
    json.dump(new_json, outfile)
