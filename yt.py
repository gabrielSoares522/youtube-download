import yt_dlp
import ffmpeg
from yt_dlp.utils import download_range_func
import os
import sys

'''
yt_opts = {
    'verbose': True,
#   'download_ranges': download_range_func(None, [(start_time, end_time)]),
    'download_ranges': lambda info_dict, yt_instance: [ {'start_time': 2, 'end_time': 7, 'title': 'first_section'}, ],
    'force_keyframes_at_cuts': True,
}
'''
try:
    arg = sys.argv[1]
except:
    arg = None

link = ''


yt_opts = {
    'verbose': True,
    'format': 'm4a/bestaudio/best',
    'writethumbnail': True,
    'embedthumbnail': True,
    'postprocessors': [{
        'key': 'FFmpegMetadata',
        'add_metadata': True,
    },
    {
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
        'preferredquality' : 'best',
    },
    {
        'key': 'EmbedThumbnail',
    },
    ]
}

if arg is None: 
    os.system('cls' if os.name == 'nt' else 'clear')

    option = input("Select with type of download (1)video (2)audio: ")

    if option == '1':
        yt_opts = {
            'force_keyframes_at_cuts': True,
            'write_thumbnail': True,
            'embed_thumbnail': True,
            'js_runtimes': {'deno': {'path': None}}
        }
        link = input("Type the video link: ")
    else:
        if option == '2':
            link = input("Type the video link: ")
        else: 
            link = option
else:
    link = arg

with yt_dlp.YoutubeDL(yt_opts) as ydl:
    error_code = ydl.download(link)

print('Some videos failed to download' if error_code
      else 'All videos successfully downloaded')