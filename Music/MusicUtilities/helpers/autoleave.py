from pyrogram.errors import PeerIdInvalid, UserNotParticipant
from Music.MusicUtilities.tgcallsrun.music import pytgcalls, smexy as user


async def leave_from_inactive_call():
    all_chat_id = []
    async for chat in user.iter_dialogs():
        if chat.chat.type in ["group", "supergroup"]:
            chat_id = chat.chat.id
            for call in pytgcalls.calls:
                call_chat_id = int(getattr(call, "chat_id"))
                if call_chat_id not in all_chat_id:
                    all_chat_id.append(call_chat_id)
                call_status = getattr(call, "status")
                try:
                    if (
                        call_chat_id == chat_id
                        and call_status == "not_playing"
                        or chat_id not in all_chat_id
                    ):
                        await user.leave_chat(chat_id)
                except UserNotParticipant:
                    pass
            if chat_id not in all_chat_id:
                try:
                    await user.leave_chat(chat_id)
                except (PeerIdInvalid, UserNotParticipant):
                    pass
                  
