import logging
import datetime
import arrow

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_month = str(today.year) + "_" + str(today.month)
date = str(arrow.now().format("YYYYMMDD"))

logging.basicConfig(
    filename="E:/THANGVT/tools/arranger_v2.2/arrange-PDF-files/{foldername}.log",
    level=logging.INFO,
)
logging.debug("This message should go to the log file")
logging.info("So should this")
logging.warning("And this, too")
