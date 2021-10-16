"""Stream type classes for tap-netlify."""

from pathlib import Path
from typing import Optional

from tap_netlify.client import NetlifyStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class SitesStream(NetlifyStream):
    """Define sites stream."""
    name = "sites"
    path = "/sites"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "sites.json"

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "site_id": record["id"]
        }


class BuildsStream(NetlifyStream):
    """Define builds stream."""
    parent_stream_type = SitesStream
    name = "builds"
    path = "sites/{site_id}/builds"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "builds.json"


class DeploysStream(NetlifyStream):
    """Define deploys stream."""
    parent_stream_type = SitesStream
    name = "deploys"
    path = "sites/{site_id}/deploys"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "deploys.json"
