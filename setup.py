from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
    'html5lib',
    'requests',
    'requests_html',
    'beautifulsoup4',
    'yt_dlp',
    'pathlib',
    'pandas'
]

setup(
    name='SpotifyToYoutubeMP3',
    version='1.0',
    description='An application that gets your Spotify songs and downloads the YoutubeMP3 version',
    author='Zeyad Bassyouni',
    author_email='sc22zb@leeds.ac.uk',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)