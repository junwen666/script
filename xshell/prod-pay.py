digist = [0,1,2,3,4,5,6,7,8,9]
clearCommand = "clear \n"
hostname = "[www@ip-10-10-13-192 ~]$ "
getPodFormatter = "sudo kubectl get pod -n product|grep -E {}\n"
execItFormatter = "sudo kubectl exec -it {} -n product /bin/sh \n"
catLogFormatter = "cd /data/logs/soa-all/{}/error/ && cat {}_{}.log.tmp | grep -v 'DUBBO' && exit \n"
userPathFormatter = "/usr/local/services/{}/opbin"

def Main():
    xsh.Screen.Send(clearCommand)
    xsh.Screen.WaitForString(hostname)
    xsh.Screen.Send(getPodFormatter.format('"pay|risk"'))
    xsh.Screen.WaitForString(hostname)
    readLine = getCurrentRowInfo(300,50)
    readlineHandle(readLine)
   

def getCurrentRowInfo(num: int,row: int):
    screenRow = xsh.Screen.CurrentRow
    xsh.Session.Sleep(500)
    line = xsh.Screen.Get(screenRow, 1, screenRow + row, num)
    return line


def readlineHandle(readLine):
    if readLine.find('\n') == -1:
        return    
    items = readLine.split('\n')
    for item in items:
        podName = substringBefore(item,' ')
        if len(podName) == 0 or hostname.find(podName.strip()) != -1:
            continue
        execCommand = execItFormatter.format(podName)
        deployName = subDigist(podName)
        catLogCommand = catLogFormatter.format(deployName,deployName,podName)
        userPathCommand = userPathFormatter.format(deployName)
        xsh.Screen.Send(execCommand)
        xsh.Screen.WaitForString(userPathCommand)
        xsh.Screen.Send(catLogCommand)
        xsh.Screen.WaitForString(hostname)
        xsh.Screen.Send('\n')
        xsh.Screen.WaitForString(hostname)
        xsh.Session.Sleep(1500)


    
def substringBefore(string,separator):
    if len(string) != 0:
        if len(separator) == 0:
            return ''
        else:
            pos = string.find(separator)
            if pos == -1:
                return string.strip()
            else:
                return string[0:pos].strip()
    else:
        return string.strip()

def substringBeforeLast(string,separator):
    if len(string) != 0:
        if len(separator) == 0:
            return ''
        else:
            pos = string.rfind(separator)
            if pos == -1:
                return string.strip()
            else:
                return string[0:pos].strip()
    else:
        return string.strip()



def subDigist(podName):
    if hasDigist(podName):
        deployTmpName = substringBeforeLast(podName, "-")
        return subDigist(deployTmpName)
    else:
        return podName


def hasDigist(content):
    if len(content) == 0:
        return False
    else:    
        for number in digist:
            if content.find(str(number)) > 0:
                return True
            else:
                continue
        return False
