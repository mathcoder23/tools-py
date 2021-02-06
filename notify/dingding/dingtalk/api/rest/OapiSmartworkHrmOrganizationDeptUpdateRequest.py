'''
Created by auto_sdk on 2021.01.26
'''
from dingtalk.api.base import RestApi
class OapiSmartworkHrmOrganizationDeptUpdateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.dept_id = None
		self.field_code = None
		self.field_value = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.smartwork.hrm.organization.dept.update'
