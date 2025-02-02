from setuptools import setup, find_packages

requires = [
    'flask>=2.0.0',
    'spotipy>=2.19.0',
    'html5lib>=1.1',
    'requests>=2.26.0',
    'requests_html>=0.10.0',
    'beautifulsoup4>=4.10.0',
    'yt-dlp>=2023.7.6',
    'pytube>=12.0.0',
    'ffmpeg-python>=0.2.0',
    'pathlib>=1.0.1',
    'pandas>=1.3.0',
    'urllib3<2.0.0,>=1.25.8'
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