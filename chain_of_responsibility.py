from abc import ABC, abstractmethod


class LogProcessor(ABC):

    INFO = 1
    DEBUG = 2
    ERROR = 3
    NOONE = 4

    def __init__(self, nextLoggerProcessor):
        self.nextLoggerProcessor = nextLoggerProcessor

    def log(self, logLevel, message):
        if self.nextLoggerProcessor != None:
            self.nextLoggerProcessor.log(logLevel, message)
        else:
            print("Now there is Processor to accept your request")


class InfoLogProcessor(LogProcessor):

    def __init__(self, nextLoggerProcessor):
        super().__init__(nextLoggerProcessor)
        

    def log(self, logLevel, message):
        if logLevel == super().INFO:
            print("This is the INFO Logger", message)
        else:
            super().log(logLevel, message)

class DebugLogProcessor(LogProcessor):

    def __init__(self, nextLoggerProcessor):
        super().__init__(nextLoggerProcessor)

    def log(self, logLevel, message):
        if logLevel == super().DEBUG:
            print("This is the Debug Logger", message)
        else:
            super().log(logLevel, message)

class ErrorLogProcessor(LogProcessor):

    def __init__(self, nextLoggerProcessor):
        super().__init__(nextLoggerProcessor)

    def log(self, logLevel, message):
        if logLevel == super().ERROR:
            print("This is the Error Logger", message)
        else:
            super().log(logLevel, message)


logProcessorObj = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor(None)))
logProcessorObj.log(LogProcessor.NOONE, message="This is no request")
