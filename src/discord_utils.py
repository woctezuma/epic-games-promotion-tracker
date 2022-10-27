import requests

from src.data_utils import load_discord_webhook
from src.git_utils import git_diff, extract_new_games

BULLET_POINT_SEPARATOR = f"\n- "


def get_webhook_id(webhook_keyword='id'):
    webhook = load_discord_webhook()
    try:
        webhook_id = webhook[webhook_keyword]
    except KeyError:
        webhook_id = None
    return webhook_id


def get_webhook_url(webhook_id):
    return f"https://discord.com/api/webhooks/{webhook_id}"


def post_message_to_discord(message, webhook_id):
    if webhook_id is None or len(message) == 0:
        response = None
    else:
        discord_url = get_webhook_url(webhook_id)
        json_data = {"content": message}
        response = requests.post(url=discord_url, json=json_data)

    return response


def format_discord_message(games, header=""):
    if len(games) > 0:
        lines = [header] + sorted(games)
        message = BULLET_POINT_SEPARATOR.join(lines)
    else:
        message = ''
    return message


def post_git_diff_to_discord(fname, header, webhook_id=None):
    if webhook_id is None:
        webhook_id = get_webhook_id()

    stdout, stderr = git_diff(fname)
    games = extract_new_games(stdout)

    message = format_discord_message(games, header=header)
    response = post_message_to_discord(message, webhook_id)

    return response
