# from newsapi import NewsApiClient
# from datetime import datetime, timedelta
# from .models import Article
# import re
# api_secret = '1c2226cbd2ac46948d5f8cae8482d9d4'
#
# api = NewsApiClient(api_key=api_secret)
#
# news_data = api.get_everything(q='covid-19 india healthcare', page=1, page_size=100,
#                                from_param=str(datetime.now().date() - timedelta(days=3)), to=str(datetime.now().date()))
#
#
# def news_api_data_storage():
#     x = 0
#     Article.objects.all().delete()
#     print('deleted articles')
#     for news in news_data['articles']:
#         try:
#             cleanr = re.compile('<.*?>')
#             cleantext = re.sub(cleanr, '', news['description'])
#             Article.objects.create(
#                 source=news['source']['name'] if news['source']['name'] else None,
#                 author=news['author'] if news['author'] else None,
#                 title=news['title'] if news['title'] else None,
#                 description=cleantext if cleantext else None,
#                 url=news['url'] if news['url'] else None,
#                 urlToImage=news['urlToImage'] if news['urlToImage'] else None,
#                 publishedAt=news['publishedAt'] if news['publishedAt'] else None,
#                 content=news['content'] if news['content'] else None
#             )
#             x = x + 1
#         except:
#             print('Article Creation Failed')
#     print(f'{x} Article added')
#
#
#
