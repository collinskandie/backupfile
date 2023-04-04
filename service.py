#import libraries.
import win32serviceutil
import win32service
import win32event

class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "DbBackup"
    _svc_display_name_ = "Auto Backup"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        import autoscript
        autoscript.main()

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(MyService)
