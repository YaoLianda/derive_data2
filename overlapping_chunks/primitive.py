opers = [
{
    "index":0,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":4665,"isNoise":"True"},
    ]},
    # {"index":1,
    # "primitive":[
    #     {"index":0,"oper_type":"malloc","size":16393,"isNoise":"True"},
    # ]},
    {"index":1,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":4665,"isNoise":"True"},
        {"index":1,"oper_type":"malloc","size":16,"isNoise":"True"},
    ]},
     {"index":2,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":4665,"isNoise":"True"},
        {"index":0,"oper_type":"free","object":(2,0),"isNoise":"True"},
    ]},
     {"index":3,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":4688,"isNoise":"True"},
    ]},
    {"index":4,
    "primitive":[
        {"index":0,"oper_type":"malloc","size":4688,"isNoise":"True"},
    ]},
    {
        "index":5,
        "primitive":[
            {"index":0,"oper_type":"free","object":(0,0),"isNoise":"True"},
        ]  
    },
      {
        "index":6,
        "primitive":[
            {"index":0,"oper_type":"free","object":(1,0),"isNoise":"True"},
        ]  
    },
       {
        "index":7,
        "primitive":[
            {"index":0,"oper_type":"free","object":(2,0),"isNoise":"True"},
        ]  
    },
        {
        "index":8,
        "primitive":[
            {"index":0,"oper_type":"free","object":(3,0),"isNoise":"True"},
        ]  
    },
    #      {
    #     "index":10,
    #     "primitive":[
    #         {"index":0,"oper_type":"free","object":(5,0),"isNoise":"True"},
    #     ]  
    # },
             {
        "index":9,
        "primitive":[
           {"index":0,"oper_type":"read","object":(0,0),"size":16,"isNoise":"True"},
        ]  
    },
              {
        "index":10,
        "primitive":[
           {"index":0,"oper_type":"read","object":(1,0),"size":16,"isNoise":"True"},
        ]  
    }
    

]
vuln =[{"type":"hof","producer":[(0,0),(9,0)]},
       {"type":"hof","producer":[(1,0),(10,0)]},]