from PIL import Image
import sys

def main():
    try:
        image = Image.open(sys.argv[1])
        columnWidth = int(sys.argv[2])
        columnHeight = int(sys.argv[3])
    except:
        print('Missing input [source image], or [column width] or [column height]!')
        return

    outputPrefix = 'output_'
    try:
        outputPrefix = sys.argv[4]
    except:
        print('No custom output file prefix. Using default prefix.')

    print('\ncell width: ' + str(columnWidth) + ', height: ' + str(columnHeight))

    width, height = image.size

    rowsCount = int(height / columnHeight)
    columnsCount = int(width / columnWidth)

    print('Input grid is ' + str(rowsCount) + ' x ' + str(columnsCount))

    startIndex = 0
    try:
        startIndex = int(sys.argv[5])
    except:
        print('No custom start index given. Starting at position 0.')
    
    endIndex = rowsCount * columnsCount
    try:
        endIndex = int(sys.argv[6])
    except:
        print('No custom end index given. Outputting entire grid of ' + str(rowsCount * columnsCount) + ' cells.')

    imgNo = 0
    try:
        imgNo = int(sys.argv[7])
    except:
        print('No custom image number given. Starting from 0.')

    row = 0
    for i in range(0, height, columnHeight):
        column = 0
        for j in range(0, width, columnWidth):
            cellIndex = row * columnsCount + column
            if cellIndex >= startIndex and cellIndex <= endIndex:
                cropBox = (j, i, j + columnWidth, i + columnHeight)
                cell = image.crop(cropBox)
                cell.save('output/' + outputPrefix + '%03d.png' % imgNo)
                imgNo += 1
            column +=1
        row += 1

if __name__ == '__main__':
    main()
