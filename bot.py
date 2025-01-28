from pyrogram import Client
from info import *


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Auto Cap",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "body"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.force_channel = FORCE_SUB
        if FORCE_SUB:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB)
                self.invitelink = link
            except Exception as e:
                print(e)
                print("Make Sure Bot admin in force sub channel")
                self.force_channel = None
        print(f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")
        await self.send_message(ADMIN, f"**{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️**")


Bot().run()
