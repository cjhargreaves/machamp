CC = gcc
NVML_INCLUDE = /usr/local/cuda/include
NVML_LIB = /usr/local/cuda/lib64

libgpu.so: gpu.c
	$(CC) -shared -fPIC -o libgpu.so gpu.c \
		-I$(NVML_INCLUDE) \
		-L$(NVML_LIB) -lnvidia-ml

clean:
	rm -f libgpu.so
