from telebot import TeleBot, types
import os

bot = TeleBot(os.environ['BOT_TOKEN'])

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    verify_btn = types.InlineKeyboardButton("🔐 Verify Now", url="https://link-target.net/1354609/FpbP1lcx3qR1")
    markup.add(verify_btn)
    bot.send_message(message.chat.id, "🚀 Welcome! To claim free YouTube subscribers, please complete verification first.", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    if "youtube.com/" in message.text or "youtu.be/" in message.text:
        markup = types.InlineKeyboardMarkup()
        share_btn = types.InlineKeyboardButton("📤 Share with Friends", url="https://wa.me/?text=Get%20Free%20YouTube%20Subscribers!%20t.me/@Freeesubsbot")
        markup.add(share_btn)
        bot.send_message(message.chat.id, "✅ Your order is completed!\n⏳ Subscribers will arrive shortly.\nTo speed up the process, share this with friends.", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "❗ Please enter a valid YouTube channel link.")

bot.infinity_polling()
