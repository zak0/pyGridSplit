from PIL import Image
import sys

def main():
    try:
        image = Image.open(sys.argv[1])
        columnWidth = int(sys.argv[2])
        columnHeight = int(sys.argv[3])
    except:
        print('Arg parse error!')
        return

    outputPrefix = 'output_'
    try:
        outputPrefix = sys.argv[4]
    except:
        print('No custom output file prefix.')

    print('\ncell width: ' + str(columnWidth) + ', height: ' + str(columnHeight))

    width, height = image.size
    imgNo = 0

    for i in range(0, height, columnHeight):
        for j in range(0, width, columnWidth):
            cropBox = (j, i, j + columnWidth, i + columnHeight)
            cell = image.crop(cropBox)
            cell.save('output\\' + outputPrefix + '%03d.png' % imgNo)
            imgNo += 1

if __name__ == '__main__':
    main()
