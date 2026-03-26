# GPU Task Scheduler

A task scheduler for GPU workloads. Accepts job submissions via CLI, tracks GPU VRAM usage via NVML, and only runs a job when enough VRAM is available.

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Build the GPU library (requires CUDA toolkit):

```bash
cd gpu && make
```

## Usage

```bash
python cli.py
```

```
> submit python train.py --vram 4000
> submit python inference.py --vram 2000
> status
> quit
```

`--vram` is the amount of VRAM in MB the job needs. The scheduler will hold the job until that much is free.
