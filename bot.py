from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

SHORT_INTRO = "鸠山💗07｜165cm｜40kg｜原创博主"
DETAIL_INTRO = "07｜165cm｜40kg｜B｜37cm｜接定制、11 + 防骗提醒"

PRODUCTS = [
    "🎬 定制详情\n20一分钟 五分钟起定\n1.不露🪷 自带玩具\n2.指定衣服道具➕4",
    "📦 库存不露🪷\n150条99🥕\n300条188🥕",
    "🎬 1对1（不露🪷）\n188🥕（十分钟）\n过门也d我‼️",
    "🚪 鸠山美志·（不露🪷）\n188基础门🚪解锁库存、不聊天‼️\n（图、视频、解锁11下单）",
    "🚪 388🚪\n基础门库存、解锁11下单9折、赠送1次11",
    "🚪 588🚪\n基础门库存、解锁11下单8折、解锁简单定制现拍、➕🛰️、赠送1次11",
    "🚪 1888🚪\n基础门库存、解锁11下单6折、解锁简单定制现拍、➕🛰️、赠送3次11",
    "🚪 3888🚪\n基础门库存、解锁11下单4折、解锁简单定制现拍、赠送6次11、➕私人🛰️",
    "🚪 5888🚪\n基础门库存、解锁11下单4折、解锁简单定制现拍、➕私人🛰️、赠送10次11或者面基需要你来找我",
    "🎬 单独接1v1\n188十分钟\n推止于推，不露🪷",
    "⚠️ ps：门槛不退❗️想好再入‼️",
]

MENU = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📦 全部商品"), KeyboardButton("🧾 我的订单")],
        [KeyboardButton("👤 个人中心")],
    ],
    resize_keyboard=True
)

def get_link_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("鸠山的入🚪机器人", url="https://t.me/JSJS07JS_bot")],
        [InlineKeyboardButton("鸠山的个人电报 ✈️", url="https://t.me/JSJS07JS")],
        [InlineKeyboardButton("电报✈️免费粉丝群聊", url="https://t.me/JSJS07JS6")],
        [InlineKeyboardButton("鸠山的唯一X账号❗️", url="https://x.com/jsjs07js")],
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"欢迎光临鸠山的小铺\n\n{SHORT_INTRO}\n{DETAIL_INTRO}",
        reply_markup=get_link_keyboard()
    )
    await update.message.reply_text(f"共 {len(PRODUCTS)} 个商品，当前第 1 页")
    for p in PRODUCTS:
        await update.message.reply_text(p)
    await update.message.reply_text("点击下方按钮操作", reply_markup=MENU)

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "📦 全部商品":
        await start(update, context)
    elif text == "🧾 我的订单":
        await update.message.reply_text("暂无订单记录")
    elif text == "👤 个人中心":
        await update.message.reply_text("个人中心")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu))
    app.run_polling()

if __name__ == "__main__":
    main()
