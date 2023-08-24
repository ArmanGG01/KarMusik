from typing import Dict, Union, List
from Music import db

chatsdb = db.chats

async def get_served_chats() -> list:
    chats = chatsdb.find({"chat_id": {'$lt': 0}})
    return [] if not chats else list(await chats.to_list(length=1000000000))   
    
async def is_served_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    return bool(chat)

async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})
 
async def get_served_chats() -> list:
    chats = chatsdb.find({"chat_id": {"$lt": 0}})
    return [] if not chats else list(await chats.to_list(length=1000000000))

async def remove_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if not is_served:
        return
    return await chatsdb.delete_one({"chat_id": chat_id})
