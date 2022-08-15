from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mkdocs-google-translate',
    version='1.0.0',
    description="A plugin to add relative links to Google Translate queries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='mkdocs markdown google translate',
    url='https://github.com/sondregronas/mkdocs-google-translate',
    author='Sondre Grønås',
    author_email='mail@sondregronas.com',
    license='AGPLv3',
    python_requires='>=3.6',
    install_requires=['mkdocs>=1'],
    tests_require=["pytest"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={'mkdocs.plugins': [
        'google-translate = mkdocs_google_translate.plugin:GoogleTranslatePlugin']}
)
