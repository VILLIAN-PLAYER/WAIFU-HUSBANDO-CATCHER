class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1813373023"
    sudo_users = "1813373023"
    GROUP_ID = -1002103727164
    TOKEN = "6123273453:AAHrLu47bfHTptowxQUtZ3S-DlLurAh3Nc8"
    mongo_url = "mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://graph.org/file/03a06170898b11ed185ef.jpg"]
    SUPPORT_CHAT = "FallenXDeveloper"
    UPDATE_CHAT = "FallenXDeveloper"
    BOT_USERNAME = "NezukaX_ProBot"
    CHARA_CHANNEL_ID = "-1002103727164"
    api_id = 21846639
    api_hash = "2cebc99bd8378b5237b31ea8e7496d79"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
