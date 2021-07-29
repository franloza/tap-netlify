# tap-netlify

`tap-netlify` is a Singer tap for [Netlify API](https://docs.netlify.com/api/get-started/).

This package is NOT officially supported by Netlify. Users are welcome to open issues or pull requests to improve the tap.

Built with the Meltano [SDK](https://gitlab.com/meltano/sdk) for Singer Taps.

## Installation

```bash
pipx install  git+https://github.com/franloza/netlify-tap.git
```

## Configuration

### Accepted Config Options

The following configuration options are available:

- auth_token (required): User-generated token. See how to obtain it from the Netlify UI [here](https://docs.netlify.com/cli/get-started/#obtain-a-token-in-the-netlify-ui)
- user_agent (optional): It should be set to something that includes the name of your app, and a contact email address should the API provider need to contact you for any reason. [Example](https://docs.netlify.com/api/get-started/#make-a-request)

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-netlify --about
```

## Usage

You can easily run `tap-netlify` by itself or in a pipeline using [Meltano](www.meltano.com).

### Executing the Tap Directly

```bash
tap-netlify --version
tap-netlify --help
tap-netlify --config CONFIG --discover > ./catalog.json
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_netlify/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-netlify` CLI interface directly using `poetry run`:

```bash
poetry run tap-netlify --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-netlify
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-netlify --version
# OR run a test `elt` pipeline:
meltano elt tap-netlify target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
