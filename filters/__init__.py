from loader import DP

from .is_emoji import IsEmojiFilter
from .is_name import IsNameFilter


if __name__ == "filters":
    DP.filters_factory.bind(IsEmojiFilter)
    DP.filters_factory.bind(IsNameFilter)
