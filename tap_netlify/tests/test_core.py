"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import get_standard_tap_tests

from tap_netlify.tap import TapNetlify

SAMPLE_CONFIG = {
    "auth_token": "MyToken",
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapNetlify,
        config=SAMPLE_CONFIG
    )
    for test in tests:
        test()

