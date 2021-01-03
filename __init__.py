
# empty file
XLIST = ['112.74.214.43']
T_PORT = 7709
X_PORT = 7727

Hi All,

In the past two weeks, I have been doing paper trading for two quantitative strategies. 
So far, both of them introduce promising results.

Volatility Trading (Ripple effect)
Ripple effect is a delta-netural strategy which makes profits if the realized volatility of underlyings is higher than
the implied volatility
The table below shows the performance of the strategy from Oct. 25 2019 to Nov. 8 2019
/table
From the table above, we can notice that the largest loss per day is ?, and our return is ? per day. So risk/reward ratio is about 1:2?. So our strategy works very well.
Note:For delta-neutral strategy, the biggest enemy is time decay.

Provide a snapshot of my portfolio monitor
/monitor
In terms of execution and portfolio risk management, I have developed a systematic model to monitor and manage greek risks in Excel. During the trading session, those greeks will change automatically
along with the changing of stock price. After the trading session, a stress test will be run to calculate the consolidated risks
of our portfolio under extreme situations (e.g., S&P down 10%, VIX down 5%). If the loss under extreme scenarios is large
than a predefined threshold, we will trim our portfolio accordingly.

Future Plan:
In the following week, I will buy options with long-term maturity which has larger vega compared to those with short-term 
maturity.

Intraday Futures trading (CBBC Magnetic Effect)
/result table
/Systmatic trading system
# CreateOrderAndRouteEx.py

import blpapi
import sys


SESSION_STARTED         = blpapi.Name("SessionStarted")
SESSION_STARTUP_FAILURE = blpapi.Name("SessionStartupFailure")
SERVICE_OPENED          = blpapi.Name("ServiceOpened")
SERVICE_OPEN_FAILURE    = blpapi.Name("ServiceOpenFailure")
ERROR_INFO              = blpapi.Name("ErrorInfo")
CREATE_ORDER_AND_ROUTE_EX  = blpapi.Name("CreateOrderAndRouteEx")

d_service="//blp/emapisvc_beta"
d_host="localhost"
d_port=8194
bEnd=False

