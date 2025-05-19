from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
import asyncio



# === Handle join requests ===
@app.on_chat_join_request()
async def handle_join_request(client, update):
    chat_id = update.chat.id
    user = update.from_user

    # Get all admins (excluding bots)
    admins = []
    async for member in client.get_chat_members(chat_id, filter="administrators"):
        if not member.user.is_bot:
            admins.append(member)

    # Tag all admins
    tags = " ".join([f"[{admin.user.first_name}](tg://user?id={admin.user.id})" for admin in admins])

    # Approve / Disapprove buttons
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ Approve", callback_data=f"approve_{chat_id}_{user.id}"),
            InlineKeyboardButton("❌ Disapprove", callback_data=f"disapprove_{chat_id}_{user.id}")
        ]
    ])

    # Send the request to group
    await client.send_message(
        chat_id,
        f"{tags}\n\nNew join request from [{user.first_name}](tg://user?id={user.id})",
        reply_markup=buttons,
        parse_mode="markdown"
    )

# === Handle button presses ===
@app.on_callback_query()
async def handle_buttons(client, callback_query):
    data = callback_query.data
    from_user = callback_query.from_user

    if data.startswith("approve_"):
        _, chat_id, user_id = data.split("_")
        await client.approve_chat_join_request(int(chat_id), int(user_id))
        await callback_query.message.edit_text("✅ User approved by admin.")
        await callback_query.answer("Approved!")

    elif data.startswith("disapprove_"):
        _, chat_id, user_id = data.split("_")
        await client.decline_chat_join_request(int(chat_id), int(user_id))
        await callback_query.message.edit_text("❌ User disapproved by admin.")
        await callback_query.answer("Disapproved.")
