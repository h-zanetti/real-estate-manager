  
import sys, os

INTERP = "/home/wwagah/repositories/virtualenvs/real-estate-manager-env/bin/python"

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from webdev.wsgi import application