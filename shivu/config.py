class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1843979302"
    sudo_users = "6602548741"
    GROUP_ID = -1002097611828
    TOKEN = "7028939424:AAFDQFZhQ-IXpt7EKQJHXy2qKyINvb-Ua24"
    mongo_url = "mongodb+srv://namanjain123eudhc:opmaster@cluster0.5iokvxo.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "Your_Waifu69bot"
    CHARA_CHANNEL_ID = "-1002087012989"
    api_id = 24431225
    api_hash = "98dfcbe440b3ea4ce62338d424c32412"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
