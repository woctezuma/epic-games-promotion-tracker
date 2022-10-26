import subprocess

LINE_SEPARATOR = '\n'
ADDITION_PREFIX = '+ '
DELETION_PREFIX = '- '
FIELD_SEPARATOR = '"'


def bytes_to_str(data_as_bytes):
    return data_as_bytes.decode()


def git_diff(file_path):
    output = subprocess.run(["git", "diff", file_path], capture_output=True)
    stdout = bytes_to_str(output.stdout)
    stderr = bytes_to_str(output.stderr)
    return stdout, stderr


def filter_diff(stdout, prefix):
    return [line for line in stdout.split(LINE_SEPARATOR) if line.startswith(prefix)]


def filter_additions(stdout):
    return filter_diff(stdout, ADDITION_PREFIX)


def filter_deletions(stdout):
    return filter_diff(stdout, DELETION_PREFIX)


def extract_games(lines):
    games = []
    for line in lines:
        elements = line.split(FIELD_SEPARATOR)
        if len(elements) > 1:
            game_name = elements[1]
            games.append(game_name)

    return games


def extract_new_games(stdout):
    added_games = extract_games(filter_additions(stdout))
    deleted_games = extract_games(filter_deletions(stdout))
    games = set(added_games).difference(deleted_games)
    return list(games)
