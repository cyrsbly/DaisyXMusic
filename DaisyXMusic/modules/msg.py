# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "Hey, I'm Katarina 🎵 I can play music in your group's voice call.  Add me to your group and play music freely!\n\nTry the /help Command below to know my abilities."
      HELP_MSG = [
        ".",
f"""
Hey, I'm Katarina 🎵 I can play music in your group's voice call.  Add me to your group and play music freely!\n\nTry the /help Command below to know my abilities.
""",

f"""
**Setting up**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /p [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

""",
f"""
**Commands**

**=>> Song Playing 🎧**

- /p: Play the requestd song
- /p [yt url] : Play the given yt url
- /p [reply yo audio]: Play replied audio

**=>> Playback ⏯**

- /player: Open Settings menu of player
- /s: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist

""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
f"""
**=>> Song Download 🎸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**=>> Search Tools 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",

f"""
**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
