##############################################
#Authentication handler for SiteHost VNC auth
#Author: Me
##############################################

import xml.dom.minidom
import urllib2

class AuthMgr(object):
  #Base URL to hit for the auth response
  endPoint = ''

  @classmethod
  def getTarget(cls,token,ipaddr):
    # Build the query string to the API : This should be changed to fit your API
    endpoint        = AuthMgr.endPoint+"&arg0="+token+"&arg1[ipaddr]="+ipaddr
    try:
      #returnXML       = open('map.xml')
      returnXML       = urllib2.urlopen(endpoint,None,5)
      doc             = xml.dom.minidom.parse(returnXML)
      status          = doc.getElementsByTagName("status")[0].firstChild.nodeValue
      ip              = doc.getElementsByTagName("ip")[0].firstChild.nodeValue
      port            = doc.getElementsByTagName("port")[0].firstChild.nodeValue
      target          = ip + ':' + port
    except:
      raise
    if status == '0':
      raise Exception("Authentication failed!")

    return target

