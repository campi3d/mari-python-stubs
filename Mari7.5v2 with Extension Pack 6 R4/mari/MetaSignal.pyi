from typing import Any

class MetaSignal(type):
    def mro(self) -> Any: ...
