from typing import Dict, List, Union
from Music import db

pytgdb = db.pytg
admindb = db.admin

## Queue Chats

async def get_active_chats() -> list:
    chats = pytgdb.find({"chat_id": {"$lt": 0}})
    return [] if not chats else list(await chats.to_list(length=1000000000))
    
async def is_active_chat(chat_id: int) -> bool:
    chat = await pytgdb.find_one({"chat_id": chat_id})
    return bool(chat)

async def add_active_chat(chat_id: int):
    is_served = await is_active_chat(chat_id)
    if is_served:
        return
    return await pytgdb.insert_one({"chat_id": chat_id})

async def remove_active_chat(chat_id: int):
    is_served = await is_active_chat(chat_id)
    if not is_served:
        return
    return await pytgdb.delete_one({"chat_id": chat_id})

  
## Music Playing or Paused  
    
async def is_music_playing(chat_id: int) -> bool:
    chat = await admindb.find_one({"chat_id_toggle": chat_id})
    return not chat

async def music_on(chat_id: int):
    is_karma = await is_music_playing(chat_id)
    if is_karma:
        return
    return await admindb.delete_one({"chat_id_toggle": chat_id})

async def music_off(chat_id: int):
    is_karma = await is_music_playing(chat_id)
    if not is_karma:
        return
    return await admindb.insert_one({"chat_id_toggle": chat_id})
