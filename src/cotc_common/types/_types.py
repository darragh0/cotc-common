from typing import Any, TypeAlias

from cotc_common.util import PublisherRank

JSONObj: TypeAlias = dict[str, Any]
JSONArr: TypeAlias = list[JSONObj]
ServerResponse: TypeAlias = tuple[dict[str, str], int]
ServerResponseWithRank: TypeAlias = tuple[ServerResponse, PublisherRank]
