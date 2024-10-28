

opers = [
{
    "index":0,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16,"isNoise":"True"}
    ]
},#dbf malloc
{
    "index":1,
    "primitive":[
        {"index":0,"oper_type":"free","object":(0,0),"isNoise":"True"}
    ]#dbf free
},
{
    "index":2,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16,"isNoise":"True"}
    ]#second malloc
},
{
    "index":3,
    "primitive":[
        {"index":0,"oper_type":"free","object":(2,0),"isNoise":"True"},
        {'index':1,"oper_type":"malloc","size":16,"isNoise":"True"}
    ]#second free
},
{
    "index":4,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16,"isNoise":"True"}
    ]#a malloc
},
{
    "index":5,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16,"isNoise":"True"}
    ]#b malloc
},
{
    "index":6,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16,"isNoise":"True"}
    ]#c malloc
},
{
      "index":7,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16,"isNoise":"True"}
    ]#c 
},
{
    "index":8,
    "primitive":[
        {"index":0,"oper_type":"free","object":(7,0),"isNoise":"True"}
    ]
},
]
vuln =[{"type":"dbf","producer":[(0,0),(1,0)]}]