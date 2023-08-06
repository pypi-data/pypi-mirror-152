import os
import requests as visit
from bs4 import BeautifulSoup as bs
from .version import version_number as version
from rich.console import Console
from .hopter import Tip_pta,Tip_ptb,Error_pta

console = Console()

def check_version():
  global visit
  global version
  with console.status("\033[96mDetecting in version …"):
    try:
      res = visit.get('https://hostudio123.github.io/HOPYBOX/version')
    except Exception as e:
      Error_pta('CheckError','Command','Failed to get update','check version')
  if version >= int(res.text):
    Tip_pta('Your current installed version of HOPYBOX is the latest')
  else:
    Tip_ptb('New version found on the official website of HOPYBOX')
    os.system('python3 -m pip install -U HOPYBOX')