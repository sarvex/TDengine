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
from clusterSetup import *
from util.sql import tdSql
from util.log import tdLog
import random

class ClusterTestcase:
    
    ## test case 24, 25, 26, 27 ##
    def run(self):
        
        nodes = Nodes()
        ctest = ClusterTest(nodes.node1.hostName)
        ctest.connectDB()
        ctest.createSTable(1)
        ctest.run()
        tdSql.init(ctest.conn.cursor(), False)


        tdSql.execute(f"use {ctest.dbName}")
        tdSql.execute(f"alter database {ctest.dbName} replica 3")

        for i in range(100):
            tdSql.execute("drop table t%d" % i)

        for i in range(100):
            tdSql.execute("create table a%d using meters tags(1)" % i)

        tdSql.execute("alter table meters add col col5 int")
        tdSql.execute("alter table meters drop col col5 int")
        tdSql.execute(f"drop database {ctest.dbName}")

        tdSql.close()
        tdLog.success(f"{__file__} successfully executed")

ct = ClusterTestcase()
ct.run()
