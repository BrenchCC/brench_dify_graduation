from dpkt.http import Request as DpktRequest
from werkzeug.test import EnvironBuilder
from werkzeug.wrappers import Request


def parse_raw_request(raw_data: bytes):
    req = DpktRequest(raw_data)
    builder = EnvironBuilder(
        method=req.method,
        path=req.uri,
        headers=req.headers,
        data=req.body,
    )
    return Request(builder.get_environ())
