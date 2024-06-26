import schedule
import threading
import pytz

def dine_job(dining_type):
    print(dining_type)

class DineMServer: 
    def __init__(self, job): 
        self.server_lock = threading.Lock()
        self.send_task_cv = threading.Condition(self.server_lock)
        self.running = False 
        self.shutdown = False
        self.send_job = job

        for menu, timing in [("breakfast", "6:30"), ("lunch", "10:00"), ("dinner", "14:00")]:
            thread = threading.Thread(target=self.run_send_task, args=(menu, timing))
            thread.daemon = True
            thread.start()

    def status(self): 
        with self.server_lock:
            return "Server Status: " + "running" if self.running else "not running"
    
    def run(self): 
        with self.server_lock:
            self.running = True
            self.send_task_cv.notify_all()
    
    def stop(self):
        with self.server_lock:
            self.running = False 

    def shutdown(self): 
        with self.server_lock: 
            self.shutdown = True
            self.send_task_cv.notify_all()

    def run_send_task(self, dining_type, time): 

        # schedule.every().second.do(self.send_job, dining_type)
        # schedule.every().day.at(time, "America/").do(self.send_job, dining_type)
        timezone = pytz.timezone("America/Detroit")
        schedule.every().day.at(time, timezone).do(self.send_job, dining_type)  

        while True: 
            with self.send_task_cv: 
                while not self.running and not self.shutdown: 
                    print("self is sleeping")
                    self.send_task_cv.wait()
                
                if self.shutdown: 
                    print("Shutting down thread", dining_type, time)
                    return 
                
                schedule.run_pending()
    
    def __del__(self): 
        self.shutdown()
        print("Server is shutting down")