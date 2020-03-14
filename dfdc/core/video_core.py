# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_video_core.ipynb (unless otherwise specified).

__all__ = ['open_cv_video_reader', 'decord_cpu_video_reader', 'get_decord_video_batch_cpu', 'video_url', 'play_video']

# Cell
from fastai.vision import *
import cv2

# Cell
def open_cv_video_reader(path, freq=None):
    "optionally sample by freq and yield RGB image frames from a video"
    vidcap = cv2.VideoCapture(str(path))
    video_len = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    for i in range(video_len):
        vidcap.grab()
        if (freq is None) or (i % freq == 0):
            _, image = vidcap.retrieve()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            yield {"frame_no":i, "frame_array":image}

# Cell
from decord import VideoReader
from decord import cpu
from decord.bridge import set_bridge
set_bridge('torch')

# Cell
def decord_cpu_video_reader(path, freq=None):
    video = VideoReader(str(path), ctx=cpu())
    len_video = len(video)
    if freq: t = video.get_batch(range(0, len(video), freq))
    else: t = video.get_batch(range(len_video))
    return t, len_video

# Cell
def get_decord_video_batch_cpu(path, freq=10, sz=640, stats:Tensor=None, device=defaults.device):
    "get resized and mean substracted batch tensor of a sampled video (scale of 255)"
    t_raw, len_video = decord_cpu_video_reader(path, freq)
    H,W = t_raw.size(2), t_raw.size(3)
    t = F.interpolate(t_raw.to(device).to(torch.float32), (sz,sz))
    if stats is not None: t -= stats[...,None,None]
    return t, t_raw, (H, W), len_video

# Cell
from IPython.display import HTML
from base64 import b64encode

def video_url(fname):
    vid1 = open(fname,'rb').read()
    data_url = "data:video/mp4;base64," + b64encode(vid1).decode()
    return data_url

def play_video(fname1, fname2=None):
    url1 = video_url(fname1)
    url2 = video_url(fname2) if fname2 else None
    if url1 and url2:
        html = HTML(
            """
        <video width=450 controls>
              <source src="%s" type="video/mp4">
        </video>
        <video width=450 controls>
              <source src="%s" type="video/mp4">
        </video>

        """ % (url1, url2))
    else:
        html = HTML(
            """
        <video width=450 controls>
              <source src="%s" type="video/mp4">
        </video>
        """ % (url1))
    return html