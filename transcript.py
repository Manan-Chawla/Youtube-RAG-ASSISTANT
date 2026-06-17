# from youtube_transcript_api import YouTubeTranscriptApi
# import re


# def extract_video_id(url):
#     pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
#     match = re.search(pattern, url)

#     if match:
#         return match.group(1)

#     return None


# def get_transcript(youtube_url):

#     video_id = extract_video_id(youtube_url)

#     ytt_api = YouTubeTranscriptApi()

#     fetched_transcript = ytt_api.fetch(video_id)

#     text = " ".join(
#         snippet.text
#         for snippet in fetched_transcript
#     )

#     return text






import re
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)

    if match:
        return match.group(1)

    return None


def clean_text(text):

    text = re.sub(r"\[.*?\]", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def get_transcript(youtube_url):

    video_id = extract_video_id(youtube_url)

    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    text = " ".join(
        snippet.text
        for snippet in transcript
    )

    return clean_text(text)