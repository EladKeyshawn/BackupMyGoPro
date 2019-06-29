# from wifi import Connect 
import subprocess
import os
from time import sleep
from wireless import Wireless
from goprocam import GoProCamera, constants
from gphotos import GPhotoUploader

wireless = Wireless() 

def main():
    print("Switching to GoPro SSID")
    wireless.connect(ssid='GP24660185', password='epic0298')
    print("Connected to GoPro SSID.")
    sleep(2)
    print("Connecting to GoPro...")
    gopro = GoProCamera.GoPro()
    print ("GoPro connected.")

    print("Downloading media...")
    media = gopro.downloadAll(option='photos')
    print("Download complete.")

    print("Powering off GoPro...")
    gopro.power_off()

    # upload to google photos
    print("Switching to Home SSID")
    wireless.connect(ssid='KS', password='00542274052')
    print("Connected to Home SSID.")
    sleep(1)
    print("Starting upload to Google Photos...")
    GPhotoUploader.upload_folder(os.path.abspath('gopro_media'), album='gopro')
    print("Upload to Google Photos complete")

if __name__ == "__main__":
    main()