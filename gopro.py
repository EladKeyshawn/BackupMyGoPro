# from wifi import Connect 
import subprocess
import os

from goprocam import GoProCamera, constants
from gphotos import GPhotoUploader

# Connect('GP24660185')

# gopro = GoProCamera.GoPro()
# print (gopro)

# media = gopro.downloadAll()

# poweroff gopro 
# switch ssid

# upload to google photos

GPhotoUploader.upload_folder(os.path.abspath('gopro_media'), album='gopro')