from pyrogram import Client
from info import *


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Auto Cap",
            api_id=22448257,
            api_hash=7f8e2def57731a61f07b264e13c130a1,
            bot_token=7627086441:AAHJvydOWzyK7mKCpHusxoofoZsqy1295Ss,
            workers=200,
            plugins={"root": "body"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.force_channel = Doraemon_tamil_links
        if FORCE_SUB:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB)
                self.invitelink = link
            except Exception as e:
                print(e)
                print("Make Sure Bot admin in force sub channel")
                self.force_channel = None
        print(f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")
        await self.send_message(ADMIN, f"**{me.Sandy}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️**")


Bot().run()
