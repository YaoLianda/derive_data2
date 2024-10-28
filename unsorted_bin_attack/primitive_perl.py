

opers = [
{
    "index":0,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":1,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":2,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":3,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":4,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":5,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":6,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":7,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":8,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":9,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":10,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":11,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":12,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#clear unsorted bin
{
    "index":13,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16393,"isNoise":"True"}
    ]
},#alloc bigger than all bins
{
    "index":14,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16393,"isNoise":"True"}
    ]
},
{
    "index":15,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16393,"isNoise":"True"},
        {"index":1,"oper_type":"malloc","size":16393,"isNoise":"True"}
    ]
},
{
    "index":16,
    "primitive":[
        {"index":0,"oper_type":"free","object":(13,0),"isNoise":"True"}
    ]#uaf free
},
{
    "index":17,
    "primitive":[
        {"index":0,"oper_type":"free","object":(14,0),"isNoise":"True"}
    ]#uaf free
},
{
    "index":18,
    "primitive":[
        {"index":0,"oper_type":"free","object":(15,0),"isNoise":"True"}
    ]#uaf free
},
{
    "index":19,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":16393,"isNoise":"True"}
    ]
},
{
    "index":20,
    "primitive":[
        {"index":0,"oper_type":"read","object":(13,0),"size":16,"isNoise":"True"}
    ]
},
{
    "index":21,
    "primitive":[
        {"index":0,"oper_type":"read","object":(14,0),"size":16,"isNoise":"True"}
    ]
},
{
    "index":22,
    "primitive":[
        {"index":0,"oper_type":"read","object":(15,0),"size":16,"isNoise":"True"}
    ]
},
{
    "index":23,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":48,"isNoise":"True"},
    ]
},#may be barrier
]
vuln =[{"type":"uaf","producer":[(13,0),(16,0),(20,0)]},
       {"type":"uaf","producer":[(14,0),(17,0),(21,0)]},
       {"type":"uaf","producer":[(15,0),(18,0),(22,0)]}]