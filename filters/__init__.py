from loader import DP

from .is_emoji import IsEmojiFilter
from .is_name import IsNameFilter
from .is_admin import IsAdminFilter


if __name__ == "filters":
    DP.filters_factory.bind(IsEmojiFilter)
    DP.filters_factory.bind(IsNameFilter)
    DP.filters_factory.bind(IsAdminFilter)
