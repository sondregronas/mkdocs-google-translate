# mkdocs-google-translate
[![Build Status](https://img.shields.io/github/workflow/status/sondregronas/mkdocs-google-translate/CI)](https://github.com/sondregronas/mkdocs-google-translate/)
[![GitHub latest commit](https://img.shields.io/github/last-commit/sondregronas/mkdocs-google-translate)](https://github.com/sondregronas/mkdocs-google-translate/commit/)
[![PyPi](https://img.shields.io/pypi/v/mkdocs-google-translate)](https://pypi.org/project/mkdocs-google-translate/)
[![AGPLv3 license](https://img.shields.io/github/license/sondregronas/mkdocs-google-translate)](https://www.gnu.org/licenses/agpl-3.0.en.html)
[![codecov](https://codecov.io/gh/sondregronas/mkdocs-google-translate/branch/main/graph/badge.svg?token=N5IDI7Q4NZ)](https://codecov.io/gh/sondregronas/mkdocs-google-translate)
[![Buymeacoffee](https://badgen.net/badge/icon/buymeacoffee?icon=buymeacoffee&label)](https://www.buymeacoffee.com/u92RMis)

Add relative paths to Google Translate queries.

![img.png](img.png)

`pip install mkdocs-google-translate`

## Usage
Activate the plugin in `mkdocs.yml` by adding the following lines, replace the values of `_x_tr_sl` and `_x_tr_tl` to match your site:
```yml
extra:
  alternate:
    - name: English
      lang: 'en'
      link: ''
    - name: Norsk
      lang: 'no'
      link: 'https://translate.goog/?_x_tr_sl=en&_x_tr_tl=no'
      # _x_tr_sl = source language
      # _x_tr_tl = translation language

plugins:
  - search
  - google-translate:
      url: example.com  # optional (required for local testing)
```
> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.
