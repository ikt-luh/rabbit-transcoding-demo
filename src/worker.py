import os, sys
import csv
import time
import yaml
import argparse
from pathlib import Path
from itertools import product
from rabbit import Transcoder, TranscoderConfig, BitstreamIO


class Worker():
    def __init__(self, codec="x265"):
        self.use_cuda = (codec == "nvenc")
        self.preset = "p1" if self.use_cuda else "ultrafast"

        config = TranscoderConfig(
                        use_cuda=self.use_cuda,
                        geometry_qp=32,
                        attribute_qp=32,
                        preset=self.preset,
                    )
        self.transcoder = Transcoder(config)
        self.io = BitstreamIO()

    def transcode(self, in_path, out_path, coding_config):
        geoQP = coding_config["geoQP"]
        attQP = coding_config["attQP"]
        config = TranscoderConfig(
                        use_cuda=self.use_cuda,
                        geometry_qp=geoQP,
                        attribute_qp=attQP,
                        preset=self.preset,
                    )
        ctxs = self.io.read(in_path)

        self.transcoder.set_config(config)
        self.transcoder.transcode_contexts(ctxs)

        self.io.write(ctxs, out_path)

