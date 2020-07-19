import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image


source_path = os.path.join(SAMPLE_INPUTS, "sample.mp4")
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
thumbnail_per_half_second_dir = os.path.join(
    SAMPLE_OUTPUTS, "thumbnails-per-half-second"
)
os.makedirs(thumbnail_dir, exist_ok=True)
os.makedirs(thumbnail_per_frame_dir, exist_ok=True)
os.makedirs(thumbnail_per_half_second_dir, exist_ok=True)

clip = VideoFileClip(source_path)  # VideoFileClip is from the moviepy
# print(clip.reader.fps)  # frames per second
# print(clip.reader.nframes)  # number of frames in the clip
# print(clip.duration)  # seconds
# print(clip.reader.nframes / clip.reader.fps)  # also gives the duration of the clip
# print(clip.duration) # clip.reader.duration
duration = int(clip.duration)
for i in range(0, duration + 1):
    # this loop creates frame for every single second
    frame = clip.get_frame(int(i))
    # print(frame)  # np.array numpy array # inference
    new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
    # print(f"frame at {i} seconds saved at {new_img_filepath}")
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)

fps = clip.reader.fps  # frames per seconds
nframes = clip.reader.nframes  # number of frames in a clip
seconds = nframes / (fps * 1.0)


for i, frame in enumerate(clip.iter_frames()):
    if (
        i % fps == 0
    ):  # the frame that satisfies the condition,gives us the frame at every second
        current_ms = int((i / fps) * 1000)  # current duration in the clip
        # this loop creates frame based on the actual number of frames
        new_img_filepath = os.path.join(thumbnail_per_frame_dir, f"{current_ms}.jpg")
        # print(f"frame at {i} seconds saved at {new_img_filepath}")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)


for i, frame in enumerate(clip.iter_frames()):
    fphs = int(fps / 2.0)  # frames per half second
    if (
        i % fphs == 0
    ):  # the frame that satisfies the condition,gives us the frame at every second
        current_ms = int((i / fps) * 1000)  # current duration in the clip
        # this loop creates frame based on the actual number of frames
        new_img_filepath = os.path.join(
            thumbnail_per_half_second_dir, f"{current_ms}.jpg"
        )
        # print(f"frame at {i} seconds saved at {new_img_filepath}")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)
