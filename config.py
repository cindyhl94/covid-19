import glob
import logging
import logging.handlers
import sys
import traceback

db_info1 = {
    'db' : 'content',
    'coll' : 'articles13'
}


logfile = "data.log"
data_logger = logging.getLogger('root')
data_logger.setLevel(10)
FORMAT = "%(levelname)s:%(asctime)s:[%(filename)s:%(lineno)s - %(funcName)s() ] %(message)s"
handler = logging.handlers.RotatingFileHandler(
              logfile, maxBytes = 10000000, backupCount = 0)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

data_logger.addHandler(handler)
data_logger.disabled = False

#FIRESTORE_SERVICE_ACCOUNT_JSON="src/common/qbit-stats-firebase-adminsdk-2t0h4-f131c35cb7.json"
#FIRESTORE_SERVICE_ACCOUNT_JSON="src/common/smackd-219314-b4a65df32a70.json"

coll = "news"
uri = "mongodb://localhost:53065/"
db_name = "qbit"
