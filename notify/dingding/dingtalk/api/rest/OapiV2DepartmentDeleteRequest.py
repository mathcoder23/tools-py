'''
Created by auto_sdk on 2020.09.29
'''
from dingtalk.api.base import RestApi
class OapiV2DepartmentDeleteRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.dept_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.v2.department.delete'
