  
import sys, os

INTERP = "/home/hermes/repositories/virtualenvs/casas-de-hermes-venv/bin/python"

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from webdev.wsgi import application