

opers = [
{
    "index":0,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16,"isNoise":"True"},
        {"index":1,"oper_type":"malloc","size":16,"isNoise":"True"},
    ]
},#dbf malloc
{
    "index":1,
    "primitive":[#无法经过check point2 read时uaf地址已不存在
        {"index":0,"oper_type":"free","object":(0,0),"isNoise":"True"},
        {"index":1,"oper_type":"malloc","size":16,"isNoise":"True"}
    ]#dbf free
},
{
    "index":2,
    "primitive":[
        {"index":0,"oper_type":"read","object":(0,0),"size":16,"isNoise":"True"}
    ]
},
{
    "index":3,
    "primitive":[
        {"index":0,"oper_type":"free","object":(0,0),"isNoise":"True"}
    ]#uaf free
},
{
    "index":4,
    "primitive":[#check point3直接通过
        {"index":0,"oper_type":"read","object":(0,0),"size":16,"isNoise":"True"},
        {"index":1,"oper_type":"malloc","size":16,"isNoise":"True"},
        {"index":2,"oper_type":"malloc","size":16,"isNoise":"True"}
    ]
},
{
    "index":5,
    "primitive":[##check point3循环超过两次才取出目标地址
        {"index":0,"oper_type":"malloc","size":16,"isNoise":"True"},
        {"index":1,"oper_type":"free","object":(0,1),"isNoise":"True"}
    ]
},
{
    "index":6,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16,"isNoise":"True"},
    ]
},{
    "index":7,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16,"isNoise":"True"},
    ]
},{
    "index":8,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16,"isNoise":"True"},
    ]
}

]
vuln =[{"type":"uaf","producer":[(0,0),(1,0),(2,0)]},
       {"type":"uaf","producer":[(0,0),(3,0),(2,0)]},
       {"type":"uaf","producer":[(0,0),(3,0),(4,0)]}
       ]