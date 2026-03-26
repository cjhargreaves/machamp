#include <nvml.h>
#include <stdint.h>

static nvmlDevice_t device;

void gpu_init(void) {
    nvmlInit();
    nvmlDeviceGetHandleByIndex(0, &device);
}

void gpu_shutdown(void) {
    nvmlShutdown();
}

uint64_t free_vram_mb(void) {
    nvmlMemory_t mem;
    nvmlDeviceGetMemoryInfo(device, &mem);
    return mem.free / (1024 * 1024);
}

uint64_t total_vram_mb(void) {
    nvmlMemory_t mem;
    nvmlDeviceGetMemoryInfo(device, &mem);
    return mem.total / (1024 * 1024);
}

unsigned int gpu_utilization(void) {
    nvmlUtilization_t util;
    nvmlDeviceGetUtilizationRates(device, &util);
    return util.gpu;
}
