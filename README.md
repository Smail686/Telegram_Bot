# YouTube-to-MP3 Telegram Bot

## Description
This Python project implements a Telegram bot that allows users to convert YouTube videos to MP3 audio files. Leveraging Aiogram for Telegram integration, Pytube for YouTube video downloads, and MoviePy for video-to-audio conversion, the bot simplifies the process for users. Send a YouTube link, and the bot will handle the download, conversion, and delivery of the MP3 file.

## Features
- Telegram bot using Aiogram.
- Downloads YouTube videos with Pytube.
- Converts videos to MP3 using MoviePy.
- Error handling for inaccessible or private videos.
- User-friendly commands: "/start" and "/help".

## Usage
1. Start a Telegram chat with the bot.
2. Send a valid YouTube video link.
3. Receive the converted MP3 file.

## Dependencies
- aiogram
- pytube
- moviepy

## How to Run
1. Install dependencies: `pip install aiogram pytube3 moviepy`.
2. Replace `API_TOKEN` with your Telegram bot token.
3. Run the script to start the bot.

## Note
Ensure secure handling of API tokens and adhere to platform terms of service.
