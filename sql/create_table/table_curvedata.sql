-- 创建表curvedata20180410
CREATE TABLE `curvedata20180410` (
`teNumber` int(9) NOT NULL COMMENT '终端地址',
`measurePoint` int(4) NOT NULL COMMENT '终端测量点号',
`gatherTime` datetime DEFAULT NULL COMMENT '采集时间',
`gatherType` tinyint(3) DEFAULT NULL COMMENT '采集类型',
`type` int(4) DEFAULT NULL COMMENT '采集项',
`freezeTime` bigint(10) DEFAULT NULL COMMENT '冻结时间',
`curveValue` decimal(11,4) DEFAULT NULL COMMENT '值',
`hour` tinyint(24) DEFAULT NULL COMMENT '小时',
UNIQUE KEY `curvedataUni` (`teNumber`,`measurePoint`,`type`,`freezeTime`) USING BTREE,
KEY `hour` (`hour`) USING BTREE) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='曲线数据';

-- 创建表nowdatadata20180410
CREATE TABLE `nowdata20180410` (
`teNumber` int(9) NOT NULL COMMENT '终端地址',
`measurePoint` int(4) NOT NULL COMMENT '终端测量点号',
`gatherTime` datetime DEFAULT NULL COMMENT '采集时间',
`gatherType` tinyint(3) DEFAULT NULL COMMENT '采集类型',
`type` int(4) DEFAULT NULL COMMENT '采集项',
`freezeTime` bigint(10) DEFAULT NULL COMMENT '冻结时间',
`curveValue` decimal(11,4) DEFAULT NULL COMMENT '值',
`feilv` int(4) DEFAULT NULL COMMENT '费率',
`max_value` decimal(11,4) DEFAULT NULL COMMENT '最大值',
`maxTime` varchar(256) DEFAULT NULL COMMENT '最大值发生时间',
`hour` tinyint(24) DEFAULT NULL COMMENT '小时',
UNIQUE KEY `curvedataUni` (`teNumber`,`measurePoint`,`type`,`freezeTime`,`feilv`) USING BTREE,
KEY `hour` (`hour`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='曲线数据';

-- 创建表curvedata20180411
CREATE TABLE `curvedata20180411` (
`teNumber` int(9) NOT NULL COMMENT '终端地址',
`measurePoint` int(4) NOT NULL COMMENT '终端测量点号',
`gatherTime` datetime DEFAULT NULL COMMENT '采集时间',
`gatherType` tinyint(3) DEFAULT NULL COMMENT '采集类型',
`type` int(4) DEFAULT NULL COMMENT '采集项',
`freezeTime` bigint(10) DEFAULT NULL COMMENT '冻结时间',
`curveValue` decimal(11,4) DEFAULT NULL COMMENT '值',
`hour` tinyint(24) DEFAULT NULL COMMENT '小时',
UNIQUE KEY `curvedataUni` (`teNumber`,`measurePoint`,`type`,`freezeTime`) USING BTREE,
KEY `hour` (`hour`) USING BTREE) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='曲线数据';

-- 创建表nowdatadata20180411
CREATE TABLE `nowdata20180411` (
`teNumber` int(9) NOT NULL COMMENT '终端地址',
`measurePoint` int(4) NOT NULL COMMENT '终端测量点号',
`gatherTime` datetime DEFAULT NULL COMMENT '采集时间',
`gatherType` tinyint(3) DEFAULT NULL COMMENT '采集类型',
`type` int(4) DEFAULT NULL COMMENT '采集项',
`freezeTime` bigint(10) DEFAULT NULL COMMENT '冻结时间',
`curveValue` decimal(11,4) DEFAULT NULL COMMENT '值',
`feilv` int(4) DEFAULT NULL COMMENT '费率',
`max_value` decimal(11,4) DEFAULT NULL COMMENT '最大值',
`maxTime` varchar(256) DEFAULT NULL COMMENT '最大值发生时间',
`hour` tinyint(24) DEFAULT NULL COMMENT '小时',
UNIQUE KEY `curvedataUni` (`teNumber`,`measurePoint`,`type`,`freezeTime`,`feilv`) USING BTREE,
KEY `hour` (`hour`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='曲线数据';

