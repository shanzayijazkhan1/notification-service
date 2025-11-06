import asyncio, queue, threading

q = queue.Queue()

def start_worker():
    def run():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        while True:
            job = q.get()
            # simulate send
            # print("sending", job)
            q.task_done()
    t = threading.Thread(target=run, daemon=True); t.start()

def push(job): q.put(job)
