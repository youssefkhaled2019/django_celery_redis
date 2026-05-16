import time

from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

@shared_task
def send_emails():
   for x in range(5):
      #   print(x)
      logger.info(f"Sending email {x}")
      time.sleep(1)

@shared_task(bind=True, max_retries=3)
def send_emails_v2(self):
   try:
         for x in range(5):
            logger.info(f"Sending email {x}")
            time.sleep(1)

   except Exception as e:
      logger.error(f"failed: {e}")  #logger.error(f"{type(e}).__name__}: {exc}")
      raise self.retry(exc=e, countdown=5)


@shared_task
def schedule_send_emails():
   for x in range(5):
      #   print(x)
      logger.info(f"Schedule- Sending email {x}")
      time.sleep(1)        