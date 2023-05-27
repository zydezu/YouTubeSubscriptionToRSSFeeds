# YouTube Subscriptions to RSS Feeds
This python scripts converts a `subscriptions.csv` Google Takeout file, to a list of valid RSS feeds for the associated YouTube subscriptions.

# Usage

Go to the [YouTube section of Google Takeout](https://takeout.google.com/settings/takeout/custom/youtube).

Press the `All YouTube data included` button and deselect all, then select `subscriptions`

Click `next step`, select your desired destination and click `Create Export`

![Selecting subscriptions only in the data options and exporting the takeout](youtubetakeout.gif)

Download the `takeout.zip` file and locate `subscriptions.csv`, it should be in `Takeout\YouTube and YouTube Music\subscriptions`

Open the `convertsubscriptionstorssfeeds.py` program, and open the `subscriptions.csv` file when prompted - a `rssfeeds.txt` file will be exported after. The RSS feeds will be located in that file.

Insert the RSS feeds into a feed reader and receive updates about videos from subscribed channels there!