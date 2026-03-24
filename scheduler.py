import subprocess
import threading
import time
from datetime import datetime
from typing import Dict, List

from job import Job, JobStatus


class Scheduler:
    def __init__(self):
        self.queue: List[Job] = []
        self.jobs: Dict[str, Job] = {} 
        self.lock = threading.Lock()
        self._running = False
        self._worker_thread = None

    def submit(self, command: str) -> Job:
        job = Job(command=command)
        with self.lock:
            self.queue.append(job)
            self.jobs[job.id] = job
        print(f"Submitted: {job}")
        return job

    def status(self) -> None:
        with self.lock:
            jobs = list(self.jobs.values())
        if not jobs:
            print("No jobs.")
            return
        for job in jobs:
            print(job)

    def start(self) -> None:
        self._running = True
        self._worker_thread = threading.Thread(target=self._worker_loop, daemon=True)
        self._worker_thread.start()
        print("Scheduler started. Press Ctrl+C to stop.")

    def stop(self) -> None:
        self._running = False

    def _worker_loop(self) -> None:
        while self._running:
            job = self._next_job()
            if job:
                self._run(job)
            else:
                time.sleep(0.5)

    def _next_job(self) -> Job | None:
        with self.lock:
            if self.queue:
                return self.queue.pop(0)
        return None

    def _run(self, job: Job) -> None:
        job.status = JobStatus.RUNNING
        job.started_at = datetime.now()
        print(f"\n→ Starting [{job.id}]: {job.command}")

        try:
            result = subprocess.run(job.command, shell=True)
            job.exit_code = result.returncode
            job.status = JobStatus.DONE if result.returncode == 0 else JobStatus.FAILED
        except Exception as e:
            print(f"  Error: {e}")
            job.status = JobStatus.FAILED
        finally:
            job.finished_at = datetime.now()

        print(f"← Finished [{job.id}]: {job.status.value} in {job.duration():.1f}s")
