import re
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options


class GoogleTranslatePlugin(BasePlugin):
    config_scheme = {
        ('url', config_options.Type(str, default='')),
        ('relative_url_syntax', config_options.Type(str, default='%GT_RELATIVE_URL%')),
    }

    def on_config(self, config):
        self.config['url'] = self.config.get('url') or config.get('site_url')
        self.config['url'] = re.match(r'(?:https?:\/\/)?([^\/\:]+)[\/\:]?', self.config['url'])
        self.config['url'] = self.config['url'].group(1).replace('.', '-')

    def on_post_page(self, output, page, config):
        # Relative URL (Original language)
        output = output.replace(self.config.get('relative_url_syntax'), page.url)

        # Translation URLs
        regex = r'(href=".+translate\.goog\/(\?.+"md-select__link"))'
        # 1: from href=" to end of line
        # 2: everything after translate.goog/
        matches = re.finditer(regex, output, flags=re.MULTILINE)
        if not matches:  # pragma: no cover
            return output
        for match in matches:
            new_url_string = f'href="https://{self.config["url"]}.translate.goog/{page.url}{match.group(2)}'
            output = output.replace(match.group(1), new_url_string)
        return output
