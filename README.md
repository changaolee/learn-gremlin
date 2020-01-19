# gremlin-examples

参考官方 Gremlin 文档，对其中的语法进行代码演示。

## 环境搭建

在[官网](http://tinkerpop.apache.org/)下载 *gremlin-console* 和 *gremlin-server* 并解压。

1. 启动 *gremlin-server*
```
bin/gremlin-server.sh start
```
2. 进入 *gremlin-console*
```
bin/gremlin.sh
```
3. 连接 *gremlin-server*
```
gremlin> :remote connect tinkerpop.server conf/remote.yaml
==>Configured localhost/127.0.0.1:8182, localhost/0:0:0:0:0:0:0:1:8182
gremlin> :remote console
==>All scripts will now be sent to Gremlin Server - [localhost/127.0.0.1:8182, localhost/0:0:0:0:0:0:0:1:8182] - type ':remote console' to return to local mode
```
4. 测试查询语句
```
gremlin> g.V().count()
==>0
```
## Steps

由于官方文档对 Steps 的说明是依照字母顺序展示的，不利于初学者学习，这里按照我自己的理解对 Steps 的难度进行了初步划分。

划分标准包括 Step 的使用频率、使用难度等，理论上初级、中级两部分的 Steps 足以满足大部分查询场景。

### 初级 Steps

| 名称 | 作用 |
| ----- | ----- |
| [AddEdge Step](./steps/AddEdge) | 添加边 |
| [AddVertex Step](./steps/AddVertex) | 添加点 |
| [AddProperty Step](./steps/AddProperty) | 添加属性 |
| And Step | |
| As Step | |
| By Step | |
| Count Step | |
| Dedup Step | |
| From Step | |
| Has Step | |
| Id Step | |
| Is Step | |
| Label Step | |
| Limit Step | |
| To Step | |
| Value Step | |
| ValueMap Step | |
| Values Step | |
| Vertex Step | |
| Where Step | |

### 中级 Steps

| 名称 | 作用 |
| ----- | ----- |
| [Aggregate Step](./steps/Aggregate) | 对象聚合 |
| Choose Step | |
| Fold Step | |
| Group Step | |
| GroupCount Step | |
| Inject Step | |
| Or Step | |
| Order Step | |
| Path Step | |
| Project Step | |
| Range Step | |
| Repeat Step | |
| Not Step | |
| Select Step | |
| Skip Step | |
| Sum Step | |
| Unfold Step | |
| Union Step | |
| Until Step | |
| With Step | |

### 高级 Steps

| 名称 | 作用 |
| ----- | ----- |
| Barrier Step | |
| Cap Step | |
| Coalesce Step | |
| Coin Step | |
| ConnectedComponent Step | |
| Constant Step | |
| CyclicPath Step | |
| Dedup Step | |
| Drop Step | |
| Emit Step | |
| Explain Step | |
| Graph Step | |
| Identity Step | |
| Index Step | |
| IO Step | |
| Key Step | |
| Local Step | |
| Loops Step | |
| Match Step | |
| Math Step | |
| Max Step | |
| Mean Step | |
| Min Step | |
| None Step | |
| Option Step | |
| Optional Step | |
| PageRank Step | |
| PeerPressure Step | |
| Profile Step | |
| Program Step | |
| Properties Step | |
| PropertyMap Step | |
| Sack Step | |
| Sample Step | |
| ShortestPath Step | |
| SimplePath Step | |
| Store Step | |
| Subgraph Step | |
| Tail Step | |
| TimeLimit Step | |
| Tree Step | |

## License

[The MIT License (MIT)](./LICENSE)