# Overview
Utilities to handle video from camera. Contains various utilites that crop and split the video files.

# Installation
In your virtual env do
```
$ pip install videoutils
```

# Scripts
The following scripts are provided by the package.
* video_capture.py
  * Captures a video from a camera to mp4 file on disk.
* video_split.py
  * Splits a mp4 file into frames stored as png file on output dir.
* video_merge.py
  * Merges the frames in png file from dir to a video file.
* video_crop.py
  * Crops a video file from frame number i to j.

# Developing VideoUtils
To install videoutils along with the tools you need to develop and run tests, run the following
in your virtual env.
```commandline
$ pip install -e .[dev]
```
