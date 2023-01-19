# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2023-01-17 14:54:26
# @Last Modified by:   E-NoR
# @Last Modified time: 2023-01-18 17:23:49
from dataclasses import dataclass
from typing import Any, Dict, Literal, Optional


@dataclass
class ApiRequest:
    api: str
    url: str
    data_type: Literal["params", "json"]
    method: Literal["GET", "POST", "PUT", "DELETE"]
    headers: Optional[Dict[str, Any]]
    data: Optional[Dict[str, Any]]

@dataclass
class YL(ApiRequest):
    @dataclass
    class ActivitiesSet(ApiRequest):
        """
        api_list:
            GetID ,
            GetList ,
            Getstatistics ,
            Save ,
            SaveFrontShowe ,
            Savescope ,
            changestatus
        """
        api = "/ActivitiesSet"
        url = "http://192.168.33.5:9100/ActivitiesSet"
        method = "GET"
        @dataclass
        class GetID(ApiRequest):
            """
            Args:
                id (int) : example( 21 )
            """
            data_type = "params"
            api = "/ActivitiesSet/GetID"
            url = "http://192.168.33.5:9100/ActivitiesSet/GetID"
            method = "POST"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                total (int) : example( 21 )
                selstatus (str) : example( -1 )
                _ (int) : example( 1673925568602 )
            """
            def __init__(self,limit=None, offset=None, total=None, selstatus=None, _=None):
                self.data = {"limit":limit,"offset":offset,"total":total,"selstatus":selstatus,"_":_}
            data_type = "params"
            api = "/ActivitiesSet/GetList"
            url = "http://192.168.33.5:9100/ActivitiesSet/GetList"
            method = "GET"
        @dataclass
        class Getstatistics(ApiRequest):
            """
            Args:
                id (int) : example( 21 )
                BEGIN_DATE (str) : example( 2023-01-15 )
                END_DATE (str) : example( 2023-01-17 )
                gametype (int) : example( 8230 )
            """
            data_type = "params"
            api = "/ActivitiesSet/Getstatistics"
            url = "http://192.168.33.5:9100/ActivitiesSet/Getstatistics"
            method = "POST"
        @dataclass
        class Save(ApiRequest):
            """
            Args:
                id (int) : example( 19 )
                Spwd (str) : example( 03f9aeef097033d251225d1247f9dd65 )
                Status (int|bool) : example( 1 )
                hidenddate (str) : example( 2022-11-03 )
                hidendtime (str) : example( 16:00 )
                ActivityType (int) : example( 8230 )
                BEGIN_DATE (str) : example( 2022-11-02 )
                END_DATE (str) : example( 2022-11-03 )
                BEGIN_DATETime (str) : example( 15:00 )
                END_DATETime (str) : example( 16:00 )
                Winningrate (str) : example( 0.5 )
                Totalbonus (int) : example( 100 )
                Singipupper (int) : example( 10 )
                ForntPerMaxPrize (int) : example( 10 )
                _csrf (str) : example( MMGNUz3l-AoylFdQrwhSjMJbiS9wmmKsJPbk )
            """
            data_type = "params"
            api = "/ActivitiesSet/Save"
            url = "http://192.168.33.5:9100/ActivitiesSet/Save"
            method = "POST"
        @dataclass
        class SaveFrontShowe(ApiRequest):
            """
            Args:
                id (int) : example( 21 )
                Spwd (str) : example( 03f9aeef097033d251225d1247f9dd65 )
                Status (int) : example( 3 )
                hidenddate (str) : example( 2023-01-18 )
                hidendtime (str) : example( 11:19 )
                FrontWinningrate (int|bool) : example( 1 )
                Totalmoney (int|bool) : example( 0 )
                _csrf (str) : example( MMGNUz3l-AoylFdQrwhSjMJbiS9wmmKsJPbk )
            """
            data_type = "params"
            api = "/ActivitiesSet/SaveFrontShowe"
            url = "http://192.168.33.5:9100/ActivitiesSet/SaveFrontShowe"
            method = "POST"
        @dataclass
        class Savescope(ApiRequest):
            """
            Args:
                id (int) : example( 21 )
                Spwd (str) : example( 03f9aeef097033d251225d1247f9dd65 )
                Status (int) : example( 3 )
                hidenddate (str) : example( 2023-01-18 )
                hidendtime (str) : example( 11:19 )
                DropoutGames (str) : example(  )
                Joinchannelid (str) : example(  )
                Dropoutlinecode (str) : example(  )
                _csrf (str) : example( MMGNUz3l-AoylFdQrwhSjMJbiS9wmmKsJPbk )
            """
            data_type = "params"
            api = "/ActivitiesSet/Savescope"
            url = "http://192.168.33.5:9100/ActivitiesSet/Savescope"
            method = "POST"
        @dataclass
        class changestatus(ApiRequest):
            """
            Args:
                id (int) : example( 21 )
                Status (int) : example( 3 )
                Spwd (str) : example( 03f9aeef097033d251225d1247f9dd65 )
                _csrf (str) : example( MMGNUz3l-AoylFdQrwhSjMJbiS9wmmKsJPbk )
            """
            data_type = "params"
            api = "/ActivitiesSet/changestatus"
            url = "http://192.168.33.5:9100/ActivitiesSet/changestatus"
            method = "POST"
    @dataclass
    class ActivityAlarm(ApiRequest):
        """
        api_list:
            addAlarm ,
            editAlarm ,
            getAlarmById ,
            getList
        """
        api = "/ActivityAlarm"
        url = "http://192.168.33.5:9100/ActivityAlarm"
        method = "GET"
        @dataclass
        class addAlarm(ApiRequest):
            """
            Args:
                activityID (int) : example( 11012 )
                wrewardType (int|bool) : example( 1 )
                outgivingType (int|bool) : example( 1 )
                limit (int|bool) : example( 1 )
                telGroupID (int) : example( 126 )
                _csrf (str) : example( 7S2P0bSw-dcj1G0ktwlbBJ7l_xb3m2afBmAE )
            """
            data_type = "params"
            api = "/ActivityAlarm/addAlarm"
            url = "http://192.168.33.5:9100/ActivityAlarm/addAlarm"
            method = "POST"
        @dataclass
        class editAlarm(ApiRequest):
            """
            Args:
                Id (int) : example( 7 )
                activityID (int) : example( 11012 )
                wrewardType (int|bool) : example( 1 )
                outgivingType (int|bool) : example( 1 )
                limit (int) : example( 100 )
                telGroupID (int) : example( 200 )
                _csrf (str) : example( 7S2P0bSw-dcj1G0ktwlbBJ7l_xb3m2afBmAE )
            """
            data_type = "params"
            api = "/ActivityAlarm/editAlarm"
            url = "http://192.168.33.5:9100/ActivityAlarm/editAlarm"
            method = "POST"
        @dataclass
        class getAlarmById(ApiRequest):
            """
            Args:
                Id (int) : example( 7 )
            """
            def __init__(self,Id=None):
                self.data = {"Id":Id}
            data_type = "params"
            api = "/ActivityAlarm/getAlarmById"
            url = "http://192.168.33.5:9100/ActivityAlarm/getAlarmById"
            method = "GET"
        @dataclass
        class getList(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                endDate (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
            """
            def __init__(self,beginDate=None, endDate=None, limit=None, offset=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"limit":limit,"offset":offset}
            data_type = "params"
            api = "/ActivityAlarm/getList"
            url = "http://192.168.33.5:9100/ActivityAlarm/getList"
            method = "GET"
    @dataclass
    class ActivityData(ApiRequest):
        """
        api_list:
            export ,
            getActivityType ,
            getlist
        """
        api = "/ActivityData"
        url = "http://192.168.33.5:9100/ActivityData"
        method = "GET"
        @dataclass
        class export(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16%2011:04 )
                endDate (str) : example( 2023-01-17%2011:04 )
                activityID (int|bool) : example( 0 )
                rnd (str) : example( 0.7345097715130793 )
            """
            def __init__(self,beginDate=None, endDate=None, activityID=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"activityID":activityID,"rnd":rnd}
            data_type = "params"
            api = "/ActivityData/export"
            url = "http://192.168.33.5:9100/ActivityData/export"
            method = "GET"
        @dataclass
        class getActivityType(ApiRequest):
            api = "/ActivityData/getActivityType"
            url = "http://192.168.33.5:9100/ActivityData/getActivityType"
            method = "GET"
        @dataclass
        class getlist(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16+11%3A04 )
                endDate (str) : example( 2023-01-17+11%3A04 )
                activityID (int|bool) : example( 0 )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                _ (int) : example( 1673924692966 )
            """
            def __init__(self,beginDate=None, endDate=None, activityID=None, limit=None, offset=None, total=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"activityID":activityID,"limit":limit,"offset":offset,"total":total,"_":_}
            data_type = "params"
            api = "/ActivityData/getlist"
            url = "http://192.168.33.5:9100/ActivityData/getlist"
            method = "GET"
    @dataclass
    class ActivitySwitch(ApiRequest):
        """
        api_list:
            addConfig ,
            changeStatus ,
            editConfig ,
            getConfigbyId ,
            getList
        """
        api = "/ActivitySwitch"
        url = "http://192.168.33.5:9100/ActivitySwitch"
        method = "GET"
        @dataclass
        class addConfig(ApiRequest):
            """
            Args:
                activityID (int) : example( 11012 )
                ChannelID (int) : example( 124 )
                childID (str) : example(  )
                _csrf (str) : example( 2OGQ9eio-O3ogqlDSrj4bS8UjJLBsUy8HGz8 )
            """
            data_type = "params"
            api = "/ActivitySwitch/addConfig"
            url = "http://192.168.33.5:9100/ActivitySwitch/addConfig"
            method = "POST"
        @dataclass
        class changeStatus(ApiRequest):
            """
            Args:
                Id (int) : example( 5 )
                ChannelID (int) : example( 124 )
            """
            def __init__(self,Id=None, ChannelID=None):
                self.data = {"Id":Id,"ChannelID":ChannelID}
            data_type = "params"
            api = "/ActivitySwitch/changeStatus"
            url = "http://192.168.33.5:9100/ActivitySwitch/changeStatus"
            method = "GET"
        @dataclass
        class editConfig(ApiRequest):
            """
            Args:
                Id (int) : example( 5 )
                activityID (int) : example( 11012 )
                ChannelID (int) : example( 124 )
                childID (str) : example(  )
                _csrf (str) : example( 2OGQ9eio-O3ogqlDSrj4bS8UjJLBsUy8HGz8 )
            """
            data_type = "params"
            api = "/ActivitySwitch/editConfig"
            url = "http://192.168.33.5:9100/ActivitySwitch/editConfig"
            method = "POST"
        @dataclass
        class getConfigbyId(ApiRequest):
            """
            Args:
                Id (int) : example( 5 )
            """
            def __init__(self,Id=None):
                self.data = {"Id":Id}
            data_type = "params"
            api = "/ActivitySwitch/getConfigbyId"
            url = "http://192.168.33.5:9100/ActivitySwitch/getConfigbyId"
            method = "GET"
        @dataclass
        class getList(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-17+11%3A05 )
                endDate (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                ChannelID (str) : example(  )
            """
            def __init__(self,beginDate=None, endDate=None, limit=None, offset=None, ChannelID=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"limit":limit,"offset":offset,"ChannelID":ChannelID}
            data_type = "params"
            api = "/ActivitySwitch/getList"
            url = "http://192.168.33.5:9100/ActivitySwitch/getList"
            method = "GET"
    @dataclass
    class AgentAccessGame(ApiRequest):
        """
        api_list:
            GetGameType ,
            exportData ,
            getlist
        """
        api = "/AgentAccessGame"
        url = "http://192.168.33.5:9100/AgentAccessGame"
        method = "GET"
        @dataclass
        class GetGameType(ApiRequest):
            api = "/AgentAccessGame/GetGameType"
            url = "http://192.168.33.5:9100/AgentAccessGame/GetGameType"
            method = "GET"
        @dataclass
        class exportData(ApiRequest):
            """
            Args:
                gameIds (str) : example( 220,230,380,390,510,520,530,540,550,600,610,620,630,650,720,730,740,830,840,860,870,880,890,900,910,920,930,950,1101,1350,1355,1370,1610,1640,1660,1670,1690,1710,1810,1850,1860,1890,1930,1940,1950,1960,1970,1980,1990,2002,2003,2005,2890,3001,3002,3003,3005,7280,8130,8230,90000,90010 )
                beginDate (str) : example( 2022-12-13 )
                endDate (str) : example( 2022-12-19 )
                searchSort (int|bool) : example( 0 )
                ChannelID (str) : example(  )
                proxyName (str) : example(  )
                proxyUID (str) : example(  )
                gameStatus (str) : example( -1 )
                isexcel (int|bool) : example( 1 )
                rnd (str) : example( 0.7474834332261691 )
            """
            def __init__(self,gameIds=None, beginDate=None, endDate=None, searchSort=None, ChannelID=None, proxyName=None, proxyUID=None, gameStatus=None, isexcel=None, rnd=None):
                self.data = {"gameIds":gameIds,"beginDate":beginDate,"endDate":endDate,"searchSort":searchSort,"ChannelID":ChannelID,"proxyName":proxyName,"proxyUID":proxyUID,"gameStatus":gameStatus,"isexcel":isexcel,"rnd":rnd}
            data_type = "params"
            api = "/AgentAccessGame/exportData"
            url = "http://192.168.33.5:9100/AgentAccessGame/exportData"
            method = "GET"
        @dataclass
        class getlist(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2022-12-13 )
                endDate (str) : example( 2022-12-19 )
                searchSort (int|bool) : example( 0 )
                gameStatus (str) : example( -1 )
                ChannelID (str) : example(  )
                proxyName (str) : example( david )
                proxyUID (str) : example(  )
                limit (int) : example( 50 )
                offset (int|bool) : example( 0 )
                gameIds (str) : example( 220%2C230%2C380%2C390%2C510%2C520%2C530%2C540%2C550%2C600%2C610%2C620%2C630%2C650%2C720%2C730%2C740%2C830%2C840%2C860%2C870%2C880%2C890%2C900%2C910%2C920%2C930%2C950%2C1101%2C1350%2C1355%2C1370%2C1610%2C1640%2C1660%2C1670%2C1690%2C1710%2C1810%2C1850%2C1860%2C1890%2C1930%2C1940%2C1950%2C1960%2C1970%2C1980%2C1990%2C2002%2C2003%2C2005%2C2890%2C3001%2C3002%2C3003%2C3005%2C7280%2C8130%2C8230%2C90000%2C90010 )
                total (int|bool) : example( 0 )
                _ (int) : example( 1673925239896 )
            """
            def __init__(self,beginDate=None, endDate=None, searchSort=None, gameStatus=None, ChannelID=None, proxyName=None, proxyUID=None, limit=None, offset=None, gameIds=None, total=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"searchSort":searchSort,"gameStatus":gameStatus,"ChannelID":ChannelID,"proxyName":proxyName,"proxyUID":proxyUID,"limit":limit,"offset":offset,"gameIds":gameIds,"total":total,"_":_}
            data_type = "params"
            api = "/AgentAccessGame/getlist"
            url = "http://192.168.33.5:9100/AgentAccessGame/getlist"
            method = "GET"
    @dataclass
    class AgentLevelManage(ApiRequest):
        """
        api_list:
            InitData ,
            del ,
            getLevelInfo ,
            save
        """
        api = "/AgentLevelManage"
        url = "http://192.168.33.5:9100/AgentLevelManage"
        method = "GET"
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                ChannelID (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673924596347 )
            """
            def __init__(self,ChannelID=None, limit=None, offset=None, _=None):
                self.data = {"ChannelID":ChannelID,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/AgentLevelManage/InitData"
            url = "http://192.168.33.5:9100/AgentLevelManage/InitData"
            method = "GET"
        @dataclass
        class del_(ApiRequest):
            """
            Args:
                channelId (int) : example( 123 )
            """
            def __init__(self,channelId=None):
                self.data = {"channelId":channelId}
            data_type = "params"
            api = "/AgentLevelManage/del"
            url = "http://192.168.33.5:9100/AgentLevelManage/del"
            method = "GET"
        @dataclass
        class getLevelInfo(ApiRequest):
            """
            Args:
                channelId (int) : example( 123 )
            """
            def __init__(self,channelId=None):
                self.data = {"channelId":channelId}
            data_type = "params"
            api = "/AgentLevelManage/getLevelInfo"
            url = "http://192.168.33.5:9100/AgentLevelManage/getLevelInfo"
            method = "GET"
        @dataclass
        class save(ApiRequest):
            """
            Args:
                param%5B0%5D%5BtopLimit%5D (int|bool) : example( 1 )
                param%5B0%5D%5BlowerLimit%5D (int|bool) : example( 1 )
                param%5B0%5D%5Bzc%5D (int|bool) : example( 1 )
                param%5B0%5D%5BlevelId%5D (int|bool) : example( 1 )
                param%5B1%5D%5BtopLimit%5D (int|bool) : example( 0 )
                param%5B1%5D%5BlowerLimit%5D (int|bool) : example( 0 )
                param%5B1%5D%5Bzc%5D (int|bool) : example( 0 )
                param%5B1%5D%5BlevelId%5D (int) : example( 2 )
                channelId (int) : example( 123 )
            """
            def __init__(self,param_0_topLimit=None, param_0_lowerLimit=None, param_0_zc=None, param_0_levelId=None, param_1_topLimit=None, param_1_lowerLimit=None, param_1_zc=None, param_1_levelId=None, channelId=None):
                self.data = {"param%5B0%5D%5BtopLimit%5D":param_0_topLimit,"param%5B0%5D%5BlowerLimit%5D":param_0_lowerLimit,"param%5B0%5D%5Bzc%5D":param_0_zc,"param%5B0%5D%5BlevelId%5D":param_0_levelId,"param%5B1%5D%5BtopLimit%5D":param_1_topLimit,"param%5B1%5D%5BlowerLimit%5D":param_1_lowerLimit,"param%5B1%5D%5Bzc%5D":param_1_zc,"param%5B1%5D%5BlevelId%5D":param_1_levelId,"channelId":channelId}
            data_type = "params"
            api = "/AgentLevelManage/save"
            url = "http://192.168.33.5:9100/AgentLevelManage/save"
            method = "GET"
    @dataclass
    class BetDetial(ApiRequest):
        api = "/BetDetial"
        url = "http://192.168.33.5:9100/BetDetial"
        method = "GET"
    @dataclass
    class BuyPointsDetail(ApiRequest):
        """
        api_list:
            ExportData ,
            initData
        """
        api = "/BuyPointsDetail"
        url = "http://192.168.33.5:9100/BuyPointsDetail"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2022-11-01 )
                endDate (str) : example( 2022-11-07 )
                orderType (str) : example(  )
                rnd (str) : example( 0.5113979192826423 )
            """
            def __init__(self,beginDate=None, endDate=None, orderType=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"orderType":orderType,"rnd":rnd}
            data_type = "params"
            api = "/BuyPointsDetail/ExportData"
            url = "http://192.168.33.5:9100/BuyPointsDetail/ExportData"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2022-11-01 )
                endDate (str) : example( 2022-11-07 )
                orderType (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                _ (int) : example( 1673923753199 )
            """
            def __init__(self,beginDate=None, endDate=None, orderType=None, limit=None, offset=None, total=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"orderType":orderType,"limit":limit,"offset":offset,"total":total,"_":_}
            data_type = "params"
            api = "/BuyPointsDetail/initData"
            url = "http://192.168.33.5:9100/BuyPointsDetail/initData"
            method = "GET"
    @dataclass
    class CNYManage(ApiRequest):
        """
        api_list:
            InitCurrency ,
            InitData ,
            add ,
            del
        """
        api = "/CNYManage"
        url = "http://192.168.33.5:9100/CNYManage"
        method = "GET"
        @dataclass
        class InitCurrency(ApiRequest):
            api = "/CNYManage/InitCurrency"
            url = "http://192.168.33.5:9100/CNYManage/InitCurrency"
            method = "GET"
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                Currency (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673924571486 )
            """
            def __init__(self,Currency=None, limit=None, offset=None, _=None):
                self.data = {"Currency":Currency,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/CNYManage/InitData"
            url = "http://192.168.33.5:9100/CNYManage/InitData"
            method = "GET"
        @dataclass
        class add(ApiRequest):
            """
            Args:
                id (int) : example( 9 )
                ChannelID (int) : example( 123 )
                Currency (str) : example( SGD )
                ExchangeRate (str) : example( 1.65 )
                RateCalculate (int|bool) : example( 0 )
                year (int) : example( 2023 )
                month (int|bool) : example( 1 )
            """
            def __init__(self,id=None, ChannelID=None, Currency=None, ExchangeRate=None, RateCalculate=None, year=None, month=None):
                self.data = {"id":id,"ChannelID":ChannelID,"Currency":Currency,"ExchangeRate":ExchangeRate,"RateCalculate":RateCalculate,"year":year,"month":month}
            data_type = "params"
            api = "/CNYManage/add"
            url = "http://192.168.33.5:9100/CNYManage/add"
            method = "GET"
        @dataclass
        class del_(ApiRequest):
            """
            Args:
                id (int) : example( 9 )
            """
            def __init__(self,id=None):
                self.data = {"id":id}
            data_type = "params"
            api = "/CNYManage/del"
            url = "http://192.168.33.5:9100/CNYManage/del"
            method = "GET"
    @dataclass
    class CashOrderDetail(ApiRequest):
        """
        api_list:
            ExportData ,
            InitData
        """
        api = "/CashOrderDetail"
        url = "http://192.168.33.5:9100/CashOrderDetail"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16%2010:46 )
                endDate (str) : example( 2023-01-17%2010:46 )
                orderType (str) : example( -2 )
                accounts (str) : example(  )
                createUser (str) : example(  )
                rnd (str) : example( 0.8863195210879848 )
            """
            def __init__(self,beginDate=None, endDate=None, orderType=None, accounts=None, createUser=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"orderType":orderType,"accounts":accounts,"createUser":createUser,"rnd":rnd}
            data_type = "params"
            api = "/CashOrderDetail/ExportData"
            url = "http://192.168.33.5:9100/CashOrderDetail/ExportData"
            method = "GET"
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16+10%3A46 )
                endDate (str) : example( 2023-01-17+10%3A46 )
                orderType (str) : example( -2 )
                accounts (str) : example(  )
                createUser (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                _ (int) : example( 1673923614241 )
            """
            def __init__(self,beginDate=None, endDate=None, orderType=None, accounts=None, createUser=None, limit=None, offset=None, total=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"orderType":orderType,"accounts":accounts,"createUser":createUser,"limit":limit,"offset":offset,"total":total,"_":_}
            data_type = "params"
            api = "/CashOrderDetail/InitData"
            url = "http://192.168.33.5:9100/CashOrderDetail/InitData"
            method = "GET"
    @dataclass
    class CheckForbidden(ApiRequest):
        """
        Args:
        """
        api = "/CheckForbidden"
        url = "http://192.168.33.5:9100/CheckForbidden"
        method = "POST"
    @dataclass
    class CheckLogin(ApiRequest):
        """
        api_list:
            ExportData ,
            GetList
        """
        api = "/CheckLogin"
        url = "http://192.168.33.5:9100/CheckLogin"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                 (str) : example(  )
                beginDate (str) : example( 2023-01-17 )
                endDate (str) : example( 2023-01-17 )
            """
            def __init__(self,beginDate=None, endDate=None):
                self.data = {"beginDate":beginDate,"endDate":endDate}
            data_type = "params"
            api = "/CheckLogin/ExportData"
            url = "http://192.168.33.5:9100/CheckLogin/ExportData"
            method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                beginDate (str) : example( 2023-01-17 )
                endDate (str) : example( 2023-01-17 )
                _ (int) : example( 1673924908210 )
            """
            def __init__(self,limit=None, offset=None, beginDate=None, endDate=None, _=None):
                self.data = {"limit":limit,"offset":offset,"beginDate":beginDate,"endDate":endDate,"_":_}
            data_type = "params"
            api = "/CheckLogin/GetList"
            url = "http://192.168.33.5:9100/CheckLogin/GetList"
            method = "GET"
    @dataclass
    class Checkproxy(ApiRequest):
        """
        Args:
        """
        api = "/Checkproxy"
        url = "http://192.168.33.5:9100/Checkproxy"
        method = "POST"
    @dataclass
    class CirCleGameStatistic(ApiRequest):
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2022-08-15 )
                isPage (int|bool) : example( 0 )
                endDate (str) : example( 2022-08-15 )
                kindId (int) : example( 1960 )
                serverId (int) : example( 19604 )
                rnd (str) : example( 0.6221013657359098 )
            """
            def __init__(self,beginDate=None, isPage=None, endDate=None, kindId=None, serverId=None, rnd=None):
                self.data = {"beginDate":beginDate,"isPage":isPage,"endDate":endDate,"kindId":kindId,"serverId":serverId,"rnd":rnd}
            data_type = "params"
            api = "/CirCleGameStatistic/InitData"
            url = "http://192.168.33.5:9100/CirCleGameStatistic/InitData"
            method = "GET"
    @dataclass
    class CircleGameStatistic(ApiRequest):
        """
        api_list:
            getCircleGameType ,
            getRoomInfo
        """
        api = "/CircleGameStatistic"
        url = "http://192.168.33.5:9100/CircleGameStatistic"
        method = "GET"
        @dataclass
        class getCircleGameType(ApiRequest):
            api = "/CircleGameStatistic/getCircleGameType"
            url = "http://192.168.33.5:9100/CircleGameStatistic/getCircleGameType"
            method = "GET"
        @dataclass
        class getRoomInfo(ApiRequest):
            """
            Args:
                kindId (int) : example( 1960 )
            """
            def __init__(self,kindId=None):
                self.data = {"kindId":kindId}
            data_type = "params"
            api = "/CircleGameStatistic/getRoomInfo"
            url = "http://192.168.33.5:9100/CircleGameStatistic/getRoomInfo"
            method = "GET"
    @dataclass
    class CustomOnline(ApiRequest):
        """
        api_list:
            getCustomOnline
        """
        api = "/CustomOnline"
        url = "http://192.168.33.5:9100/CustomOnline"
        method = "GET"
        @dataclass
        class getCustomOnline(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
            """
            def __init__(self,beginDate=None, endDate=None):
                self.data = {"beginDate":beginDate,"endDate":endDate}
            data_type = "params"
            api = "/CustomOnline/getCustomOnline"
            url = "http://192.168.33.5:9100/CustomOnline/getCustomOnline"
            method = "GET"
    @dataclass
    class DMGameRecordSort(ApiRequest):
        """
        api_list:
            getGameType
        """
        api = "/DMGameRecordSort"
        url = "http://192.168.33.5:9100/DMGameRecordSort"
        method = "GET"
        @dataclass
        class getGameType(ApiRequest):
            api = "/DMGameRecordSort/getGameType"
            url = "http://192.168.33.5:9100/DMGameRecordSort/getGameType"
            method = "GET"
    @dataclass
    class DMPreview(ApiRequest):
        """
        api_list:
            getPreviewData ,
            getThirtyData
        """
        api = "/DMPreview"
        url = "http://192.168.33.5:9100/DMPreview"
        method = "GET"
        @dataclass
        class getPreviewData(ApiRequest):
            """
            Args:
                channelIds (str) : example(  )
            """
            def __init__(self,channelIds=None):
                self.data = {"channelIds":channelIds}
            data_type = "params"
            api = "/DMPreview/getPreviewData"
            url = "http://192.168.33.5:9100/DMPreview/getPreviewData"
            method = "GET"
        @dataclass
        class getThirtyData(ApiRequest):
            api = "/DMPreview/getThirtyData"
            url = "http://192.168.33.5:9100/DMPreview/getThirtyData"
            method = "GET"
    @dataclass
    class EstimateLossStatistics(ApiRequest):
        """
        api_list:
            ExportData ,
            InitData
        """
        api = "/EstimateLossStatistics"
        url = "http://192.168.33.5:9100/EstimateLossStatistics"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                fbeginDate (str) : example( 2022-12-07%2010:50 )
                fendDate (str) : example( 2022-12-07%2023:59 )
                sbeginDate (str) : example( 2023-01-16%2010:50 )
                sendDate (str) : example( 2023-01-16%2023:59 )
                channelId (str) : example(  )
            """
            def __init__(self,fbeginDate=None, fendDate=None, sbeginDate=None, sendDate=None, channelId=None):
                self.data = {"fbeginDate":fbeginDate,"fendDate":fendDate,"sbeginDate":sbeginDate,"sendDate":sendDate,"channelId":channelId}
            data_type = "params"
            api = "/EstimateLossStatistics/ExportData"
            url = "http://192.168.33.5:9100/EstimateLossStatistics/ExportData"
            method = "GET"
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                fbeginDate (str) : example( 2022-12-07+10%3A50 )
                fendDate (str) : example( 2022-12-07+23%3A59 )
                sbeginDate (str) : example( 2023-01-16+10%3A50 )
                sendDate (str) : example( 2023-01-16+23%3A59 )
                channelId (str) : example(  )
                _ (int) : example( 1673923814679 )
            """
            def __init__(self,fbeginDate=None, fendDate=None, sbeginDate=None, sendDate=None, channelId=None, _=None):
                self.data = {"fbeginDate":fbeginDate,"fendDate":fendDate,"sbeginDate":sbeginDate,"sendDate":sendDate,"channelId":channelId,"_":_}
            data_type = "params"
            api = "/EstimateLossStatistics/InitData"
            url = "http://192.168.33.5:9100/EstimateLossStatistics/InitData"
            method = "GET"
    @dataclass
    class GameDataMonitor(ApiRequest):
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                gameIds (str) : example( 220,230,380,390,510,520,530,540,550,600,610,620,630,650,720,730,740,830,840,860,870,880,890,900,910,920,930,950,1101,1350,1355,1370,1610,1640,1660,1670,1690,1710,1810,1850,1860,1890,1930,1940,1950,1960,1970,1980,1990,2002,2003,2005,2890,3001,3002,3003,3005,7280,8130,8230,90000,90010 )
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                type (str) : example( undefined )
                isexcel (int|bool) : example( 1 )
                rnd (str) : example( 0.3215339923253342 )
            """
            def __init__(self,gameIds=None, beginDate=None, endDate=None, type=None, isexcel=None, rnd=None):
                self.data = {"gameIds":gameIds,"beginDate":beginDate,"endDate":endDate,"type":type,"isexcel":isexcel,"rnd":rnd}
            data_type = "params"
            api = "/GameDataMonitor/ExportData"
            url = "http://192.168.33.5:9100/GameDataMonitor/ExportData"
            method = "GET"
    @dataclass
    class GameDataMonitor(ApiRequest):
        @dataclass
        class GetData(ApiRequest):
            """
            Args:
                gameIds (str) : example( 220%2C230%2C380%2C390%2C510%2C520%2C530%2C540%2C550%2C600%2C610%2C620%2C630%2C650%2C720%2C730%2C740%2C830%2C840%2C860%2C870%2C880%2C890%2C900%2C910%2C920%2C930%2C950%2C1101%2C1350%2C1355%2C1370%2C1610%2C1640%2C1660%2C1670%2C1690%2C1710%2C1810%2C1850%2C1860%2C1890%2C1930%2C1940%2C1950%2C1960%2C1970%2C1980%2C1990%2C2002%2C2003%2C2005%2C2890%2C3001%2C3002%2C3003%2C3005%2C7280%2C8130%2C8230%2C90000%2C90010 )
            """
            def __init__(self,gameIds=None):
                self.data = {"gameIds":gameIds}
            data_type = "params"
            api = "/GameDataMonitor/GetData"
            url = "http://192.168.33.5:9100/GameDataMonitor/GetData"
            method = "GET"
    @dataclass
    class GameDataMonitor(ApiRequest):
        @dataclass
        class GetGameType(ApiRequest):
            api = "/GameDataMonitor/GetGameType"
            url = "http://192.168.33.5:9100/GameDataMonitor/GetGameType"
            method = "GET"
    @dataclass
    class GameDataMonitor(ApiRequest):
        @dataclass
        class get24HoursOnline(ApiRequest):
            """
            Args:
                gameIds (str) : example( 220%2C230%2C380%2C390%2C510%2C520%2C530%2C540%2C550%2C600%2C610%2C620%2C630%2C650%2C720%2C730%2C740%2C830%2C840%2C860%2C870%2C880%2C890%2C900%2C910%2C920%2C930%2C950%2C1101%2C1350%2C1355%2C1370%2C1610%2C1640%2C1660%2C1670%2C1690%2C1710%2C1810%2C1850%2C1860%2C1890%2C1930%2C1940%2C1950%2C1960%2C1970%2C1980%2C1990%2C2002%2C2003%2C2005%2C2890%2C3001%2C3002%2C3003%2C3005%2C7280%2C8130%2C8230%2C90000%2C90010 )
                interval (int|bool) : example( 1 )
            """
            def __init__(self,gameIds=None, interval=None):
                self.data = {"gameIds":gameIds,"interval":interval}
            data_type = "params"
            api = "/GameDataMonitor/get24HoursOnline"
            url = "http://192.168.33.5:9100/GameDataMonitor/get24HoursOnline"
            method = "GET"
    @dataclass
    class GameLog(ApiRequest):
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                gameNo (str) : example( 50-1673922906-58236827-2 )
            """
            def __init__(self,gameNo=None):
                self.data = {"gameNo":gameNo}
            data_type = "params"
            api = "/GameLog/InitData"
            url = "http://192.168.33.5:9100/GameLog/InitData"
            method = "GET"
    @dataclass
    class GameResult(ApiRequest):
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                endDate (str) : example(  )
                kindId (str) : example(  )
                serverId (str) : example(  )
                gameNo (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                Accounts (str) : example( 1_tim )
                _ (int) : example( 1673923594994 )
            """
            def __init__(self,beginDate=None, endDate=None, kindId=None, serverId=None, gameNo=None, limit=None, offset=None, total=None, Accounts=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"kindId":kindId,"serverId":serverId,"gameNo":gameNo,"limit":limit,"offset":offset,"total":total,"Accounts":Accounts,"_":_}
            data_type = "params"
            api = "/GameResult/InitData"
            url = "http://192.168.33.5:9100/GameResult/InitData"
            method = "GET"
    @dataclass
    class GetRole(ApiRequest):
        api = "/GetRole"
        url = "http://192.168.33.5:9100/GetRole"
        method = "GET"
    @dataclass
    class IncomeReport(ApiRequest):
        """
        api_list:
            CheckFinance ,
            ExportData ,
            GetChannelInfo ,
            InitData ,
            InitDetail ,
            checkPreMonth ,
            save
        """
        api = "/IncomeReport"
        url = "http://192.168.33.5:9100/IncomeReport"
        method = "GET"
        @dataclass
        class CheckFinance(ApiRequest):
            """
            Args:
                payMonth (str) : example( 2023-01 )
                channelId (int|bool) : example( 1 )
            """
            def __init__(self,payMonth=None, channelId=None):
                self.data = {"payMonth":payMonth,"channelId":channelId}
            data_type = "params"
            api = "/IncomeReport/CheckFinance"
            url = "http://192.168.33.5:9100/IncomeReport/CheckFinance"
            method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                year (int) : example( 2023 )
                monthBegin (int|bool) : example( 1 )
                monthEnd (int|bool) : example( 1 )
                sort (int|bool) : example( 1 )
                channelId (str) : example(  )
                rnd (str) : example( 0.05437385125990013 )
            """
            def __init__(self,year=None, monthBegin=None, monthEnd=None, sort=None, channelId=None, rnd=None):
                self.data = {"year":year,"monthBegin":monthBegin,"monthEnd":monthEnd,"sort":sort,"channelId":channelId,"rnd":rnd}
            data_type = "params"
            api = "/IncomeReport/ExportData"
            url = "http://192.168.33.5:9100/IncomeReport/ExportData"
            method = "GET"
        @dataclass
        class GetChannelInfo(ApiRequest):
            """
            Args:
                channelId (int|bool) : example( 1 )
            """
            def __init__(self,channelId=None):
                self.data = {"channelId":channelId}
            data_type = "params"
            api = "/IncomeReport/GetChannelInfo"
            url = "http://192.168.33.5:9100/IncomeReport/GetChannelInfo"
            method = "GET"
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                channelId (str) : example(  )
                year (int) : example( 2023 )
                monthBegin (int|bool) : example( 1 )
                monthEnd (int|bool) : example( 1 )
                sort (int|bool) : example( 1 )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673924650951 )
            """
            def __init__(self,channelId=None, year=None, monthBegin=None, monthEnd=None, sort=None, limit=None, offset=None, _=None):
                self.data = {"channelId":channelId,"year":year,"monthBegin":monthBegin,"monthEnd":monthEnd,"sort":sort,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/IncomeReport/InitData"
            url = "http://192.168.33.5:9100/IncomeReport/InitData"
            method = "GET"
        @dataclass
        class InitDetail(ApiRequest):
            """
            Args:
                channelId (str) : example(  )
                year (int) : example( 2023 )
                monthBegin (int|bool) : example( 1 )
                monthEnd (int|bool) : example( 1 )
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673924650950 )
            """
            def __init__(self,channelId=None, year=None, monthBegin=None, monthEnd=None, limit=None, offset=None, _=None):
                self.data = {"channelId":channelId,"year":year,"monthBegin":monthBegin,"monthEnd":monthEnd,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/IncomeReport/InitDetail"
            url = "http://192.168.33.5:9100/IncomeReport/InitDetail"
            method = "GET"
        @dataclass
        class checkPreMonth(ApiRequest):
            """
            Args:
                payYear (int) : example( 2023 )
                payMonth (int|bool) : example( 1 )
                incomeType (int|bool) : example( 0 )
                channelId (int|bool) : example( 1 )
            """
            def __init__(self,payYear=None, payMonth=None, incomeType=None, channelId=None):
                self.data = {"payYear":payYear,"payMonth":payMonth,"incomeType":incomeType,"channelId":channelId}
            data_type = "params"
            api = "/IncomeReport/checkPreMonth"
            url = "http://192.168.33.5:9100/IncomeReport/checkPreMonth"
            method = "GET"
        @dataclass
        class save(ApiRequest):
            """
            Args:
                id (str) : example(  )
                channelId (int|bool) : example( 1 )
                incomeType (int|bool) : example( 0 )
                payYear (int) : example( 2023 )
                payMonth (int|bool) : example( 1 )
                incomeMoney (int|bool) : example( 1 )
                incomeDate (str) : example( 2023-01-17 )
                rebate (str) : example(  )
                reQuarter (str) : example(  )
                reMonth (str) : example(  )
                otherPay (str) : example(  )
                otherPayRemark (str) : example(  )
                otherIncome (str) : example(  )
                otherIncomeRemark (str) : example(  )
            """
            def __init__(self,id=None, channelId=None, incomeType=None, payYear=None, payMonth=None, incomeMoney=None, incomeDate=None, rebate=None, reQuarter=None, reMonth=None, otherPay=None, otherPayRemark=None, otherIncome=None, otherIncomeRemark=None):
                self.data = {"id":id,"channelId":channelId,"incomeType":incomeType,"payYear":payYear,"payMonth":payMonth,"incomeMoney":incomeMoney,"incomeDate":incomeDate,"rebate":rebate,"reQuarter":reQuarter,"reMonth":reMonth,"otherPay":otherPay,"otherPayRemark":otherPayRemark,"otherIncome":otherIncome,"otherIncomeRemark":otherIncomeRemark}
            data_type = "params"
            api = "/IncomeReport/save"
            url = "http://192.168.33.5:9100/IncomeReport/save"
            method = "GET"
    @dataclass
    class KeepGameUsers(ApiRequest):
        """
        api_list:
            ExportData ,
            InitData ,
            getGameType
        """
        api = "/KeepGameUsers"
        url = "http://192.168.33.5:9100/KeepGameUsers"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                gameId (str) : example(  )
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                rnd (str) : example( 0.4849831757519316 )
            """
            def __init__(self,gameId=None, beginDate=None, endDate=None, rnd=None):
                self.data = {"gameId":gameId,"beginDate":beginDate,"endDate":endDate,"rnd":rnd}
            data_type = "params"
            api = "/KeepGameUsers/ExportData"
            url = "http://192.168.33.5:9100/KeepGameUsers/ExportData"
            method = "GET"
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                gameId (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673925280967 )
            """
            def __init__(self,beginDate=None, endDate=None, gameId=None, limit=None, offset=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"gameId":gameId,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/KeepGameUsers/InitData"
            url = "http://192.168.33.5:9100/KeepGameUsers/InitData"
            method = "GET"
        @dataclass
        class getGameType(ApiRequest):
            api = "/KeepGameUsers/getGameType"
            url = "http://192.168.33.5:9100/KeepGameUsers/getGameType"
            method = "GET"
    @dataclass
    class MaintainAlarm(ApiRequest):
        """
        api_list:
            GetList
        """
        api = "/MaintainAlarm"
        url = "http://192.168.33.5:9100/MaintainAlarm"
        method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 50 )
                offset (int|bool) : example( 0 )
            """
            def __init__(self,limit=None, offset=None):
                self.data = {"limit":limit,"offset":offset}
            data_type = "params"
            api = "/MaintainAlarm/GetList"
            url = "http://192.168.33.5:9100/MaintainAlarm/GetList"
            method = "GET"
    @dataclass
    class OrderStatusQuery(ApiRequest):
        """
        api_list:
            getOrderStatus
        """
        api = "/OrderStatusQuery"
        url = "http://192.168.33.5:9100/OrderStatusQuery"
        method = "GET"
        @dataclass
        class getOrderStatus(ApiRequest):
            """
            Args:
                orderId (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/OrderStatusQuery/getOrderStatus"
            url = "http://192.168.33.5:9100/OrderStatusQuery/getOrderStatus"
            method = "POST"
    @dataclass
    class PetInfoByInterface(ApiRequest):
        """
        api_list:
            getData
        """
        api = "/PetInfoByInterface"
        url = "http://192.168.33.5:9100/PetInfoByInterface"
        method = "GET"
        @dataclass
        class getData(ApiRequest):
            """
            Args:
                accounts (str) : example( 1_tim )
                _ (int) : example( 1673923803519 )
            """
            def __init__(self,accounts=None, _=None):
                self.data = {"accounts":accounts,"_":_}
            data_type = "params"
            api = "/PetInfoByInterface/getData"
            url = "http://192.168.33.5:9100/PetInfoByInterface/getData"
            method = "GET"
    @dataclass
    class QueryAllBet(ApiRequest):
        """
        api_list:
            query
        """
        api = "/QueryAllBet"
        url = "http://192.168.33.5:9100/QueryAllBet"
        method = "GET"
        @dataclass
        class query(ApiRequest):
            """
            Args:
                date (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                channelId (int|bool) : example( 1 )
            """
            def __init__(self,date=None, endDate=None, channelId=None):
                self.data = {"date":date,"endDate":endDate,"channelId":channelId}
            data_type = "params"
            api = "/QueryAllBet/query"
            url = "http://192.168.33.5:9100/QueryAllBet/query"
            method = "GET"
    @dataclass
    class SBObettingReport(ApiRequest):
        """
        api_list:
            ExportData ,
            initData
        """
        api = "/SBObettingReport"
        url = "http://192.168.33.5:9100/SBObettingReport"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2022-10-12 )
                endDate (str) : example( 2022-10-18 )
                sportsType (str) : example( %E5%85%A8%E9%83%A8 )
                league (str) : example(  )
                match (str) : example(  )
                rnd (str) : example( 0.09870520611046962 )
            """
            def __init__(self,beginDate=None, endDate=None, sportsType=None, league=None, match=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"sportsType":sportsType,"league":league,"match":match,"rnd":rnd}
            data_type = "params"
            api = "/SBObettingReport/ExportData"
            url = "http://192.168.33.5:9100/SBObettingReport/ExportData"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2022-10-12 )
                endDate (str) : example( 2022-10-18 )
                sportsType (str) : example( %E5%85%A8%E9%83%A8 )
                league (str) : example(  )
                match (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673924848072 )
            """
            def __init__(self,beginDate=None, endDate=None, sportsType=None, league=None, match=None, limit=None, offset=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"sportsType":sportsType,"league":league,"match":match,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/SBObettingReport/initData"
            url = "http://192.168.33.5:9100/SBObettingReport/initData"
            method = "GET"
    @dataclass
    class SBOorderDetail(ApiRequest):
        """
        api_list:
            ExportData ,
            InitData
        """
        api = "/SBOorderDetail"
        url = "http://192.168.33.5:9100/SBOorderDetail"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2022-10-01%2011:06 )
                endDate (str) : example( 2022-10-27%2011:06 )
                transferCode (str) : example(  )
                account (str) : example(  )
                agnet (str) : example( undefined )
                lineCode (str) : example(  )
                mark (int|bool) : example( 0 )
                type (str) : example( orderDetail )
                status_winLost (int|bool) : example( 0 )
                rnd (str) : example( 0.9287320477675658 )
            """
            def __init__(self,beginDate=None, endDate=None, transferCode=None, account=None, agnet=None, lineCode=None, mark=None, type=None, status_winLost=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"transferCode":transferCode,"account":account,"agnet":agnet,"lineCode":lineCode,"mark":mark,"type":type,"status_winLost":status_winLost,"rnd":rnd}
            data_type = "params"
            api = "/SBOorderDetail/ExportData"
            url = "http://192.168.33.5:9100/SBOorderDetail/ExportData"
            method = "GET"
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                selTimeType (int|bool) : example( 1 )
                beginDate (str) : example( 2022-10-01+11%3A06 )
                endDate (str) : example( 2022-10-27+11%3A06 )
                transferCode (str) : example(  )
                account (str) : example(  )
                agent (str) : example(  )
                lineCode (str) : example(  )
                status_winLost (int|bool) : example( 0 )
                mark (int|bool) : example( 0 )
                type (str) : example( orderDetail )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673924802181 )
            """
            def __init__(self,selTimeType=None, beginDate=None, endDate=None, transferCode=None, account=None, agent=None, lineCode=None, status_winLost=None, mark=None, type=None, limit=None, offset=None, _=None):
                self.data = {"selTimeType":selTimeType,"beginDate":beginDate,"endDate":endDate,"transferCode":transferCode,"account":account,"agent":agent,"lineCode":lineCode,"status_winLost":status_winLost,"mark":mark,"type":type,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/SBOorderDetail/InitData"
            url = "http://192.168.33.5:9100/SBOorderDetail/InitData"
            method = "GET"
    @dataclass
    class SBOproxyStatis(ApiRequest):
        """
        api_list:
            initData
        """
        api = "/SBOproxyStatis"
        url = "http://192.168.33.5:9100/SBOproxyStatis"
        method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                endDate (str) : example(  )
                proxyName (str) : example(  )
                channelId (int|bool) : example( 1 )
                sort (str) : example( general )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                searchType (str) : example( EST )
                _ (int) : example( 1673924790037 )
            """
            def __init__(self,beginDate=None, endDate=None, proxyName=None, channelId=None, sort=None, limit=None, offset=None, total=None, searchType=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"proxyName":proxyName,"channelId":channelId,"sort":sort,"limit":limit,"offset":offset,"total":total,"searchType":searchType,"_":_}
            data_type = "params"
            api = "/SBOproxyStatis/initData"
            url = "http://192.168.33.5:9100/SBOproxyStatis/initData"
            method = "GET"
    @dataclass
    class UserCapacityAnalyze(ApiRequest):
        """
        api_list:
            ExportData ,
            GetList
        """
        api = "/UserCapacityAnalyze"
        url = "http://192.168.33.5:9100/UserCapacityAnalyze"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                SearchDate (str) : example( 2023-01-16 )
                ProxyID (int|bool) : example( 1 )
                ProxyName (str) : example(  )
            """
            def __init__(self,SearchDate=None, ProxyID=None, ProxyName=None):
                self.data = {"SearchDate":SearchDate,"ProxyID":ProxyID,"ProxyName":ProxyName}
            data_type = "params"
            api = "/UserCapacityAnalyze/ExportData"
            url = "http://192.168.33.5:9100/UserCapacityAnalyze/ExportData"
            method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                SearchDate (str) : example( 2023-01-16 )
                ProxyID (int|bool) : example( 1 )
                ProxyName (str) : example(  )
            """
            def __init__(self,SearchDate=None, ProxyID=None, ProxyName=None):
                self.data = {"SearchDate":SearchDate,"ProxyID":ProxyID,"ProxyName":ProxyName}
            data_type = "params"
            api = "/UserCapacityAnalyze/GetList"
            url = "http://192.168.33.5:9100/UserCapacityAnalyze/GetList"
            method = "GET"
    @dataclass
    class UserLogin(ApiRequest):
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-16 )
                accounts (str) : example( 1_tim )
                loginIp (str) : example(  )
                ipblack (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                _ (int) : example( 1673924213639 )
            """
            def __init__(self,beginDate=None, endDate=None, accounts=None, loginIp=None, ipblack=None, limit=None, offset=None, total=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"accounts":accounts,"loginIp":loginIp,"ipblack":ipblack,"limit":limit,"offset":offset,"total":total,"_":_}
            data_type = "params"
            api = "/UserLogin/InitData"
            url = "http://192.168.33.5:9100/UserLogin/InitData"
            method = "GET"
    @dataclass
    class VipSystem(ApiRequest):
        api = "/VipSystem"
        url = "http://192.168.33.5:9100/VipSystem"
        method = "GET"
    @dataclass
    class WinAndLoseReport(ApiRequest):
        @dataclass
        class initSameTableData(ApiRequest):
            """
            Args:
                id (int) : example( 72626 )
                gameName (str) : example( %E6%9E%81%E9%80%9F%E7%99%BE%E5%AE%B6%E4%B9%90 )
                gameEndTime (str) : example( 2023-01-17+10%3A35%3A25 )
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673923564470 )
            """
            def __init__(self,id=None, gameName=None, gameEndTime=None, limit=None, offset=None, _=None):
                self.data = {"id":id,"gameName":gameName,"gameEndTime":gameEndTime,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/WinAndLoseReport/initSameTableData"
            url = "http://192.168.33.5:9100/WinAndLoseReport/initSameTableData"
            method = "GET"
    @dataclass
    class accountCompare(ApiRequest):
        """
        api_list:
            ExportData ,
            initData
        """
        api = "/accountCompare"
        url = "http://192.168.33.5:9100/accountCompare"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                 (str) : example(  )
                staticBegin (str) : example( 2023-01-15 )
                staticEnd (str) : example( 2023-01-16 )
                compareBegin (str) : example( 2023-01-15 )
                compareEnd (str) : example( 2023-01-16 )
                channelId (int|bool) : example( 1 )
                channelName (str) : example(  )
            """
            def __init__(self,staticBegin=None, staticEnd=None, compareBegin=None, compareEnd=None, channelId=None, channelName=None):
                self.data = {"staticBegin":staticBegin,"staticEnd":staticEnd,"compareBegin":compareBegin,"compareEnd":compareEnd,"channelId":channelId,"channelName":channelName}
            data_type = "params"
            api = "/accountCompare/ExportData"
            url = "http://192.168.33.5:9100/accountCompare/ExportData"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                staticBegin (str) : example( 2023-01-15 )
                staticEnd (str) : example( 2023-01-16 )
                compareBegin (str) : example( 2023-01-15 )
                compareEnd (str) : example( 2023-01-16 )
                channelId (int|bool) : example( 1 )
                channelName (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673923952313 )
            """
            def __init__(self,staticBegin=None, staticEnd=None, compareBegin=None, compareEnd=None, channelId=None, channelName=None, limit=None, offset=None, _=None):
                self.data = {"staticBegin":staticBegin,"staticEnd":staticEnd,"compareBegin":compareBegin,"compareEnd":compareEnd,"channelId":channelId,"channelName":channelName,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/accountCompare/initData"
            url = "http://192.168.33.5:9100/accountCompare/initData"
            method = "GET"
    @dataclass
    class activeMemberVisitRoute(ApiRequest):
        """
        api_list:
            exportData
        """
        api = "/activeMemberVisitRoute"
        url = "http://192.168.33.5:9100/activeMemberVisitRoute"
        method = "GET"
        @dataclass
        class exportData(ApiRequest):
            """
            Args:
                startDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                exportName (str) : example( %E6%B4%BB%E8%B7%83%E7%94%A8%E6%88%B7%E8%AE%BF%E9%97%AE%E8%B7%AF%E5%BE%84%E6%8A%A5%E8%A1%A8 )
                type (int) : example( 2 )
            """
            def __init__(self,startDate=None, endDate=None, exportName=None, type=None):
                self.data = {"startDate":startDate,"endDate":endDate,"exportName":exportName,"type":type}
            data_type = "params"
            api = "/activeMemberVisitRoute/exportData"
            url = "http://192.168.33.5:9100/activeMemberVisitRoute/exportData"
            method = "GET"
    @dataclass
    class batchAddScores(ApiRequest):
        """
        api_list:
            addScores ,
            cutBackScores ,
            downloadDemo ,
            exportExcel ,
            opensavedemo01 ,
            opensavedemo02 ,
            outGame ,
            seal ,
            unseal
        """
        api = "/batchAddScores"
        url = "http://192.168.33.5:9100/batchAddScores"
        method = "GET"
        @dataclass
        class addScores(ApiRequest):
            """
            Args:
                data (list) : example( [{'Account': '1_tim'}] )
            """
            data_type = "json"
            api = "/batchAddScores/addScores"
            url = "http://192.168.33.5:9100/batchAddScores/addScores"
            method = "POST"
        @dataclass
        class cutBackScores(ApiRequest):
            """
            Args:
                data (list) : example( [{'Account': '1_tim'}] )
            """
            data_type = "json"
            api = "/batchAddScores/cutBackScores"
            url = "http://192.168.33.5:9100/batchAddScores/cutBackScores"
            method = "POST"
        @dataclass
        class downloadDemo(ApiRequest):
            api = "/batchAddScores/downloadDemo"
            url = "http://192.168.33.5:9100/batchAddScores/downloadDemo"
            method = "GET"
        @dataclass
        class exportExcel(ApiRequest):
            """
            Args:
                data (list) : example( [{'Account': '70022_lance'}, {'Account': '70022_lance01'}] )
            """
            data_type = "json"
            api = "/batchAddScores/exportExcel"
            url = "http://192.168.33.5:9100/batchAddScores/exportExcel"
            method = "POST"
        @dataclass
        class opensavedemo01(ApiRequest):
            """
            Args:
                data (list) : example( [{'Account': '1_tim'}] )
            """
            data_type = "json"
            api = "/batchAddScores/opensavedemo01"
            url = "http://192.168.33.5:9100/batchAddScores/opensavedemo01"
            method = "POST"
        @dataclass
        class opensavedemo02(ApiRequest):
            """
            Args:
                data (list) : example( [{'Account': '1_tim'}] )
            """
            data_type = "json"
            api = "/batchAddScores/opensavedemo02"
            url = "http://192.168.33.5:9100/batchAddScores/opensavedemo02"
            method = "POST"
        @dataclass
        class outGame(ApiRequest):
            """
            Args:
                data (list) : example( [{'Account': '1_tim'}] )
            """
            data_type = "json"
            api = "/batchAddScores/outGame"
            url = "http://192.168.33.5:9100/batchAddScores/outGame"
            method = "POST"
        @dataclass
        class seal(ApiRequest):
            """
            Args:
                data (list) : example( [{'Account': '1_tim'}] )
            """
            data_type = "json"
            api = "/batchAddScores/seal"
            url = "http://192.168.33.5:9100/batchAddScores/seal"
            method = "POST"
        @dataclass
        class unseal(ApiRequest):
            """
            Args:
                data (list) : example( [{'Account': '1_tim'}] )
            """
            data_type = "json"
            api = "/batchAddScores/unseal"
            url = "http://192.168.33.5:9100/batchAddScores/unseal"
            method = "POST"
    @dataclass
    class betDetial(ApiRequest):
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-17%2010:51 )
                endDate (str) : example( 2023-01-17%2010:51 )
                accounts (str) : example(  )
                channelID (str) : example(  )
            """
            def __init__(self,beginDate=None, endDate=None, accounts=None, channelID=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"accounts":accounts,"channelID":channelID}
            data_type = "params"
            api = "/betDetial/ExportData"
            url = "http://192.168.33.5:9100/betDetial/ExportData"
            method = "GET"
    @dataclass
    class betDetial(ApiRequest):
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-17+10%3A51 )
                endDate (str) : example( 2023-01-17+10%3A51 )
                accounts (str) : example(  )
                channelId (str) : example(  )
                limit (int) : example( 50 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673923894924 )
            """
            def __init__(self,beginDate=None, endDate=None, accounts=None, channelId=None, limit=None, offset=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"accounts":accounts,"channelId":channelId,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/betDetial/InitData"
            url = "http://192.168.33.5:9100/betDetial/InitData"
            method = "GET"
    @dataclass
    class bulletin(ApiRequest):
        """
        api_list:
            Edit ,
            GetID ,
            GetList ,
            GetTypes ,
            changestatus ,
            delete ,
            getGameType
        """
        api = "/bulletin"
        url = "http://192.168.33.5:9100/bulletin"
        method = "GET"
        @dataclass
        class Edit(ApiRequest):
            """
            Args:
                id (int) : example( 82 )
                BEGIN_DATE (str) : example( 2022-12-01+15:18 )
                END_DATE (str) : example( 2022-12-07+15:18 )
                BulTitle (int) : example( 333 )
                BulContent (int) : example( 222 )
                AB (str) : example( zh-CN )
                GameName (int|bool) : example( 0 )
                SendInterval (int|bool) : example( 1 )
                _csrf (str) : example( abNeUUDw-1BROJW1dkFNrHOVu81j5InQOc3Y )
            """
            data_type = "params"
            api = "/bulletin/Edit"
            url = "http://192.168.33.5:9100/bulletin/Edit"
            method = "POST"
        @dataclass
        class GetID(ApiRequest):
            """
            Args:
                id (int) : example( 82 )
            """
            data_type = "params"
            api = "/bulletin/GetID"
            url = "http://192.168.33.5:9100/bulletin/GetID"
            method = "POST"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                total (int) : example( 26 )
                _ (int) : example( 1673925511128 )
            """
            def __init__(self,limit=None, offset=None, total=None, _=None):
                self.data = {"limit":limit,"offset":offset,"total":total,"_":_}
            data_type = "params"
            api = "/bulletin/GetList"
            url = "http://192.168.33.5:9100/bulletin/GetList"
            method = "GET"
        @dataclass
        class GetTypes(ApiRequest):
            api = "/bulletin/GetTypes"
            url = "http://192.168.33.5:9100/bulletin/GetTypes"
            method = "GET"
        @dataclass
        class changestatus(ApiRequest):
            """
            Args:
                id (int) : example( 88 )
                BulletinStatus (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/bulletin/changestatus"
            url = "http://192.168.33.5:9100/bulletin/changestatus"
            method = "POST"
        @dataclass
        class delete(ApiRequest):
            """
            Args:
                ids (int) : example( 88 )
            """
            data_type = "params"
            api = "/bulletin/delete"
            url = "http://192.168.33.5:9100/bulletin/delete"
            method = "POST"
        @dataclass
        class getGameType(ApiRequest):
            api = "/bulletin/getGameType"
            url = "http://192.168.33.5:9100/bulletin/getGameType"
            method = "GET"
    @dataclass
    class company(ApiRequest):
        """
        api_list:
            GetList ,
            addCompany ,
            changeCompanyStatus ,
            changeGameStatus ,
            editCompany ,
            editGame ,
            gameList
        """
        api = "/company"
        url = "http://192.168.33.5:9100/company"
        method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 50 )
                offset (int|bool) : example( 0 )
                nickname (str) : example(  )
                companyId (str) : example(  )
                selStatus (str) : example( -1 )
            """
            def __init__(self,limit=None, offset=None, nickname=None, companyId=None, selStatus=None):
                self.data = {"limit":limit,"offset":offset,"nickname":nickname,"companyId":companyId,"selStatus":selStatus}
            data_type = "params"
            api = "/company/GetList"
            url = "http://192.168.33.5:9100/company/GetList"
            method = "GET"
        @dataclass
        class addCompany(ApiRequest):
            """
            Args:
                id (str) : example(  )
                nickname (str) : example( 開源體育	 )
                abbreviation (str) : example( 開源體育	 )
                companyid (str) : example( 開源體育	 )
                companyPwd (str) : example( 96e79218965eb72c92a549dd5a330112 )
                whiteip (str) : example(  )
                mark (str) : example(  )
            """
            data_type = "params"
            api = "/company/addCompany"
            url = "http://192.168.33.5:9100/company/addCompany"
            method = "POST"
        @dataclass
        class changeCompanyStatus(ApiRequest):
            """
            Args:
                id (int) : example( 21012 )
                oldStatus (int|bool) : example( 0 )
                newStatus (int|bool) : example( 0 )
            """
            data_type = "params"
            api = "/company/changeCompanyStatus"
            url = "http://192.168.33.5:9100/company/changeCompanyStatus"
            method = "POST"
        @dataclass
        class changeGameStatus(ApiRequest):
            """
            Args:
                id (int) : example( 1004 )
                oldStatus (int|bool) : example( 0 )
                newStatus (int|bool) : example( 0 )
                gameId (int) : example( 7280 )
            """
            data_type = "params"
            api = "/company/changeGameStatus"
            url = "http://192.168.33.5:9100/company/changeGameStatus"
            method = "POST"
        @dataclass
        class editCompany(ApiRequest):
            """
            Args:
                id (int) : example( 21012 )
                nickname (str) : example( 开元体育 )
                abbreviation (str) : example( 开元体育 )
                companyid (int) : example( 21012 )
                companyPwd (str) : example( 96e79218965eb72c92a549dd5a330112 )
                whiteip (str) : example(  )
                mark (str) : example(  )
            """
            data_type = "params"
            api = "/company/editCompany"
            url = "http://192.168.33.5:9100/company/editCompany"
            method = "POST"
        @dataclass
        class editGame(ApiRequest):
            """
            Args:
                id (int) : example( 1004 )
                gameName (str) : example( KYSport )
                gameId (int) : example( 7280 )
                companyid (int) : example( 21012 )
                gameParameter (str) : example( kysport )
                gameUrl (str) : example( 127.0.0.1 )
                regType (int|bool) : example( 0 )
                isShow (int|bool) : example( 0 )
                langIsopen (int|bool) : example( 0 )
                sequence (int) : example( 2 )
                HallData (str) : example( {[4]=1,[5]=1} )
                Vertical (int) : example( 2 )
                HotGame (str) : example( {} )
                extra (str) : example( {category+=+"21012",+type+=+"4"} )
            """
            data_type = "params"
            api = "/company/editGame"
            url = "http://192.168.33.5:9100/company/editGame"
            method = "POST"
        @dataclass
        class gameList(ApiRequest):
            """
            Args:
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                companyId (int) : example( 21012 )
                selStatus (str) : example( -1 )
                _ (int) : example( 1673925112088 )
            """
            def __init__(self,limit=None, offset=None, companyId=None, selStatus=None, _=None):
                self.data = {"limit":limit,"offset":offset,"companyId":companyId,"selStatus":selStatus,"_":_}
            data_type = "params"
            api = "/company/gameList"
            url = "http://192.168.33.5:9100/company/gameList"
            method = "GET"
    @dataclass
    class dailyProfitMonitoring(ApiRequest):
        """
        api_list:
            ExportData ,
            initData
        """
        api = "/dailyProfitMonitoring"
        url = "http://192.168.33.5:9100/dailyProfitMonitoring"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-15 )
                endDate (str) : example( 2023-01-16 )
                account (str) : example(  )
                UID (int|bool) : example( 1 )
                lineCode (str) : example(  )
                rnd (str) : example( 0.08865950045927007 )
            """
            def __init__(self,beginDate=None, endDate=None, account=None, UID=None, lineCode=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"account":account,"UID":UID,"lineCode":lineCode,"rnd":rnd}
            data_type = "params"
            api = "/dailyProfitMonitoring/ExportData"
            url = "http://192.168.33.5:9100/dailyProfitMonitoring/ExportData"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-15 )
                endDate (str) : example( 2023-01-16 )
                account (str) : example(  )
                UID (int|bool) : example( 1 )
                lineCode (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                _ (int) : example( 1673924006285 )
            """
            def __init__(self,beginDate=None, endDate=None, account=None, UID=None, lineCode=None, limit=None, offset=None, total=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"account":account,"UID":UID,"lineCode":lineCode,"limit":limit,"offset":offset,"total":total,"_":_}
            data_type = "params"
            api = "/dailyProfitMonitoring/initData"
            url = "http://192.168.33.5:9100/dailyProfitMonitoring/initData"
            method = "GET"
    @dataclass
    class default(ApiRequest):
        api = "/default"
        url = "http://192.168.33.5:9100/default"
        method = "GET"
    @dataclass
    class deliveryReport(ApiRequest):
        """
        api_list:
            ExportData ,
            InitData ,
            create
        """
        api = "/deliveryReport"
        url = "http://192.168.33.5:9100/deliveryReport"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                statisDate (str) : example( 2023-01 )
                channelId (str) : example(  )
                rnd (str) : example( 0.3705380454716949 )
            """
            def __init__(self,statisDate=None, channelId=None, rnd=None):
                self.data = {"statisDate":statisDate,"channelId":channelId,"rnd":rnd}
            data_type = "params"
            api = "/deliveryReport/ExportData"
            url = "http://192.168.33.5:9100/deliveryReport/ExportData"
            method = "GET"
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                statisDate (str) : example( 2023-01 )
                channelId (int|bool) : example( 1 )
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673924620039 )
            """
            def __init__(self,statisDate=None, channelId=None, limit=None, offset=None, _=None):
                self.data = {"statisDate":statisDate,"channelId":channelId,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/deliveryReport/InitData"
            url = "http://192.168.33.5:9100/deliveryReport/InitData"
            method = "GET"
        @dataclass
        class create(ApiRequest):
            """
            Args:
                createDate1 (str) : example( 2023-01-16 )
                createDate2 (str) : example( 2023-01-17 )
                channelIds (int|bool) : example( 1 )
            """
            def __init__(self,createDate1=None, createDate2=None, channelIds=None):
                self.data = {"createDate1":createDate1,"createDate2":createDate2,"channelIds":channelIds}
            data_type = "params"
            api = "/deliveryReport/create"
            url = "http://192.168.33.5:9100/deliveryReport/create"
            method = "GET"
    @dataclass
    class estAgent(ApiRequest):
        """
        api_list:
            GetChannelInfo ,
            InitData ,
            add ,
            del
        """
        api = "/estAgent"
        url = "http://192.168.33.5:9100/estAgent"
        method = "GET"
        @dataclass
        class GetChannelInfo(ApiRequest):
            """
            Args:
                channelId (int) : example( 123 )
            """
            def __init__(self,channelId=None):
                self.data = {"channelId":channelId}
            data_type = "params"
            api = "/estAgent/GetChannelInfo"
            url = "http://192.168.33.5:9100/estAgent/GetChannelInfo"
            method = "GET"
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                channelId (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673924551353 )
            """
            def __init__(self,channelId=None, limit=None, offset=None, _=None):
                self.data = {"channelId":channelId,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/estAgent/InitData"
            url = "http://192.168.33.5:9100/estAgent/InitData"
            method = "GET"
        @dataclass
        class add(ApiRequest):
            """
            Args:
                channelId (int) : example( 123 )
                nickName (int) : example( 333 )
            """
            def __init__(self,channelId=None, nickName=None):
                self.data = {"channelId":channelId,"nickName":nickName}
            data_type = "params"
            api = "/estAgent/add"
            url = "http://192.168.33.5:9100/estAgent/add"
            method = "GET"
        @dataclass
        class del_(ApiRequest):
            """
            Args:
                channelId (int) : example( 123 )
            """
            def __init__(self,channelId=None):
                self.data = {"channelId":channelId}
            data_type = "params"
            api = "/estAgent/del"
            url = "http://192.168.33.5:9100/estAgent/del"
            method = "GET"
    @dataclass
    class gameDataMonitor(ApiRequest):
        api = "/gameDataMonitor"
        url = "http://192.168.33.5:9100/gameDataMonitor"
        method = "GET"
    @dataclass
    class gameInfoChannel(ApiRequest):
        """
        api_list:
            GetList ,
            StatusCompanyGame ,
            StatusJC
        """
        api = "/gameInfoChannel"
        url = "http://192.168.33.5:9100/gameInfoChannel"
        method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                channelID (int|bool) : example( 1 )
                accounts (str) : example(  )
                selstatus (str) : example( -1 )
            """
            def __init__(self,channelID=None, accounts=None, selstatus=None):
                self.data = {"channelID":channelID,"accounts":accounts,"selstatus":selstatus}
            data_type = "params"
            api = "/gameInfoChannel/GetList"
            url = "http://192.168.33.5:9100/gameInfoChannel/GetList"
            method = "GET"
        @dataclass
        class StatusCompanyGame(ApiRequest):
            """
            Args:
                ChannelID (int|bool) : example( 1 )
                Status (int|bool) : example( 0 )
            """
            data_type = "params"
            api = "/gameInfoChannel/StatusCompanyGame"
            url = "http://192.168.33.5:9100/gameInfoChannel/StatusCompanyGame"
            method = "POST"
        @dataclass
        class StatusJC(ApiRequest):
            """
            Args:
                ChannelID (int|bool) : example( 1 )
                GameID%5B%5D (int) : example( 220 )
                Status (int|bool) : example( 0 )
            """
            data_type = "params"
            api = "/gameInfoChannel/StatusJC"
            url = "http://192.168.33.5:9100/gameInfoChannel/StatusJC"
            method = "POST"
    @dataclass
    class gameLog(ApiRequest):
        api = "/gameLog"
        url = "http://192.168.33.5:9100/gameLog"
        method = "GET"
    @dataclass
    class gameOnlineList(ApiRequest):
        """
        api_list:
            initData
        """
        api = "/gameOnlineList"
        url = "http://192.168.33.5:9100/gameOnlineList"
        method = "GET"
        @dataclass
        class initData(ApiRequest):
            api = "/gameOnlineList/initData"
            url = "http://192.168.33.5:9100/gameOnlineList/initData"
            method = "GET"
    @dataclass
    class gameRecordSort(ApiRequest):
        """
        api_list:
            ExportData ,
            getGameType ,
            initData
        """
        api = "/gameRecordSort"
        url = "http://192.168.33.5:9100/gameRecordSort"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                serverId (str) : example(  )
                endDate (str) : example(  )
                kindid (str) : example(  )
                accounts (str) : example( 1_tim )
                sort (int) : example( 2 )
                proxyid (str) : example(  )
                lineCode (str) : example(  )
                rnd (str) : example( 0.3882070516799645 )
            """
            def __init__(self,beginDate=None, serverId=None, endDate=None, kindid=None, accounts=None, sort=None, proxyid=None, lineCode=None, rnd=None):
                self.data = {"beginDate":beginDate,"serverId":serverId,"endDate":endDate,"kindid":kindid,"accounts":accounts,"sort":sort,"proxyid":proxyid,"lineCode":lineCode,"rnd":rnd}
            data_type = "params"
            api = "/gameRecordSort/ExportData"
            url = "http://192.168.33.5:9100/gameRecordSort/ExportData"
            method = "GET"
        @dataclass
        class getGameType(ApiRequest):
            api = "/gameRecordSort/getGameType"
            url = "http://192.168.33.5:9100/gameRecordSort/getGameType"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                endDate (str) : example(  )
                kindid (str) : example(  )
                accounts (str) : example( 1_tim )
                proxyid (str) : example(  )
                sort (int) : example( 2 )
                limit (int) : example( 50 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                serverId (str) : example(  )
                lineCode (str) : example(  )
                _ (int) : example( 1673924193342 )
            """
            def __init__(self,beginDate=None, endDate=None, kindid=None, accounts=None, proxyid=None, sort=None, limit=None, offset=None, total=None, serverId=None, lineCode=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"kindid":kindid,"accounts":accounts,"proxyid":proxyid,"sort":sort,"limit":limit,"offset":offset,"total":total,"serverId":serverId,"lineCode":lineCode,"_":_}
            data_type = "params"
            api = "/gameRecordSort/initData"
            url = "http://192.168.33.5:9100/gameRecordSort/initData"
            method = "GET"
    @dataclass
    class gameResult(ApiRequest):
        api = "/gameResult"
        url = "http://192.168.33.5:9100/gameResult"
        method = "GET"
    @dataclass
    class gameinfo(ApiRequest):
        """
        api_list:
            GetList ,
            GetPTStatus ,
            GetSystemGameInfo ,
            Getmatchedmodel ,
            UpdateWhetherSupportSingleWallet ,
            getSDKMaintenanceStatus ,
            savePTstatus ,
            switchSDKMaintenanceStatus
        """
        api = "/gameinfo"
        url = "http://192.168.33.5:9100/gameinfo"
        method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 50 )
                offset (int|bool) : example( 0 )
                selstatus (str) : example( -1 )
                total (int|bool) : example( 0 )
            """
            def __init__(self,limit=None, offset=None, selstatus=None, total=None):
                self.data = {"limit":limit,"offset":offset,"selstatus":selstatus,"total":total}
            data_type = "params"
            api = "/gameinfo/GetList"
            url = "http://192.168.33.5:9100/gameinfo/GetList"
            method = "GET"
        @dataclass
        class GetPTStatus(ApiRequest):
            api = "/gameinfo/GetPTStatus"
            url = "http://192.168.33.5:9100/gameinfo/GetPTStatus"
            method = "GET"
        @dataclass
        class GetSystemGameInfo(ApiRequest):
            """
            Args:
                gameId (int) : example( 220 )
            """
            def __init__(self,gameId=None):
                self.data = {"gameId":gameId}
            data_type = "params"
            api = "/gameinfo/GetSystemGameInfo"
            url = "http://192.168.33.5:9100/gameinfo/GetSystemGameInfo"
            method = "GET"
        @dataclass
        class Getmatchedmodel(ApiRequest):
            """
            Args:
                id (int) : example( 220 )
            """
            data_type = "params"
            api = "/gameinfo/Getmatchedmodel"
            url = "http://192.168.33.5:9100/gameinfo/Getmatchedmodel"
            method = "POST"
        @dataclass
        class UpdateWhetherSupportSingleWallet(ApiRequest):
            """
            Args:
                gameId (int) : example( 220 )
                isSupportSingleWallet (int|bool) : example( 1 )
                _csrf (str) : example( 15kg6qap-4eBtf6LhMbJ-6mnldtNHTQUwqeQ )
            """
            data_type = "params"
            api = "/gameinfo/UpdateWhetherSupportSingleWallet"
            url = "http://192.168.33.5:9100/gameinfo/UpdateWhetherSupportSingleWallet"
            method = "POST"
        @dataclass
        class getSDKMaintenanceStatus(ApiRequest):
            """
            Args:
                type (int) : example( 2 )
            """
            def __init__(self,type=None):
                self.data = {"type":type}
            data_type = "params"
            api = "/gameinfo/getSDKMaintenanceStatus"
            url = "http://192.168.33.5:9100/gameinfo/getSDKMaintenanceStatus"
            method = "GET"
        @dataclass
        class savePTstatus(ApiRequest):
            """
            Args:
                PTselradio (int|bool) : example( 1 )
                _csrf (str) : example( 15kg6qap-4eBtf6LhMbJ-6mnldtNHTQUwqeQ )
            """
            data_type = "params"
            api = "/gameinfo/savePTstatus"
            url = "http://192.168.33.5:9100/gameinfo/savePTstatus"
            method = "POST"
        @dataclass
        class switchSDKMaintenanceStatus(ApiRequest):
            """
            Args:
                outGamestatus (int|bool) : example( 0 )
                type (int) : example( 2 )
                _csrf (str) : example( 15kg6qap-4eBtf6LhMbJ-6mnldtNHTQUwqeQ )
            """
            data_type = "params"
            api = "/gameinfo/switchSDKMaintenanceStatus"
            url = "http://192.168.33.5:9100/gameinfo/switchSDKMaintenanceStatus"
            method = "POST"
    @dataclass
    class getCurPageGrant(ApiRequest):
        """
        Args:
            powerid (int) : example( 291 )
        """
        def __init__(self,powerid=None):
            self.data = {"powerid":powerid}
        data_type = "params"
        api = "/getCurPageGrant"
        url = "http://192.168.33.5:9100/getCurPageGrant"
        method = "GET"
    @dataclass
    class getGameType(ApiRequest):
        api = "/getGameType"
        url = "http://192.168.33.5:9100/getGameType"
        method = "GET"
    @dataclass
    class getUserDomain(ApiRequest):
        """
        api_list:
            ExportDomainLogTxt ,
            GetList ,
            status
        """
        api = "/getUserDomain"
        url = "http://192.168.33.5:9100/getUserDomain"
        method = "GET"
        @dataclass
        class ExportDomainLogTxt(ApiRequest):
            """
            Args:
                str (str) : example( 2023-01-17 )
            """
            def __init__(self,str=None):
                self.data = {"str":str}
            data_type = "params"
            api = "/getUserDomain/ExportDomainLogTxt"
            url = "http://192.168.33.5:9100/getUserDomain/ExportDomainLogTxt"
            method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                _ (int) : example( 1673925061236 )
            """
            def __init__(self,beginDate=None, endDate=None, limit=None, offset=None, total=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"limit":limit,"offset":offset,"total":total,"_":_}
            data_type = "params"
            api = "/getUserDomain/GetList"
            url = "http://192.168.33.5:9100/getUserDomain/GetList"
            method = "GET"
        @dataclass
        class status(ApiRequest):
            """
            Args:
                statusCode (int|bool) : example( 1 )
            """
            def __init__(self,statusCode=None):
                self.data = {"statusCode":statusCode}
            data_type = "params"
            api = "/getUserDomain/status"
            url = "http://192.168.33.5:9100/getUserDomain/status"
            method = "GET"
    @dataclass
    class hotupdatecode(ApiRequest):
        """
        api_list:
            GetGameType ,
            GetList ,
            Save ,
            SaveUpdateDemo ,
            SaveUpdateDemoAI ,
            SaveUpdateromm ,
            Updatestatus ,
            deletes
        """
        api = "/hotupdatecode"
        url = "http://192.168.33.5:9100/hotupdatecode"
        method = "GET"
        @dataclass
        class GetGameType(ApiRequest):
            api = "/hotupdatecode/GetGameType"
            url = "http://192.168.33.5:9100/hotupdatecode/GetGameType"
            method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                total (int) : example( 14651 )
                _ (int) : example( 1673925489295 )
            """
            def __init__(self,limit=None, offset=None, total=None, _=None):
                self.data = {"limit":limit,"offset":offset,"total":total,"_":_}
            data_type = "params"
            api = "/hotupdatecode/GetList"
            url = "http://192.168.33.5:9100/hotupdatecode/GetList"
            method = "GET"
        @dataclass
        class Save(ApiRequest):
            """
            Args:
                Serversads (str) : example( updateBServer )
                Demo (str) : example( updateBServer )
                _csrf (str) : example( edKFenlp-41-AkFLv3KaTUwvhWGoVwoWKZSc )
            """
            data_type = "params"
            api = "/hotupdatecode/Save"
            url = "http://192.168.33.5:9100/hotupdatecode/Save"
            method = "POST"
        @dataclass
        class SaveUpdateDemo(ApiRequest):
            """
            Args:
                num (int) : example( 8 )
                msg (str) : example( 更新并重启C端 )
                PSpwd (str) : example( 03f9aeef097033d251225d1247f9dd65 )
                bSideHotUpdatePwd (str) : example(  )
                _csrf (str) : example( Pij2ty3M-rqi35YVLzjsQUSb7cKEU-F6-ugg )
            """
            data_type = "params"
            api = "/hotupdatecode/SaveUpdateDemo"
            url = "http://192.168.33.5:9100/hotupdatecode/SaveUpdateDemo"
            method = "POST"
        @dataclass
        class SaveUpdateDemoAI(ApiRequest):
            """
            Args:
                num (int) : example( 9 )
                msg (str) : example( 更新AI动作 )
                PSpwd (str) : example( 03f9aeef097033d251225d1247f9dd65 )
                ainum (int|bool) : example( 0 )
                UGame (str) : example( gflower )
                bSideHotUpdatePwd (str) : example( Abcd1234! )
                _csrf (str) : example( jVTcAWF4-xMv23nIXFj69Ecxn5Qu9U6V6TlQ )
            """
            data_type = "params"
            api = "/hotupdatecode/SaveUpdateDemoAI"
            url = "http://192.168.33.5:9100/hotupdatecode/SaveUpdateDemoAI"
            method = "POST"
        @dataclass
        class SaveUpdateromm(ApiRequest):
            """
            Args:
                num (int) : example( 5 )
                msg (str) : example( 更新房间配置 )
                PSpwd (str) : example( 03f9aeef097033d251225d1247f9dd65 )
                bSideHotUpdatePwd (str) : example( !Aa123456 )
                _csrf (str) : example( jVTcAWF4-xMv23nIXFj69Ecxn5Qu9U6V6TlQ )
            """
            data_type = "params"
            api = "/hotupdatecode/SaveUpdateromm"
            url = "http://192.168.33.5:9100/hotupdatecode/SaveUpdateromm"
            method = "POST"
        @dataclass
        class Updatestatus(ApiRequest):
            """
            Args:
                id (int) : example( 14844 )
                Spwd (str) : example( 03f9aeef097033d251225d1247f9dd65 )
                bSideHotUpdatePwd (str) : example( !Aa123456 )
            """
            data_type = "params"
            api = "/hotupdatecode/Updatestatus"
            url = "http://192.168.33.5:9100/hotupdatecode/Updatestatus"
            method = "POST"
        @dataclass
        class deletes(ApiRequest):
            """
            Args:
                id (int) : example( 14844 )
                status (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/hotupdatecode/deletes"
            url = "http://192.168.33.5:9100/hotupdatecode/deletes"
            method = "POST"
    @dataclass
    class iPwhitelis(ApiRequest):
        """
        api_list:
            GetID ,
            GetList ,
            delete ,
            edit ,
            save
        """
        api = "/iPwhitelis"
        url = "http://192.168.33.5:9100/iPwhitelis"
        method = "GET"
        @dataclass
        class GetID(ApiRequest):
            """
            Args:
                id (int) : example( 83 )
            """
            data_type = "params"
            api = "/iPwhitelis/GetID"
            url = "http://192.168.33.5:9100/iPwhitelis/GetID"
            method = "POST"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                id (str) : example(  )
                total (int) : example( 2 )
            """
            def __init__(self,limit=None, offset=None, id=None, total=None):
                self.data = {"limit":limit,"offset":offset,"id":id,"total":total}
            data_type = "params"
            api = "/iPwhitelis/GetList"
            url = "http://192.168.33.5:9100/iPwhitelis/GetList"
            method = "GET"
        @dataclass
        class delete(ApiRequest):
            """
            Args:
                ids (int) : example( 83 )
            """
            data_type = "params"
            api = "/iPwhitelis/delete"
            url = "http://192.168.33.5:9100/iPwhitelis/delete"
            method = "POST"
        @dataclass
        class edit(ApiRequest):
            """
            Args:
                id (int) : example( 83 )
                IPAddress (str) : example( 2.2.2.2 )
                IPMark (str) : example( 2.2.2.2 )
                username (str) : example( guanli )
                _csrf (str) : example( 4iGk4oL9-iMk0uizU0AersxLS8ptQvVnzmws )
            """
            data_type = "params"
            api = "/iPwhitelis/edit"
            url = "http://192.168.33.5:9100/iPwhitelis/edit"
            method = "POST"
        @dataclass
        class save(ApiRequest):
            """
            Args:
                IPAddress (str) : example( 2.2.2.2 )
                IPMark (str) : example( 2.2.2.2 )
                username (str) : example(  )
                _csrf (str) : example( 4iGk4oL9-iMk0uizU0AersxLS8ptQvVnzmws )
            """
            data_type = "params"
            api = "/iPwhitelis/save"
            url = "http://192.168.33.5:9100/iPwhitelis/save"
            method = "POST"
    @dataclass
    class ipKillmanagement(ApiRequest):
        """
        api_list:
            GetList ,
            Save
        """
        api = "/ipKillmanagement"
        url = "http://192.168.33.5:9100/ipKillmanagement"
        method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                ip (str) : example(  )
                type (int) : example( 2 )
                _ (int) : example( 1673924253572 )
            """
            def __init__(self,limit=None, offset=None, ip=None, type=None, _=None):
                self.data = {"limit":limit,"offset":offset,"ip":ip,"type":type,"_":_}
            data_type = "params"
            api = "/ipKillmanagement/GetList"
            url = "http://192.168.33.5:9100/ipKillmanagement/GetList"
            method = "GET"
        @dataclass
        class Save(ApiRequest):
            """
            Args:
                type (int|bool) : example( 1 )
                ip (str) : example( 192.168.17.55 )
                _csrf (str) : example( KbwpQQPw-NzC_9O3lVRxQLqh8d1hPuHVMPOg )
            """
            data_type = "params"
            api = "/ipKillmanagement/Save"
            url = "http://192.168.33.5:9100/ipKillmanagement/Save"
            method = "POST"
    @dataclass
    class killmanagement(ApiRequest):
        """
        api_list:
            GetList ,
            Killrecord ,
            updatemstatus
        """
        api = "/killmanagement"
        url = "http://192.168.33.5:9100/killmanagement"
        method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                total (int|bool) : example( 0 )
                selstatus (str) : example( -1 )
                Accounts (str) : example( 1_tim )
                selsort (int) : example( 2 )
                offset (int|bool) : example( 0 )
                limit (int) : example( 10 )
            """
            def __init__(self,total=None, selstatus=None, Accounts=None, selsort=None, offset=None, limit=None):
                self.data = {"total":total,"selstatus":selstatus,"Accounts":Accounts,"selsort":selsort,"offset":offset,"limit":limit}
            data_type = "params"
            api = "/killmanagement/GetList"
            url = "http://192.168.33.5:9100/killmanagement/GetList"
            method = "GET"
        @dataclass
        class Killrecord(ApiRequest):
            """
            Args:
                ZSAccounts (str) : example( 1_tim )
                beginend (int|bool) : example( 0 )
                ZMark (str) : example( TEST )
                _csrf (str) : example( BLUm13sr-_nhQRifQP-lsV63f8s08Gytguvk )
            """
            data_type = "params"
            api = "/killmanagement/Killrecord"
            url = "http://192.168.33.5:9100/killmanagement/Killrecord"
            method = "POST"
        @dataclass
        class updatemstatus(ApiRequest):
            """
            Args:
                account (str) : example( 1_tim )
                Sign (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/killmanagement/updatemstatus"
            url = "http://192.168.33.5:9100/killmanagement/updatemstatus"
            method = "POST"
    @dataclass
    class killseveraladjustments(ApiRequest):
        """
        api_list:
            GetList ,
            Save ,
            SavekillRate ,
            SavekillRateByLineCode ,
            getkillnumber ,
            selkillrate ,
            selkillrateByLineCode
        """
        api = "/killseveraladjustments"
        url = "http://192.168.33.5:9100/killseveraladjustments"
        method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                agentId (int|bool) : example( 1 )
                linecode (str) : example(  )
                limit (int) : example( 5 )
                offset (int|bool) : example( 0 )
            """
            def __init__(self,agentId=None, linecode=None, limit=None, offset=None):
                self.data = {"agentId":agentId,"linecode":linecode,"limit":limit,"offset":offset}
            data_type = "params"
            api = "/killseveraladjustments/GetList"
            url = "http://192.168.33.5:9100/killseveraladjustments/GetList"
            method = "GET"
        @dataclass
        class Save(ApiRequest):
            """
            Args:
                KillRate (int) : example( 10 )
                _csrf (str) : example( 5oEoAgfA-F9vH2404Od3YuNZfHftR-Qe6eFU )
            """
            data_type = "params"
            api = "/killseveraladjustments/Save"
            url = "http://192.168.33.5:9100/killseveraladjustments/Save"
            method = "POST"
        @dataclass
        class SavekillRate(ApiRequest):
            """
            Args:
                killRate (str) : example( 0.05 )
                ChannelID (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/killseveraladjustments/SavekillRate"
            url = "http://192.168.33.5:9100/killseveraladjustments/SavekillRate"
            method = "POST"
        @dataclass
        class SavekillRateByLineCode(ApiRequest):
            """
            Args:
                killRate (str) : example( 0.25 )
                ChannelID (str) : example( 1_1_simonlinecode )
            """
            data_type = "params"
            api = "/killseveraladjustments/SavekillRateByLineCode"
            url = "http://192.168.33.5:9100/killseveraladjustments/SavekillRateByLineCode"
            method = "POST"
        @dataclass
        class getkillnumber(ApiRequest):
            """
            Args:
            """
            api = "/killseveraladjustments/getkillnumber"
            url = "http://192.168.33.5:9100/killseveraladjustments/getkillnumber"
            method = "POST"
        @dataclass
        class selkillrate(ApiRequest):
            """
            Args:
                ChannelIDLinecode (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/killseveraladjustments/selkillrate"
            url = "http://192.168.33.5:9100/killseveraladjustments/selkillrate"
            method = "POST"
        @dataclass
        class selkillrateByLineCode(ApiRequest):
            """
            Args:
                ChannelIDLinecode (str) : example( 1_1_simonlinecode )
            """
            data_type = "params"
            api = "/killseveraladjustments/selkillrateByLineCode"
            url = "http://192.168.33.5:9100/killseveraladjustments/selkillrateByLineCode"
            method = "POST"
    @dataclass
    class linecodeMonitoring(ApiRequest):
        """
        api_list:
            ExportData ,
            initData ,
            initTop5Data
        """
        api = "/linecodeMonitoring"
        url = "http://192.168.33.5:9100/linecodeMonitoring"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                date (str) : example( 2023-01-16 )
                linecode (str) : example(  )
                rnd (str) : example( 0.1423799796653713 )
            """
            def __init__(self,date=None, linecode=None, rnd=None):
                self.data = {"date":date,"linecode":linecode,"rnd":rnd}
            data_type = "params"
            api = "/linecodeMonitoring/ExportData"
            url = "http://192.168.33.5:9100/linecodeMonitoring/ExportData"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                date (str) : example( 2023-01-16 )
                linecode (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673924148405 )
            """
            def __init__(self,date=None, linecode=None, limit=None, offset=None, _=None):
                self.data = {"date":date,"linecode":linecode,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/linecodeMonitoring/initData"
            url = "http://192.168.33.5:9100/linecodeMonitoring/initData"
            method = "GET"
        @dataclass
        class initTop5Data(ApiRequest):
            """
            Args:
                date (str) : example( 2023-01-16 )
                linecode (str) : example( 1_1_simonlinecode )
                channelid (int|bool) : example( 1 )
                type (str) : example( user )
                _ (int) : example( 1673924148407 )
            """
            def __init__(self,date=None, linecode=None, channelid=None, type=None, _=None):
                self.data = {"date":date,"linecode":linecode,"channelid":channelid,"type":type,"_":_}
            data_type = "params"
            api = "/linecodeMonitoring/initTop5Data"
            url = "http://192.168.33.5:9100/linecodeMonitoring/initTop5Data"
            method = "GET"
    @dataclass
    class linecodecount(ApiRequest):
        """
        api_list:
            ExportData ,
            GetList
        """
        api = "/linecodecount"
        url = "http://192.168.33.5:9100/linecodecount"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                BEGIN_DATE (str) : example( 2023-01-16 )
                rnd (str) : example( 0.20329398107111984 )
            """
            def __init__(self,BEGIN_DATE=None, rnd=None):
                self.data = {"BEGIN_DATE":BEGIN_DATE,"rnd":rnd}
            data_type = "params"
            api = "/linecodecount/ExportData"
            url = "http://192.168.33.5:9100/linecodecount/ExportData"
            method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                Accounts (int|bool) : example( 1 )
                LineCode (str) : example(  )
                Sort (str) : example( -1 )
                total (int|bool) : example( 0 )
                BEGIN_DATES (str) : example( 2023-01-13 )
                _ (int) : example( 1673924024864 )
            """
            def __init__(self,limit=None, offset=None, Accounts=None, LineCode=None, Sort=None, total=None, BEGIN_DATES=None, _=None):
                self.data = {"limit":limit,"offset":offset,"Accounts":Accounts,"LineCode":LineCode,"Sort":Sort,"total":total,"BEGIN_DATES":BEGIN_DATES,"_":_}
            data_type = "params"
            api = "/linecodecount/GetList"
            url = "http://192.168.33.5:9100/linecodecount/GetList"
            method = "GET"
    @dataclass
    class login(ApiRequest):
        """
        Args:
            name (str) : example( guanli )
            password (str) : example( 03f9aeef097033d251225d1247f9dd65 )
            validateCode (str) : example(  )
            count (int|bool) : example( 0 )
        """
        data_type = "params"
        api = "/login"
        url = "http://192.168.33.5:9100/login"
        method = "POST"
    @dataclass
    class memberHistoryBet(ApiRequest):
        """
        api_list:
            ExportData ,
            getGameType ,
            initData
        """
        api = "/memberHistoryBet"
        url = "http://192.168.33.5:9100/memberHistoryBet"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                kindId (int) : example( 610 )
                accounts (str) : example( 1_tim )
                proxyid (int|bool) : example( 1 )
                rnd (str) : example( 0.5086934696730461 )
            """
            def __init__(self,beginDate=None, endDate=None, kindId=None, accounts=None, proxyid=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"kindId":kindId,"accounts":accounts,"proxyid":proxyid,"rnd":rnd}
            data_type = "params"
            api = "/memberHistoryBet/ExportData"
            url = "http://192.168.33.5:9100/memberHistoryBet/ExportData"
            method = "GET"
        @dataclass
        class getGameType(ApiRequest):
            api = "/memberHistoryBet/getGameType"
            url = "http://192.168.33.5:9100/memberHistoryBet/getGameType"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                kindId (int) : example( 610 )
                accounts (str) : example( 1_tim )
                proxyid (int|bool) : example( 1 )
                limit (int) : example( 50 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                _ (int) : example( 1673924461949 )
            """
            def __init__(self,beginDate=None, endDate=None, kindId=None, accounts=None, proxyid=None, limit=None, offset=None, total=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"kindId":kindId,"accounts":accounts,"proxyid":proxyid,"limit":limit,"offset":offset,"total":total,"_":_}
            data_type = "params"
            api = "/memberHistoryBet/initData"
            url = "http://192.168.33.5:9100/memberHistoryBet/initData"
            method = "GET"
    @dataclass
    class memberInfo(ApiRequest):
        """
        api_list:
            ClearMoney ,
            ClearMoneyHundred ,
            GetGamePlay ,
            OutGame ,
            Statuschange ,
            drawmemberMoney ,
            readSBOInfo ,
            savememberMoney
        """
        api = "/memberInfo"
        url = "http://192.168.33.5:9100/memberInfo"
        method = "GET"
        @dataclass
        class ClearMoney(ApiRequest):
            """
            Args:
                account (str) : example( 1_khjgkjh )
                Spwd (str) : example( 03f9aeef097033d251225d1247f9dd65 )
                flag (int|bool) : example( 0 )
            """
            data_type = "params"
            api = "/memberInfo/ClearMoney"
            url = "http://192.168.33.5:9100/memberInfo/ClearMoney"
            method = "POST"
        @dataclass
        class ClearMoneyHundred(ApiRequest):
            """
            Args:
                account (str) : example( 1_khjgkjh )
                Spwd (str) : example( 03f9aeef097033d251225d1247f9dd65 )
                flag (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/memberInfo/ClearMoneyHundred"
            url = "http://192.168.33.5:9100/memberInfo/ClearMoneyHundred"
            method = "POST"
        @dataclass
        class GetGamePlay(ApiRequest):
            """
            Args:
                account (str) : example( 1_khjgkjh )
                lineCode (str) : example( 1_1_simonlinecode )
                agent (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/memberInfo/GetGamePlay"
            url = "http://192.168.33.5:9100/memberInfo/GetGamePlay"
            method = "POST"
        @dataclass
        class OutGame(ApiRequest):
            """
            Args:
                account (str) : example( 1_khjgkjh )
            """
            data_type = "params"
            api = "/memberInfo/OutGame"
            url = "http://192.168.33.5:9100/memberInfo/OutGame"
            method = "POST"
        @dataclass
        class Statuschange(ApiRequest):
            """
            Args:
                account (str) : example( 1_khjgkjh )
                status (int|bool) : example( 0 )
                ChannelID (int|bool) : example( 1 )
                Mark (str) : example( TEST )
                _csrf (str) : example( JfapBOxp-LeusQKAixuUStSQHEBenBJRFGhU )
            """
            data_type = "params"
            api = "/memberInfo/Statuschange"
            url = "http://192.168.33.5:9100/memberInfo/Statuschange"
            method = "POST"
        @dataclass
        class drawmemberMoney(ApiRequest):
            """
            Args:
                id (str) : example(  )
                ChannelID (int|bool) : example( 1 )
                CZMoney (int) : example( 100 )
                CZAccount (str) : example( 1_khjgkjh )
                hidsymoney (int) : example( 10199 )
            """
            data_type = "params"
            api = "/memberInfo/drawmemberMoney"
            url = "http://192.168.33.5:9100/memberInfo/drawmemberMoney"
            method = "POST"
        @dataclass
        class readSBOInfo(ApiRequest):
            """
            Args:
                account (str) : example( 1_khjgkjh )
            """
            data_type = "params"
            api = "/memberInfo/readSBOInfo"
            url = "http://192.168.33.5:9100/memberInfo/readSBOInfo"
            method = "POST"
        @dataclass
        class savememberMoney(ApiRequest):
            """
            Args:
                id (str) : example(  )
                ChannelID (int|bool) : example( 1 )
                CZMoney (int) : example( 100 )
                CZAccount (str) : example( 1_khjgkjh )
                hidsymoney (int) : example( 10099 )
            """
            data_type = "params"
            api = "/memberInfo/savememberMoney"
            url = "http://192.168.33.5:9100/memberInfo/savememberMoney"
            method = "POST"
    @dataclass
    class memberVisitRoute(ApiRequest):
        """
        api_list:
            exportData ,
            getVisitOrder
        """
        api = "/memberVisitRoute"
        url = "http://192.168.33.5:9100/memberVisitRoute"
        method = "GET"
        @dataclass
        class exportData(ApiRequest):
            """
            Args:
                startDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                exportName (str) : example( %E6%96%B0%E7%94%A8%E6%88%B7%E8%AE%BF%E9%97%AE%E8%B7%AF%E5%BE%84%E6%8A%A5%E8%A1%A8 )
                type (int|bool) : example( 1 )
            """
            def __init__(self,startDate=None, endDate=None, exportName=None, type=None):
                self.data = {"startDate":startDate,"endDate":endDate,"exportName":exportName,"type":type}
            data_type = "params"
            api = "/memberVisitRoute/exportData"
            url = "http://192.168.33.5:9100/memberVisitRoute/exportData"
            method = "GET"
        @dataclass
        class getVisitOrder(ApiRequest):
            """
            Args:
                startDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                GameID (str) : example(  )
                type (int) : example( 2 )
                gameParameter (str) : example(  )
                playGameSort (str) : example(  )
            """
            def __init__(self,startDate=None, endDate=None, GameID=None, type=None, gameParameter=None, playGameSort=None):
                self.data = {"startDate":startDate,"endDate":endDate,"GameID":GameID,"type":type,"gameParameter":gameParameter,"playGameSort":playGameSort}
            data_type = "params"
            api = "/memberVisitRoute/getVisitOrder"
            url = "http://192.168.33.5:9100/memberVisitRoute/getVisitOrder"
            method = "GET"
    @dataclass
    class memberfeedback(ApiRequest):
        """
        api_list:
            ExportData ,
            GetList ,
            getGameType
        """
        api = "/memberfeedback"
        url = "http://192.168.33.5:9100/memberfeedback"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2022-12-01%2011:10 )
                endDate (str) : example( 2022-12-07%2011:10 )
                account (str) : example(  )
                selGameType (str) : example(  )
                rnd (str) : example( 0.9378289962500301 )
            """
            def __init__(self,beginDate=None, endDate=None, account=None, selGameType=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"account":account,"selGameType":selGameType,"rnd":rnd}
            data_type = "params"
            api = "/memberfeedback/ExportData"
            url = "http://192.168.33.5:9100/memberfeedback/ExportData"
            method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                account (str) : example(  )
                total (int|bool) : example( 0 )
                beginDate (str) : example( 2022-12-01+11%3A10 )
                endDate (str) : example( 2022-12-07+11%3A10 )
                selGameType (str) : example(  )
            """
            def __init__(self,limit=None, offset=None, account=None, total=None, beginDate=None, endDate=None, selGameType=None):
                self.data = {"limit":limit,"offset":offset,"account":account,"total":total,"beginDate":beginDate,"endDate":endDate,"selGameType":selGameType}
            data_type = "params"
            api = "/memberfeedback/GetList"
            url = "http://192.168.33.5:9100/memberfeedback/GetList"
            method = "GET"
        @dataclass
        class getGameType(ApiRequest):
            api = "/memberfeedback/getGameType"
            url = "http://192.168.33.5:9100/memberfeedback/getGameType"
            method = "GET"
    @dataclass
    class memberinfo(ApiRequest):
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                BeginDate (str) : example(  )
                EndDate (str) : example(  )
                Accounts (str) : example(  )
                Proxyaccount (int|bool) : example( 1 )
                mstatus (str) : example( -1 )
            """
            def __init__(self,BeginDate=None, EndDate=None, Accounts=None, Proxyaccount=None, mstatus=None):
                self.data = {"BeginDate":BeginDate,"EndDate":EndDate,"Accounts":Accounts,"Proxyaccount":Proxyaccount,"mstatus":mstatus}
            data_type = "params"
            api = "/memberinfo/ExportData"
            url = "http://192.168.33.5:9100/memberinfo/ExportData"
            method = "GET"
    @dataclass
    class memberinfo(ApiRequest):
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                Accounts (str) : example(  )
                total (int|bool) : example( 0 )
                selstatus (str) : example( -1 )
                Proxyaccount (int|bool) : example( 1 )
                hidserch (int|bool) : example( 1 )
                BeginDate (str) : example(  )
                EndDate (str) : example(  )
                _ (int) : example( 1673923517801 )
            """
            def __init__(self,limit=None, offset=None, Accounts=None, total=None, selstatus=None, Proxyaccount=None, hidserch=None, BeginDate=None, EndDate=None, _=None):
                self.data = {"limit":limit,"offset":offset,"Accounts":Accounts,"total":total,"selstatus":selstatus,"Proxyaccount":Proxyaccount,"hidserch":hidserch,"BeginDate":BeginDate,"EndDate":EndDate,"_":_}
            data_type = "params"
            api = "/memberinfo/GetList"
            url = "http://192.168.33.5:9100/memberinfo/GetList"
            method = "GET"
    @dataclass
    class menumanage(ApiRequest):
        """
        api_list:
            del ,
            edit ,
            initDataByModuleid ,
            initTree ,
            save
        """
        api = "/menumanage"
        url = "http://192.168.33.5:9100/menumanage"
        method = "GET"
        @dataclass
        class del_(ApiRequest):
            """
            Args:
                ids (int) : example( 1228 )
                pid (int|bool) : example( 0 )
            """
            data_type = "params"
            api = "/menumanage/del"
            url = "http://192.168.33.5:9100/menumanage/del"
            method = "POST"
        @dataclass
        class edit(ApiRequest):
            """
            Args:
                id (int) : example( 1228 )
                pid (int|bool) : example( 0 )
                menuTitle (int) : example( 123 )
                menuLink (str) : example(  )
                menuIcon (str) : example(  )
                status (int|bool) : example( 1 )
                sort (int|bool) : example( 0 )
                mark (str) : example(  )
                isagent (int|bool) : example( 1 )
                _csrf (str) : example( vincRgde-CVeQLXZcOfCnZNSjPQbVRnjpxbU )
            """
            data_type = "params"
            api = "/menumanage/edit"
            url = "http://192.168.33.5:9100/menumanage/edit"
            method = "POST"
        @dataclass
        class initDataByModuleid(ApiRequest):
            """
            Args:
                status (str) : example(  )
                pid (int|bool) : example( 0 )
                menuTitle (str) : example(  )
                total (int|bool) : example( 0 )
                _ (int) : example( 1673924497034 )
            """
            def __init__(self,status=None, pid=None, menuTitle=None, total=None, _=None):
                self.data = {"status":status,"pid":pid,"menuTitle":menuTitle,"total":total,"_":_}
            data_type = "params"
            api = "/menumanage/initDataByModuleid"
            url = "http://192.168.33.5:9100/menumanage/initDataByModuleid"
            method = "GET"
        @dataclass
        class initTree(ApiRequest):
            api = "/menumanage/initTree"
            url = "http://192.168.33.5:9100/menumanage/initTree"
            method = "GET"
        @dataclass
        class save(ApiRequest):
            """
            Args:
                pid (int|bool) : example( 0 )
                menuTitle (int) : example( 123 )
                menuLink (str) : example(  )
                menuIcon (str) : example(  )
                status (int|bool) : example( 1 )
                sort (str) : example(  )
                mark (str) : example(  )
                isagent (int|bool) : example( 1 )
                _csrf (str) : example( vincRgde-CVeQLXZcOfCnZNSjPQbVRnjpxbU )
            """
            data_type = "params"
            api = "/menumanage/save"
            url = "http://192.168.33.5:9100/menumanage/save"
            method = "POST"
    @dataclass
    class onlineplayer(ApiRequest):
        """
        api_list:
            get24HoursOnline
        """
        api = "/onlineplayer"
        url = "http://192.168.33.5:9100/onlineplayer"
        method = "GET"
        @dataclass
        class get24HoursOnline(ApiRequest):
            """
            Args:
                interval (int|bool) : example( 1 )
            """
            def __init__(self,interval=None):
                self.data = {"interval":interval}
            data_type = "params"
            api = "/onlineplayer/get24HoursOnline"
            url = "http://192.168.33.5:9100/onlineplayer/get24HoursOnline"
            method = "GET"
    @dataclass
    class preview(ApiRequest):
        """
        api_list:
            getPreviewData ,
            getThirtyData ,
            initProxyList ,
            previewRangeExport ,
            previewSingleExport
        """
        api = "/preview"
        url = "http://192.168.33.5:9100/preview"
        method = "GET"
        @dataclass
        class getPreviewData(ApiRequest):
            """
            Args:
                channelIds (str) : example(  )
            """
            def __init__(self,channelIds=None):
                self.data = {"channelIds":channelIds}
            data_type = "params"
            api = "/preview/getPreviewData"
            url = "http://192.168.33.5:9100/preview/getPreviewData"
            method = "GET"
        @dataclass
        class getThirtyData(ApiRequest):
            api = "/preview/getThirtyData"
            url = "http://192.168.33.5:9100/preview/getThirtyData"
            method = "GET"
        @dataclass
        class initProxyList(ApiRequest):
            """
            Args:
                proxyName (str) : example(  )
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673924921751 )
            """
            def __init__(self,proxyName=None, limit=None, offset=None, _=None):
                self.data = {"proxyName":proxyName,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/preview/initProxyList"
            url = "http://192.168.33.5:9100/preview/initProxyList"
            method = "GET"
        @dataclass
        class previewRangeExport(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                rnd (str) : example( 0.02548659220037175 )
            """
            def __init__(self,beginDate=None, endDate=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"rnd":rnd}
            data_type = "params"
            api = "/preview/previewRangeExport"
            url = "http://192.168.33.5:9100/preview/previewRangeExport"
            method = "GET"
        @dataclass
        class previewSingleExport(ApiRequest):
            """
            Args:
                singleDate (str) : example( 2023-01-16 )
                rnd (str) : example( 0.9641244774392208 )
            """
            def __init__(self,singleDate=None, rnd=None):
                self.data = {"singleDate":singleDate,"rnd":rnd}
            data_type = "params"
            api = "/preview/previewSingleExport"
            url = "http://192.168.33.5:9100/preview/previewSingleExport"
            method = "GET"
    @dataclass
    class profitcharts(ApiRequest):
        """
        api_list:
            GetList ,
            Killrecord
        """
        api = "/profitcharts"
        url = "http://192.168.33.5:9100/profitcharts"
        method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 100 )
                offset (int|bool) : example( 0 )
                id (str) : example(  )
                Accounts (str) : example( 1_XD001 )
                total (int|bool) : example( 0 )
                selsort (int|bool) : example( 0 )
            """
            def __init__(self,limit=None, offset=None, id=None, Accounts=None, total=None, selsort=None):
                self.data = {"limit":limit,"offset":offset,"id":id,"Accounts":Accounts,"total":total,"selsort":selsort}
            data_type = "params"
            api = "/profitcharts/GetList"
            url = "http://192.168.33.5:9100/profitcharts/GetList"
            method = "GET"
        @dataclass
        class Killrecord(ApiRequest):
            """
            Args:
                ZSAccounts (str) : example( 1_XD001 )
                beginend (int|bool) : example( 1 )
                ZMark (str) : example( TEST )
                _csrf (str) : example( MDovsJPM-zTYkATolt2cQySYbUAXAl8cLWqE )
            """
            data_type = "params"
            api = "/profitcharts/Killrecord"
            url = "http://192.168.33.5:9100/profitcharts/Killrecord"
            method = "POST"
    @dataclass
    class proxyCardStatis(ApiRequest):
        """
        api_list:
            ExportData ,
            GetGameType ,
            InitLinecode ,
            getAllLinecode ,
            initData
        """
        api = "/proxyCardStatis"
        url = "http://192.168.33.5:9100/proxyCardStatis"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                endDate (str) : example(  )
                proxyName (str) : example(  )
                sort (str) : example( general )
                gameid (str) : example(  )
                GameName (str) : example( %E5%85%A8%E9%83%A8 )
                searchType (str) : example(  )
                channelId (str) : example(  )
                typeAllId (int) : example( 3 )
                Disablelinecode (int|bool) : example( 0 )
                rnd (str) : example( 0.11582126615947974 )
            """
            def __init__(self,beginDate=None, endDate=None, proxyName=None, sort=None, gameid=None, GameName=None, searchType=None, channelId=None, typeAllId=None, Disablelinecode=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"proxyName":proxyName,"sort":sort,"gameid":gameid,"GameName":GameName,"searchType":searchType,"channelId":channelId,"typeAllId":typeAllId,"Disablelinecode":Disablelinecode,"rnd":rnd}
            data_type = "params"
            api = "/proxyCardStatis/ExportData"
            url = "http://192.168.33.5:9100/proxyCardStatis/ExportData"
            method = "GET"
        @dataclass
        class GetGameType(ApiRequest):
            """
            Args:
                type (int) : example( 3 )
            """
            def __init__(self,type=None):
                self.data = {"type":type}
            data_type = "params"
            api = "/proxyCardStatis/GetGameType"
            url = "http://192.168.33.5:9100/proxyCardStatis/GetGameType"
            method = "GET"
        @dataclass
        class InitLinecode(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                endDate (str) : example(  )
                linecode (str) : example(  )
                kindId (str) : example(  )
                channelId (int|bool) : example( 1 )
                channelName (str) : example( simonagent )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                searchType (str) : example(  )
                typeAllId (int) : example( 3 )
                _ (int) : example( 1673923662672 )
            """
            def __init__(self,beginDate=None, endDate=None, linecode=None, kindId=None, channelId=None, channelName=None, limit=None, offset=None, total=None, searchType=None, typeAllId=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"linecode":linecode,"kindId":kindId,"channelId":channelId,"channelName":channelName,"limit":limit,"offset":offset,"total":total,"searchType":searchType,"typeAllId":typeAllId,"_":_}
            data_type = "params"
            api = "/proxyCardStatis/InitLinecode"
            url = "http://192.168.33.5:9100/proxyCardStatis/InitLinecode"
            method = "GET"
        @dataclass
        class getAllLinecode(ApiRequest):
            """
            Args:
                channelId (int) : example( 2 )
            """
            def __init__(self,channelId=None):
                self.data = {"channelId":channelId}
            data_type = "params"
            api = "/proxyCardStatis/getAllLinecode"
            url = "http://192.168.33.5:9100/proxyCardStatis/getAllLinecode"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                endDate (str) : example(  )
                proxyName (str) : example(  )
                channelId (int|bool) : example( 0 )
                sort (str) : example( general )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                gameid (str) : example(  )
                GameName (str) : example( %E5%85%A8%E9%83%A8 )
                searchType (str) : example(  )
                typeAllId (int) : example( 3 )
                _ (int) : example( 1673923662674 )
            """
            def __init__(self,beginDate=None, endDate=None, proxyName=None, channelId=None, sort=None, limit=None, offset=None, total=None, gameid=None, GameName=None, searchType=None, typeAllId=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"proxyName":proxyName,"channelId":channelId,"sort":sort,"limit":limit,"offset":offset,"total":total,"gameid":gameid,"GameName":GameName,"searchType":searchType,"typeAllId":typeAllId,"_":_}
            data_type = "params"
            api = "/proxyCardStatis/initData"
            url = "http://192.168.33.5:9100/proxyCardStatis/initData"
            method = "GET"
    @dataclass
    class proxyMoneyChangeDetail(ApiRequest):
        """
        api_list:
            ExportData ,
            initData
        """
        api = "/proxyMoneyChangeDetail"
        url = "http://192.168.33.5:9100/proxyMoneyChangeDetail"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                endDate (str) : example(  )
                orderType (str) : example(  )
                orderstatus (str) : example(  )
                proxyName (str) : example(  )
                createUser (str) : example(  )
                rnd (str) : example( 0.7044227261626159 )
            """
            def __init__(self,beginDate=None, endDate=None, orderType=None, orderstatus=None, proxyName=None, createUser=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"orderType":orderType,"orderstatus":orderstatus,"proxyName":proxyName,"createUser":createUser,"rnd":rnd}
            data_type = "params"
            api = "/proxyMoneyChangeDetail/ExportData"
            url = "http://192.168.33.5:9100/proxyMoneyChangeDetail/ExportData"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                endDate (str) : example(  )
                orderType (str) : example(  )
                proxyName (str) : example(  )
                createUser (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                orderstatus (str) : example(  )
                _ (int) : example( 1673923622640 )
            """
            def __init__(self,beginDate=None, endDate=None, orderType=None, proxyName=None, createUser=None, limit=None, offset=None, total=None, orderstatus=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"orderType":orderType,"proxyName":proxyName,"createUser":createUser,"limit":limit,"offset":offset,"total":total,"orderstatus":orderstatus,"_":_}
            data_type = "params"
            api = "/proxyMoneyChangeDetail/initData"
            url = "http://192.168.33.5:9100/proxyMoneyChangeDetail/initData"
            method = "GET"
    @dataclass
    class proxyStatis(ApiRequest):
        """
        api_list:
            ExportData ,
            GetGameType ,
            InitLinecode ,
            initData
        """
        api = "/proxyStatis"
        url = "http://192.168.33.5:9100/proxyStatis"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                proxyName (str) : example(  )
                sort (str) : example( sort )
                gameid (str) : example(  )
                GameName (str) : example( %E5%85%A8%E9%83%A8 )
                searchType (str) : example(  )
                channelId (int|bool) : example( 0 )
                typeAllId (int|bool) : example( 0 )
                Disablelinecode (int|bool) : example( 0 )
                rnd (str) : example( 0.7394370890189288 )
            """
            def __init__(self,beginDate=None, endDate=None, proxyName=None, sort=None, gameid=None, GameName=None, searchType=None, channelId=None, typeAllId=None, Disablelinecode=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"proxyName":proxyName,"sort":sort,"gameid":gameid,"GameName":GameName,"searchType":searchType,"channelId":channelId,"typeAllId":typeAllId,"Disablelinecode":Disablelinecode,"rnd":rnd}
            data_type = "params"
            api = "/proxyStatis/ExportData"
            url = "http://192.168.33.5:9100/proxyStatis/ExportData"
            method = "GET"
        @dataclass
        class GetGameType(ApiRequest):
            """
            Args:
                type (int|bool) : example( 0 )
            """
            def __init__(self,type=None):
                self.data = {"type":type}
            data_type = "params"
            api = "/proxyStatis/GetGameType"
            url = "http://192.168.33.5:9100/proxyStatis/GetGameType"
            method = "GET"
        @dataclass
        class InitLinecode(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                endDate (str) : example(  )
                linecode (str) : example(  )
                kindId (str) : example(  )
                channelId (int) : example( 23 )
                channelName (str) : example( weiagent2 )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                searchType (str) : example(  )
                typeAllId (int|bool) : example( 0 )
                _ (int) : example( 1673923627204 )
            """
            def __init__(self,beginDate=None, endDate=None, linecode=None, kindId=None, channelId=None, channelName=None, limit=None, offset=None, total=None, searchType=None, typeAllId=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"linecode":linecode,"kindId":kindId,"channelId":channelId,"channelName":channelName,"limit":limit,"offset":offset,"total":total,"searchType":searchType,"typeAllId":typeAllId,"_":_}
            data_type = "params"
            api = "/proxyStatis/InitLinecode"
            url = "http://192.168.33.5:9100/proxyStatis/InitLinecode"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                proxyName (str) : example(  )
                channelId (int|bool) : example( 0 )
                sort (str) : example( sort )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                gameid (str) : example(  )
                GameName (str) : example( %E5%85%A8%E9%83%A8 )
                searchType (str) : example(  )
                typeAllId (int|bool) : example( 0 )
                _ (int) : example( 1673923627209 )
            """
            def __init__(self,beginDate=None, endDate=None, proxyName=None, channelId=None, sort=None, limit=None, offset=None, total=None, gameid=None, GameName=None, searchType=None, typeAllId=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"proxyName":proxyName,"channelId":channelId,"sort":sort,"limit":limit,"offset":offset,"total":total,"gameid":gameid,"GameName":GameName,"searchType":searchType,"typeAllId":typeAllId,"_":_}
            data_type = "params"
            api = "/proxyStatis/initData"
            url = "http://192.168.33.5:9100/proxyStatis/initData"
            method = "GET"
    @dataclass
    class proxyaccount(ApiRequest):
        """
        api_list:
            GetList ,
            GetListSpecial ,
            GetRole ,
            addProxy ,
            addipwhitelis ,
            addproxygames ,
            addtsproxy ,
            addupdatedownloadlink ,
            changeproxystatus ,
            configsproxyaddress ,
            deletetsProxy ,
            drawproxyMoney ,
            editProxy ,
            getapiproxy ,
            getipwhitebyid ,
            getproxybyid ,
            resetproxyPassword ,
            saveproxyMoney ,
            seldownlink ,
            selproxyaddress ,
            updateapi
        """
        api = "/proxyaccount"
        url = "http://192.168.33.5:9100/proxyaccount"
        method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 50 )
                offset (int|bool) : example( 0 )
                Accounts (str) : example(  )
                proxyUID (str) : example(  )
                proxyUIDS (str) : example(  )
                NickName (str) : example(  )
                ChannelID (str) : example(  )
                BeginDate (str) : example(  )
                EndDate (str) : example(  )
            """
            def __init__(self,limit=None, offset=None, Accounts=None, proxyUID=None, proxyUIDS=None, NickName=None, ChannelID=None, BeginDate=None, EndDate=None):
                self.data = {"limit":limit,"offset":offset,"Accounts":Accounts,"proxyUID":proxyUID,"proxyUIDS":proxyUIDS,"NickName":NickName,"ChannelID":ChannelID,"BeginDate":BeginDate,"EndDate":EndDate}
            data_type = "params"
            api = "/proxyaccount/GetList"
            url = "http://192.168.33.5:9100/proxyaccount/GetList"
            method = "GET"
        @dataclass
        class GetListSpecial(ApiRequest):
            """
            Args:
                Accounts (str) : example(  )
            """
            def __init__(self,Accounts=None):
                self.data = {"Accounts":Accounts}
            data_type = "params"
            api = "/proxyaccount/GetListSpecial"
            url = "http://192.168.33.5:9100/proxyaccount/GetListSpecial"
            method = "GET"
        @dataclass
        class GetRole(ApiRequest):
            api = "/proxyaccount/GetRole"
            url = "http://192.168.33.5:9100/proxyaccount/GetRole"
            method = "GET"
        @dataclass
        class addProxy(ApiRequest):
            """
            Args:
                id (str) : example(  )
                sel_MoneyType (int|bool) : example( 1 )
                ProxyAccount (int) : example( 202301171 )
                ProxyPawd (str) : example( 03f9aeef097033d251225d1247f9dd65 )
                NickName (str) : example(  )
                AccountingFor (int) : example( 10 )
                sportAccountingFor (str) : example(  )
                WhiteIP (str) : example(  )
                Mark (str) : example(  )
                CallBackURL (int|bool) : example( 0 )
                ProxyURL (str) : example(  )
                Forbidden (int|bool) : example( 0 )
                ProxyRevenue (str) : example( 0.05 )
                Pushbutton (int|bool) : example( 0 )
                Deskey (str) : example( JZSI2Z94RACFDSKC )
                Md5key (str) : example( NDSB86Z4MQFNYVK9 )
                banckstatus (int|bool) : example( 0 )
                CallBackLink (str) : example(  )
                feedEnabled (int|bool) : example( 0 )
                Cooperation (int|bool) : example( 0 )
                Timezone (int|bool) : example( 0 )
                Winloschart (int|bool) : example( 1 )
                Disablelinecode (int|bool) : example( 0 )
                logourl (str) : example(  )
                HotGameShow (int|bool) : example( 0 )
                SingleOrSystem (int|bool) : example( 1 )
                DisBusinessAccount (int|bool) : example( 0 )
                BusinessAccount (str) : example(  )
                IsShowRevenue (int|bool) : example( 0 )
                walletType (int|bool) : example( 0 )
                parentId (int|bool) : example( 1 )
                isautopay (int|bool) : example( 0 )
                isPayPopUps (int|bool) : example( 1 )
                language (int|bool) : example( 1 )
                bridgeMoneyType (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/proxyaccount/addProxy"
            url = "http://192.168.33.5:9100/proxyaccount/addProxy"
            method = "POST"
        @dataclass
        class addipwhitelis(ApiRequest):
            """
            Args:
                insertId (int) : example( 155 )
                IPAddress (str) : example(  )
                ProxyAccount (int) : example( 202301171 )
            """
            data_type = "params"
            api = "/proxyaccount/addipwhitelis"
            url = "http://192.168.33.5:9100/proxyaccount/addipwhitelis"
            method = "POST"
        @dataclass
        class addproxygames(ApiRequest):
            """
            Args:
                insertId (int) : example( 155 )
                walletType (int|bool) : example( 0 )
            """
            data_type = "params"
            api = "/proxyaccount/addproxygames"
            url = "http://192.168.33.5:9100/proxyaccount/addproxygames"
            method = "POST"
        @dataclass
        class addtsproxy(ApiRequest):
            """
            Args:
                Accounts (int) : example( 202301171 )
            """
            data_type = "params"
            api = "/proxyaccount/addtsproxy"
            url = "http://192.168.33.5:9100/proxyaccount/addtsproxy"
            method = "POST"
        @dataclass
        class addupdatedownloadlink(ApiRequest):
            """
            Args:
                ChineseAPI (str) : example(  )
                EnglishAPI (str) : example(  )
                AlllanguagesAPI (str) : example(  )
                Lockerdecodedemo (str) : example(  )
                GameNestDemo (str) : example(  )
                Artresources (str) : example(  )
                id (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/proxyaccount/addupdatedownloadlink"
            url = "http://192.168.33.5:9100/proxyaccount/addupdatedownloadlink"
            method = "POST"
        @dataclass
        class changeproxystatus(ApiRequest):
            """
            Args:
                id (int) : example( 150 )
                status (int|bool) : example( 0 )
            """
            data_type = "params"
            api = "/proxyaccount/changeproxystatus"
            url = "http://192.168.33.5:9100/proxyaccount/changeproxystatus"
            method = "POST"
        @dataclass
        class configsproxyaddress(ApiRequest):
            """
            Args:
                Behindaddress (str) : example(  )
                Portaddress (str) : example(  )
                Pullinterface (str) : example(  )
                id (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/proxyaccount/configsproxyaddress"
            url = "http://192.168.33.5:9100/proxyaccount/configsproxyaddress"
            method = "POST"
        @dataclass
        class deletetsProxy(ApiRequest):
            """
            Args:
                id (int) : example( 43 )
            """
            data_type = "params"
            api = "/proxyaccount/deletetsProxy"
            url = "http://192.168.33.5:9100/proxyaccount/deletetsProxy"
            method = "POST"
        @dataclass
        class drawproxyMoney(ApiRequest):
            """
            Args:
                ChannelID (int) : example( 150 )
                CZMoney (int) : example( 100 )
                hidIdtype (int|bool) : example( 1 )
                CZAccount (str) : example( test1121 )
                hidsymoney (int) : example( 100 )
                orderid (int) : example( 15020230117112251412 )
                orderidpj (int) : example( 00000230117112251 )
                AccountingFor (str) : example(  )
            """
            data_type = "params"
            api = "/proxyaccount/drawproxyMoney"
            url = "http://192.168.33.5:9100/proxyaccount/drawproxyMoney"
            method = "POST"
        @dataclass
        class editProxy(ApiRequest):
            """
            Args:
                id (int) : example( 155 )
                sel_MoneyType (int|bool) : example( 1 )
                ProxyAccount (int) : example( 202301171 )
                ProxyPawd (str) : example( 0d04886625da16287684b801d1ccf140 )
                NickName (str) : example(  )
                AccountingFor (int) : example( 10 )
                sportAccountingFor (int|bool) : example( 0 )
                WhiteIP (str) : example(  )
                Mark (str) : example(  )
                CallBackURL (int|bool) : example( 0 )
                ProxyURL (str) : example(  )
                Forbidden (int|bool) : example( 0 )
                ProxyRevenue (str) : example( 0.05 )
                Pushbutton (int|bool) : example( 0 )
                Deskey (str) : example( LUH1SWLNYFYHGWIT )
                Md5key (str) : example( 2XKZQGJHZRTJ8R4E )
                banckstatus (int|bool) : example( 0 )
                CallBackLink (str) : example(  )
                feedEnabled (int|bool) : example( 0 )
                Cooperation (int|bool) : example( 0 )
                Timezone (int|bool) : example( 0 )
                Winloschart (int|bool) : example( 1 )
                Disablelinecode (int|bool) : example( 0 )
                logourl (str) : example(  )
                HotGameShow (int|bool) : example( 0 )
                SingleOrSystem (int|bool) : example( 1 )
                DisBusinessAccount (int|bool) : example( 1 )
                BusinessAccount (str) : example(  )
                IsShowRevenue (int|bool) : example( 0 )
                walletType (int|bool) : example( 0 )
                parentId (int|bool) : example( 1 )
                isautopay (int|bool) : example( 0 )
                isPayPopUps (int|bool) : example( 1 )
                language (int|bool) : example( 1 )
                bridgeMoneyType (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/proxyaccount/editProxy"
            url = "http://192.168.33.5:9100/proxyaccount/editProxy"
            method = "POST"
        @dataclass
        class getapiproxy(ApiRequest):
            """
            Args:
                agent (int) : example( 150 )
            """
            data_type = "params"
            api = "/proxyaccount/getapiproxy"
            url = "http://192.168.33.5:9100/proxyaccount/getapiproxy"
            method = "POST"
        @dataclass
        class getipwhitebyid(ApiRequest):
            """
            Args:
                ChannelID (int) : example( 150 )
            """
            data_type = "params"
            api = "/proxyaccount/getipwhitebyid"
            url = "http://192.168.33.5:9100/proxyaccount/getipwhitebyid"
            method = "POST"
        @dataclass
        class getproxybyid(ApiRequest):
            """
            Args:
                ChannelID (int) : example( 150 )
            """
            data_type = "params"
            api = "/proxyaccount/getproxybyid"
            url = "http://192.168.33.5:9100/proxyaccount/getproxybyid"
            method = "POST"
        @dataclass
        class resetproxyPassword(ApiRequest):
            """
            Args:
                id (int) : example( 150 )
            """
            data_type = "params"
            api = "/proxyaccount/resetproxyPassword"
            url = "http://192.168.33.5:9100/proxyaccount/resetproxyPassword"
            method = "POST"
        @dataclass
        class saveproxyMoney(ApiRequest):
            """
            Args:
                ChannelID (int) : example( 150 )
                CZMoney (int) : example( 100 )
                hidIdtype (int|bool) : example( 0 )
                CZAccount (str) : example( test1121 )
                hidsymoney (int|bool) : example( 0 )
                orderid (int) : example( 15020230117112204855 )
                orderidpj (int) : example( 00000230117112204 )
                AccountingFor (int) : example( 2 )
            """
            data_type = "params"
            api = "/proxyaccount/saveproxyMoney"
            url = "http://192.168.33.5:9100/proxyaccount/saveproxyMoney"
            method = "POST"
        @dataclass
        class seldownlink(ApiRequest):
            api = "/proxyaccount/seldownlink"
            url = "http://192.168.33.5:9100/proxyaccount/seldownlink"
            method = "GET"
        @dataclass
        class selproxyaddress(ApiRequest):
            api = "/proxyaccount/selproxyaddress"
            url = "http://192.168.33.5:9100/proxyaccount/selproxyaddress"
            method = "GET"
        @dataclass
        class updateapi(ApiRequest):
            """
            Args:
                ChannelID (int) : example( 150 )
                Deskey (str) : example( 9F8C7F31C8930181 )
                Md5key (str) : example( 77CA2750593DABEF )
                WhiteIP (str) : example( 192.168.20.205,192.168.17.71,192.168.17.71,192.168.17.70 )
                ISinheritwhiteIP (int|bool) : example( 0 )
            """
            data_type = "params"
            api = "/proxyaccount/updateapi"
            url = "http://192.168.33.5:9100/proxyaccount/updateapi"
            method = "POST"
    @dataclass
    class reduceScoreBlackList(ApiRequest):
        """
        api_list:
            delete ,
            getCondition ,
            initData ,
            save ,
            saveCondition
        """
        api = "/reduceScoreBlackList"
        url = "http://192.168.33.5:9100/reduceScoreBlackList"
        method = "GET"
        @dataclass
        class delete(ApiRequest):
            """
            Args:
                account (str) : example( 1_tim )
            """
            data_type = "params"
            api = "/reduceScoreBlackList/delete"
            url = "http://192.168.33.5:9100/reduceScoreBlackList/delete"
            method = "POST"
        @dataclass
        class getCondition(ApiRequest):
            api = "/reduceScoreBlackList/getCondition"
            url = "http://192.168.33.5:9100/reduceScoreBlackList/getCondition"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                total (int) : example( 7 )
                selectType (int|bool) : example( 1 )
                account (str) : example(  )
                _ (int) : example( 1673924299283 )
            """
            def __init__(self,limit=None, offset=None, total=None, selectType=None, account=None, _=None):
                self.data = {"limit":limit,"offset":offset,"total":total,"selectType":selectType,"account":account,"_":_}
            data_type = "params"
            api = "/reduceScoreBlackList/initData"
            url = "http://192.168.33.5:9100/reduceScoreBlackList/initData"
            method = "GET"
        @dataclass
        class save(ApiRequest):
            """
            Args:
                status (int) : example( 2 )
                account (str) : example( 1_tim )
                mark (str) : example( TEST )
            """
            data_type = "params"
            api = "/reduceScoreBlackList/save"
            url = "http://192.168.33.5:9100/reduceScoreBlackList/save"
            method = "POST"
        @dataclass
        class saveCondition(ApiRequest):
            """
            Args:
                registerDays (int) : example( 10 )
                scoreProportion (str) : example( 0.12 )
            """
            data_type = "params"
            api = "/reduceScoreBlackList/saveCondition"
            url = "http://192.168.33.5:9100/reduceScoreBlackList/saveCondition"
            method = "POST"
    @dataclass
    class rolemanage(ApiRequest):
        """
        api_list:
            delRole ,
            editRole ,
            initData ,
            saveRole
        """
        api = "/rolemanage"
        url = "http://192.168.33.5:9100/rolemanage"
        method = "GET"
        @dataclass
        class delRole(ApiRequest):
            """
            Args:
                ids (int) : example( 5541 )
            """
            data_type = "params"
            api = "/rolemanage/delRole"
            url = "http://192.168.33.5:9100/rolemanage/delRole"
            method = "POST"
        @dataclass
        class editRole(ApiRequest):
            """
            Args:
                id (int) : example( 5541 )
                roleName (str) : example( TEST )
                roleMark (str) : example(  )
                _csrf (str) : example( pEcOyuHQ-aFvy14K4NXwFSa-BeYp57Y4Li3Y )
            """
            data_type = "params"
            api = "/rolemanage/editRole"
            url = "http://192.168.33.5:9100/rolemanage/editRole"
            method = "POST"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                roleName (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673924525934 )
            """
            def __init__(self,roleName=None, limit=None, offset=None, _=None):
                self.data = {"roleName":roleName,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/rolemanage/initData"
            url = "http://192.168.33.5:9100/rolemanage/initData"
            method = "GET"
        @dataclass
        class saveRole(ApiRequest):
            """
            Args:
                roleName (str) : example( TEST )
                roleMark (str) : example(  )
                _csrf (str) : example( pEcOyuHQ-aFvy14K4NXwFSa-BeYp57Y4Li3Y )
            """
            data_type = "params"
            api = "/rolemanage/saveRole"
            url = "http://192.168.33.5:9100/rolemanage/saveRole"
            method = "POST"
    @dataclass
    class roomBanishMonitor(ApiRequest):
        """
        api_list:
            InitData ,
            exportData
        """
        api = "/roomBanishMonitor"
        url = "http://192.168.33.5:9100/roomBanishMonitor"
        method = "GET"
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                gameType (str) : example(  )
                roomType (str) : example(  )
                type (int|bool) : example( 0 )
                kdvalue (int|bool) : example( 0 )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673923986799 )
            """
            def __init__(self,beginDate=None, endDate=None, gameType=None, roomType=None, type=None, kdvalue=None, limit=None, offset=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"gameType":gameType,"roomType":roomType,"type":type,"kdvalue":kdvalue,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/roomBanishMonitor/InitData"
            url = "http://192.168.33.5:9100/roomBanishMonitor/InitData"
            method = "GET"
        @dataclass
        class exportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                gameType (str) : example(  )
                roomType (str) : example(  )
                type (int|bool) : example( 0 )
                kdvalue (int|bool) : example( 0 )
            """
            def __init__(self,beginDate=None, endDate=None, gameType=None, roomType=None, type=None, kdvalue=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"gameType":gameType,"roomType":roomType,"type":type,"kdvalue":kdvalue}
            data_type = "params"
            api = "/roomBanishMonitor/exportData"
            url = "http://192.168.33.5:9100/roomBanishMonitor/exportData"
            method = "GET"
    @dataclass
    class roomMonitoring(ApiRequest):
        """
        api_list:
            ExportData ,
            getGameType ,
            getRoomList ,
            initData
        """
        api = "/roomMonitoring"
        url = "http://192.168.33.5:9100/roomMonitoring"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                rnd (str) : example( 0.8919517048121426 )
            """
            def __init__(self,beginDate=None, endDate=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"rnd":rnd}
            data_type = "params"
            api = "/roomMonitoring/ExportData"
            url = "http://192.168.33.5:9100/roomMonitoring/ExportData"
            method = "GET"
        @dataclass
        class getGameType(ApiRequest):
            api = "/roomMonitoring/getGameType"
            url = "http://192.168.33.5:9100/roomMonitoring/getGameType"
            method = "GET"
        @dataclass
        class getRoomList(ApiRequest):
            api = "/roomMonitoring/getRoomList"
            url = "http://192.168.33.5:9100/roomMonitoring/getRoomList"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                gameType (str) : example(  )
                _ (int) : example( 1673924091112 )
            """
            def __init__(self,beginDate=None, endDate=None, gameType=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"gameType":gameType,"_":_}
            data_type = "params"
            api = "/roomMonitoring/initData"
            url = "http://192.168.33.5:9100/roomMonitoring/initData"
            method = "GET"
    @dataclass
    class roomOnlineMonitoring(ApiRequest):
        """
        api_list:
            initData
        """
        api = "/roomOnlineMonitoring"
        url = "http://192.168.33.5:9100/roomOnlineMonitoring"
        method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                kindId (str) : example(  )
                total (int|bool) : example( 0 )
                _ (int) : example( 1673924164736 )
            """
            def __init__(self,kindId=None, total=None, _=None):
                self.data = {"kindId":kindId,"total":total,"_":_}
            data_type = "params"
            api = "/roomOnlineMonitoring/initData"
            url = "http://192.168.33.5:9100/roomOnlineMonitoring/initData"
            method = "GET"
    @dataclass
    class roomRobotMonitoring(ApiRequest):
        """
        api_list:
            initData
        """
        api = "/roomRobotMonitoring"
        url = "http://192.168.33.5:9100/roomRobotMonitoring"
        method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-15 )
                endDate (str) : example( 2023-01-17 )
                kindId (str) : example(  )
                total (int|bool) : example( 0 )
                _ (int) : example( 1673924180249 )
            """
            def __init__(self,beginDate=None, endDate=None, kindId=None, total=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"kindId":kindId,"total":total,"_":_}
            data_type = "params"
            api = "/roomRobotMonitoring/initData"
            url = "http://192.168.33.5:9100/roomRobotMonitoring/initData"
            method = "GET"
    @dataclass
    class roomWinLossAnalysyis(ApiRequest):
        """
        api_list:
            ExportData ,
            initData
        """
        api = "/roomWinLossAnalysyis"
        url = "http://192.168.33.5:9100/roomWinLossAnalysyis"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                kindId (str) : example(  )
                rnd (str) : example( 0.25155786009743575 )
            """
            def __init__(self,beginDate=None, endDate=None, kindId=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"kindId":kindId,"rnd":rnd}
            data_type = "params"
            api = "/roomWinLossAnalysyis/ExportData"
            url = "http://192.168.33.5:9100/roomWinLossAnalysyis/ExportData"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                kindId (str) : example(  )
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                _ (int) : example( 1673924070950 )
            """
            def __init__(self,kindId=None, beginDate=None, endDate=None, _=None):
                self.data = {"kindId":kindId,"beginDate":beginDate,"endDate":endDate,"_":_}
            data_type = "params"
            api = "/roomWinLossAnalysyis/initData"
            url = "http://192.168.33.5:9100/roomWinLossAnalysyis/initData"
            method = "GET"
    @dataclass
    class sportDeliveryReport(ApiRequest):
        """
        api_list:
            InitData ,
            create
        """
        api = "/sportDeliveryReport"
        url = "http://192.168.33.5:9100/sportDeliveryReport"
        method = "GET"
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                statisDate (str) : example( 2023-01 )
                channelId (str) : example(  )
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                _ (int) : example( 1673924678412 )
            """
            def __init__(self,statisDate=None, channelId=None, limit=None, offset=None, _=None):
                self.data = {"statisDate":statisDate,"channelId":channelId,"limit":limit,"offset":offset,"_":_}
            data_type = "params"
            api = "/sportDeliveryReport/InitData"
            url = "http://192.168.33.5:9100/sportDeliveryReport/InitData"
            method = "GET"
        @dataclass
        class create(ApiRequest):
            """
            Args:
                createDate1 (str) : example( 2023-01-15 )
                createDate2 (str) : example( 2023-01-17 )
                channelIds (int|bool) : example( 1 )
            """
            def __init__(self,createDate1=None, createDate2=None, channelIds=None):
                self.data = {"createDate1":createDate1,"createDate2":createDate2,"channelIds":channelIds}
            data_type = "params"
            api = "/sportDeliveryReport/create"
            url = "http://192.168.33.5:9100/sportDeliveryReport/create"
            method = "GET"
    @dataclass
    class statisAgentInfo(ApiRequest):
        """
        api_list:
            ExportData ,
            ExportData2 ,
            initData
        """
        api = "/statisAgentInfo"
        url = "http://192.168.33.5:9100/statisAgentInfo"
        method = "GET"
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                proxyName (str) : example( undefined )
                channelId (int|bool) : example( 0 )
                sort (str) : example( sort )
                NickName (str) : example(  )
                rnd (str) : example( 0.10504581773558552 )
            """
            def __init__(self,beginDate=None, endDate=None, proxyName=None, channelId=None, sort=None, NickName=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"proxyName":proxyName,"channelId":channelId,"sort":sort,"NickName":NickName,"rnd":rnd}
            data_type = "params"
            api = "/statisAgentInfo/ExportData"
            url = "http://192.168.33.5:9100/statisAgentInfo/ExportData"
            method = "GET"
        @dataclass
        class ExportData2(ApiRequest):
            """
            Args:
                statisDate (str) : example( 2023-01 )
                rnd (str) : example( 0.5342619664746462 )
            """
            def __init__(self,statisDate=None, rnd=None):
                self.data = {"statisDate":statisDate,"rnd":rnd}
            data_type = "params"
            api = "/statisAgentInfo/ExportData2"
            url = "http://192.168.33.5:9100/statisAgentInfo/ExportData2"
            method = "GET"
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
                channelId (int|bool) : example( 0 )
                sort (str) : example( sort )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                NickName (str) : example(  )
                proxyId (int|bool) : example( 1 )
                _ (int) : example( 1673924949562 )
            """
            def __init__(self,beginDate=None, endDate=None, channelId=None, sort=None, limit=None, offset=None, total=None, NickName=None, proxyId=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"channelId":channelId,"sort":sort,"limit":limit,"offset":offset,"total":total,"NickName":NickName,"proxyId":proxyId,"_":_}
            data_type = "params"
            api = "/statisAgentInfo/initData"
            url = "http://192.168.33.5:9100/statisAgentInfo/initData"
            method = "GET"
    @dataclass
    class sysLog(ApiRequest):
        """
        api_list:
            GetList
        """
        api = "/sysLog"
        url = "http://192.168.33.5:9100/sysLog"
        method = "GET"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 15 )
                offset (int|bool) : example( 0 )
                Accounts (str) : example(  )
                total (int|bool) : example( 0 )
                beginDate (str) : example( 2023-01-16 )
                endDate (str) : example( 2023-01-17 )
            """
            def __init__(self,limit=None, offset=None, Accounts=None, total=None, beginDate=None, endDate=None):
                self.data = {"limit":limit,"offset":offset,"Accounts":Accounts,"total":total,"beginDate":beginDate,"endDate":endDate}
            data_type = "params"
            api = "/sysLog/GetList"
            url = "http://192.168.33.5:9100/sysLog/GetList"
            method = "GET"
    @dataclass
    class sysbulletin(ApiRequest):
        """
        api_list:
            Edit ,
            GetID ,
            GetList ,
            Save ,
            changestatus ,
            delete
        """
        api = "/sysbulletin"
        url = "http://192.168.33.5:9100/sysbulletin"
        method = "GET"
        @dataclass
        class Edit(ApiRequest):
            """
            Args:
                id (int) : example( 79 )
                BulTitle (str) : example( &gt; )
                BulContent (str) : example( &gt; )
                Btype (int) : example( 2 )
                _csrf (str) : example( XX6PjgwS-jJemRdBQLtknnwul3y5vzl1PiFw )
            """
            data_type = "params"
            api = "/sysbulletin/Edit"
            url = "http://192.168.33.5:9100/sysbulletin/Edit"
            method = "POST"
        @dataclass
        class GetID(ApiRequest):
            """
            Args:
                id (int) : example( 79 )
            """
            data_type = "params"
            api = "/sysbulletin/GetID"
            url = "http://192.168.33.5:9100/sysbulletin/GetID"
            method = "POST"
        @dataclass
        class GetList(ApiRequest):
            """
            Args:
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                total (int) : example( 8 )
                _ (int) : example( 1673924994949 )
            """
            def __init__(self,limit=None, offset=None, total=None, _=None):
                self.data = {"limit":limit,"offset":offset,"total":total,"_":_}
            data_type = "params"
            api = "/sysbulletin/GetList"
            url = "http://192.168.33.5:9100/sysbulletin/GetList"
            method = "GET"
        @dataclass
        class Save(ApiRequest):
            """
            Args:
                id (str) : example(  )
                BulTitle (str) : example( test )
                BulContent (str) : example( test )
                Btype (int) : example( 2 )
                _csrf (str) : example( XX6PjgwS-jJemRdBQLtknnwul3y5vzl1PiFw )
            """
            data_type = "params"
            api = "/sysbulletin/Save"
            url = "http://192.168.33.5:9100/sysbulletin/Save"
            method = "POST"
        @dataclass
        class changestatus(ApiRequest):
            """
            Args:
                id (int) : example( 79 )
                BulletinStatus (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/sysbulletin/changestatus"
            url = "http://192.168.33.5:9100/sysbulletin/changestatus"
            method = "POST"
        @dataclass
        class delete(ApiRequest):
            """
            Args:
                ids (int) : example( 87 )
            """
            data_type = "params"
            api = "/sysbulletin/delete"
            url = "http://192.168.33.5:9100/sysbulletin/delete"
            method = "POST"
    @dataclass
    class user(ApiRequest):
        """
        api_list:
            SQSave ,
            addUser ,
            changestatus ,
            editUser ,
            resetPassword ,
            searchUser
        """
        api = "/user"
        url = "http://192.168.33.5:9100/user"
        method = "GET"
    @dataclass
    class userExit(ApiRequest):
        """
        Args:
        """
        api = "/userExit"
        url = "http://192.168.33.5:9100/userExit"
        method = "POST"
    @dataclass
    class userLogin(ApiRequest):
        api = "/userLogin"
        url = "http://192.168.33.5:9100/userLogin"
        method = "GET"
    @dataclass
    class userMoneyChangeDetail(ApiRequest):
        @dataclass
        class ExportData(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                endDate (str) : example(  )
                orderType (str) : example(  )
                orderStatus (str) : example(  )
                accounts (str) : example( 1_tim )
                createUser (str) : example(  )
                rnd (str) : example( 0.8840095432486856 )
            """
            def __init__(self,beginDate=None, endDate=None, orderType=None, orderStatus=None, accounts=None, createUser=None, rnd=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"orderType":orderType,"orderStatus":orderStatus,"accounts":accounts,"createUser":createUser,"rnd":rnd}
            data_type = "params"
            api = "/userMoneyChangeDetail/ExportData"
            url = "http://192.168.33.5:9100/userMoneyChangeDetail/ExportData"
            method = "GET"
    @dataclass
    class userMoneyChangeDetail(ApiRequest):
        @dataclass
        class GetAccountMoney(ApiRequest):
            """
            Args:
                account (str) : example( 1_tim )
            """
            data_type = "params"
            api = "/userMoneyChangeDetail/GetAccountMoney"
            url = "http://192.168.33.5:9100/userMoneyChangeDetail/GetAccountMoney"
            method = "POST"
    @dataclass
    class userMoneyChangeDetail(ApiRequest):
        @dataclass
        class initData(ApiRequest):
            """
            Args:
                beginDate (str) : example(  )
                endDate (str) : example(  )
                orderType (str) : example(  )
                accounts (str) : example( 1_tim )
                createUser (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                orderStatus (str) : example(  )
                _ (int) : example( 1673923705577 )
            """
            def __init__(self,beginDate=None, endDate=None, orderType=None, accounts=None, createUser=None, limit=None, offset=None, total=None, orderStatus=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"orderType":orderType,"accounts":accounts,"createUser":createUser,"limit":limit,"offset":offset,"total":total,"orderStatus":orderStatus,"_":_}
            data_type = "params"
            api = "/userMoneyChangeDetail/initData"
            url = "http://192.168.33.5:9100/userMoneyChangeDetail/initData"
            method = "GET"
        @dataclass
        class SQSave(ApiRequest):
            """
            Args:
                Timezone (int|bool) : example( 0 )
            """
            data_type = "params"
            api = "/user/SQSave"
            url = "http://192.168.33.5:9100/user/SQSave"
            method = "POST"
        @dataclass
        class addUser(ApiRequest):
            """
            Args:
                name (int) : example( 2023117 )
                pwd (str) : example( 03f9aeef097033d251225d1247f9dd65 )
                NickName (str) : example(  )
                roleid (int|bool) : example( 1 )
                isagent (int|bool) : example( 0 )
                Timezone (int|bool) : example( 0 )
            """
            data_type = "params"
            api = "/user/addUser"
            url = "http://192.168.33.5:9100/user/addUser"
            method = "POST"
        @dataclass
        class changestatus(ApiRequest):
            """
            Args:
                id (int) : example( 139 )
                status (int|bool) : example( 1 )
            """
            data_type = "params"
            api = "/user/changestatus"
            url = "http://192.168.33.5:9100/user/changestatus"
            method = "POST"
        @dataclass
        class editUser(ApiRequest):
            """
            Args:
                id (int|bool) : example( 1 )
                name (str) : example( guanli )
                pwd (str) : example( 5e543256c480ac577d30f76f9120eb74 )
                NickName (str) : example( test12345 )
                roleid (int|bool) : example( 1 )
                isagent (int|bool) : example( 0 )
                Timezone (int|bool) : example( 0 )
            """
            data_type = "params"
            api = "/user/editUser"
            url = "http://192.168.33.5:9100/user/editUser"
            method = "POST"
        @dataclass
        class resetPassword(ApiRequest):
            """
            Args:
                id (int) : example( 139 )
            """
            data_type = "params"
            api = "/user/resetPassword"
            url = "http://192.168.33.5:9100/user/resetPassword"
            method = "POST"
        @dataclass
        class searchUser(ApiRequest):
            """
            Args:
                limit (int) : example( 10 )
                offset (int|bool) : example( 0 )
                name (str) : example(  )
                total (int|bool) : example( 1 )
                proxyUID (str) : example(  )
                proxyS (str) : example(  )
                hidIdproxyserchtype (str) : example(  )
            """
            def __init__(self,limit=None, offset=None, name=None, total=None, proxyUID=None, proxyS=None, hidIdproxyserchtype=None):
                self.data = {"limit":limit,"offset":offset,"name":name,"total":total,"proxyUID":proxyUID,"proxyS":proxyS,"hidIdproxyserchtype":hidIdproxyserchtype}
            data_type = "params"
            api = "/user/searchUser"
            url = "http://192.168.33.5:9100/user/searchUser"
            method = "GET"
    @dataclass
    class usermoneychangedetail(ApiRequest):
        api = "/usermoneychangedetail"
        url = "http://192.168.33.5:9100/usermoneychangedetail"
        method = "GET"
    @dataclass
    class validateCode(ApiRequest):
        """
        Args:
            d (str) : example( 0.3091343198649332 )
        """
        def __init__(self,d=None):
            self.data = {"d":d}
        data_type = "params"
        api = "/validateCode"
        url = "http://192.168.33.5:9100/validateCode"
        method = "GET"
    @dataclass
    class welcome(ApiRequest):
        api = "/welcome"
        url = "http://192.168.33.5:9100/welcome"
        method = "GET"
    @dataclass
    class winAndLoseReport(ApiRequest):
        """
        api_list:
            GetGameType ,
            InitData ,
            getGameType ,
            getGameType1 ,
            mirrorTable ,
            sameTable
        """
        api = "/winAndLoseReport"
        url = "http://192.168.33.5:9100/winAndLoseReport"
        method = "GET"
        @dataclass
        class GetGameType(ApiRequest):
            api = "/winAndLoseReport/GetGameType"
            url = "http://192.168.33.5:9100/winAndLoseReport/GetGameType"
            method = "GET"
        @dataclass
        class InitData(ApiRequest):
            """
            Args:
                beginDate (str) : example( 2023-01-16+10%3A45 )
                endDate (str) : example( 2023-01-17+10%3A46 )
                kindId (str) : example(  )
                accounts (str) : example(  )
                serverId (str) : example(  )
                limit (int) : example( 20 )
                offset (int|bool) : example( 0 )
                total (int|bool) : example( 0 )
                GameUserNO (str) : example(  )
                RoomType (str) : example(  )
                _ (int) : example( 1673923558325 )
            """
            def __init__(self,beginDate=None, endDate=None, kindId=None, accounts=None, serverId=None, limit=None, offset=None, total=None, GameUserNO=None, RoomType=None, _=None):
                self.data = {"beginDate":beginDate,"endDate":endDate,"kindId":kindId,"accounts":accounts,"serverId":serverId,"limit":limit,"offset":offset,"total":total,"GameUserNO":GameUserNO,"RoomType":RoomType,"_":_}
            data_type = "params"
            api = "/winAndLoseReport/InitData"
            url = "http://192.168.33.5:9100/winAndLoseReport/InitData"
            method = "GET"
        @dataclass
        class getGameType(ApiRequest):
            api = "/winAndLoseReport/getGameType"
            url = "http://192.168.33.5:9100/winAndLoseReport/getGameType"
            method = "GET"
        @dataclass
        class getGameType1(ApiRequest):
            api = "/winAndLoseReport/getGameType1"
            url = "http://192.168.33.5:9100/winAndLoseReport/getGameType1"
            method = "GET"
        @dataclass
        class mirrorTable(ApiRequest):
            """
            Args:
                id (int) : example( 72626 )
                gameName (str) : example( %E6%9E%81%E9%80%9F%E7%99%BE%E5%AE%B6%E4%B9%90 )
                accounts (str) : example( 1_tim )
                serverName (str) : example( %E6%9E%81%E9%80%9F%E7%99%BE%E5%AE%B6%E4%B9%90%E4%BD%93%E9%AA%8C%E6%88%BF )
                gameEndTime (str) : example( 2023-01-17%2010:35:25 )
                beginDate (str) : example( 2023-01-15%2010:45 )
                endDate (str) : example( 2023-01-17%2010:45 )
            """
            def __init__(self,id=None, gameName=None, accounts=None, serverName=None, gameEndTime=None, beginDate=None, endDate=None):
                self.data = {"id":id,"gameName":gameName,"accounts":accounts,"serverName":serverName,"gameEndTime":gameEndTime,"beginDate":beginDate,"endDate":endDate}
            data_type = "params"
            api = "/winAndLoseReport/mirrorTable"
            url = "http://192.168.33.5:9100/winAndLoseReport/mirrorTable"
            method = "GET"
        @dataclass
        class sameTable(ApiRequest):
            """
            Args:
                id (int) : example( 72626 )
                gameName (str) : example( %E6%9E%81%E9%80%9F%E7%99%BE%E5%AE%B6%E4%B9%90 )
                accounts (str) : example( 1_tim )
                serverName (str) : example( %E6%9E%81%E9%80%9F%E7%99%BE%E5%AE%B6%E4%B9%90%E4%BD%93%E9%AA%8C%E6%88%BF )
                gameEndTime (str) : example( 2023-01-17%2010:35:25 )
                beginDate (str) : example( 2023-01-16%2010:45 )
                endDate (str) : example( 2023-01-17%2010:46 )
            """
            def __init__(self,id=None, gameName=None, accounts=None, serverName=None, gameEndTime=None, beginDate=None, endDate=None):
                self.data = {"id":id,"gameName":gameName,"accounts":accounts,"serverName":serverName,"gameEndTime":gameEndTime,"beginDate":beginDate,"endDate":endDate}
            data_type = "params"
            api = "/winAndLoseReport/sameTable"
            url = "http://192.168.33.5:9100/winAndLoseReport/sameTable"
            method = "GET"
