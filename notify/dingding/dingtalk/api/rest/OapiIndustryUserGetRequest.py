'''
Created by auto_sdk on 2020.09.16
'''
from dingtalk.api.base import RestApi
class OapiIndustryUserGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.dept_id = None
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.industry.user.get'
