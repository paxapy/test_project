from django.utils.log import getLogger
from django.db import connection


logger = getLogger(__name__)


class StoreDbRequestsMiddleware(object):

    def process_response(self, request, response):
        queries = connection.queries
        for query in queries:
            logger.info(query['sql'])
        return response
