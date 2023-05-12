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
import time

class ClusterTestcase:
    
    ## test case 32 ##
    def run(self):
        
        nodes = Nodes()
        ctest = ClusterTest(nodes.node1.hostName)
        ctest.connectDB()
        ctest.createSTable(1)
        ctest.run()
        tdSql.init(ctest.conn.cursor(), False)

        tdSql.execute(f"use {ctest.dbName}")
        totalTime = 0
        for _ in range(10):
            startTime = time.time()
            tdSql.query(f"select * from {ctest.stbName}")
            totalTime += time.time() - startTime
        print("replica 1: avarage query time for %d records: %f seconds" % (ctest.numberOfTables * ctest.numberOfRecords,totalTime / 10))

        tdSql.execute(f"alter database {ctest.dbName} replica 3")
        tdLog.sleep(60)
        totalTime = 0
        for _ in range(10):
            startTime = time.time()
            tdSql.query(f"select * from {ctest.stbName}")
            totalTime += time.time() - startTime
        print("replica 3: avarage query time for %d records: %f seconds" % (ctest.numberOfTables * ctest.numberOfRecords,totalTime / 10))

        tdSql.close()
        tdLog.success(f"{__file__} successfully executed")

ct = ClusterTestcase()
ct.run()
