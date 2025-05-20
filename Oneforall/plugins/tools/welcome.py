from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
from Oneforall import app

mongo = MongoClient("mongodb+srv://I-LOVE-PDF-BOT:I-LOVE-PDF-BOT@cluster0.c51o3a9.mongodb.net/?retryWrites=true&w=majority")  
db = mongo["telegram_bot"]
welcome_col = db["welcome_messages"]

@app.on_message(filters.command("setwelcome") & filters.group)
async def set_welcome(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage:\n/setwelcome Your welcome message here.")
    
    welcome_text = message.text.split(" ", 1)[1]
    chat_id = message.chat.id

    welcome_col.update_one(
        {"chat_id": chat_id},
        {"$set": {"message": welcome_text, "enabled": True}},
        upsert=True
    )
    await message.reply("Custom welcome message has been set!")

@app.on_message(filters.command("welcome") & filters.group)
async def toggle_welcome(client, message: Message):
    if len(message.command) >= 2 and message.command[1].lower() == "off":
        chat_id = message.chat.id
        welcome_col.update_one(
            {"chat_id": chat_id},
            {"$set": {"enabled": False}},
            upsert=True
        )
        await message.reply("Welcome system disabled.")
    else:
        await message.reply("Use `/welcome off` to disable welcome system.", quote=True)

@Client.on_message(filters.new_chat_members & filters.group)
async def welcome_new_member(client, message: Message):
    chat_id = message.chat.id
    data = welcome_col.find_one({"chat_id": chat_id, "enabled": True})
    
    if data:
        for member in message.new_chat_members:
            text = data["message"].replace("{name}", member.mention(style='md')).replace("{first}", member.first_name)
            await message.reply(text)
