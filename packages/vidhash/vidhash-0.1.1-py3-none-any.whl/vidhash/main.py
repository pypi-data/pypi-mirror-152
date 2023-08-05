import dataclasses
import glob
import os
import pathlib
import subprocess
import uuid
from multiprocessing.pool import ThreadPool
from typing import TYPE_CHECKING

import ffmpy3
from PIL import Image


if TYPE_CHECKING:
    from typing import Tuple, Iterator, Optional, Dict, List, Set
    import imagehash
    from vidhash.hash_options import HashOptions
    from vidhash.match_options import MatchOptions

TEMP_DIR = "temp/"


@dataclasses.dataclass
class VideoHash:
    image_hashes: List[imagehash.ImageHash]
    video_length: float
    hash_options: HashOptions

    @property
    def hash_set(self) -> Set[imagehash.ImageHash]:
        return set(self.image_hashes)

    def matching_hashes(self, other_hash: imagehash.ImageHash, hamming_dist: int = 0) -> Iterator[imagehash.ImageHash]:
        for image_hash in self.hash_set:
            if (image_hash - other_hash) <= hamming_dist:
                yield image_hash

    def contains_hash(self, other_hash: imagehash.ImageHash, hamming_dist: int = 0) -> bool:
        return any(self.matching_hashes(other_hash, hamming_dist))


async def _process_ffmpeg(ff: ffmpy3.FFmpeg) -> Tuple[str, str]:
    ff_process = await ff.run_async(stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ff_out = await ff_process.communicate()
    await ff.wait()
    output = ff_out[0].decode("utf-8", errors="replace").strip()
    error = ff_out[1].decode("utf-8", errors="replace").strip()
    return output, error


async def _run_ffmpeg(
    inputs: Dict[str, Optional[str]],
    outputs: Dict[str, Optional[str]],
    global_options: Optional[List[str]] = None,
) -> Tuple[str, str]:
    ff = ffmpy3.FFmpeg(global_options=global_options, inputs=inputs, outputs=outputs)
    return await _process_ffmpeg(ff)


async def _run_ffprobe(inputs: Dict[str, Optional[str]], global_options: Optional[List[str]] = None) -> Tuple[str, str]:
    ff = ffmpy3.FFmpeg(global_options=global_options, inputs=inputs)
    return await _process_ffmpeg(ff)


async def _decompose_video(video_path: str, decompose_path: str, fps: float, max_size: float) -> None:
    # Convert video and downscale
    output_path = pathlib.Path(TEMP_DIR) / f"{uuid.uuid4()}.mp4"
    filters = [
        f"scale='min({max_size},iw)':'min({max_size},ih)':force_original_aspect_ratio=decrease",
        "scale=trunc(iw/2)*2:trunc(ih/2)*2",
    ]
    await _run_ffmpeg(
        inputs={video_path: None},
        outputs={f"{output_path}": f"-vf \"{','.join(filters)}\""},
    )
    # Decompose it
    await _run_ffmpeg(
        inputs={f"{output_path}": None},
        outputs={f"{decompose_path}/out%d.png": f"-vf fps={fps} -vsync 0"},
        global_options=["-y"],
    )


async def _video_length(video_path: str) -> float:
    out, err = await _run_ffprobe(
        inputs={video_path: "-show_entries format=duration -of default=noprint_wrappers=1:nokey=1"},
        global_options=["-v error"],
    )
    return float(out)


async def hash_video(video_path: str, options: HashOptions) -> VideoHash:
    # Get video length
    video_length = await _video_length(video_path)
    # Decompose into images
    video_id = str(uuid.uuid4())
    decompose_path = str(pathlib.Path(TEMP_DIR) / video_id)
    await _decompose_video(video_path, decompose_path, options.fps, options.settings.video_size)
    # Hash images
    image_files = glob.glob(f"{decompose_path}/*.png")
    hash_pool = ThreadPool(os.cpu_count())
    hash_list = hash_pool.map(lambda image_path: options.settings.hash_image(Image.open(image_path)), image_files)
    # Create VideoHash and return
    return VideoHash(hash_list, video_length, options)


@dataclasses.dataclass
class CheckOptions:
    hash_options: HashOptions
    match_options: MatchOptions


async def check_match(video_path_1: str, video_path_2: str, options: CheckOptions) -> bool:
    hash1 = await hash_video(video_path_1, options.hash_options)
    hash2 = await hash_video(video_path_2, options.hash_options)
    return options.match_options.check_match(hash1, hash2)
