import re

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin


class GoogleTranslatePlugin(BasePlugin):
    config_scheme = {
        ("url", config_options.Type(str, default="")),
        ("relative_url_syntax", config_options.Type(str, default="%GT_RELATIVE_URL%")),
    }

    def __init__(self):
        super().__init__()
        self.location = ""
        self.fqdn = ""

    def on_config(self, config):
        full_url = self.config.get("url") or config.get("site_url")
        fqdn = re.match(r"(?:https?:\/\/)?([^\/\:]+)[\/\:]?", full_url).group(1)

        # Get the location part of the URL if it exists (e.g., /subpath/)
        location = re.search(rf"{fqdn}/([^/]*)", full_url)
        location = f"{location.group(1)}" if location else ""

        # FQDN for Google Translate urls use hyphens instead of dots
        self.fqdn = fqdn.replace(".", "-")
        self.location = location

    def on_post_page(self, output, page, config):
        # Relative URL (Original language)
        output = output.replace(self.config.get("relative_url_syntax"), page.url)

        # Translation URLs
        regex = r'(href=".+translate\.goog\/(\?.+"md-select__link"))'
        # 1: from href=" to end of line
        # 2: everything after translate.goog/
        matches = re.finditer(regex, output, flags=re.MULTILINE)
        if not matches:  # pragma: no cover
            return output
        for match in matches:
            url = page.url
            if self.location:
                url = f"{self.location}{'/' + url if url else ''}"
            new_url_string = (
                f'href="https://{self.fqdn}.translate.goog/{url}{match.group(2)}'
            )
            output = output.replace(match.group(1), new_url_string)
        return output
