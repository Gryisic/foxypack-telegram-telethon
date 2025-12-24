from enum import Enum

from foxypack.foxypack_abc.answers import (
    AnswersAnalysis,
    AnswersSocialContent,
    AnswersSocialContainer,
)


class TelegramEnum(Enum):
    channel = "channel"
    post = "post"
    private_channel = "private_channel"
    private_post = "private_post"


class TelegramAnswersAnalysis(AnswersAnalysis):
    code: str


class TelegramPostAnswersStatistics(AnswersSocialContent):
    post_id: int
    channel_id: int
    channel_username: str | None
    text: str | None
    forwards: int | None
    replies: int | None


class TelegramChannelAnswersStatistics(AnswersSocialContainer):
    channel_id: int
    username: str | None
    title: str
    description: str | None
    verified: bool
