#!/usr/bin/env python

######################################################
#
# shopper - check for deals on your shopping preferences
# written by Petar Petkov (petkov.generali@gmail.com)
#
######################################################

import os
import sqlite3
import datetime

from tqdm import tqdm


db_path = os.path.join(ROOT_DIR, 'db.sqlite3')
sqlite_file = os.path.join(db_path)
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


print("Hello World!")