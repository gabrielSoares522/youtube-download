import yt_dlp
from yt_dlp.utils import download_range_func
import os

'''
yt_opts = {
    'verbose': True,
#   'download_ranges': download_range_func(None, [(start_time, end_time)]),
    'download_ranges': lambda info_dict, yt_instance: [ {'start_time': 2, 'end_time': 7, 'title': 'first_section'}, ],
    'force_keyframes_at_cuts': True,
}
'''

os.system('cls' if os.name == 'nt' else 'clear')

option = input("Select with type of download (1)video (2)audio: ")

if option == '1':
    yt_opts = {
        'force_keyframes_at_cuts': True,
    }

if option == '2':
    yt_opts = {
        'format': 'bestaudio/best',
        'force_keyframes_at_cuts': True,
    }


link = input("Type the video link: ")


with yt_dlp.YoutubeDL(yt_opts) as ydl:
    error_code = ydl.download(link)

print('Some videos failed to download' if error_code
      else 'All videos successfully downloaded')