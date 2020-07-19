def convertTimeIntoSec(timeCon):

    for _ in timeCon:
        #hoursIndex
        hoursFind = timeCon.find(" hour")
        #minsIndex
        minsFind = timeCon.find(" minute")
        #secsIndex
        secsFind = timeCon.find(" second")
        #hour,mins,secs
        if ((hoursFind >=0) and (minsFind >=0) and (secsFind >=0)):
            hoursIndex = timeCon.index(" hour")
            hours = int(timeCon[0:hoursIndex])
            sliceStr = (slice(hoursIndex+6,len(timeCon)))
            minuteStr = timeCon[sliceStr]
            nextMinStr = minuteStr.index(" minute")
            minutes = int(minuteStr[0:nextMinStr])
            sliceStr1 = (slice(nextMinStr+8,len(minuteStr)-7))
            seconds = minuteStr[sliceStr1]
        #mins,secs
        elif ((hoursFind < 0) and (minsFind >=0) and (secsFind >=0)):
            #hoursIndex = 0
            hours = 0
            minuteStr = timeCon
            nextMinStr = minuteStr.index(" minute")
            minutes = int(minuteStr[0:nextMinStr])
            sliceStr1 = (slice(nextMinStr+8,len(minuteStr)-7))
            seconds = minuteStr[sliceStr1]
        #hour,secs
        elif ((hoursFind >= 0) and (minsFind < 0) and (secsFind >=0)):
            minutes = 0
            hoursIndex = timeCon.index(" hour")
            hours = int(timeCon[0:hoursIndex])
            slicestr2 = (slice(hoursIndex+6,len(timeCon)-7))
            seconds = timeCon[slicestr2]
        #hours,mins
        elif ((hoursFind >= 0) and (minsFind >= 0) and (secsFind < 0)):
            seconds = 0
            hoursIndex = timeCon.index(" hour")
            hours = int(timeCon[0:hoursIndex])
            sliceStr = (slice(hoursIndex+6,len(timeCon)))
            minuteStr = timeCon[sliceStr]
            nextMinStr = minuteStr.index(" minute")
            minutes = int(minuteStr[0:nextMinStr])
        #mins
        elif ((hoursFind < 0) and (minsFind >= 0) and (secsFind < 0)):
            hours = 0
            seconds = 0
            minsIndex = timeCon.index(" minute")
            minutes = int(timeCon[0:minsIndex])
        #hours
        elif ((hoursFind >= 0) and (minsFind < 0) and (secsFind < 0)):
            minutes = 0
            seconds = 0
            hoursIndex = timeCon.index(" hour")
            hours = int(timeCon[0:hoursIndex])

    hoursCon = int(hours * 3600)
    minutesCon = int(minutes * 60)
    secondsCon = int(seconds)
    timeCon =  (hoursCon + minutesCon + secondsCon)
    print(timeCon,"seconds")

    return timeCon
def tc():    
    print("example of input : 5 hour 30 minute 5 seconds")
    time = input("Enter time in '_ hour<space>_minute<space>_second' format:")
    convertTimeIntoSec(time)
    print("Thank you for using Time convertor !!")
