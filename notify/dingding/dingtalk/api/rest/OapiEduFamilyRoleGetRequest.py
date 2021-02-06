'''
Created by auto_sdk on 2021.01.27
'''
from dingtalk.api.base import RestApi
class OapiEduFamilyRoleGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.corp_id = None
		self.staff_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.edu.family.role.get'
