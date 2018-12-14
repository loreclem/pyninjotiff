import os
from satpy import Scene
from datetime import datetime
from satpy.utils import debug_on
import pyninjotiff
from glob import glob
from pyresample.utils import load_area
import copy
debug_on()


chn = "C13"
ninjoRegion = load_area("areas.def", "NinJoGOESWregion")
filenames = glob("/var/tmp/cll/goes17/*")
global_scene = Scene(reader="abi_l1b", filenames=filenames)
global_scene.load([chn])
local_scene = global_scene.resample(ninjoRegion, cache_dir="/var/tmp/cll")
local_scene[chn].clip(-87.5 - 273.15, 40 - 273.15)
local_scene.save_dataset(chn, filename="goes17.tif", writer='ninjotiff',
                      sat_id=6300014,
                      chan_id=900015,
                      data_cat='GORN',
                      data_source='EUMCAST',
                      physic_unit='C',
                      ch_max_measurement_unit=40,
                      ch_min_measurement_unit=-87.5,
                      zero_seconds=True,
                      invert_colorscale=True)
