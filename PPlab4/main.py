import telebot
import pandas as pd
import kaggle
import zipfile
bot = telebot.TeleBot('BOT-TOKEN')#в кавычках должен быть токен
@bot.message_handler(content_types=['text'])
def get_command(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Это бот для поиска справочной информации о книгах")
    elif message.text == "/stop":
        bot.send_message(message.from_user.id, "Бот остановлен")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Список команд:\n/start - вывести описание бота"
                                               "\n/stop - остановить бот"
                                               "\n/help - вывести список команд"
                                               "\n/search - поиск информации о книге по названию")
    elif message.text == "/search":
        bot.send_message(message.from_user.id, "Введите название книги")
        bot.register_next_step_handler(message, search)
    else:
        bot.send_message(message.from_user.id, "Не команда. Для вывода списка команд введите /help.")

def search(message):
    print(message.text)
    pd.set_option('display.max_colwidth', None)
    book = df.loc[(df['title'] == message.text)]
    if not (book.empty):
        bot.send_message(message.from_user.id, book_to_str(book))
        print(book)
    else:
        bot.send_message(message.from_user.id, "Книги с таким названием нет в базе данных")
def book_to_str(book):
    res = "id:" + str(book['id'].item())+'\n'
    res += "Название:" + str(book['title'].item())+'\n'
    res += "Жанры:" + str(book['genres'].item())+'\n'
    res += "Авторы:" + str(book['authors'].item())+'\n'
    res += "Год издания:" + str(book['year'].item())
    return res

kaggle.api.dataset_download_file("sharthz23/mts-library", "items.csv")
with zipfile.ZipFile("items.csv.zip", 'r') as zip_ref:
    zip_ref.extractall()
df = pd.read_csv("items.csv")
bot.polling(none_stop=True, interval=0)
