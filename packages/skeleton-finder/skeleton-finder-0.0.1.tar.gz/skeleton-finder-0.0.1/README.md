# Skeleton_Finder

## Description
A Napari plugin for skeleton computation on 2D gray-scale images. Currently support:

1. Skeleton finding and drawing
2. A customizable segmentation parameter for thresholding the area of interest
3. A customizable pruning parameter to keep a part of the skeleton
4. Skeleton colored by distance to the boundary
5. Only support single png or jpg images

![example](imgs/horse.png)


## Usage
Install with

```
pip install skeleton-finder
```

Open the plugin widget and select an image layer.

Adjust parameters and find skeleton.

Re-adjusting parameters after computing a skeleton is also supported.

Be sure to use the Reset button after finishing the computation for an image

## License
The plugin is distributed under the terms of [BSD-3](https://opensource.org/licenses/BSD-3-Clause) license.

## Issues
If you encounter any issues, please file an issue along with a detailed description
