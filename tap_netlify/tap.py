"""Netlify tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th

from tap_netlify.streams import (
    SitesStream, BuildsStream
)

STREAM_TYPES = [
    SitesStream,
    BuildsStream
]


class TapNetlify(Tap):
    """Netlify tap class."""
    name = "tap-netlify"

    config_jsonschema = th.PropertiesList(
        th.Property("auth_token", th.StringType, required=True),
        # TODO: Support start_date
        th.Property("start_date", th.DateTimeType)
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
