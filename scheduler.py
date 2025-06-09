import logging
import schedule
import time

def run_scheduler():
    logging.info("Scheduler started.")
    while True:
        schedule.run_pending()
        time.sleep(1)