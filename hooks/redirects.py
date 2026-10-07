"""Keep bookmarks working after source pages move, without duplicate articles."""

import json
import posixpath
from html import escape
from pathlib import Path

from mkdocs.exceptions import PluginError


def on_post_build(*, config):
    site = Path(config["site_dir"])
    redirects = json.loads(Path(__file__).with_suffix(".json").read_text())
    for old_url, new_url in redirects.items():
        if not (site / new_url).is_file():
            raise PluginError(f"Redirect destination is missing: {new_url}")

        destination = site / old_url
        destination.parent.mkdir(parents=True, exist_ok=True)
        relative_url = posixpath.relpath(new_url, posixpath.dirname(old_url))
        link = escape(relative_url, quote=True)
        destination.write_text(
            '<!doctype html>\n<html lang="en">\n<head>\n'
            '  <meta charset="utf-8">\n'
            '  <meta name="robots" content="noindex">\n'
            f'  <meta http-equiv="refresh" content="0; url={link}">\n'
            '  <title>Page moved</title>\n'
            '</head>\n<body>\n'
            f'  <p>This page has moved. <a href="{link}">Continue to the page</a>.</p>\n'
            '</body>\n</html>\n',
            encoding="utf-8",
        )
