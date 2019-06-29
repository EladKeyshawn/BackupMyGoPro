class Config:
    MEDIA_DEST_FOLDER = "media"
    MEDIA_TYPE = 'photos'  # photos / videos / *

    class GoPro:
        SSID = "GP24660185"
        SSID_PASS = ""
        is_power_off_when_done=False

    class GooglePhotos:
        DEST_ALBUM = "gopro"
        CREDENTIALS_PATH = "gphoto_credentials.json"

    class HomeNetwork:
        SSID = "KS"
        SSID_PASS = ""
