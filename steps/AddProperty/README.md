## AddProperty Step

### 介绍

`property()` 用于给图的基本元素添加属性。

### DSL 语句

#### 初始化

创建一个 **person** 类型的顶点。

```gremlin
g.addV('person')
```

#### 测试

1. 给 **person** 类型的顶点添加 *name* 和 *age* 属性。

```gremlin
g.V().hasLabel("person").
    property('name', 'stephen').
    property('age', 25)
```

2. 使用 `properties()` 查询指定字段。

```gremlin
g.V().properties('age').valueMap(true)
```

### 操作结果
```
gremlin> g.V().valueMap(true)
==>[id:ff6f2633-8319-4e7c-b42b-475b20dbcdc8,label:person,age:[25],name:[stephen]]
gremlin> g.V().properties('age').valueMap(true)
==>[id:ff6f2633-8319-4e7c-b42b-475b20dbcdc8,key:age,value:25]
```

```json
{
    "vertex": [
        {
            "age": "25",
            "id": "ff6f2633-8319-4e7c-b42b-475b20dbcdc8",
            "label": "person",
            "name": "stephen"
        }
    ]
}
```
