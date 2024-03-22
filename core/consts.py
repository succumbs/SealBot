import disnake


ACTIVITIES = [
    disnake.Activity(
        type=disnake.ActivityType.streaming,
        name="24/7 Seals",
        platform="YouTube",
        url="https://www.youtube.com/watch?v=aXAsMcmtJTc",
    ),
    disnake.Activity(
        type=disnake.ActivityType.listening,
        name="Seal breakcore",
        url="https://www.youtube.com/watch?v=-m7iS1TvphE",
    ),
    disnake.Activity(
        type=disnake.ActivityType.custom, name="Custom Status", state="Being seally"
    ),
    disnake.Activity(
        type=disnake.ActivityType.custom, name="Custom Status", state="Galumphing"
    ),
    disnake.Activity(
        type=disnake.ActivityType.custom, name="Custom Status", state="R.I.P. Ponsuke"
    ),
]


class EmbedColors:
    SUCCESS = 0x6DBEED
    ERROR = 0xED6D73
