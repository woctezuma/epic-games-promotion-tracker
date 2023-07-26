import os

from src.json_utils import save_json

TARGET_PREFIX = "DISCORD_"
WEBHOOK_FNAME = "data/discord_webhook.json"


def get_environment():
    return os.environ


def filter_dict_by_key(d, target_prefix):
    return {k: v for k, v in d.items() if k.startswith(target_prefix)}


def format_dict_keys(d, target_prefix):
    return {format_key(k, target_prefix): v for k, v in d.items()}


def format_key(k, prefix):
    return k.removeprefix(prefix).lower()


def main():
    environment = filter_dict_by_key(get_environment(), TARGET_PREFIX)
    discord_webhooks = format_dict_keys(environment, TARGET_PREFIX)
    save_json(discord_webhooks, WEBHOOK_FNAME)


if __name__ == "__main__":
    main()
