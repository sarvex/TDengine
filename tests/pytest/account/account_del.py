###################################################################
#           Copyright (c) 2016 by TAOS Technologies, Inc.
#                     All rights reserved.
#
#  This file is proprietary and confidential to TAOS Technologies.
#  No part of this file may be reproduced, stored, transmitted,
#  disclosed or used in any form or by any means other than as
#  expressly provided by the written permission from Jianhui Tao
#
###################################################################

# -*- coding: utf-8 -*-

import sys
import taos
from util.log import tdLog
from util.cases import tdCases
from util.sql import tdSql


class TDTestCase:
    def init(self, conn, logSql):
        tdLog.debug(f"start to execute {__file__}")
        tdSql.init(conn.cursor(), logSql)

    def run(self):
        print("==========step1")
        print("drop built-in account")
        try:
            tdSql.execute("drop account root")
        except Exception as e:
            if len(e.args) > 0 and e.args[0] != 'no rights':
                tdLog.exit(e)

        print("==========step2")
        print("drop built-in user")
        try:
            tdSql.execute("drop user root")
        except Exception as e:
            if len(e.args) > 0 and e.args[0] != 'no rights':
                tdLog.exit(e)
            return

        tdLog.exit("drop built-in user is error.")

    def stop(self):
        tdSql.close()
        tdLog.success(f"{__file__} successfully executed")


tdCases.addWindows(__file__, TDTestCase())
tdCases.addLinux(__file__, TDTestCase())
