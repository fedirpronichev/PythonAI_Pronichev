from bs4 import BeautifulSoup
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

url = "https://uaserials.pro/films/"

# Парсим главную страницу
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

# Получаем ссылки на фильмы
soup_list_href = soup.find_all('a', {"class": "short-img img-fit"})
with open('link.txt', "w", encoding='utf-8') as f:
    for href in soup_list_href:
        f.write(f"{href['href']}\n")

# Чтение ссылок из файла
links_list = []
with open('link.txt', 'r', encoding='utf-8') as file:
    links_list = [line.strip() for line in file.readlines()]  # Убираем лишние пробелы и символы новой строки

# Парсим информацию о фильмах
list_name = []
list_desc = []
with open('info.txt', 'w', encoding='utf-8') as f:
    for link in links_list:
        req = requests.get(link)
        soup1 = BeautifulSoup(req.text, features="html.parser")

        # Получаем название фильма
        soup_list_name_film = soup1.find_all('span', {"class": "oname_ua"})
        if len(soup_list_name_film) > 0:
            f.write(f'{soup_list_name_film[0].text.strip()}\n')  # Убираем лишние пробелы
            list_name.append(soup_list_name_film[0].text.strip())

        # Получаем описание фильма
        soup_list_ul = soup1.find_all('ul', {"class": "short-list fx-1"})
        for item in soup_list_ul:
            f.write(f"{item.text.strip()}\n")  # Убираем лишние пробелы
            list_desc.append(item.text.strip())

# Команды бота
command = """/help - список всіх команд бота
/hello - привітання,
/film - список найновіщих фільмів,
/last_film - останній фільм,
/random_film - випадковий фільм,
/count_films - кількість фільмів,
/search_film [назва] - пошук фільму по назві,
/genre_films [жанр] - фільми по жанру,
/update_films - оновити список фільмів"""

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Перебираем фильмы и отправляем информацию о каждом
    for i in range(len(links_list)):
        text = f"{list_name[i]}\n{list_desc[i]}\n{links_list[i]}"  # Индекс links_list[i] для правильной ссылки
        await update.message.reply_text(text)

async def last_film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if list_name and list_desc and links_list:
        # Отправляем информацию о последнем фильме
        text = f"Останній фільм: {list_name[-1]}\n{list_desc[-1]}\n{links_list[-1]}"
        await update.message.reply_text(text)
    else:
        await update.message.reply_text("Не вдалося знайти фільми.")

async def random_film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if list_name and list_desc and links_list:
        random_index = random.randint(0, len(list_name) - 1)
        text = f"Случайный фильм: {list_name[random_index]}\n{list_desc[random_index]}\n{links_list[random_index]}"
        await update.message.reply_text(text)
    else:
        await update.message.reply_text("Фільми не знайдені.")

async def count_films(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    count = len(list_name)
    await update.message.reply_text(f"Кількість доступних фільмів: {count}")

async def search_film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    search_query = ' '.join(context.args).lower()
    found = False
    for i in range(len(list_name)):
        if search_query in list_name[i].lower():
            text = f"Знайдений фільм: {list_name[i]}\n{list_desc[i]}\n{links_list[i]}"
            await update.message.reply_text(text)
            found = True
            break
    if not found:
        await update.message.reply_text("Фільм не знайдений.")

async def genre_films(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    genre = ' '.join(context.args).lower()
    found = False
    for i in range(len(list_name)):
        if genre in list_desc[i].lower():  # Предполагаем, что описание может содержать жанр
            text = f"Фільм за жанром {genre}: {list_name[i]}\n{list_desc[i]}\n{links_list[i]}"
            await update.message.reply_text(text)
            found = True
    if not found:
        await update.message.reply_text(f"Фільми жанру {genre} не знайдено.")

async def update_films(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global list_name, list_desc, links_list
    # Повторно парсим сайт и обновляем данные
    url = "https://uaserials.pro/films/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    soup_list_href = soup.find_all('a', {"class": "short-img img-fit"})

    # Перезаписываем ссылки
    links_list = [href['href'] for href in soup_list_href]

    # Получаем новые имена и описания
    list_name = []
    list_desc = []
    for link in links_list:
        req = requests.get(link)
        soup1 = BeautifulSoup(req.text, features="html.parser")

        # Название фильма
        soup_list_name_film = soup1.find_all('span', {"class": "oname_ua"})
        if len(soup_list_name_film) > 0:
            list_name.append(soup_list_name_film[0].text.strip())

        # Описание фильма
        soup_list_ul = soup1.find_all('ul', {"class": "short-list fx-1"})
        for item in soup_list_ul:
            list_desc.append(item.text.strip())

    await update.message.reply_text("Список фільмів оновлено!")

# Инициализация и запуск бота
app = ApplicationBuilder().token("7979412313:AAHtHppXAuVsUaWR8HWV6ssCSQYt2Br5zVA").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("last_film", last_film))
app.add_handler(CommandHandler("random_film", random_film))
app.add_handler(CommandHandler("count_films", count_films))
app.add_handler(CommandHandler("search_film", search_film))
app.add_handler(CommandHandler("genre_films", genre_films))
app.add_handler(CommandHandler("update_films", update_films))
app.add_handler(CommandHandler("help", lambda update, context: update.message.reply_text(command)))

app.run_polling()
