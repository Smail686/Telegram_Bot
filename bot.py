import os
from aiogram import Bot, Dispatcher, types
from pytube import YouTube
from moviepy.editor import VideoFileClip

API_TOKEN = 'YOUR_BOT_TOKEN'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def download_video(url: str) -> str:
    youtube = YouTube(url)
    video = youtube.streams.first()
    filename = video.download()

    # Конвертация видео в mp3
    video_clip = VideoFileClip(filename)
    audio_filename = filename.split(".")[0] + ".mp3"
    video_clip.audio.write_audiofile(audio_filename)
    video_clip.close()
    os.remove(filename)

    return audio_filename

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Отправь мне ссылку на видео YouTube, и я скачаю его и конвертирую в mp3.")

@dp.message_handler()
async def download_and_send_video(message: types.Message):
    url = message.text
    if "https://" not in url or "youtu" not in url:
        await message.reply("Пожалуйста, отправьте действительную ссылку на YouTube, начинающуюся с https://")
        return
    await message.reply(f'Ожидай, скачиваю видео по ссылке')
    try:
        
        filename = download_video(url)
    except Exception as e:
        print(e)
        await message.reply("Видео не существует или оно приватное")
        return
    
    await bot.send_audio(chat_id=message.chat.id, audio=open(filename, 'rb'))

    await message.reply(f'Лови конвертированное видео')
    os.remove(filename)  # Удаление файла после отправки


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
