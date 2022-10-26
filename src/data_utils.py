from src.json_utils import load_json_failsafe

DATA_FOLDER = 'data'
STORE_DATA_FNAME = f"{DATA_FOLDER}/store_data.json"
PROMOTION_DATA_FNAME = f"{DATA_FOLDER}/promotion_data.json"
DISCORD_WEBHOOK_FNAME = f'{DATA_FOLDER}/discord_webhook.json'


def load_discord_webhook():
    return load_json_failsafe(f"{DISCORD_WEBHOOK_FNAME}")
