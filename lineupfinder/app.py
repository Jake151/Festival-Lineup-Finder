import json
import sys

import click
import pylast


def get_similar_artists(network, user, artist_limit, similar_limit):
    lastfm_user = network.get_user(user)
    artists = lastfm_user.get_top_artists(limit=artist_limit)

    similar_artists = []
    for artist in artists:
        # Add the aritsts to the list to include them in the lineup generator.
        similar_artists.append(artist.item)
        similar = artist.item.get_similar(limit=similar_limit)
        for s in similar:
            similar_artists.append(s.item)

    return similar_artists


def load_clashfinder_bands(file):
    try:
        with open(file) as f:
            clashfinder = json.load(f)
    except ValueError:
        print("Selected file isn't a valid ClashFinder JSON file.")
        sys.exit(1)

    bands = []
    for l in clashfinder["locations"]:
        for event in l["events"]:
            bands.append(event["name"])

    return bands


def generate_lineup(lineup_artists, similar_artists):
    artists = []
    for artist in similar_artists:
        artists.append(artist.name)

    lineup = []
    for a in sorted(set(artists)):
        if a in lineup_artists:
            lineup.append(a)

    return lineup


@click.command()
@click.option("-u", "--user", required=True, help="User to analyse.")
@click.option("-f", "--file", required=True, help="Clashfinder JSON file.")
@click.option(
    "-al", "--artist-limit", default=50, show_default=True, help="Limit of top artists."
)
@click.option(
    "-sl",
    "--similar-limit",
    default=100,
    show_default=True,
    help="Limit of similar artists.",
)
@click.option("--api-key", required=True, help="Last.fm API key. Can be declared as env var LINEUPFINDER_API_KEY.")
@click.option("--api-secret", required=True, help="Last.fm API secret. Can be declared as env var LINEUPFINDER_API_SECRET.")
def run(user, file, artist_limit, similar_limit, api_key, api_secret):
    festival_lineup = load_clashfinder_bands(file)
    network = pylast.LastFMNetwork(api_key=api_key, api_secret=api_secret)
    similar_artists = get_similar_artists(network, user, artist_limit, similar_limit)

    print("** Your Bands to See List **")
    for artist in generate_lineup(festival_lineup, similar_artists):
        print(artist)


if __name__ == "__main__":
    run()
