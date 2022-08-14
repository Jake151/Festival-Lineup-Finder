# Festival Lineup Finder
A simple script to interact and compare your last.fm artist recommendations to a festival line up. Idea being that you'll find a hidden gem you may have missed otherwise! 

By defualt the last.fm API returns simmilar artists in order of which they match your top artists. Try playing around with the `similar-limit` parameter to return a wider or more concise range of artists to watch. 

# Requirements
- Last.fm API key, https://www.last.fm/api/account/create to create one
- Clashfinder JSON export of the line up
    - From the festival page select Data -> Export -> Full Calendar -> JSON -> OK

# Setup
Install requirements: `pip install -r requirements.txt`

# Usage
```
python -m lineupfinder --help
Usage: python -m lineupfinder [OPTIONS]

Options:
  -u, --user TEXT               User to analyse.  [required]
  -f, --file PATH               Clashfinder JSON file.  [required]
  -al, --artist-limit INTEGER   Limit of top artists.  [default: 50]
  -sl, --similar-limit INTEGER  Limit of similar artists.  [default: 100]
  --api-key TEXT                Last.fm API key. Can be declared as env var
                                LINEUPFINDER_API_KEY.  [required]
  --api-secret TEXT             Last.fm API secret. Can be declared as env var
                                LINEUPFINDER_API_SECRET.  [required]
  --help                        Show this message and exit.
```