import colors

def succes_alert(msg,bold=False,newline=False):
    if newline is True:
        prefix="\n"
    else:
        prefix = ""
    print (f'{prefix}{colors.BOLD if bold else colors.BOLDOFF}[{colors.GREEN}+{colors.WHITE}]{colors.WHITE} {msg} {colors.ENDC}')
def info_alert(msg,bold=False,newline=False):
    if newline is True:
        prefix="\n"
    else:
        prefix = ""
    print (f'{prefix}{colors.BOLD if bold else colors.BOLDOFF}[{colors.INFOCOLOR}i{colors.WHITE}]{colors.WHITE} {msg} {colors.ENDC}')
def succes_msg(msg,bold=False):
    return (f'\r[{colors.GREEN}+{colors.WHITE}]{colors.WHITE} {msg} {colors.ENDC}')


def error_alert(msg,bold=False,newline=False):
    if newline is True:
        prefix="\n"
    else:
        prefix = ""
    print (f'{prefix}{colors.BOLD if bold else colors.BOLDOFF}[{colors.RED}!{colors.WHITE}]{colors.WHITE} {msg} {colors.ENDC}')
