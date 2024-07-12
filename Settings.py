""" Settings for app"""
import os

DEBUG_ENABLED = os.getenv('DEBUG_ENABLED', "false").lower() == "true"
if DEBUG_ENABLED:
    INDEX_FILE = 'index.dev.html'
else:
    INDEX_FILE = 'index.html'
DIRNAME = os.path.dirname(__file__)
APP_ROOT = os.environ.get('APP_ROOT', '')
if APP_ROOT.strip('/') != '':
    APP_ROOT = r'/{}/'.format(os.environ['APP_ROOT'])
    # Ensure string is like "/APP_ROOT" without trailing slash :
    APP_ROOT = os.path.normpath(APP_ROOT)
STATIC_PATH = os.path.join(DIRNAME, 'static')
TEMPLATE_PATH = os.path.join(DIRNAME, 'templates')
import logging
# log linked to the standard error stream
LOG_LEVEL = logging.DEBUG if DEBUG_ENABLED else logging.WARNING
logging.basicConfig(level=LOG_LEVEL,
                    format='%(asctime)s - %(levelname)-8s - %(message)s',
                    datefmt='%d/%m/%Y %Hh%Mm%Ss')
# console = logging.StreamHandler(sys.stderr)
