import pynvml

pynvml.nvmlInit()

DEVICE_INDEX = 0  # your 3080
_handle = pynvml.nvmlDeviceGetHandleByIndex(DEVICE_INDEX)


def free_vram_mb() -> int:
    info = pynvml.nvmlDeviceGetMemoryInfo(_handle)
    return info.free // (1024 * 1024)


def total_vram_mb() -> int:
    info = pynvml.nvmlDeviceGetMemoryInfo(_handle)
    return info.total // (1024 * 1024)


def gpu_utilization() -> int:
    rates = pynvml.nvmlDeviceGetUtilizationRates(_handle)
    return rates.gpu  # percentage 0-100
