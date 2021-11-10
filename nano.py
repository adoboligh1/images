#!/usr/bin/python3

from datetime import datetime

version = 1.0
bot_name = "@JoeyMusicBot"
creator = "@whereareyoufrom"
donation = "https://www.paypal.com/paypalme/an0nimia"
source_code_bot = "https://github.com/An0nimia/DeezloaderBIB_bot"
source_code_lib = "https://pypi.org/project/deezloader/"
forum = "@JoeymusicGroup"
active_since = "24/07/2021"
date_start = datetime.now()
last_reset = datetime.strftime(date_start, "%d/%m/%Y %H:%M:%S")

not_found_query_gif = "https://i.ibb.co/YQr9vvq/coding-programming-errors-404-page-not-found.gif"
empty_image_url = "https://e-cdns-images.dzcdn.net/images/cover/1000x1000-000000-80-0-0.jpg"

banning_msg1 = "Too many requests per microsecond, please relax and be patient when using my commands else.... :)"
banning_msg2 = "Sorry but i'll have to ban you for not being cautious of the warning, yes this -> {banning_msg1}"

album_too_long = "Album too long and cannot download.."
track_too_long = "This song is too long and big for even russia to fit.. cannot download :("

shazam_function_msg = "Simple, record and send me an audio and i will be able to find and download you that song."
max_download_user_msg = "Sorry, you have reached max download per time avalaible, wait or kill someone :)"
help_msg = f"WELCOME IN {bot_name} here you can find the commands avalaible, JUST TRY IT :)"
help_photo = open("photos/help_msg.jpg", "rb")

feedback_text = f"If you have any question, just ask to this dude {creator}"
donate_text = f"If you are poor like me, I understand you, IF NOT, I will appreciate a little donation 🥺"

startup_text = (
	f"""
	Hello guys welcome in {bot_name}⚡️, developed by {creator}.
	If you want to stay updated join to {forum}
	If you like my project support my buying a kebab [DONATE]({donation})

		*DISCLAIMER*:
			1): DO NOT USE THIS BOT FOR YOUR OWN PURPOSE
			2): I AM NOT RESPONSABLE FOR ANY ILLEGIT USAGE
			3): The source code can be found here:
					a): [DeezSpot_bot]({source_code_bot})
					b): [Main lib]({source_code_lib})
			5): For the artists songs I don't think would get poor if someone doesn't pay for their content.
			6): ENJOY THE MUSIC ART🔥
	"""
)

reasons_text = (
	"WHY I MADE THIS BOT?\
	\n1): This was a nice challenge for me as a little dev\
	\n2): No all of us have the possibility to pay for music content, so I did this to give to everybody for free the chance to download songs"
)

what_can_I_do = (
	"Glad you asked, I can do:\
	\n1): Download songs in three different qualities (/quality)\
	\n2): Shazam engine like to download songs around you\
	\n3): Zip sending\
	\n4): I hope enough performing JAJAJAJAJAJ\
	\n5): I am too lazy to continue, found out by yourself :)"
)

bot_settings_config = [
	("Quality", "quality", "MP3_320"),
	("Send zips", "zips", True),
	("Send tracks", "tracks", True),
	("Language", "lang", "en"),
	("Search Method", "search_method", "results_audio_article")
]

search_methods = [
	("results_audio", "Results in Audio"), 
	("results_article", "Results in Articles"),
	("results_audio_article", "Results Smooth ;)")
]

send_image_track_query = (
	"🎧 Track title: %s\
	\n👤 Artist: %s\
	\n💽 Album: %s\
	\n📅 Released On: %s"
)

send_image_album_query = (
	"💽 Album: %s\
	\n👤 Artist: %s\
	\n📅 Date: %s\
	\n🎧 Total Tracks: %d"
)

send_image_artist_query = (
	"👤 Artist: %s\
	\n💽 Albums: %d\
	\n👥 Fans: %d"
)

send_image_playlist_query = (
	"📅 Creation: %s\
	\n👤 User: %s\
	\n🎧 Tracks: %d\
	\n👥 Fans: %d"
)

shazam_audio_query = (
	"👤 Artist: %s\
	\nGenre: %s\
	\n💽 Album: %s\
	\nLabel: %s\
	\n📅 Release On: %s\
	\n🎧 Title: %s"
)

inline_textes = {
	"download_track": {
		"text": "⬇️ Download track 🎧"
	},

	"download_album": {
		"text": "⬇️ Download album 💽"
	},

	"download_artist": {
		"text": "⬇️ Get artist 👤"
	},

	"back": {
		"text": "BACK 🔙"
	}
}

commands_queries = {
	"s_art": {
		"query": "art: %s",
		"text": "Search by artist 👤"
	},

	"s_alb": {
		"query": "alb: %s",
		"text": "Album Search"
	},

	"s_pla": {
		"query": "pla: %s",
		"text": "Playlist Search"
	},

	"s_trk": {
		"query": "trk: %s",
		"text": "Track Search"
	},

	"s_global": {
		"query": "%s",
		"text": "Global Search"
	}
}

artist_commands_queries = {
	"top": {
		"query": "%s:top",
		"text": "TOP 30 🔝"
	},

	"albums": {
		"query": "%s:albums",
		"text": "ALBUMS 💽"
	},

	"related": {
		"query": "%s:related",
		"text": "RELATED 🗣"
	},

	"radio": {
		"query": "%s:radio",
		"text": "RADIO 📻"
	},

	"playlists": {
		"query": "%s:playlists",
		"text": "PLAYLISTS 📂"
	}
}
