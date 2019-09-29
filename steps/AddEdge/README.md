## AddEdge Step

### 介绍

`addE()` 用于给图中的顶点添加边。

### DSL 语句

#### 初始化

创建两个 **person** 类型的顶点。

```gremlin
g.addV('person').
    property(id, '1').
    property('name', 'marko').
  addV('person').
    property(id, '2').
    property('name', 'stephen')
```

#### 测试

给两个顶点之间添加 **knows** 类型的边，并指定 *id*。

```gremlin
g.V('1').addE('knows').to(V('2')).
    property(id, '1-knows-2')
```

### 操作结果
```
gremlin> g.V().valueMap(true)
==>[id:1,label:person,name:[marko]]
==>[id:2,label:person,name:[stephen]]
gremlin>
gremlin> g.E().valueMap(true)
==>[id:1-knows-2,label:knows]
```

```json
{
    "edge": [
        {
            "id": "1-knows-2",
            "label": "knows"
        }
    ],
    "vertex": [
        {
            "id": "1",
            "label": "person",
            "name": "marko"
        },
        {
            "id": "2",
            "label": "person",
            "name": "stephen"
        }
    ]
}
```
