## And Step

### 介绍

`and()` 单步可以传入不定长个数的遍历，但在这些遍历中，至少一个产生输出后才能让原来的遍历进入下一单步。

### DSL 语句

#### 初始化

创建两个 **person** 类型的顶点。

```gremlin
g.addV('person').
    property(id, 1).
    property('age', 20).
  addV('person').
    property(id, 2).
    property('age', 25)
```

#### 测试

找到年龄为 (10, 30) 与 (-∞, 15) U (20, +∞) 的交集 => 25

```gremlin
g.V().has('age', inside(10, 30)).
    and().
    has('age', outside(15, 20)).
values('age')
```

### 操作结果
```
gremlin> g.V().valueMap(true)
==>{id=1, label=person, age=[20]}
==>{id=2, label=person, age=[25]}
gremlin>
gremlin> g.V().has('age', inside(10, 30)).
......1>     and().
......2>     has('age', outside(15, 20)).
......3> values('age')
==>v[2]
```

```json
{
    "vertex": [
        {
            "age": 20,
            "id": 1,
            "label": "person"
        },
        {
            "age": 25,
            "id": 2,
            "label": "person"
        }
    ]
}
```
