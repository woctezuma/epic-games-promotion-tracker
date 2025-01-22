# Epic Games Promotion Tracker

This repository contains Python code to track upcoming promotions on the Epic Games store (EGS).

![Illustration cover][img-cover]

## Disclaimer

> [!Note]
> As of April 26, 2024, the leak is plugged: upcoming promotions (aside from giveaways) cannot be fetched from Epic Games anymore.

## Requirements

-   Install the latest version of [Python 3.X][python-download-url].
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run:
```bash
python fetch_data_for_today.py
```

Alternatively, schedule `update.bat` for daily runs.

## Results

Visit [the website][tracker-website].

## References

- [`woctezuma/egs-15DaysofGames`][egs-15DaysofGames]
- [`woctezuma/epic-games-tracker`][epic-games-tracker]

<!-- Definitions -->

[img-cover]: <https://github.com/woctezuma/epic-games-promotion-tracker/wiki/img/cover.png>
[python-download-url]: <https://www.python.org/downloads/>
[tracker-website]: <https://woctezuma.github.io/epic-games-promotion-tracker/>
[egs-15DaysofGames]: <https://github.com/woctezuma/egs-15DaysofGames>
[epic-games-tracker]: <https://github.com/woctezuma/epic-games-tracker>
