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
import random
from util.log import *
from util.cases import *
from util.sql import *
from util.dnodes import tdDnodes


class TDTestCase:
    def init(self, conn, logSql):
        tdLog.debug(f"start to execute {__file__}")
        tdSql.init(conn.cursor(), logSql)

    def run(self):
        tdSql.prepare()

        flagList=["debugflag", "cdebugflag", "tmrDebugFlag", "uDebugFlag", "rpcDebugFlag"]

        for flag in flagList:
            tdSql.execute(f"alter local {flag} 131")
            tdSql.execute(f"alter local {flag} 135")
            tdSql.execute(f"alter local {flag} 143")
            randomFlag = random.randint(100, 250)
            if randomFlag not in [131, 135, 143]:
                tdSql.error("alter local %s %d" % (flag, randomFlag))

        tdSql.query("show dnodes")
        dnodeId = tdSql.getData(0, 0)

        for flag in flagList:
            tdSql.execute("alter dnode %d %s 131" % (dnodeId, flag))
            tdSql.execute("alter dnode %d %s 135" % (dnodeId, flag))
            tdSql.execute("alter dnode %d %s 143" % (dnodeId, flag)) 

    def stop(self):
        tdSql.close()
        tdLog.success(f"{__file__} successfully executed")


tdCases.addWindows(__file__, TDTestCase()) 
tdCases.addLinux(__file__, TDTestCase())
