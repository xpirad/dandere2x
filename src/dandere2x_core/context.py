"""
Name: Dandere2X Frame
Author: CardinalPanda
Date Created: 5-4-2019
Last Modified: 5-4-2019

Description:

Have all the variables used in Dandere2x stored in here
and have this class be passed to scripts
rather than passing like 8-9 variables
"""

import configparser
import os
from dandere2x_core.dandere2x_utils import get_seconds_from_time
import logging


# init is pretty messy at the moment. I'll look into
# cleaning this up in the future ;-;
class Context:

    def __init__(self, config_file: str):
        config = configparser.ConfigParser()
        config.read(config_file)

        self.this_folder = os.path.dirname(os.path.realpath(__file__)) + os.path.sep

        # directories
        self.waifu2x_caffe_cui_dir = config.get('dandere2x', 'waifu2x_caffe_cui_dir')
        self.model_dir = config.get('dandere2x', 'model_dir')

        self.workspace = config.get('dandere2x', 'workspace')
        self.dandere2x_cpp_dir = config.get('dandere2x', 'dandere2x_cpp_dir')
        self.ffmpeg_dir = config.get('dandere2x', 'ffmpeg_dir')
        self.file_dir = config.get('dandere2x', 'file_dir')
        self.waifu2x_type = config.get('dandere2x', 'waifu2x_type')

        self.waifu2x_conv_dir = config.get('dandere2x', 'waifu2x_conv_dir')
        self.waifu2x_conv_dir_dir = config.get('dandere2x', 'waifu2x_conv_dir_dir')

        if '[this]' in self.waifu2x_conv_dir:
            self.waifu2x_conv_dir = self.waifu2x_conv_dir.replace('[this]', self.this_folder)

        if '[this]' in self.waifu2x_conv_dir_dir:
            self.waifu2x_conv_dir_dir = self.waifu2x_conv_dir_dir.replace('[this]', self.this_folder)

        # parse [this] for release versions (removing this feature in the future, just for early testing.

        if '[this]' in self.waifu2x_caffe_cui_dir:
            self.waifu2x_caffe_cui_dir = self.waifu2x_caffe_cui_dir.replace('[this]', self.this_folder)

        if '[this]' in self.workspace:
            self.workspace = self.workspace.replace('[this]', self.this_folder)

        if '[this]' in self.dandere2x_cpp_dir:
            self.dandere2x_cpp_dir = self.dandere2x_cpp_dir.replace('[this]', self.this_folder)

        if '[this]' in self.ffmpeg_dir:
            self.ffmpeg_dir = self.ffmpeg_dir.replace('[this]', self.this_folder)

        if '[this]' in self.file_dir:
            self.file_dir = self.file_dir.replace('[this]', self.this_folder)

        if '[this]' in self.model_dir:
            self.model_dir = self.model_dir.replace('[this]', self.this_folder)
        # linux
        self.dandere_dir = config.get('dandere2x', 'dandere_dir')

        # User Settings
        self.time_frame = config.get('dandere2x', 'time_frame')
        self.duration = config.get('dandere2x', 'duration')
        self.audio_layer = config.get('dandere2x', 'audio_layer')
        self.frame_rate = config.get('dandere2x', 'frame_rate')
        self.width = config.get('dandere2x', 'width')
        self.height = config.get('dandere2x', 'height')
        self.block_size = int(config.get('dandere2x', 'block_size'))
        self.tolerance = config.get('dandere2x', 'tolerance')
        self.step_size = config.get('dandere2x', 'step_size')
        self.bleed = config.get('dandere2x', 'bleed')
        self.quality_low = int(config.get('dandere2x', 'quality_low'))
        self.quality_high = int(config.get('dandere2x', 'quality_high'))

        # waifu2x settings
        self.noise_level = config.get('dandere2x', 'noise_level')
        self.scale_factor = config.get('dandere2x', 'scale_factor')
        self.process_type = config.get('dandere2x', 'process_type')
        self.extension_type = config.get('dandere2x', 'extension_type')
        self.audio_type = config.get('dandere2x', 'audio_type')

        # setup directories
        self.input_frames_dir = self.workspace + "inputs" + os.path.sep
        self.differences_dir = self.workspace + "differences" + os.path.sep
        self.upscaled_dir = self.workspace + "upscaled" + os.path.sep
        self.correction_data_dir = self.workspace + "correction_data" + os.path.sep
        self.merged_dir = self.workspace + "merged" + os.path.sep
        self.inversion_data_dir = self.workspace + "inversion_data" + os.path.sep
        self.pframe_data_dir = self.workspace + "pframe_data" + os.path.sep
        self.debug_dir = self.workspace + "debug" + os.path.sep
        self.log_dir = self.workspace + "logs" + os.path.sep
        self.frame_count = get_seconds_from_time(self.duration) * int(self.frame_rate)

        logging.basicConfig(filename='dandere2x.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self.mse_min = 0
        self.mse_max = 0

        # Bleed has not changed
        self.bleed = 1