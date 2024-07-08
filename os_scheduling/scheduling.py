class Process:


    def __init__(self, 
                 process_id,
                 arrival_time, 
                 burst_time, 
                 deadline):

        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.deadline = deadline
        self.start = None
        self.end = None



def FIFO(processes):
    current_time = 0
    
    for process in processes:

        if current_time < process.arrival_time :
            current_time = process.arrival_time

        process.start = current_time
        current_time += process.burst_time 

        process.end = current_time
        print(f"Process {process.pid} finished at {process.finish_time}")

""" def SJN(processes):

    current_time = 0
    waiting_list = []

    while processes or waiting_list:
         """


def main():

    processes = [
        Process(1, 0, 8, 12),
        Process(2, 1, 4, 10),
        Process(3, 2, 9, 15),
        Process(4, 3, 5, 8),
    ]

    print("FIFO: ")
    FIFO(processes.copy())