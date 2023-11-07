import os

from pydub import AudioSegment
from mutagen.id3 import ID3
from io import BytesIO
from PIL import Image


class AudioFile:

    def __init__(self, name_file):

        sound = AudioSegment.from_file(name_file)

        # sound._data is a bytestring
        raw_data = sound._data
        bytes_per_sample = sound.sample_width

        self.data = self.__get_data(raw_data, bytes_per_sample)

        music1 = ID3(name_file)

        self.name = None
        self.album_image = None

        try:
            self.name = music1.getall('TIT2')[0]
        except:
            self.name = os.path.basename(name_file)

        size_image = (200, 200)
        try:
            image_data = music1.getall("APIC")[0].data

            self.album_image = Image.open(BytesIO(image_data)).resize(size_image)
        except:
            self.album_image = Image.open("base_image.png").resize(size_image)

    @property
    def Data(self):
        return self.data

    @property
    def Image(self):
        return self.album_image

    def __get_data(self, bytes_of_samples, bytes_per_sample=1):

        data = []
        for i in range(bytes_per_sample - 1, len(bytes_of_samples), bytes_per_sample):
            data.append(int.from_bytes(bytes_of_samples[i:i + bytes_per_sample], "big"))

        return data
