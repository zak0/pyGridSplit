## What is pyGridSplit

It is a python script that I wrote to solve a problem I faced. For a mobile app project I needed to extract image resources from an image file that consisted of a grid of these single images.

## Usage

1. Create a folder `output` in the working directory.
2. Run the script:

```
python gridsplit.py [input grid] [cell width] [cell height] [output file prefix] [first index] [last index] [filename numbering start]
```

in which the arguments are respectively:
- (Mandatory) Path to the image file with the grid
- (Mandatory) Width of a single image within the grid
- (Mandatory) Height of a single image within the grid
- (Optional) Prefix to add to the file name of the split images. Defaults to 'output_'. A running number will be added to the file name of each image.
- (Optional) First index of cell from grid to output. Cells before this are ignored. Indices go from left-to-right, top-to-bottom.
- (Optional) Last index of cell from grid to output. Cells after this are ignored.
- (Optional) First number to start the output file name numbering with. Useful if to prevent overriding earlier output files when you want to use the same prefix.

Example:
```
python gridsplit.py /path/to/the/grid/image.png 64 64 myPrefix_ 0 15
```

## Technical stuff

-   Dependencies: PIL (`pip install pillow`)

## License

The project is licensed under the terms of **MIT** license. See the LICENSE file for full license.