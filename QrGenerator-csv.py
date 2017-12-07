
from QrUtils import Create
import os


def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = os.listdir(path_to_dir)
    return [ path_to_dir+filename for filename in filenames if filename.endswith( suffix ) ]



filenames = find_csv_filenames('Upload/')

print ('Start creating qr-image')
for fname in filenames:
	csv=open(fname,'r')
	
	for line in csv:
		col=line.split(';')
		out=Create(col[0])
		out.save('Image/'+col[0]+'.jpg')
print('End')