import os
import sys

# Window
WIDTH = 1280
HEIGHT = 720
TITLE = "2d animation"
FPS = 24

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def resource_path(relative_path):
    base_path = os.path.abspath(".")

    return os.path.join(ROOT_DIR, relative_path)
