from importlib.metadata import version, PackageNotFoundError

from mkdocs_google_translate.plugin import GoogleTranslatePlugin

try:
    __version__ = version("mkdocs-google-translate")
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    pass
