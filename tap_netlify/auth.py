"""Netlify Authentication."""


from singer_sdk.authenticators import SimpleAuthenticator


class NetlifyAuthenticator(SimpleAuthenticator):
    """Authenticator class for Netlify."""

    @classmethod
    def create_for_stream(cls, stream) -> "NetlifyAuthenticator":
        return cls(
            stream=stream,
            auth_headers={
                "Authorization": f"Bearer {stream.config.get('auth_token')}"
            }
        )
