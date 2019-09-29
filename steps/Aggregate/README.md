## Aggregate Step

### 介绍

`aggregate()` 用于在遍历过程中一个特殊点上，将所有对象聚合成一个 collection。

### DSL 语句

#### 初始化

1. 创建两个 **person** 类型的顶点和两个 **song** 类型的顶点。

```gremlin
g.addV('person').
    property(id, 'u1').
    property('name', 'marko').
  addV('person').
    property(id, 'u2').
    property('name', 'stephen').
  addV('song').
    property(id, 's1').
    property('name', 'song-A').
  addV('song').
    property(id, 's2').
    property('name', 'song-B')
```

2. 添加三条 **like** 类型的边。

```gremlin
g.V('u1').addE('like').to(V('s1')).
  V('u2').addE('like').to(V('s1')).
  V('u2').addE('like').to(V('s2'))
```

#### 测试

找到与 marko 有共同兴趣的人还喜欢哪些 marko 没喜欢的歌曲。

```gremlin
g.V('u1').out('like').aggregate('x').
    in('like').out('like').
    where(without('x')).
    values('name')
```

### 操作结果
```
gremlin> g.V().valueMap(true)
==>[id:u1,label:person,name:[marko]]
==>[id:u2,label:person,name:[stephen]]
==>[id:s1,label:song,name:[song-A]]
==>[id:s2,label:song,name:[song-B]]
gremlin>
gremlin> g.E().valueMap(true)
==>[id:u1-like-song-A,label:like]
==>[id:u2-like-song-A,label:like]
==>[id:u2-like-song-B,label:like]
gremlin>
gremlin> g.V('u1').out('like').aggregate('x').
......1>     in('like').out('like').
......2>     where(without('x')).
......3>     values('name')
==>song-B
```

```json
{
    "edge": [
        {
            "id": "u1-like-song-A",
            "label": "like"
        },
        {
            "id": "u2-like-song-A",
            "label": "like"
        },
        {
            "id": "u2-like-song-B",
            "label": "like"
        }
    ],
    "vertex": [
        {
            "id": "u1",
            "label": "person",
            "name": "marko"
        },
        {
            "id": "u2",
            "label": "person",
            "name": "stephen"
        },
        {
            "id": "s1",
            "label": "song",
            "name": "song-A"
        },
        {
            "id": "s2",
            "label": "song",
            "name": "song-B"
        }
    ]
}
```
