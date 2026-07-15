from django.http import JsonResponse

from middleware.redis_client import redis_client

EXCLUDED_PREFIXES = (
    "/static/",
    "/media/",
)

EXCLUDED_PATHS = (
    "/favicon.ico",
    "/accounts/login/",
    "/accounts/register/",
)


class RateLimitMiddleware:

    WINDOW = 60

    def __init__(self, get_response):
        self.get_response = get_response

    def get_limit(self, request):

        if not request.user.is_authenticated:
            return 5

        role = request.user.role

        if role == "gold":
            return 10

        elif role == "silver":
            return 5

        elif role == "bronze":
            return 10

        return 5

    def get_key(self, request):

        if request.user.is_authenticated:
            return f"user:{request.user.id}"

        return f"ip:{request.META.get('REMOTE_ADDR')}"

    def __call__(self, request):

        print(request.method, request.path)

        # Skip rate limiting for excluded paths
        if request.path in EXCLUDED_PATHS or request.path.startswith(EXCLUDED_PREFIXES):
            return self.get_response(request)

        key = self.get_key(request)
        limit = self.get_limit(request)

        count = redis_client.incr(key)

        if count == 1:
            redis_client.expire(key, self.WINDOW)

        print(
            f"Key={key} | Count={count} | Limit={limit} | TTL={redis_client.ttl(key)}"
        )

        if count > limit:

            ttl = redis_client.ttl(key)

            return JsonResponse(
                {
                    "error": "Too many requests.",
                    "retry_after": ttl,
                    "limit": limit,
                },
                status=429,
            )

        return self.get_response(request)
