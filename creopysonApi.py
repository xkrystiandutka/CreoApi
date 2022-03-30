#https://creopyson.readthedocs.io/en/latest/usage.html?fbclid=IwAR1mCBVooqEREKZptaq_bz44eclg6QKDsKMu6hIRQBciIaiffITIPbhR1yk
#https://docs.python.org/3/library/logging.html

import creopyson
import logging

# I found out how to configure requests's logging level, it's done via the standard logging module. 
# I decided to configure it to not log messages unless they are at least warnings:

def enableLogging():
    logging.basicConfig(level=logging.DEBUG)

    ## Hide urllib3 logging
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    # Create a Client object and create a connection with Creoson
def creoConnection(
    file_path:str
) -> creopyson.Client:
    """
    Connects to creo using creopy method connect()
    If Creo is not running, the given file will be opened
    """
    creopysonClient = creopyson.Client()
    creopysonClient.connect()

    if not creopysonClient.is_creo_running():
        creopysonClient.start_creo(file_path)

    return creopysonClient

# If you are using Creo 7 you must declare it once per session to prevent errors on deprecated features:
def setCreoVersion(
    creo_cxn:creopyson.Client
) -> None:
    """
    Sets the Creo version to 7
    """
    creopyson.creo_set_creo_version(client=creo_cxn, version=7)


