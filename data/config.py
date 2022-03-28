from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
URL_RULES = env.str("url_rules")
SLACK_LINK = env.str("slack_link")
API_ZAPIER = env.str("API_ZAPIER")
