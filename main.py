import youtube_dl, subprocess

video_url = "https://www.youtube.com/watch?v=gq4DYnQjWvw"
start_at = "00:01:20"
duration = "23"
video_name = "video.mp4"

with youtube_dl.YoutubeDL({'format': 'best'}) as ydl:
    result = ydl.extract_info(video_url, download=False)
    video = result['entries'][0] if 'entries' in result else result

actual_download_url = video['url']
get_video = 'ffmpeg -ss %s  -t %s -i "%s" %s' % (start_at, duration, actual_download_url, video_name)
subprocess.call(get_video)
