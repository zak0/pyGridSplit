## What is pyGridSplit

It is a python script that I wrote to solve a problem I faced. For a mobile app project I needed to extract image resources from an image file that consisted of a grid of these single images.

## Example usage

python gridsplit.py /path/to/the/grid/image.png 64 64 myPrefix_

in which the arguments are respectively:
- (Mandatory) Path to the image file with the grid
- (Mandatory) Width of a single image within the grid
- (Mandatory) Height of a single image within the grid
- (Optional) Prefix to add to the file name of the split images. Defaults to 'output_'. A running number will be added to the file name of each image.

## Technical stuff

-   Dependencies: PIL

## License

The project is licensed under the terms of **MIT** license. See the LICENSE file for full license.