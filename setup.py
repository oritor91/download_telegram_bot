from setuptools import setup, find_packages

setup(
    name='telegram_jellyfin_bot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'python-telegram-bot>=13.0',
        'yt-dlp',
    ],
    entry_points={
        'console_scripts': [
            'telegram_jellyfin_bot=telegram_jellyfin_bot.bot:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Telegram bot to download videos to a Jellyfin server.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/telegram_jellyfin_bot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
