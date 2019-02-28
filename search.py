#!/usr/bin/python
import operator
from django.db.models import Q

'''
class searchListView(searchView):
	def getQuerySet(self):
		result = super(searchListView, self).getQuerySet()
		query = self.request.GET.get('searchBar')''
		if query:
			queryList = query.split()
'''
			''' SELECT * FROM blog_table WHERE content LIKE '%first_word%' OR content LIKE '%second_word%' OR content LIKE '%third_word% '''
'''
			result = result.filter(
						reduce(operator.and_,
							(Q(content_icontains=searchBar) for searchBar in queryList)))
		return result
'''

''' SELECT * FROM BlogPost WHERE title LIKE '%your_search_query%' OR intro LIKE '%your_search_query%' OR content LIKE '%your_search_query%' COLLATE UTF8_GENERAL_CI'''
results = BlogPost.objects.filter(Q(title__icontains=your_search_query) | Q(intro__icontains=your_search_query) | Q(content__icontains=your_search_query))