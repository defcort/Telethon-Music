import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5603046691:AAE9o99TJ8pqHJS6UuN3UNr62MkyprBLsE4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIMBu2m3fUI3hXRDkASNU-eGRQumZ4zsRJNk4WYBiYViGXj19WDcZl2RsH-PP1vabmAIsw4RB92xV0tdf2yT9GhsnjWEFKIHTqtrAk7SUPILi6lQRz2cOQQOXU2rEkx4y_6YZg7fFc8jxHUcp1LIvsLGEzL46ZJ4ar5h_AjnVXrL7hqtDlDu-NC7J5-QziqylhQ0m2n_6yllWkihPJlMeIW_2XZbsI2NnionoafPAG4XZI8RM_QgHm2lZ7W0WpsYvqYYcvCRPxYfGF-Fp7WQNWPjXf3GhJOCbg4bPVDRgUkun2XVb4uqhmWNueFa2VMHnNn1BZMtu5aDV1eTAPclWhmgdp8=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Defcort_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5643012018")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
