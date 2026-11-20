# Leaflet cluster map of talk locations
#
# Run from the repository root:  python talkmap.py
#
# Reads the `location` field of every talk in _talks/, geocodes it with
# geopy/Nominatim, and uses getorg to write a standalone cluster map to talkmap/
# (map.html, org-locations.js, leaflet_dist/). The deploy workflow
# (.github/workflows/deploy.yml) runs this before every build, so talkmap/ is
# build output and is not committed.
#
# Talks whose location cannot be geocoded are skipped with a warning. The script
# exits with an error only if no talk could be placed, so a geocoder outage
# stops the deploy instead of publishing an empty map.
import glob
import os
import sys

import frontmatter
import getorg
from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Nominatim's usage policy asks for an identifying user agent and at most one
# request per second.
USER_AGENT = os.environ.get("NOMINATIM_USER_AGENT", "panyidong.github.io")
geocoder = Nominatim(user_agent=USER_AGENT, timeout=10)
geocode = RateLimiter(geocoder.geocode, min_delay_seconds=1.1, max_retries=3,
                      error_wait_seconds=5.0, swallow_exceptions=True)

location_dict = {}
skipped = []

for file in sorted(glob.glob("_talks/*.md")):
    data = frontmatter.load(file).to_dict()
    location = str(data.get("location") or "").strip()
    if not location:
        continue

    title = str(data.get("title", "")).strip()
    venue = str(data.get("venue", "")).strip()
    description = f"{title}<br />{venue}; {location}"

    place = geocode(location)
    if place is None:
        skipped.append(f"{file}: {location}")
        print(f"::warning file={file}::Could not geocode location '{location}'; talk left off the map")
        continue

    location_dict[description] = place
    print(f"{file}: {location} -> {place.latitude:.4f}, {place.longitude:.4f}")

if not location_dict:
    sys.exit("No talk locations could be geocoded; not writing an empty map.")

getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)
print(f"Wrote talkmap/ with {len(location_dict)} talk(s); skipped {len(skipped)}.")
