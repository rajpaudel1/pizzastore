from django.core.management.base import BaseCommand 
from django.db.models import Count 
from blog.models import Article, Comment 
from datetime import timedelta, datetime 
from django.utils.timezone import utc 


class Command(BaseCommand): 
	help = 'To load order information to Orders models'

	def handle(self, *args, **kwargs): 
		orders = [
			{
				'id':1,
				'cust_name': 'foo',
				'address': '1016, huntingdon dr, san jose, CA 95129',
				'items': 'veg pizza'
			},
			{
				'id':2,
				'cust_name': 'bar',
				'address': '1580, benton St, Sunnyvale, CA 95129',
				'items': 'veg pizza'
			},
			{
				'id':3,
				'cust_name': 'user3',
				'address': '10239, E Estates Dr, cupertino, CA 95129',
				'items': 'veg pizza'
			},
			{
				'id':4,
				'cust_name': 'user4',
				'address': '2112, huntingdon dr, san jose, ca 95129',
				'items': 'veg pizza'
			},
			{
				'id':5,
				'cust_name': 'user5',
				'address': '1017, huntingdon dr,  xyz, ca 95129',
				'items': 'veg pizza'
			}
		]
