import os

import markups as nav

from aiogram.dispatcher.filters import Text

from aiogram.utils import executor

from aiogram import types, Dispatcher, Bot

import gspread

from google.oauth2 import service_account

from googleapiclient.errors import HttpError

from googleapiclient.discovery import build


bot_token = '5933129176:AAHklxOUrJ9LM61ZIntCohudtzTmYuG702U'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'for-me-378011-d3a6a8c8d528.json')

creds = service_account.Credentials.from_service_account_file(creds_path, scopes=scope)
client = gspread.authorize(creds)
drive_service = build('drive', 'v3', credentials=creds)
bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def talabalar(message: types.Message):
    file_id = message.document.file_id
    file_info = await bot.get_file(file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    task_name = message.document.file_name
    with open(task_name, 'wb') as new_file:
        new_file.write(downloaded_file.getvalue())
    file_metadata = {'name': f'{task_name}', 'parents': ['1_dlD3MobEHOr4vXB2yI3h9Vmnilj0oFY']}
    media = await bot.send_message(message.chat.id, "Fayl yuklanmoqda...")
    try:
        file = drive_service.files().create(body=file_metadata, media_body=task_name, fields='id').execute()
        await bot.edit_message_text("Fayl muvaffaqiyatli yuklandi!", chat_id=media.chat.id, message_id=media.message_id)
    except HttpError as error:
        await bot.edit_message_text("An error occurred: %s" % error, chat_id=media.chat.id, message_id=media.message_id)
    os.remove(task_name)

async def maqola(message: types.Message):
    file_id = message.document.file_id
    file_info = await bot.get_file(file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    task_name = message.document.file_name
    with open(task_name, 'wb') as new_file:
        new_file.write(downloaded_file.getvalue())
    file_metadata = {'name': f'{task_name}', 'parents': ['1Ydv1Frdzn4v2Mx1ChDIC_xcx-8o_kG8L']}
    media = await bot.send_message(message.chat.id, "Fayl yuklanmoqda...")
    try:
        file = drive_service.files().create(body=file_metadata, media_body=task_name, fields='id').execute()
        await bot.edit_message_text("Fayl muvaffaqiyatli yuklandi!", chat_id=media.chat.id, message_id=media.message_id)
    except HttpError as error:
        await bot.edit_message_text("An error occurred: %s" % error, chat_id=media.chat.id, message_id=media.message_id)
    os.remove(task_name)


async def diplom(message: types.Message):
    file_id = message.document.file_id
    file_info = await bot.get_file(file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    task_name = message.document.file_name
    with open(task_name, 'wb') as new_file:
        new_file.write(downloaded_file.getvalue())
    file_metadata = {'name': f'{task_name}', 'parents': ['12fnmpN4mjx1xhEtJi5Y1-vzD2jLGG81m']}
    media = await bot.send_message(message.chat.id, "Fayl yuklanmoqda...")
    try:
        file = drive_service.files().create(body=file_metadata, media_body=task_name, fields='id').execute()
        await bot.edit_message_text("Fayl muvaffaqiyatli yuklandi!", chat_id=media.chat.id, message_id=media.message_id)
    except HttpError as error:
        await bot.edit_message_text("An error occurred: %s" % error, chat_id=media.chat.id, message_id=media.message_id)
    os.remove(task_name)


# Register the main menu handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu Alaykum FDU Botiga hush kelibsiz! \nTopshiriqni tanlang!", reply_markup=nav.mainMenu)

# Register the handler for the "Diplom" button
@dp.message_handler(Text(equals='Diplom'))
async def handle_diplom_message(message: types.Message):
    if message.text == 'Diplom':
        await message.reply("Kaferangizni tanlang!", reply_markup=nav.Kafedra)
    else:
        await message.reply("Noto'g'ri boyruq yubordingiz iltimos qayta urunib ko'ring!")
# Register separate handlers for each kafedra
@dp.message_handler(Text(equals='Fizika'))
async def handle_fizika_message(message: types.Message):
    await message.reply("Fayilni yuklang!")
    dp.register_message_handler(diplom, content_types=['document'])

@dp.message_handler(Text(equals='Matematika'))
async def handle_matematika_message(message: types.Message):
    await message.reply("Fayilni yuklang!")
    dp.register_message_handler(diplom, content_types=['document'])

@dp.message_handler(Text(equals='Iqtisod'))
async def handle_iqtisod_message(message: types.Message):
    await message.reply("Fayilni yuklang!")
    dp.register_message_handler(diplom, content_types=['document'])

@dp.message_handler(Text(equals='Tarix'))
async def handle_tarix_message(message: types.Message):
    await message.reply("Fayilni yuklang!")
    dp.register_message_handler(diplom, content_types=['document'])

@dp.message_handler(Text(equals='Maqola'))
async def handle_maqola_message(message: types.Message):
    if message.text == "Maqola":
        await message.reply("Fakultetingizni tanlang!", reply_markup=nav.Fakultet)
    else:
        await message.reply("Noto'g'ri boyruq yubordingiz iltimos qayta urunib ko'ring!")

@dp.message_handler(Text(equals='Fizika-Texnika'))
async def handle_fizika_texnika_message(message: types.Message):
    await message.reply("Fayilni yuklang!")
    dp.register_message_handler(maqola, content_types=['document'])

@dp.message_handler(Text(equals='Matematika-Informatika'))
async def handle_matematika_informatika_message(message: types.Message):
    await message.reply("Fayilni yuklang!")
    dp.register_message_handler(maqola, content_types=['document'])

@dp.message_handler(Text(equals='Iqtisodiyot'))
async def handle_iqtisodiyot_message(message: types.Message):
    await message.reply("Fayilni yuklang!")
    dp.register_message_handler(maqola, content_types=['document'])

@dp.message_handler(Text(equals='Tarix-fakulteti'))
async def handle_tarix_message(message: types.Message):
    await message.reply("Fayilni yuklang!")
    dp.register_message_handler(maqola, content_types=['document'])

@dp.message_handler(Text(equals='Talabalar'))
async def handle_talabalar_message(message: types.Message):
    if message.text == "Talabalar":
        await message.reply("Kaferangizni tanlang!", reply_markup=nav.Kafedra2)
    else:
        await message.reply("Noto'g'ri boyruq yubordingiz iltimos qayta urunib ko'ring!")

@dp.message_handler(Text(equals='Fizika1'))
async def handle_fizika1_message(message: types.Message):
    await message.reply("Fayilni yuklang!")
    dp.register_message_handler(talabalar, content_types=['document'])

@dp.message_handler(Text(equals='Matematika1'))
async def handle_matematika1_message(message: types.Message):
    await message.reply("Fayilni yuklang!")
    dp.register_message_handler(talabalar, content_types=['document'])

@dp.message_handler(Text(equals='Iqtisod1'))
async def handle_iqtisod1_message(message: types.Message):
    await message.reply("Fayilni yuklang!")
    dp.register_message_handler(talabalar, content_types=['document'])

@dp.message_handler(Text(equals='Tarix1'))
async def handle_tarix1_message(message: types.Message):
    await message.reply("Fayilni yuklang!")
    dp.register_message_handler(talabalar, content_types=['document'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)