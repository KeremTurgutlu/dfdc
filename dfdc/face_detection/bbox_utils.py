# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/10_bbox_utils.ipynb (unless otherwise specified).

__all__ = ['bboxes_to_original_scale', 'resize_bbox_by_scale', 'landmarks_to_original_scale']

# Cell
from fastai.vision import *

# Cell
def bboxes_to_original_scale(bboxes, H, W, sz):
    """
    convert bbox points to original image scale

    bboxes: List of numpy arrays with shape (M, 4) M: # of bbox coordinates
    """
    res = []
    for bb in bboxes:
        h_scale, w_scale = H/sz, W/sz
        orig_bboxes = (bb*array([w_scale, h_scale, w_scale, h_scale])[None, ...]).astype(int)
        res.append(orig_bboxes)
    return res

# Cell
def resize_bbox_by_scale(bb, bb_scale, H, W):
    """
    resize a bbox with a given scale parameter

    bb: a bounding box with (left, top, right, bottom) values
    """
    left, top, right, bottom = bb

    cx,cy = (top + bottom)//2, (left + right)//2
    h,w = (bottom - top), (right - left)
    sh, sw = int(h*bb_scale), int(w*bb_scale)

    stop, sbottom = cx - sh//2, cx + sh//2
    sleft, sright = cy - sw//2, cy + sw//2
    stop, sleft, sbottom, sright = max(0, stop), max(0, sleft), min(H, sbottom), min(W, sright)
    return (sleft, stop, sright, sbottom)

# Cell
def landmarks_to_original_scale(landmarks, H, W, sz):
    """
    convert landmarks to original image scale

    landmarks: List of numpy arrays with shape (M, 10) M: # landmark coordinates
    """
    res = []
    for landms in landmarks:
        h_scale, w_scale = H/sz, W/sz
        orig_landms = (landms*array([w_scale, h_scale]*5)[None, ...]).astype(int)
        res.append(orig_landms)
    return res