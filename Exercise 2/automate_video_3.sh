



#!/bin/bash
sudo x264 --output bbb_600k.264 --fps 30 --bitrate 600 --video-filter resize:width=2560,height=1440 ../bbb1.mp4
sudo MP4Box -add bbb_600k.264 -fps 30 bbb_600k.mp4
sudo MP4Box -dash 4000 -frag 4000 -rap -segment-name segment_600k_ bbb_600k.mp4








