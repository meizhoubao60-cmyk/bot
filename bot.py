from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

SHORT_INTRO = "鸠山💗07｜165cm｜40kg｜原创博主"
DETAIL_INTRO = "07｜165cm｜40kg｜B｜37cm｜接定制、11 + 防骗提醒"

CHANNEL_LINK = "https://t.me/+p9xBNPYJLcswMGZh"

PRODUCTS = {
    "188": "🚪 188基础门🚪解锁库存、不聊天‼️\n（图、视频、解锁11下单）",
    "388": "🚪 388🚪\n基础门库存、解锁11下单9折、赠送1次11",
    "588": "🚪 588🚪\n基础门库存、解锁11下单8折、解锁简单定制现拍、➕🛰️、赠送1次11",
    "1888": "🚪 1888🚪\n基础门库存、解锁11下单6折、解锁简单定制现拍、➕🛰️、赠送3次11",
    "3888": "🚪 3888🚪\
