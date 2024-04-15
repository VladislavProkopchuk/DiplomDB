import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
import logging

# Словарь с вопросами и ответами
words = {
    'apple': 'яблоко',
    'banana': 'банан',
    'pear': 'груша'
}

# Функция для генерации вариантов ответа
def generate_options(correct_answer):
    options = [correct_answer]
    while len(options) < 4:
        random_word = list(words.keys())[random.randint(0, len(words) - 1)]
        if random_word not in options:
            options.append(random_word)
    random.shuffle(options)
    return options

# Функция для начала викторины
def start_quiz(update: Update, context: CallbackContext):
    question_word = random.choice(list(words.keys()))
    correct_answer = words[question_word]
    options = generate_options(correct_answer)

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(option, callback_data=f'{question_word} {option}') for option in options]
    ])

    update.message.reply_text(f'Как переводится слово "{question_word}"?', reply_markup=reply_markup)

# Функция для проверки ответа
def check_answer(update: Update, context: CallbackContext):
    query = update.callback_query
    user_answer = query.data.split()[1]
    correct_answer = words[query.data.split()[0]]

    if user_answer == correct_answer:
        query.edit_message_text('Правильно!')
    else:
        query.edit_message_text('Неправильно. Попробуйте снова.')

# Функция для добавления нового слова
def add_word(update: Update, context: CallbackContext):
    user = update.message.from_user.id
    text = update.message.text.replace('/add_word', '').strip()
    word, translation = text.split('=') if '=' in text else (None, None)

    if word and translation:
        words[word] = translation
        update.message.reply_text('Слово успешно добавлено.')
    else:
        update.message.reply_text('Неверный формат ввода. Попробуйте снова.')

# Функция для удаления слова
def delete_word(update: Update, context: CallbackContext):
    user = update.message.from_user.id
    word = update.message.text.replace('/delete_word', '').strip()

    if word in words:
        del words[word]
        update.message.reply_text(f'Слово "{word}" успешно удалено.')
    else:
        update.message.reply_text('Слово не найдено.')

# Инициализация бота
def main():
    updater = Updater("7096429466:AAHZe5Yly8w8_NiZH5bSukMoEWSHJJHRAho", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start_quiz", start_quiz))
    dp.add_handler(CallbackQueryHandler(check_answer))
    dp.add_handler(MessageHandler(Filters.regex(r'/add_word'), add_word))
    dp.add_handler(MessageHandler(Filters.regex(r'/delete_word'), delete_word))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
