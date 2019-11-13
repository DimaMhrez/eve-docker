import json

my_schema = {
# 'title' tag used in item links. 
# Defaults to the resource title minus
# the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'instrument',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'cod'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=100,must-revalidate',
    'cache_expires': 100,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': {
    'cod':{
        'type': 'string',
        'nullable' : True,
        'minlength': 1,
        'maxlength': 100,
       
    },
    'codIsin': {
        'type': 'string',
        'nullable' : True,
        'minlength': 1,
        'maxlength': 100,
        
        
    },
    
    'codDiv': {
        'type': 'string',
        'nullable' : True,
        'minlength': 1,
        'maxlength': 100,
        
    },
     'codDivTr': {
        'type': 'string',
        'nullable' : True,
        'minlength': 1,
        'maxlength': 100,
       
    },
    'codAcc': {

        'type': 'string',
        'nullable' : True,
        'minlength': 1,
        'maxlength': 100,
        
        
    },
   
    'codInt': {
        'type': 'string',
        'nullable' : True,
        'minlength': 1,
        'maxlength': 100,
        
    },
   'desc': {
        'type': 'string',
        'nullable' : True,
        'minlength': 1,
        'maxlength': 100,
        
    },
     'catStrum': {
        'type': 'string',
        'nullable' : True,
        'minlength': 1,
        'maxlength': 100,
        
    },
   
    'ctv': {
        'type': 'number'
        
        
    },
     'ctvTobe': {
        'type': 'number',
        
       
    },
    'qta': {
        'type': 'number',
        
       
        
    },
    
    'qtaTobe': {
        'type': 'number',
        
        
    },
     'perce': {
        'type': 'number'
        
        
    },
     'perceTobe': {
        'type': 'number',
        
       
    },
    'gap': {
        'type': 'number',
           
    },
  
    'gapTobe': {
        'type': 'number',
     },
     'gapPerceTobe': {
     'type': 'number'
        
        
    },
     'ctvTra': {
        'type': 'number',
        
       
    },
    'ctvTraTobe': {
        'type': 'number',
        
       
    },
  
    'negBal': {
        'type': 'number',
        
        
    
        
        
        
    },
    
    
    'netContribution': {

        'type': 'string',
        'nullable' : True,
        'minlength': 1,
        'maxlength': 100,
       
        
    },
     
    'profitLoss': {

        'type': 'string',
        'nullable' : True,
        'minlength': 1,
        'maxlength': 100,
       
        
    },
    
     'transactionAmount': {
        'type': 'number'
    },
    
    'color': {
        'type': 'string',
        'nullable' : True,
        'minlength': 1,
        'maxlength': 100,
        
    },
   'colorPendingSale': {
        'type': 'string',
        'nullable' : True,
        'minlength': 1,
        'maxlength': 100,
        
    },
  'children': {
    'type': 'list',
     'schema': {
      'type': 'dict',
      
      'schema': {
       
         'cod': {'type': 'string',
         'nullable' : True,
          },
         'codIsin': {'type': 'string',
         'nullable' : True,
          },
         'codDiv': {'type': 'string',
         'nullable' : True,
          },
         'codDivTr': {'type': 'string',
         'nullable' : True,
          },
         'codAcc': {'type': 'string',
         'nullable' : True,
          },
         'codInt': {'type': 'string',
         'nullable' : True,
          },
         'desc': {'type': 'string',
         'nullable' : True,
          },
         'catStrum': {'type': 'string',
         'nullable' : True,
          },
         'ctv': {
         'type': 'number'
    },
         'ctvTobe': {
         'type': 'number'
    },
         'qta': {
         'type': 'number'
    },
         'qtaTobe': {
         'type': 'number'
    },
         'perce': {
         'type': 'number'
    },
         'perceTobe': {
         'type': 'number'
    },
         'gap': {
         'type': 'number'
    },
         'gapTobe': {
         'type': 'number',
    },
          'gapPerceTobe': {
         'type': 'number'
    },
         'ctvTra': {
         'type': 'number'
    },
         'ctvTraTobe': {
         'type': 'number'
    },
         'negBal': {
         'type': 'number'
    },
         'netContribution': {'type': 'string',
         'nullable' : True,
          },
         'profitLoss': {'type': 'string',
         'nullable' : True,
          },
          'transactionAmount': {
         'type': 'number'
    },
         'color': {'type': 'string',
         'nullable' : True,
          },
         'colorPendingSale': {'type': 'string',
         'nullable' : True,
          },
         'children': {
         'type': 'list',
         'nullable' : True,
       },
          'var': {
         'type': 'number'
    },
         'prodStrategy': {'type': 'string',
         'nullable' : True,
          },
         'tipoQta': {'type': 'string',
         'nullable' : True,
          },
         'codAssetTest': {'type': 'string',
         'nullable' : True,
          },
         'insuranceNeeds': {'type': 'string',
         'nullable' : True,
          },
          'divisa': {
          'type': 'boolean',
          
        },
         'hasProductSheet': {'type': 'string',
         'nullable' : True,
          },
          'prefered': {
          'type': 'boolean',
          'nullable' : True,
          
        },
         'bloccoPosizione': {'type': 'string',
         'nullable' : True,
          },
         'taxBlocked': {
         'type': 'boolean',
          
        },
          
         'taxAccount': {'type': 'string',
         'nullable' : True,
          },
         'pacBlocked': {
         'type': 'boolean',
          
        },
         'pacActive': {
         'type': 'boolean',
          
        },
        'pacAvailable': {
         'type': 'boolean',
          
        },
         'pacOnly': {
         'type': 'boolean',
          
        },
         'pacPayment': {'type': 'string',
         'nullable' : True,
          },
         'totPacAmount': {'type': 'string',
         'nullable' : True,
          },
         'pacMonths': {'type': 'string',
         'nullable' : True,
          },
         'pacTaglioMin': {'type': 'number',
         'nullable' : True,
          },
         'pacTaglioMax': {'type': 'number',
         'nullable' : True,
          },
         'spMinInv': {'type': 'decimal',
         'nullable' : True,
          },
         'pacAdditionalPremium': {'type': 'string',
         'nullable' : True,
          },
         'pacRedemptionAmount': {'type': 'string',
         'nullable' : True,
          },
         'pacTotalRedemption': {
         'type': 'boolean',
          
        },
         'combiBlocked': {
         'type': 'boolean',
          
        },
         'codCmb': {'type': 'string',
         'nullable' : True,
          },
         'codStrumBench': {'type': 'string',
         'nullable' : True,
          },
         'codAssetBench': {'type': 'string',
         'nullable' : True,
          },
         'codClassBench': {'type': 'string',
         'nullable' : True,
          },
         'perceInvBench': {'type': 'string',
         'nullable' : True,
          },
         'codPort': {'type': 'string',
         'nullable' : True,
          },
         'minExpectedValue': {'type': 'string',
         'nullable' : True,
          },
         'dtScadStrum': {'type': 'string',
         'nullable' : True,
          },
         'keyPos': {'type': 'string',
         'nullable' : True,
         },
         'waivers': {'type': 'string',
         'nullable' : True,
          },
         'area': {'type': 'string',
         'nullable' : True,
          },
         'actualArea': {'type': 'string',
         'nullable' : True,
         },
         'hmAA': {'type': 'dict',
         'nullable' : True,
         },
         'assetClass': {
         'type': 'boolean',
          
        },         
      
    }
}  
  },
    'var': {
         'type': 'number'
    },
         'prodStrategy': {'type': 'string',
         'nullable' : True,
          },
         'tipoQta': {'type': 'string',
         'nullable' : True,
          },
         'codAssetTest': {'type': 'string',
         'nullable' : True,
          },
         'insuranceNeeds': {'type': 'string',
         'nullable' : True,
          },
          'divisa': {
          'type': 'boolean',
          
        },
         'hasProductSheet': {'type': 'string',
         'nullable' : True,
          },
          'prefered': {
          'type': 'boolean',
          'nullable' : True,
          
        },
         'bloccoPosizione': {'type': 'string',
         'nullable' : True,
          },
         'taxBlocked': {
         'type': 'boolean',
          
        },
          
         'taxAccount': {'type': 'string',
         'nullable' : True,
          },
         'pacBlocked': {
         'type': 'boolean',
          
        },
         'pacActive': {
         'type': 'boolean',
          
        },
        'pacAvailable': {
         'type': 'boolean',
          
        },
         'pacOnly': {
         'type': 'boolean',
          
        },
         'pacPayment': {'type': 'string',
         'nullable' : True,
          },
         'totPacAmount': {'type': 'string',
         'nullable' : True,
          },
         'pacMonths': {'type': 'string',
         'nullable' : True,
          },
         'pacTaglioMin': {'type': 'number',
         'nullable' : True,
          },
         'pacTaglioMax': {'type': 'number',
         'nullable' : True,
          },
         'spMinInv': {'type': 'decimal',
         'nullable' : True,
          },
         'pacAdditionalPremium': {'type': 'string',
         'nullable' : True,
          },
         'pacRedemptionAmount': {'type': 'string',
         'nullable' : True,
          },
         'pacTotalRedemption': {
         'type': 'boolean',
          
        },
         'combiBlocked': {
         'type': 'boolean',
          
        },
         'codCmb': {'type': 'string',
         'nullable' : True,
          },
         'codStrumBench': {'type': 'string',
         'nullable' : True,
          },
         'codAssetBench': {'type': 'string',
         'nullable' : True,
          },
         'codClassBench': {'type': 'string',
         'nullable' : True,
          },
         'perceInvBench': {'type': 'string',
         'nullable' : True,
          },
         'codPort': {'type': 'string',
         'nullable' : True,
          },
         'minExpectedValue': {'type': 'string',
         'nullable' : True,
          },
         'dtScadStrum': {'type': 'string',
         'nullable' : True,
          },
         'keyPos': {'type': 'string',
         'nullable' : True,
         },
         'waivers': {'type': 'string',
         'nullable' : True,
          },
         'area': {'type': 'string',
         'nullable' : True,
          },
         'actualArea': {'type': 'string',
         'nullable' : True,
         },
         'hmAA': {'type': 'dict',
         'nullable' : True,
         },
         'assetClass': {
         'type': 'boolean',
          
        },         
 


    
}
}

my_schema1_json = json.dumps(my_schema)

open("my_schema.json", "w").write(my_schema1_json)


