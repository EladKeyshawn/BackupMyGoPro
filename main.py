# from wifi import Connect
import os
from time import sleep
from wireless import Wireless

from goprocam import GoProCamera, constants
from gphotos import GPhotoUploader
from config import Config


def main():
    wireless = Wireless()

    print("Switching to GoPro SSID={}".format(Config.GoPro.SSID))
    wireless.connect(ssid=Config.GoPro.SSID, password=Config.GoPro.SSID_PASS)
    print("Connected to GoPro SSID.")

    sleep(2)  # sleep since it takes time for network connection to establish

    print("Connecting to GoPro...")
    gopro = GoProCamera.GoPro()
    print("GoPro connected.")

    print("Downloading media...")
    media = gopro.downloadAll(
        media_type = Config.MEDIA_TYPE, dest_folder=Config.MEDIA_DEST_FOLDER)
    print("Download complete.")

    if (Config.GoPro.is_power_off_when_done):
        print("Powering off GoPro...")
        gopro.power_off()
        print("GoPro powered off.")

    print("Switching to Home SSID")
    wireless.connect(ssid=Config.HomeNetwork.SSID,
                     password=Config.HomeNetwork.SSID_PASS)
    print("Connected to Home SSID.")

    sleep(2)

    print("Starting upload to Google Photos...")
    GPhotoUploader.upload_folder(os.path.abspath(Config.MEDIA_DEST_FOLDER), album=Config.GooglePhotos.DEST_ALBUM)
    print("Upload to Google Photos complete")


if __name__ == "__main__":
    main()
