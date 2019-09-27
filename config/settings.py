environ = "product"  # 运行环境：dev/product

if environ == "dev":
    from . import *
elif environ == "product":
    from .production import *
