from sys import argv
from os import system, popen, chdir
import os.path
from . import messager

@messager.log_it
def main():
    mypath = os.path.dirname(os.path.abspath(__file__))
    print(mypath)
    chdir(mypath)
    cmd = argv[1]
    if cmd == 'gui':
        opt = argv[2] if len(argv) == 3 else ''
        if opt == '':
            #popen('pythonw NewFTP.pyw')
            from .NewFTP import main
            main()
        if opt == 'config':
            system('explorer config.yaml')
        if opt == 'style.show':
            system('explorer Styles')
    ##    if opt == 'style.install':
    ##        import shutil
    ##        file = argv[3]
    ##        if os.path.isfile(file):
    ##            filename = os.path.split(file)
    ##            shutil.copy2(file,os.path.expanduser('~/.NewFTP/Styles/'))
    ##        if os.isdir(file):

        if opt == 'log.show':
            system('explorer gui_log.txt')
main()