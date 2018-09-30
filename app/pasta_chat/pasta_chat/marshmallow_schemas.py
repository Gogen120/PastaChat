from pasta_chat import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'created_at')
