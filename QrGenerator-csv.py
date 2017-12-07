
from QrUtils import Create
import os


def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = os.listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]


FileCsvDir='Upload/'
filenames = find_csv_filenames(FileCsvDir)

print ('Start creating qr-image')
for fname in filenames:
	csv=open(FileCsvDir+fname,'r')
	fileDir=fname.split('.')
	imgQrDir='Image/'+fileDir[0]+'/'
	print('Savng on: ' + imgQrDir)
	for line in csv:
		col=line.split(';')
		out=Create(col[0])
		if not os.path.exists(imgQrDir):
			os.makedirs('Image/'+fileDir[0])
		out.save(imgQrDir+col[0]+'.jpg')
print('End')