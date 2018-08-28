class SendMessageEntity:
    """Message entity"""

    __slots__ = (
        'id',
        'body',
        'type',
        'sender_name',
        'from_me',
        'author',
        'time',
        'chat_id',
        'message_number',
    )

    def __init__(self, _id: str, _body: str, _type: str, _sender_name: str,
                 _from_me: bool, _author: str, _time: int, _chat_id: str, _message_number: str):
        """
        Конструктор
        Args:
            _id: Уникальный ID
            _body: текст сообщения для типа "chat" или ссылка на скачивание файла для "ptt", "image", "audio" и "document"
            _type: Тип сообщения - "chat" - текстовое, "image", "ptt" - голосовое, "document", "audio", "call_log"
            _sender_name: Имя отправителя
            _from_me: true - исходящее, false - входящее
            _author: ID автора сообщения, полезно для групп
            _time: Время отправления, unix timestamp
            _chat_id: ID чата
            _message_number: Порядковый номер сообщения в базе данных
        """
        self.id = _id
        self.body = _body
        self.type = _type
        self.sender_name = _sender_name
        self.from_me = _from_me
        self.author = _author
        self.time = _time
        self.chat_id = _chat_id
        self.message_number = _message_number
