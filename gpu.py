import ctypes
import os

_lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "libgpu.so"))

_lib.gpu_init.restype = None
_lib.gpu_shutdown.restype = None
_lib.free_vram_mb.restype = ctypes.c_uint64
_lib.total_vram_mb.restype = ctypes.c_uint64
_lib.gpu_utilization.restype = ctypes.c_uint

_lib.gpu_init()


def free_vram_mb() -> int:
    return _lib.free_vram_mb()


def total_vram_mb() -> int:
    return _lib.total_vram_mb()


def gpu_utilization() -> int:
    return _lib.gpu_utilization()


def shutdown() -> None:
    _lib.gpu_shutdown()
