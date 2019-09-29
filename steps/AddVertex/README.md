## AddVertex Step

### 介绍

`addV()` 用于给图添加顶点。每传入一个对象，就会创建一个顶点。

### DSL 语句

创建一个 **person** 类型的顶点，并指定 *id* 和 *name*。

```gremlin
g.addV('person').property(id, '1').property('name', 'stephen')
```

### 操作结果
```
gremlin> g.V().valueMap(true)
==>[id:1,label:person,name:[stephen]]
```

```json
{
    "vertex": [
        {
            "id": "1",
            "label": "person",
            "name": "stephen"
        }
    ]
}
```
