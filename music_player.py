class MusicPlayer:

    def __init__(self):
        self.cur_song_index = -1
        self.name_of_songs = []
        self.audio_files = []

    @staticmethod
    def instance():
        ...
