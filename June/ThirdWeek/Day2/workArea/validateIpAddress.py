'''#from ipaddress import AddressValueError
from __future__ import unicode_literals
import ipaddress

def validIPAddress(IP):
    try:
        k = ipaddress.ip_address(IP)
        print(type(k))
        if type(k) == (ipaddress.IPv4Address):
            return 'IPv4'
        elif type(k) == (ipaddress.IPv6Address):
            return 'IPv6'
    except ValueError:
        return 'Neither'
# ob = Solution()
# print(validIPAddress("172.16.254.001"))

ipaddress.ip_address('172.16.254.001')
'''


class Solution(object):
   def validIPAddress(self, IP):
      """
      :type IP: str
      :rtype: str
      """
      def isIPv4(s):
         try: return str(int(s)) == s and 0 <= int(s) <= 255
         except: return False
      def isIPv6(s):
         if len(s) > 4:
            return False
         try : return int(s, 16) >= 0 and s[0] != '-'
         except:
            return False
      if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
         return "IPv4"
      if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
         return "IPv6"
      return "Neither"
ob = Solution()
print(ob.validIPAddress("172.16.254.01"))