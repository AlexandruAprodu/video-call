from django.shortcuts import render
from .models import Keys
import sys
import os
from .RtcTokenBuilder import RtcTokenBuilder, Role_Attendee
import time
from random import randint

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


appID = "f5648bb23083402cbd9c2faa5692593a"
appCertificate = "83abc34dba2f4efc84fa13dfb6c0134a"
channelName = "Suzeta"
# Fill in the user ID. 0 means that the server does not authenticate user IDs.
uid = 0
# uid = 2882341273

# userAccount = "2882341273"
# expireTimeInSeconds = 3600
# currentTimestamp = int(time.time())
# privilegeExpiredTs = currentTimestamp + expireTimeInSeconds
privilegeExpiredTs = 0  # 24h


def main():
    token = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, channelName, uid, Role_Attendee, privilegeExpiredTs)
    return token


if __name__ == "__main__":
    main()


def agora(request):
    context = {'Keys': Keys.objects.latest('-id'), 'token': main()}

    return render(request, 'video/agora.html', context)

