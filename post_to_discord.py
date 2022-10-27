from src.discord_utils import post_git_diff_to_discord
from src.export_utils import FREE_GAME_FNAME
from src.webhook_utils import DISCORD_FREE_HEADER


def main():
    post_git_diff_to_discord(fname=FREE_GAME_FNAME, header=DISCORD_FREE_HEADER)

    return


if __name__ == '__main__':
    main()
