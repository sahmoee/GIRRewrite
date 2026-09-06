import json
import os
from pathlib import Path


default_extensions = [
    "cogs.community_suite",
    "cogs.server_suite",
    "cogs.commands.info.devices",
    "cogs.commands.info.stats",
    "cogs.commands.info.help",
    "cogs.commands.info.tags",
    "cogs.commands.info.userinfo",
    "cogs.commands.misc.admin",
    "cogs.commands.misc.canister",
    "cogs.commands.misc.genius_submod",
    "cogs.commands.misc.giveaway",
    "cogs.commands.misc.ioscfw",
    "cogs.commands.misc.memes",
    "cogs.commands.misc.misc",
    "cogs.commands.misc.timezones",
    "cogs.commands.mod.antiraid",
    "cogs.commands.mod.filter",
    "cogs.commands.mod.modactions",
    "cogs.commands.mod.modutils",
    "cogs.monitors.misc.boosteremojis",
    "cogs.monitors.misc.fixsocials",
    "cogs.monitors.misc.songs",
    "cogs.monitors.mod.antiraid",
    "cogs.monitors.mod.logging",
    "cogs.monitors.mod.filter",
    "cogs.monitors.mod.sabbath",
    "cogs.monitors.mod.unban_appeals",
    "cogs.monitors.utils.applenews",
    "cogs.monitors.utils.birthday",
    "cogs.monitors.utils.jailbreak_monitors",
    "cogs.monitors.utils.xp",
]

feature_path = os.environ.get("GIR_FEATURE_FILE")
if feature_path:
    try:
        enabled_extensions = set(json.loads(Path(feature_path).read_text()).get("enabled", []))
        initial_extensions = [name for name in default_extensions if name in enabled_extensions]
    except (OSError, ValueError, TypeError):
        initial_extensions = list(default_extensions)
else:
    initial_extensions = list(default_extensions)
