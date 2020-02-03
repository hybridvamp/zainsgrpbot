from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 868272198  # my telegram ID
    OWNER_USERNAME = "Zain_stech"  # my telegram username
    API_KEY = "1031307220:AAF7a5KHlKKEh2SRpfKD1EgNDNMO7xk5d2k"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://mbsjayagpjvepk:b154b95a66f2db7509892c463837cce657b40818f9b0ec29c9a23a6a93640aa5@ec2-35-175-170-131.compute-1.amazonaws.com:5432/dr3hs06mcn9g8'  # sample db credentials
    MESSAGE_DUMP = '-385841987' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [868272198]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
