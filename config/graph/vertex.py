vertex_properties = {
    'default': {
        'user': {'id': str, 'age': int, 'level': int, 'name': str, 'sex': str, 'is_deleted': int},  # 普通用户
        'singer': {'id': str, 'name': str, 'is_deleted': int},  # 歌手
        'song': {'id': str, 'name': str, 'singer': str, 'is_deleted': int},  # 歌曲
    }
}
