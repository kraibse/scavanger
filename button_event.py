#-------------------------------------------------------------------------------
# Author:      schmmar1857
# Created:     27.11.2024
# Version:     1
#-------------------------------------------------------------------------------

from globals import *

def toggle_shop():
    global shop_active
    shop_active = not shop_active
    print(shop_active)