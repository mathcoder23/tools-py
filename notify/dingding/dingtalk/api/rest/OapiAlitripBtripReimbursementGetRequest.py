'''
Created by auto_sdk on 2020.06.15
'''
from dingtalk.api.base import RestApi
class OapiAlitripBtripReimbursementGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.corpid = None
		self.thirdparty_flow_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.alitrip.btrip.reimbursement.get'
