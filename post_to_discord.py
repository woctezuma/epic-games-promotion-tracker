from src.discord_utils import post_git_diff_to_discord_using_keyword
from src.export_utils import FREE_GAME_FNAME
from src.webhook_utils import WEBHOOK_KEYWORD_FREE


def main():
    post_git_diff_to_discord_using_keyword(fname=FREE_GAME_FNAME, webhook_keyword=WEBHOOK_KEYWORD_FREE)



if __name__ == '__main__':
    main()
