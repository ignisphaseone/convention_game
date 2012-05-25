from django.db import models
from django.contrib.auth.models import User
import string

#Player Default Index
PDI = 0

CONTACT_PREF_OPTIONS = (
    ('email',"via Email"),
    ('phone',"via Text Message/SMS"),
    ('combo',"via both Email and Text Message/SMS"),
    )

STAFF_ACCESS_OPTIONS = (
    ('norml', "Normal"),
    ('staff', "Staff"),
    ('admin', "Admin")
    )

ACTOR_STATUS_OPTIONS = (
    ('prereg',"Preregistered"),
    ('iactiv',"Inactive"),
    ('human',"Human"),
    ('zombie',"Zombie")
    )

# The static information below and its corresponding populate PROVIDER_ARRAY with tuples,
# each corresponding to a phone provider and an email suffix that said provider uses.
PROVIDER_NAME = ["None","3 River Wireless","ACS Wireless","Alltel","AT&T"
            ,"Bell Canada","Bell Canada","Bell Mobility (Canada)","Bell Mobility"
            ,"Blue Sky Frog","Bluegrass Cellular","Boost Mobile","BPL Mobile"
            ,"Carolina West Wireless","Cellular One","Cellular South","Centennial Wireless"
            ,"CenturyTel","Cingular (Now AT&T)","Clearnet","Comcast","Corr Wireless Communications"
            ,"Dobson","Edge Wireless","Fido","Golden Telecom","Helio","Houston Cellular"
            ,"Idea Cellular","Illinois Valley Cellular","Inland Cellular Telephone","MCI"
            ,"Metrocall","Metrocall 2-way","Metro PCS","Microcell","Midwest Wireless"
            ,"Mobilcomm","MTS","Nextel","OnlineBeep","PCS One","President's Choice"
            ,"Public Service Cellular","Qwest","Rogers AT&T Wireless","Rogers Canada"
            ,"Satellink","Southwestern Bell","Sprint","Sumcom","Surewest Communicaitons"
            ,"T-Mobile","Telus","Tracfone","Triton","Unicel","US Cellular","Solo Mobile","Sprint"
            ,"Sumcom","Surewest Communicaitons","T-Mobile","Telus","Triton","Unicel","US Cellular"
            ,"US West","Verizon","Virgin Mobile","Virgin Mobile Canada","West Central Wireless"
            ,"Western Wireless"]

PROVIDER_EMAIL = ["@none.no","@sms.3rivers.net","@paging.acswireless.com,","@message.alltel.com","@txt.att.net"
            ,"@txt.bellmobility.ca","@bellmobility.ca","@txt.bell.ca","@txt.bellmobility.ca"
            ,"@blueskyfrog.com","@sms.bluecell.com","@myboostmobile.com","@bplmobile.com"
            ,"@cwwsms.com","@mobile.celloneusa.com","@csouth1.com","@cwemail.com"
            ,"@messaging.centurytel.net","@txt.att.net","@msg.clearnet.com","@comcastpcs.textmsg.com"
            ,"@corrwireless.net","@mobile.dobson.net","@sms.edgewireless.com","@fido.ca"
            ,"@sms.goldentele.com","@messaging.sprintpcs.com","@text.houstoncellular.net"
            ,"@ideacellular.net","@ivctext.com","@inlandlink.com","@pagemci.com"
            ,"@page.metrocall.com","@my2way.com","@mymetropcs.com","@fido.ca","@clearlydigital.com"
            ,"@mobilecomm.net","@text.mtsmobility.com","@messaging.nextel.com","@onlinebeep.net"
            ,"@pcsone.net","@txt.bell.ca","@sms.pscel.com","@qwestmp.com","@pcs.rogers.com"
            ,"@pcs.rogers.com",".pageme@satellink.net","@email.swbw.com","@messaging.sprintpcs.com"
            ,"@tms.suncom.com","@mobile.surewest.com","@tmomail.net","@msg.telus.com","@txt.att.net"
            ,"@tms.suncom.com","@utext.com","@email.uscc.net","@txt.bell.ca","@messaging.sprintpcs.com"
            ,"@tms.suncom.com","@mobile.surewest.com","@tmomail.net","@msg.telus.com","@tms.suncom.com"
            ,"@utext.com","@email.uscc.net","@uswestdatamail.com","@vtext.com","@vmobl.com"
            ,"@vmobile.ca","@sms.wcc.net","@cellularonewest.com"]

PROVIDER_ARRAY = []

def provider_array():
    value = 0
    tup = ()
    for pn in PROVIDER_NAME:
        tup = (value, PROVIDER_NAME[value])
        PROVIDER_ARRAY.append(tup)
        value+=1

provider_array()

# Create your models here.
class UserProfile(models.Model):
    def __unicode__(self):
        return self.user.username # +" (" + str(self.id) + ")"
    def gen_sms_field(self):
        strip_num = self.phone_number
        strip_num = string.replace(strip_num,' ','')
        strip_num = string.replace(strip_num,'-','')
        strip_num = string.rjust(strip_num, 11, '1')
        return str(strip_num)+PROVIDER_EMAIL[int(self.phone_provider)]
    phone_number = models.CharField("Phone Number", max_length=15, blank=True, null=True,
        help_text="Enter your phone number here.")
    phone_provider = models.IntegerField("Phone Provider", max_length=3, choices=PROVIDER_ARRAY, default=PDI,
        help_text="Enter your phone service provider here.")
    sms_field = models.CharField("SMS Email Address", max_length=80, default="", editable=False, blank=True,
        help_text="This is the email address we use to send information to your phone directly.")
    contact_pref = models.CharField("Preferred Contact Method", max_length=5, default=CONTACT_PREF_OPTIONS[PDI][PDI], choices=CONTACT_PREF_OPTIONS,
        help_text="This determines how you want real-time game alerts sent to you.")
    user = models.OneToOneField(User)