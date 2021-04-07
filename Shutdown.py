# Shutdown Center version 2.0
# Raj Sandhu

import os


# Functions
def shutdown_now():
    os.system("shutdown /s")


def restart():
    os.system("shutdown -r -t 10")


def cancel():
    os.system("shutdown /a")

# Button Functions
