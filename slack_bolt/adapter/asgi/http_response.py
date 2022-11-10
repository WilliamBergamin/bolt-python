from typing import Iterable, Sequence, Tuple, Dict, Union

ENCODING = "utf-8"  # should always be utf-8


class AsgiHttpResponse:
    __slots__ = ("status", "raw_headers", "body")

    def __init__(self, status: int, headers: Dict[str, Sequence[str]] = {}, body: str = ""):
        self.status: int = status
        self.raw_headers: Iterable[Tuple[bytes, bytes]] = [
            (bytes(key, ENCODING), bytes(value[0], ENCODING)) for key, value in headers.items()
        ]
        self.raw_headers.append((b"content-length", bytes(str(len(body)), ENCODING)))
        self.body: bytes = bytes(body, ENCODING)

    def get_response_start(self) -> Dict[str, Union[str, int, Iterable[Tuple[bytes, bytes]]]]:
        return {
            "type": "http.response.start",
            "status": self.status,
            "headers": self.raw_headers,
        }

    def get_response_body(self) -> Dict[str, Union[str, bytes, bool]]:
        return {
            "type": "http.response.body",
            "body": self.body,
            "more_body": False,
        }
