

opers = [
{
    "index":0,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":4664,"isNoise":"True"},
    ]
},
{
    "index":1,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":1040,"isNoise":"True"},
    ]
},
{
    "index":2,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":1056,"isNoise":"True"},
        {"index":1,"oper_type":"free","object":(2,0),"isNoise":"True"},
    ]
},
{
    "index":3,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":1040,"isNoise":"True"},
    ]
},
{
    "index":4,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":1040,"isNoise":"True"},
    ]
},
{
    "index":5,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":1040,"isNoise":"True"},
    ]
},
{
    "index":6,
    "primitive":[
        {"index":0,"oper_type":"free","object":(3,0),"isNoise":"True"}
    ]#uaf free
},
{
    "index":7,
    "primitive":[
        {"index":0,"oper_type":"free","object":(4,0),"isNoise":"True"}
    ]#uaf free
},
{
    "index":8,
    "primitive":[
        {"index":0,"oper_type":"free","object":(5,0),"isNoise":"True"}
    ]#uaf free
},
{
    "index":9,
    "primitive":[
        {"index":0,"oper_type":"read","object":(3,0),"size":16,"isNoise":"True"}
    ]
},
{
    "index":10,
    "primitive":[
        {"index":0,"oper_type":"read","object":(4,0),"size":16,"isNoise":"True"}
    ]
},
{
    "index":11,
    "primitive":[
        {"index":0,"oper_type":"read","object":(5,0),"size":16,"isNoise":"True"}
    ]
},


]
vuln =[{"type":"uaf","producer":[(3,0),(6,0),(9,0)]},
       {"type":"uaf","producer":[(4,0),(7,0),(10,0)]},
       {"type":"uaf","producer":[(5,0),(8,0),(11,0)]}]