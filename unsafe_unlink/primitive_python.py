

opers = [
{
    "index":0,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":3040,"isNoise":"True"},
        {"index":1,"oper_type":"malloc","size":1040,"isNoise":"True"},
    ]
},#dbf malloc
{
    "index":1,
    "primitive":[
        {"index":0,"oper_type":"free","object":(0,0),"isNoise":"True"},
        {"index":1,"oper_type":"malloc","size":3040,"isNoise":"True"}
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
    "primitive":[
        {"index":0,"oper_type":"read","object":(0,0),"size":16,"isNoise":"True"},
        {"index":1,"oper_type":"malloc","size":3040,"isNoise":"True"},
        {"index":2,"oper_type":"malloc","size":3040,"isNoise":"True"}
    ]
},
{
    "index":5,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":3040,"isNoise":"True"},
        {"index":1,"oper_type":"free","object":(0,1),"isNoise":"True"}
    ]
},
{
    "index":6,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":1033,"isNoise":"True"},
    ]
},{
    "index":7,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":3040,"isNoise":"True"},
    ]
},{
    "index":8,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":1033,"isNoise":"True"},
    ]
},
{
    "index":9,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":1033,"isNoise":"True"},
    ]
},
{
    "index":10,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":1033,"isNoise":"True"},
    ]
},{
    "index":11,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":1033,"isNoise":"True"},
    ]
},
{
    "index":12,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":1033,"isNoise":"True"},
    ]
},
{
    "index":13,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":3040,"isNoise":"True"},
    ]
},{
    "index":14,
      "primitive":[
        {"index":0,"oper_type":"free","object":(7,0),"isNoise":"True"}
    ]#uaf
},{
    "index":15,
      "primitive":[
        {"index":0,"oper_type":"free","object":(8,0),"isNoise":"True"}
    ]#uaf
},{
  "index":16,
    "primitive":[
        {"index":0,"oper_type":"read","object":(13,0),"size":16,"isNoise":"True"}
    ]
},{
    "index":17,
      "primitive":[
        {"index":0,"oper_type":"free","object":(4,1),"isNoise":"True"},
        {"index":1,"oper_type":"free","object":(4,2),"isNoise":"True"}
    ]#uaf
},{
  "index":18,
    "primitive":[
        {"index":0,"oper_type":"read","object":(8,0),"size":16,"isNoise":"True"}
    ]
},{
       "index":19,
      "primitive":[
        {"index":0,"oper_type":"free","object":(8,0),"isNoise":"True"},
    ]#uaf
},{
    
       "index":20,
      "primitive":[
        {"index":0,"oper_type":"free","object":(9,0),"isNoise":"True"},
    ]#uaf
},
    {
    
       "index":21,
      "primitive":[
        {"index":0,"oper_type":"free","object":(10,0),"isNoise":"True"},
    ]#uaf

}, {
    
       "index":22,
      "primitive":[
        {"index":0,"oper_type":"free","object":(11,0),"isNoise":"True"},
    ]#uaf

}, {
    
       "index":23,
      "primitive":[
        {"index":0,"oper_type":"free","object":(12,0),"isNoise":"True"},
    ]#uaf

},{
    
       "index":24,
      "primitive":[
          {"index":0,"oper_type":"read","object":(12,0),"size":16,"isNoise":"True"}
    ]#uaf

},{
    
       "index":25,
      "primitive":[
          {"index":0,"oper_type":"read","object":(11,0),"size":16,"isNoise":"True"}
    ]#uaf

},{
    
       "index":26,
      "primitive":[
          {"index":0,"oper_type":"read","object":(10,0),"size":16,"isNoise":"True"}
    ]#uaf

},{
    
       "index":27,
      "primitive":[
          {"index":0,"oper_type":"read","object":(9,0),"size":16,"isNoise":"True"}
    ]#uaf

}

]
vuln =[{"type":"hof","producer":[(0,0),(2,0)]},
       {"type":"hof","producer":[(13,0),(16,0)]},
       {"type":"hof","producer":[(0,0),(4,0)]},
       {"type":"hof","producer":[(8,0),(18,0)]},
       {"type":"hof","producer":[(12,0),(24,0)]},
       {"type":"hof","producer":[(9,0),(27,0)]},
       {"type":"hof","producer":[(10,0),(26,0)]},
       {"type":"hof","producer":[(11,0),(25,0)]},
       ]