class EMSXExecutionSystem():
    def __init__(self):
        sessionOptions = blpapi.SessionOptions()
        sessionOptions.setServerHost(d_host)
        sessionOptions.setServerPort(d_port)

        print ("Connecting to %s:%d" % (d_host,d_port))

        self.__sessionStarted = False
        self.__serviceOpened = False

        self.__session = blpapi.Session(sessionOptions)
        self.__sessionStarted = self.__session.start()
        if not self.__sessionStarted:
            print ("Failed to start session.")

        self.__serviceOpened = self.__session.openService(d_service)
        if not self.__serviceOpened:
            print ("Failed to open service.")

    def sendRequest(self):
        service = self.__session.getService(d_service)
        request = service.createRequest("CreateOrderAndRouteEx")

        # The fields below are mandatory
        request.set("EMSX_TICKER", "IBM US Equity")
        request.set("EMSX_AMOUNT", 1000)
        request.set("EMSX_ORDER_TYPE", "MKT")
        request.set("EMSX_TIF", "DAY")
        request.set("EMSX_HAND_INSTRUCTION", "ANY")
        request.set("EMSX_SIDE", "BUY")
        request.set("EMSX_BROKER", "BMTB")

        #The fields below are optional
        #request.set("EMSX_ACCOUNT","TestAccount")
        #request.set("EMSX_BOOKNAME","BookName")
        #request.set("EMSX_BASKET_NAME", "HedgingBasket")
        #request.set("EMSX_CFD_FLAG", "1")
        #request.set("EMSX_CLEARING_ACCOUNT", "ClrAccName")
        #request.set("EMSX_CLEARING_FIRM", "FirmName")
        #request.set("EMSX_CUSTOM_NOTE1", "Note1")
        #request.set("EMSX_CUSTOM_NOTE2", "Note2")
        #request.set("EMSX_CUSTOM_NOTE3", "Note3")
        #request.set("EMSX_CUSTOM_NOTE4", "Note4")
        #request.set("EMSX_CUSTOM_NOTE5", "Note5")
        #request.set("EMSX_EXCHANGE_DESTINATION", "ExchDest")
        #request.set("EMSX_EXEC_INSTRUCTION", "Drop down values from EMSX Ticket")
        #request.set("EMSX_GET_WARNINGS", "0")
        #request.set("EMSX_GTD_DATE", "20170105")
        #request.set("EMSX_INVESTOR_ID", "InvID")
        #request.set("EMSX_LIMIT_PRICE", 123.45)
        #request.set("EMSX_LOCATE_BROKER", "BMTB")
        #request.set("EMSX_LOCATE_ID", "SomeID")
        #request.set("EMSX_LOCATE_REQ", "Y")
        #request.set("EMSX_NOTES", "Some notes")
        #request.set("EMSX_ODD_LOT", "0")
        #request.set("EMSX_ORDER_ORIGIN", "")
        #request.set("EMSX_ORDER_REF_ID", "UniqueID")
        #request.set("EMSX_P_A", "P")
        #request.set("EMSX_RELEASE_TIME", 34341)
        #request.set("EMSX_REQUEST_SEQ", 1001)
        #request.set("EMSX_ROUTE_REF_ID", "UniqueID")
        #request.set("EMSX_SETTLE_CURRENCY", "USD")
        #request.set("EMSX_SETTLE_DATE", 20170106)
        #request.set("EMSX_SETTLE_TYPE", "T+2")
        #request.set("EMSX_STOP_PRICE", 123.5)

        # Below we establish the strategy details

        strategy = request.getElement("EMSX_STRATEGY_PARAMS")
        strategy.setElement("EMSX_STRATEGY_NAME", "VWAP")

        indicator = strategy.getElement("EMSX_STRATEGY_FIELD_INDICATORS")
        data = strategy.getElement("EMSX_STRATEGY_FIELDS")

        # Strategy parameters must be appended in the correct order. See the output
        # of GetBrokerStrategyInfo request for the order. The indicator value is 0 for
        # a field that carries a value, and 1 where the field should be ignored

        data.appendElement().setElement("EMSX_FIELD_DATA", "09:30:00") # StartTime
        indicator.appendElement().setElement("EMSX_FIELD_INDICATOR", 0)

        data.appendElement().setElement("EMSX_FIELD_DATA", "10:30:00") # EndTime
        indicator.appendElement().setElement("EMSX_FIELD_INDICATOR", 0)

        data.appendElement().setElement("EMSX_FIELD_DATA", "")         # Max%Volume
        indicator.appendElement().setElement("EMSX_FIELD_INDICATOR", 1)

        data.appendElement().setElement("EMSX_FIELD_DATA", "")         # %AMSession
        indicator.appendElement().setElement("EMSX_FIELD_INDICATOR", 1)

        data.appendElement().setElement("EMSX_FIELD_DATA", "")         # OPG
        indicator.appendElement().setElement("EMSX_FIELD_INDICATOR", 1)

        data.appendElement().setElement("EMSX_FIELD_DATA", "")         # MOC
        indicator.appendElement().setElement("EMSX_FIELD_INDICATOR", 1)

        data.appendElement().setElement("EMSX_FIELD_DATA", "")         # CompletePX
        indicator.appendElement().setElement("EMSX_FIELD_INDICATOR", 1)

        data.appendElement().setElement("EMSX_FIELD_DATA", "")         # TriggerPX
        indicator.appendElement().setElement("EMSX_FIELD_INDICATOR", 1)

        data.appendElement().setElement("EMSX_FIELD_DATA", "")         # DarkComplete
        indicator.appendElement().setElement("EMSX_FIELD_INDICATOR", 1)

        data.appendElement().setElement("EMSX_FIELD_DATA", "")         # DarkCompPX
        indicator.appendElement().setElement("EMSX_FIELD_INDICATOR", 1)

        data.appendElement().setElement("EMSX_FIELD_DATA", "")         # RefIndex
        indicator.appendElement().setElement("EMSX_FIELD_INDICATOR", 1)

        data.appendElement().setElement("EMSX_FIELD_DATA", "")         # Discretion
        indicator.appendElement().setElement("EMSX_FIELD_INDICATOR", 1)

        print ("Request: %s" % request.toString())

        self.requestID = blpapi.CorrelationId()

        session.sendRequest(request, correlationId=self.requestID )

    def catchServerEvent(self):
        bExit = False
        While bExit == False:
            event = self.__session.nextEvent()
            if (event.eventType() == blpapi.Event.RESPONSE )| (event.eventType() == blpapi.Event.PARTIAL_RESPONSE):
                self.processResponseEvent(event)
                If event.eventType() == blpapi.Event.RESPONSE :
                    bExit = True

    def processResponseEvent(self, event):
        print ("Processing RESPONSE event")

        for msg in event:

            print ("MESSAGE: %s" % msg.toString())
            print ("CORRELATION ID: %d" % msg.correlationIds()[0].value())


            if msg.correlationIds()[0].value() == self.requestID.value():
                print ("MESSAGE TYPE: %s" % msg.messageType())

                if msg.messageType() == ERROR_INFO:
                    errorCode = msg.getElementAsInteger("ERROR_CODE")
                    errorMessage = msg.getElementAsString("ERROR_MESSAGE")
                    print ("ERROR CODE: %d\tERROR MESSAGE: %s" % (errorCode,errorMessage))
                elif msg.messageType() == CREATE_ORDER_AND_ROUTE_EX:
                    emsx_sequence = msg.getElementAsInteger("EMSX_SEQUENCE")
                    emsx_route_id = msg.getElementAsInteger("EMSX_ROUTE_ID")
                    message = msg.getElementAsString("MESSAGE")
                    print ("EMSX_SEQUENCE: %d\tEMSX_ROUTE_ID: %d\tMESSAGE: %s" % (emsx_sequence,emsx_route_id,message))

                # global bEnd
                # bEnd = True

    def releaseObjects(self):
        self.__session.Stop()

def createOrder(es):

def main():
    es = EMSXExecutionSystem()
    createOrder(es)
    modifyOrder(es)
    cancelOrder(es)


if __name__ == "__main__":
    print ("Bloomberg - EMSX API Example - CreateOrderAndRouteEx")
    try:
        main()
    except KeyboardInterrupt:
        print ("Ctrl+C pressed. Stopping...")


__copyright__ = """
Copyright 2017. Bloomberg Finance L.P.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:  The above
copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
"""
