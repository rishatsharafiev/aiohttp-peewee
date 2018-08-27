class SendMessageEntity:
    """Send message entity"""

    __slots__ = (
        'phone',
        'chat_id',
        'body',
    )

    def __init__(self, _phone: str, _chat_id: str, _body: int):
        """
        Конструктор
        Args:
            _phone: Номер телефона, начинающийся с кода страны. Для России и Казахстана это всегда 7, затем 10 цифр.
            _chat_id: ID чата из списка сообщений. Примеры: 79633123456@c.us для личных сообщений и 79680561234-1479621234@g.us для группы. Используется вместо параметра phone
            _body: Текст сообщения, любая строка включая emoji
        """
        self.phone = _phone
        self.chat_id = _chat_id
        self.body = _body
