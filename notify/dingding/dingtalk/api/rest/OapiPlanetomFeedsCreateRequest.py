'''
Created by auto_sdk on 2021.01.28
'''
from dingtalk.api.base import RestApi
class OapiPlanetomFeedsCreateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.anchor_id = None
		self.appoint_begin_time = None
		self.cover_url = None
		self.feed_type = None
		self.group_ids = None
		self.introduction = None
		self.pic_introduction_url = None
		self.title = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.planetom.feeds.create'
