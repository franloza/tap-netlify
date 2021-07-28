"""REST client handling, including NetlifyStream base class."""

import requests
from urllib.parse import parse_qs, urlparse
from pathlib import Path
from typing import Any, Dict, Optional, Iterable

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from tap_netlify.auth import NetlifyAuthenticator


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class NetlifyStream(RESTStream):
    """Netlify stream class."""

    url_base = "https://api.netlify.com/api/v1/"

    records_jsonpath = "$[*]"

    @property
    def authenticator(self) -> NetlifyAuthenticator:
        """Return a new authenticator object."""
        return NetlifyAuthenticator.create_for_stream(self)

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        next_page_token = None
        link = response.headers.get("Link", None)
        if link:
            link_parts = map(lambda x: x.split(';'), link.split(','))
            for url, rel in link_parts:
                if "next" in rel:
                    params = parse_qs(urlparse(url.replace('<', '').replace('>', '')).query)
                    next_page_token = params["page"][0]
        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {'per_page': 2}
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

