from src.calculator import *
from src.permutator import *
from src.user_interactor import *

from queue import Queue
from concurrent.futures import ThreadPoolExecutor, as_completed



interactor = Interactor()

interactor.start()

possible_sequences: Queue = (Permutator((interactor.num_1, interactor.num_2, interactor.num_3, interactor.num_4))
                             .get_possible_sequence())

executor = ThreadPoolExecutor(max_workers=12)
futures = []

while True:
    try:
        processing_sequence = possible_sequences.get(timeout=1)
        futures.append(executor.submit(Calculator(processing_sequence).run))

    except queue.Empty:
        executor.shutdown()
        break

for future in as_completed(futures):
    res = future.result()
    if res != "":
        interactor.set_result(res)
        break

interactor.set_no_result()
