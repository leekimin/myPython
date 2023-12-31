import eyed3
import time, os
from pathlib import Path

class Music:
    artist : str # 상위 폴더명이라 아티스트 또는 앨범명
    track : str 
    full_path : str

    def __init__(self, artist, track, full_path) -> None:
        self.artist = artist
        self.track = track
        self.full_path = full_path

    def debug(self):
        print('*' * 40, 'debug')
        print('* artist : ', self.artist)
        print('* track : ', self.track)
        print('* full_path : ', self.full_path)

arrFileList = list()
arrFolderList = list()

def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            listdirs(it)
            d = Music(it.name, 0, it.path)
            arrFolderList.append(d)
        if it.is_file() and (it.name.find('.mp3') > -1 or it.name.find('.flac') > -1):
            p = Path(it.path)
            n, e = os.path.splitext(it.name)
            m = Music(p.parent.name, n, it.path)
            arrFileList.append(m)

def get_spotify_search():
    print('api')

def duration_from_seconds(s):
    """Module to get the convert Seconds to a time like format."""
    s = s
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    TIMELAPSED  = f"{d:03.0f}:{h:02.0f}:{m:02.0f}:{s:02.0f}"
    return TIMELAPSED

def track_info(mp3_path):
    mp3 = eyed3.load(mp3_path)
    tag = mp3.tag
    a = mp3
    print("# {}".format('=' * 78))
    print("Track Name:     {}".format(tag.title))
    print("Track Images:     {}".format(tag.images))
    print("Track Artist:   {}".format(tag.artist))
    print("Track Album:    {}".format(tag.album))
    print("Track Duration: {}".format(duration_from_seconds(a.info.time_secs)))
    print("Track Number:   {}".format(tag.track_num))
    print("Track BitRate:  {}".format(a.info.bit_rate))
    print("Track BitRate:  {}".format(a.info.bit_rate_str))
    print("Sample Rate:    {}".format(a.info.sample_freq))
    print("Mode:           {}".format(a.info.mode))
    print("# {}".format('=' * 78))
    print("Album Artist:         {}".format(tag.album_artist))
    print("Album Year:           {}".format(tag.getBestDate()))
    print("Album Recording Date: {}".format(tag.recording_date))
    print("Album Type:           {}".format(tag.album_type))
    print("Disc Num:             {}".format(tag.disc_num))
    print("Artist Origin:        {}".format(tag.artist_origin))
    print("# {}".format('=' * 78))
    print("Artist URL:         {}".format(tag.artist_url))
    print("Audio File URL:     {}".format(tag.audio_file_url))
    print("Audio Source URL:   {}".format(tag.audio_source_url))
    print("Commercial URL:     {}".format(tag.commercial_url))
    print("Copyright URL:      {}".format(tag.copyright_url))
    print("Internet Radio URL: {}".format(tag.internet_radio_url))
    print("Publisher URL:      {}".format(tag.publisher_url))
    print("Payment URL:        {}".format(tag.payment_url))
    print("# {}".format('=' * 78))
    print("Publisher: {}".format(tag.publisher))
    print("Original Release Date: {}".format(tag.original_release_date))
    print("Play Count: {}".format(tag.play_count))
    print("Tagging Date: {}".format(tag.tagging_date))
    print("Release Date: {}".format(tag.release_date))
    print("Terms Of Use: {}".format(tag.terms_of_use))
    print("isV1: {}".format(tag.isV1()))
    print("isV2: {}".format(tag.isV2()))
    print("BPM: {}".format(tag.bpm))
    print("Cd Id: {}".format(tag.cd_id))
    print("Composer: {}".format(tag.composer))
    print("Encoding date: {}".format(tag.encoding_date))
    print("# {}".format('=' * 78))
    print("Genre: {}".format(tag.genre.name))
    print("Non Std Genre Name: {}".format(tag.non_std_genre.name))
    print("Genre ID: {}".format(tag.genre.id))
    print("Non Std Genre ID: {}".format(tag.non_std_genre.id))
    print("LAME Tag:       {}".format(a.info.lame_tag))
    print("# {}".format('=' * 78))
    print("Header Version: {}".format(tag.header.version))
    print("Header Major Version: {}".format(tag.header.major_version))
    print("Header Minor Version: {}".format(tag.header.minor_version))
    print("Header Rev Version: {}".format(tag.header.rev_version))
    print("Header Extended: {}".format(tag.header.extended))
    print("Header Footer: {}".format(tag.header.footer))
    print("Header Experimental: {}".format(tag.header.experimental))
    print("Header SIZE: {}".format(tag.header.SIZE))
    print("Header Tag Size: {}".format(tag.header.tag_size))
    print("Extended Header Size: {}".format(tag.extended_header.size))
    print("# {}".format('=' * 78))
    print("File Name: {}".format(tag.file_info.name))
    print("File Tag Size: {}".format(tag.file_info.tag_size))
    print("File Tag Padding Size: {}".format(tag.file_info.tag_padding_size))
    print("File Read Only: {}".format(tag.read_only))
    print("File Size: {}".format(a.info.size_bytes))
    print("Last Modified: {}".format(time.strftime('%Y-%m-%d %H:%M:%S',
                                     time.localtime(tag.file_info.mtime))))
    print("Last Accessed: {}".format(time.strftime('%Y-%m-%d %H:%M:%S',
                                     time.localtime(tag.file_info.atime))))
    print("# {}".format('=' * 78))