'''
Created by auto_sdk on 2020.09.11
'''
from dingtalk.api.base import RestApi
class OapiAlitripBtripApplySearchRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.rq = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.alitrip.btrip.apply.search'
