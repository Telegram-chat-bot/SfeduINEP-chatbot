from loader import DEBUG
import logging
import os
from django_admin.django_admin.settings import ROOT_DIR

filename: str = "" if DEBUG else os.path.join(ROOT_DIR, "bot.log")
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO, filename=filename)

