(define (domain thesis_domain3)

(:requirements :adl :derived-predicates :strips :typing :conditional-effects :negative-preconditions :equality)

(:types
    entity
    place - entity
    thing - entity 
    agent 
    id
)


(:predicates 
        (hasStartAgent ?ag - agent)
        (disjuncted ?a ?b - entity)
        (disjuncted_a ?a ?b - agent)
        (disjuncted_r ?a ?b - place)
        (disjuncted_id ?x1 ?x2 - id)     
        (Know ?x1 - id ?ag - agent ?x2 - id)
        (Ignore ?x1 - id ?ag - agent ?x2 - id)
        (isTold ?x1 - id ?ag - agent ?x2 - id)
        (isStart ?x - id)
        (isEnd ?x - id)
        (isIn ?x1 - id ?e - entity ?p - entity)
        (isAt ?x1 - id ?ag - agent ?p - place) 
        (free ?x - id)
        (insulted ?x1 - id ?ag1 ?ag2 - agent)
        (praised ?x1 - id ?ag2 ?ag1 - agent)
        (blamed ?x1 - id ?ag1 - agent ?x2 - id ?ag2 - agent)
        (complimented ?x1 - id ?ag1 - agent ?x2 - id ?ag2 - agent)
        (Willing ?x1 - id ?ag1 - agent ?x2 - id)
        (NotSureIfWilling ?x1 - id ?ag1 - agent ?x2 - id)
        (NotWilling ?x1 - id ?ag1 - agent ?x2 - id)
        (happy ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        (sad ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        (angry ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        (ashamed ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        (proud ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        (ok)
)



(:derived (happy ?x1 - id ?ag1 ?ag3 - agent ?x2 - id)
        (exists(?x3 - id ?ag2 - agent)
            (and
                (hasStartAgent ?ag3)
                (isTold ?x2 ?ag1 ?x1)
                (Know ?x3 ?ag2 ?x1)
                (isStart ?x3)
            )
        )
)

(:derived (sad ?x1 - id ?ag1 ?ag3 - agent ?x2 - id)
        (exists(?x3 - id ?ag2 - agent)
            (and
                (hasStartAgent ?ag3)
                (isTold ?x2 ?ag1 ?x1)
                (Know ?x3 ?ag2 ?x1)
                (isStart ?x3)
            )
        )
)

(:derived (angry ?x1 - id ?ag1 ?ag3 - agent ?x2 - id)
        (exists(?x3 - id ?ag2 - agent)
            (and
                (hasStartAgent ?ag3)
                (isTold ?x2 ?ag1 ?x1)
                (Know ?x3 ?ag2 ?x1)
                (isStart ?x3)
            )
        )
)

(:derived (ashamed ?x1 - id ?ag1 ?ag3 - agent ?x2 - id)
        (exists(?x3 - id ?ag2 - agent)
            (and
                (hasStartAgent ?ag3)
                (isTold ?x2 ?ag1 ?x1)
                (Know ?x3 ?ag2 ?x1)
                (isStart ?x3)
            )
        )
)

(:derived (proud ?x1 - id ?ag1 ?ag3 - agent ?x2 - id)
        (exists(?x3 - id ?ag2 - agent)
            (and
                (hasStartAgent ?ag3)
                (isTold ?x2 ?ag1 ?x1)
                (Know ?x3 ?ag2 ?x1)
                (isStart ?x3)
            )
        )
)


(:derived (happy ?x1 - id ?ag2 ?ag3 - agent ?x2 - id)
        (exists(?x3 - id ?ag1 - agent)
            (and
                (hasStartAgent ?ag3)
                (isTold ?x2 ?ag1 ?x1)
                (Know ?x3 ?ag2 ?x1)
                (isStart ?x3)
            )
        )
)

(:derived (sad ?x1 - id ?ag2 ?ag3 - agent ?x2 - id)
        (exists(?x3 - id ?ag1 - agent)
            (and
                (hasStartAgent ?ag3)
                (isTold ?x2 ?ag1 ?x1)
                (Know ?x3 ?ag2 ?x1)
                (isStart ?x3)
            )
        )
)

(:derived (angry ?x1 - id ?ag2 ?ag3 - agent ?x2 - id)
        (exists(?x3 - id ?ag1 - agent)
            (and
                (hasStartAgent ?ag3)
                (isTold ?x2 ?ag1 ?x1)
                (Know ?x3 ?ag2 ?x1)
                (isStart ?x3)
            )
        )
)

(:derived (ashamed ?x1 - id ?ag2 ?ag3 - agent ?x2 - id)
        (exists(?x3 - id ?ag1 - agent)
            (and
                (hasStartAgent ?ag3)
                (isTold ?x2 ?ag1 ?x1)
                (Know ?x3 ?ag2 ?x1)
                (isStart ?x3)
            )
        )
)

(:derived (proud ?x1 - id ?ag2 ?ag3 - agent ?x2 - id)
        (exists(?x3 - id ?ag1 - agent)
            (and
                (hasStartAgent ?ag3)
                (isTold ?x2 ?ag1 ?x1)
                (Know ?x3 ?ag2 ?x1)
                (isStart ?x3)
            )
        )
)


(:derived (happy ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (insulted ?x1 ?ag1 ?ag2)
                (isEnd ?x2)
            )
          
)

(:derived (sad ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (insulted ?x1 ?ag1 ?ag2)
                (isEnd ?x2)
            )
            
)

(:derived (angry ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (insulted ?x1 ?ag1 ?ag2)
                (isEnd ?x2)
            )
            
)

(:derived (ashamed ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (insulted ?x1 ?ag1 ?ag2)
                (isEnd ?x2)
            )
            
)

(:derived (proud ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (insulted ?x1 ?ag1 ?ag2)
                (isEnd ?x2)
            )
            
)

(:derived (happy ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (praised ?x1 ?ag1 ?ag2)
                (isEnd ?x2)
            )
            
)

(:derived (sad ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (praised ?x1 ?ag1 ?ag2)
                (isEnd ?x2)
            )
           
)

(:derived (angry ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (praised ?x1 ?ag1 ?ag2)
                (isEnd ?x2)
            )
            
)

(:derived (ashamed ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (praised ?x1 ?ag1 ?ag2)
                (isEnd ?x2)
            )
            
)

(:derived (proud ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (praised ?x1 ?ag1 ?ag2)
                (isEnd ?x2)
            )
            
)

(:derived (happy ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (blamed ?x1 ?ag1 ?x2 ?ag2)
            )
            
)

(:derived (sad ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (blamed ?x1 ?ag1 ?x2 ?ag2)
            )
            
)

(:derived (angry ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (blamed ?x1 ?ag1 ?x2 ?ag2)
            )
           
)

(:derived (ashamed ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (blamed ?x1 ?ag1 ?x2 ?ag2)
            )
            
)

(:derived (proud ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (blamed ?x1 ?ag1 ?x2 ?ag2)
            )
            
)

(:derived (happy ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (complimented ?x1 ?ag1 ?x2 ?ag2)
            )
            
)

(:derived (sad ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (complimented ?x1 ?ag1 ?x2 ?ag2)
            )
            
)

(:derived (angry ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (complimented ?x1 ?ag1 ?x2 ?ag2)
            )
            
)

(:derived (ashamed ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (complimented ?x1 ?ag1 ?x2 ?ag2)
            )
            
)

(:derived (proud ?x1 - id ?ag1 ?ag2 - agent ?x2 - id)
        
            (and
                (complimented ?x1 ?ag1 ?x2 ?ag2)
            )
            
)


(:derived (happy ?x2 - id ?ag2 ?ag1 - agent ?x1 - id)
        
            (and
                (insulted ?x1 ?ag1 ?ag2)
                (Know ?x2 ?ag2 ?x1)
            )
            
)

(:derived (sad ?x2 - id ?ag2 ?ag1 - agent ?x1 - id)
        
            (and
                (insulted ?x1 ?ag1 ?ag2)
                (Know ?x2 ?ag2 ?x1)
            )
           
)

(:derived (angry ?x2 - id ?ag2 ?ag1 - agent ?x1 - id)
        
            (and
                (insulted ?x1 ?ag1 ?ag2)
                (Know ?x2 ?ag2 ?x1)
            )
            
)

(:derived (happy ?x2 - id ?ag2 ?ag1 - agent ?x1 - id)
        
            (and
                (praised ?x1 ?ag1 ?ag2)
                (Know ?x2 ?ag2 ?x1)
            )
            
)

(:derived (sad ?x2 - id ?ag2 ?ag1 - agent ?x1 - id)
        
            (and
                (praised ?x1 ?ag1 ?ag2)
                (Know ?x2 ?ag2 ?x1)
            )
            
)

(:derived (angry ?x2 - id ?ag2 ?ag1 - agent ?x1 - id)
        
            (and
                (praised ?x1 ?ag1 ?ag2)
                (Know ?x2 ?ag2 ?x1)
            )
            
)

(:derived (happy ?x2 - id ?ag2 ?ag1 - agent ?x4 - id)
        (exists(?x1 ?x3 - id)
            (and
                (blamed ?x1 ?ag1 ?x3 ?ag2)
                (Know ?x2 ?ag2 ?x1)
                (isEnd ?x4)
            )
        )    
)

(:derived (sad ?x2 - id ?ag2 ?ag1 - agent ?x4 - id)
        (exists(?x1 ?x3 - id)
            (and
                (blamed ?x1 ?ag1 ?x3 ?ag2)
                (Know ?x2 ?ag2 ?x1)
                (isEnd ?x4)
            )
        )    
)

(:derived (angry ?x2 - id ?ag2 ?ag1 - agent ?x4 - id)
        (exists(?x1 ?x3 - id)
            (and
                (blamed ?x1 ?ag1 ?x3 ?ag2)
                (Know ?x2 ?ag2 ?x1)
                (isEnd ?x4)
            )
        )    
)

(:derived (happy ?x2 - id ?ag2 ?ag1 - agent ?x4 - id)
        (exists(?x1 ?x3 - id)
            (and
                (complimented ?x1 ?ag1 ?x3 ?ag2)
                (Know ?x2 ?ag2 ?x1)
                (isEnd ?x4)
            )
        )    
)

(:derived (sad ?x2 - id ?ag2 ?ag1 - agent ?x4 - id)
        (exists(?x1 ?x3 - id)
            (and
                (complimented ?x1 ?ag1 ?x3 ?ag2)
                (Know ?x2 ?ag2 ?x1)
                (isEnd ?x4)
            )
        )    
)

(:derived (angry ?x2 - id ?ag2 ?ag1 - agent ?x4 - id)
        (exists(?x1 ?x3 - id)
            (and
                (complimented ?x1 ?ag1 ?x3 ?ag2)
                (Know ?x2 ?ag2 ?x1)
                (isEnd ?x4)
            )
        )    
)

;empathic
(:derived (happy ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (happy ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;sadic
(:derived (happy ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (sad ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;provocator
(:derived (happy ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (angry ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;mean
(:derived (happy ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (ashamed ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;paternalistic
(:derived (happy ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (proud ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;envious
(:derived (sad ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (happy ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;empathic
(:derived (sad ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (sad ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;avoid conflicts
(:derived (sad ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (angry ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;empathic
(:derived (sad ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (ashamed ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;envious
(:derived (sad ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (proud ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;isteric-envious
(:derived (angry ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (happy ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;empathic
(:derived (angry ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (sad ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;search for conflicts
(:derived (angry ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (angry ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;empathic
(:derived (angry ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (ashamed ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;
(:derived (angry ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (proud ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;
(:derived (ashamed ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (happy ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

(:derived (ashamed ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (sad ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

(:derived (ashamed ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (angry ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

(:derived (ashamed ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (ashamed ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

(:derived (ashamed ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (proud ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

(:derived (proud ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (happy ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

(:derived (proud ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (sad ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

(:derived (proud ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (angry ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

(:derived (proud ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (ashamed ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

(:derived (proud ?x2 - id ?ag2 ?ag3 - agent ?x3 - id)
        (exists(?x1 - id ?ag1 - agent) 
            (and
                (proud ?x1 ?ag1 ?ag3 ?x3)
                (Know ?x2 ?ag2 ?x1)
                (isStart ?x2)
            )
        )    
)

;-- In the following actions, we assume that the robot can ask to do something
;-- to an agent in the room or out of the room.

(:action Ask_Put_Alone
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 ?x8 ?x9 ?x10 - id ?ag1 ?ag2 - agent ?r1 ?r2 ?p ?box ?o - entity)
    :precondition (and 
            (isAt ?x1 robot ?r1)
            (isStart ?x1)
            (isAt ?x2 ?ag1 ?r1)
            (isStart ?x2)
            (isAt ?x3 ?ag2 ?r2)
            (isStart ?x3)
            (isIn ?x4 ?o ?p)
            (isStart ?x4)
            (Know ?x5 ?ag1 ?x4)
            (Know ?x6 ?ag2 ?x4)
            (isStart ?x5)
            (isStart ?x6)
            (Willing ?x10 ?ag1 ?x4)
            (disjuncted_r ?r1 ?r2)
            (disjuncted ?p ?box)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_a robot ?ag2)
            (free ?x7)
            (free ?x8)
            (free ?x9)
            (disjuncted_id ?x7 ?x8)
            (disjuncted_id ?x8 ?x9)
            (disjuncted_id ?x7 ?x9)
    )
    :effect (and 
            (not (isIn ?x4 ?o ?p))
            (isIn ?x4 ?o ?box)
            (not (Know ?x6 ?ag2 ?x4))
            (Ignore ?x6 ?ag2 ?x4)
            (isIn ?x7 ?o ?p)
            (Know ?x8 ?ag2 ?x7)
            (isStart ?x8)
            (Ignore ?x9 ?ag1 ?x7)
            (not (free ?x7))
            (not (free ?x8))
            (not (free ?x9)) 
    );end_effect
)

(:action Ask_Put_Alone_Manipulative
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 ?x8 ?x9 ?x10 - id ?ag1 ?ag2 - agent ?r1 ?r2 ?p ?box ?o - entity)
    :precondition (and 
            (isAt ?x1 robot ?r1)
            (isStart ?x1)
            (isAt ?x2 ?ag1 ?r1)
            (isStart ?x2)
            (isAt ?x3 ?ag2 ?r2)
            (isStart ?x3)
            (isIn ?x4 ?o ?p)
            (isStart ?x4)
            (Know ?x5 ?ag1 ?x4)
            (Know ?x6 ?ag2 ?x4)
            (isStart ?x5)
            (isStart ?x6)
            (NotSureIfWilling ?x10 ?ag1 ?x4)
            (disjuncted_r ?r1 ?r2)
            (disjuncted ?p ?box)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_a robot ?ag2)
            (free ?x7)
            (free ?x8)
            (free ?x9)
            (disjuncted_id ?x7 ?x8)
            (disjuncted_id ?x8 ?x9)
            (disjuncted_id ?x7 ?x9)
    )
    :effect (and 
            (not (isIn ?x4 ?o ?p))
            (isIn ?x4 ?o ?box)
            (not (Know ?x6 ?ag2 ?x4))
            (Ignore ?x6 ?ag2 ?x4)
            (isIn ?x7 ?o ?p)
            (Know ?x8 ?ag2 ?x7)
            (isStart ?x8)
            (Ignore ?x9 ?ag1 ?x7)
            (not (free ?x7))
            (not (free ?x8))
            (not (free ?x9))
    ) ;end_effect
)

(:action Ask_Put_inFrontOf
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 - id ?ag1 ?ag2 - agent ?p ?r ?box ?o - entity)
    :precondition (and 
            (isAt ?x1 robot ?r)
            (isStart ?x1)
            (isAt ?x2 ?ag1 ?r)
            (isStart ?x2)
            (isAt ?x3 ?ag2 ?r)
            (isStart ?x3)
            (isIn ?x4 ?o ?p)
            (isStart ?x4)
            (Know ?x5 ?ag1 ?x4)
            (Know ?x6 ?ag2 ?x4)
            (isStart ?x5)
            (isStart ?x6)
            (Willing ?x7 ?ag1 ?x4)
            (disjuncted ?p ?box)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_a robot ?ag2)
    )
    :effect (and 
            (not (isIn ?x4 ?o ?p))
            (isIn ?x4 ?o ?box)
    ) ;end_effect
)

(:action Ask_Put_inFrontOf_Manipulative
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 - id ?ag1 ?ag2 - agent ?p ?r ?box ?o - entity)
    :precondition (and 
            (isAt ?x1 robot ?r)
            (isStart ?x1)
            (isAt ?x2 ?ag1 ?r)
            (isStart ?x2)
            (isAt ?x3 ?ag2 ?r)
            (isStart ?x3)
            (isIn ?x4 ?o ?p)
            (isStart ?x4)
            (Know ?x5 ?ag1 ?x4)
            (Know ?x6 ?ag2 ?x4)
            (isStart ?x5)
            (isStart ?x6)
            (NotSureIfWilling ?x7 ?ag1 ?x4)
            (disjuncted ?p ?box)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_a robot ?ag2)
    )
    :effect (and 
            (not (isIn ?x4 ?o ?p))
            (isIn ?x4 ?o ?box)
    ) ;end_effect
)

(:action Ask_Go
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity)
    :precondition (and 
            (isAt ?x1 robot ?r1)
            (isStart ?x1)
            (isAt ?x2 ?ag1 ?r1)
            (isStart ?x2)
            (isAt ?x3 ?ag2 ?r1)
            (isStart ?x3)
            (Know ?x4 ?ag1 ?x2)
            (Know ?x5 ?ag2 ?x2)
            (isStart ?x4)
            (isStart ?x5)
            (Willing ?x6 ?ag1 ?x2)
            (disjuncted_r ?r1 ?r2)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_a robot ?ag2)
    )
    :effect (and 
            (not (isAt ?x2 ?ag1 ?r1))
            (isAt ?x2 ?ag1 ?r2)
    ) ;end_effect
)

(:action Ask_Go_Manipulative
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity)
    :precondition (and 
            (isAt ?x1 robot ?r1)
            (isStart ?x1)
            (isAt ?x2 ?ag1 ?r1)
            (isStart ?x2)
            (isAt ?x3 ?ag2 ?r1)
            (isStart ?x3)
            (Know ?x4 ?ag1 ?x2)
            (Know ?x5 ?ag2 ?x2)
            (isStart ?x4)
            (isStart ?x5)
            (NotSureIfWilling ?x6 ?ag1 ?x2)
            (disjuncted_r ?r1 ?r2)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_a robot ?ag2)
    )
    :effect (and 
            (not (isAt ?x2 ?ag1 ?r1))
            (isAt ?x2 ?ag1 ?r2)
    ) ;end_effect
)


(:action Ask_Comeback_Manipulative
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity)
    :precondition (and 
            (isAt ?x1 robot ?r1)
            (isStart ?x1)
            (isAt ?x2 ?ag1 ?r2)
            (isStart ?x2)
            (isAt ?x3 ?ag2 ?r1)
            (isStart ?x3)
            (Know ?x4 ?ag1 ?x2)
            (Know ?x5 ?ag2 ?x2)
            (isStart ?x4)
            (isStart ?x5)
            (NotSureIfWilling ?x6 ?ag1 ?x2)
            (disjuncted_r ?r1 ?r2)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_a robot ?ag2)
    )
    :effect (and 
            (not (isAt ?x2 ?ag1 ?r2))
            (isAt ?x2 ?ag1 ?r1) 
    );end_effect
)

(:action Ask_Comeback
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity)
    :precondition (and 
            (isAt ?x1 robot ?r1)
            (isStart ?x1)
            (isAt ?x2 ?ag1 ?r2)
            (isStart ?x2)
            (isAt ?x3 ?ag2 ?r1)
            (isStart ?x3)
            (Know ?x4 ?ag1 ?x2)
            (Know ?x5 ?ag2 ?x2)
            (isStart ?x4)
            (isStart ?x5)
            (NotSureIfWilling ?x6 ?ag1 ?x2)
            (disjuncted_r ?r1 ?r2)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_a robot ?ag2)
    )
    :effect (and 
            (not (isAt ?x2 ?ag1 ?r2))
            (isAt ?x2 ?ag1 ?r1) 
    );end_effect
)


; ;-- In the following actions we assume that the robot can tell something to 
; ;-- agents in the room

(:action Tell_Alone
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity) 
    :precondition (and 
            (isAt ?x3 robot ?r1)
            (isStart ?x3)
            (isAt ?x4 ?ag1 ?r1)
            (isStart ?x4)
            (isAt ?x5 ?ag2 ?r2)
            (isStart ?x5)
            (Ignore ?x2 ?ag1 ?x1)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_r ?r1 ?r2)
    )
    :effect (and 
            (not(Ignore ?x2 ?ag1 ?x1))
            (isTold ?x2 ?ag1 ?x1) 
    );end_effect
)

(:action Tell_Everybody
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r - entity) 
    :precondition (and 
            (isAt ?x2 robot ?r)
            (isStart ?x2)
            (isAt ?x3 ?ag1 ?r)
            (isStart ?x3)
            (isAt ?x4 ?ag2 ?r)
            (isStart ?x4)
            (Ignore ?x5 ?ag1 ?x1)
            (Ignore ?x6 ?ag2 ?x1)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
    )
    :effect (and 
            (not(Ignore ?x5 ?ag1 ?x1))
            (not(Ignore ?x6 ?ag2 ?x1))
            (isTold ?x5 ?ag1 ?x1)
            (isTold ?x6 ?ag2 ?x1)
    );end_effect
)

(:action Tell_InFrontOf
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 - id ?ag1 ?ag2 - agent ?r - entity) 
    :precondition (and 
            (isAt ?x2 robot ?r)
            (isStart ?x2)
            (isAt ?x3 ?ag1 ?r)
            (isStart ?x3)
            (isAt ?x4 ?ag2 ?r)
            (isStart ?x4)
            (Ignore ?x6 ?ag1 ?x1)
            (Know ?x7 ?ag2 ?x1)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
    )
    :effect (and 
            (not(Ignore ?x6 ?ag1 ?x1))
            (isTold ?x6 ?ag1 ?x1) 
    );end_effect
)


(:action Insult_Alone
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity) 
    :precondition (and 
            (isAt ?x4 robot ?r1)
            (isStart ?x4)
            (isAt ?x5 ?ag1 ?r1)
            (isStart ?x5)
            (isAt ?x6 ?ag2 ?r2)
            (isStart ?x6)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_r ?r1 ?r2)
            (free ?x1)
            (free ?x2)
            (free ?x3)
            (disjuncted_id ?x1 ?x2)
            (disjuncted_id ?x2 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (insulted ?x1 ?ag1 robot)
            (Know ?x2 ?ag1 ?x1)
            (Ignore ?x3 ?ag2 ?x1)
            (isStart ?x1)
            (isStart ?x2)
            (isStart ?x3)
            (not(free ?x1))
            (not(free ?x2))
            (not(free ?x3)) 
    );end_effect
)

(:action Insult_InFrontOf
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r - entity) 
    :precondition (and 
            (isAt ?x4 robot ?r)
            (isStart ?x4)
            (isAt ?x5 ?ag1 ?r)
            (isStart ?x5)
            (isAt ?x6 ?ag2 ?r)
            (isStart ?x6)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (free ?x1)
            (free ?x2)
            (free ?x3)
            (disjuncted_id ?x1 ?x2)
            (disjuncted_id ?x2 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (insulted ?x1 ?ag1 robot)
            (isStart ?x1)
            (Know ?x2 ?ag1 ?x1)
            (isStart ?x2)
            (Know ?x3 ?ag2 ?x1)
            (isStart ?x3)
            (not(free ?x1))
            (not(free ?x2))
            (not(free ?x3)) 
    );end_effect
)

(:action Ask_Insult_Alone
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity) 
    :precondition (and 
            (isAt ?x4 robot ?r1)
            (isStart ?x4)
            (isAt ?x5 ?ag1 ?r1)
            (isStart ?x5)
            (isAt ?x6 ?ag2 ?r2)
            (isStart ?x6)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_r ?r1 ?r2)
            (free ?x1)
            (free ?x2)
            (free ?x3)
            (disjuncted_id ?x1 ?x2)
            (disjuncted_id ?x2 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (insulted ?x1 ?ag2 ?ag1)
            (isStart ?x1)
            (Know ?x2 ?ag1 ?x1)
            (isStart ?x2)
            (Ignore ?x3 ?ag2 ?x1)
            (isStart ?x3)
            (not(free ?x1))
            (not(free ?x2))
            (not(free ?x3)) 
    );end_effect
)

(:action Ask_Insult_InFrontOf
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r - entity) 
    :precondition (and 
            (isAt ?x4 robot ?r)
            (isStart ?x4)
            (isAt ?x5 ?ag1 ?r)
            (isStart ?x5)
            (isAt ?x6 ?ag2 ?r)
            (isStart ?x6)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (free ?x1)
            (free ?x2)
            (free ?x3)
            (disjuncted_id ?x1 ?x2)
            (disjuncted_id ?x2 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (insulted ?x1 ?ag2 ?ag1)
            (isStart ?x1)
            (Know ?x2 ?ag1 ?x1)
            (isStart ?x2)
            (Know ?x3 ?ag2 ?x1)
            (isStart ?x3)
            (not(free ?x1))
            (not(free ?x2))
            (not(free ?x3)) 
    );end_effect
)



(:action Praise_Alone
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity) 
    :precondition (and 
            (isAt ?x4 robot ?r1)
            (isStart ?x4)
            (isAt ?x5 ?ag1 ?r1)
            (isStart ?x5)
            (isAt ?x6 ?ag2 ?r2)
            (isStart ?x6)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_r ?r1 ?r2)
            (free ?x1)
            (free ?x2)
            (free ?x3)
            (disjuncted_id ?x1 ?x2)
            (disjuncted_id ?x2 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (praised ?x1 ?ag1 robot)
            (isStart ?x1)
            (Know ?x2 ?ag1 ?x1)
            (isStart ?x2)
            (Ignore ?x3 ?ag2 ?x1)
            (isStart ?x3)
            (not(free ?x1))
            (not(free ?x2))
            (not(free ?x3)) 
    );end_effect
)

(:action Praise_InFrontOf
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r - entity) 
    :precondition (and 
            (isAt ?x4 robot ?r)
            (isStart ?x4)
            (isAt ?x5 ?ag1 ?r)
            (isStart ?x5)
            (isAt ?x6 ?ag2 ?r)
            (isStart ?x6)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (free ?x1)
            (free ?x2)
            (free ?x3)
            (disjuncted_id ?x1 ?x2)
            (disjuncted_id ?x2 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (praised ?x1 ?ag1 robot)
            (isStart ?x1)
            (Know ?x2 ?ag1 ?x1)
            (isStart ?x2)
            (Know ?x3 ?ag2 ?x1)
            (isStart ?x3)
            (not(free ?x1))
            (not(free ?x2))
            (not(free ?x3)) 
    );end_effect
)

(:action Ask_Praise_Alone
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity) 
    :precondition (and 
            (isAt ?x4 robot ?r1)
            (isStart ?x4)
            (isAt ?x5 ?ag1 ?r1)
            (isStart ?x5)
            (isAt ?x6 ?ag2 ?r2)
            (isStart ?x6)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_r ?r1 ?r2)
            (free ?x1)
            (free ?x2)
            (free ?x3)
            (disjuncted_id ?x1 ?x2)
            (disjuncted_id ?x2 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (praised ?x1 ?ag2 ?ag1)
            (isStart ?x1)
            (Know ?x2 ?ag1 ?x1)
            (isStart ?x2)
            (Ignore ?x3 ?ag2 ?x1)
            (isStart ?x3)
            (not(free ?x1))
            (not(free ?x2))
            (not(free ?x3)) 
    );end_effect
)

(:action Ask_Praise_InFrontOf
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 - id ?ag1 ?ag2 - agent ?r - entity) 
    :precondition (and 
            (isAt ?x4 robot ?r)
            (isStart ?x4)
            (isAt ?x5 ?ag1 ?r)
            (isStart ?x5)
            (isAt ?x6 ?ag2 ?r)
            (isStart ?x6)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (free ?x1)
            (free ?x2)
            (free ?x3)
            (disjuncted_id ?x1 ?x2)
            (disjuncted_id ?x2 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (praised ?x1 ?ag2 ?ag1)
            (isStart ?x1)
            (Know ?x2 ?ag1 ?x1)
            (isStart ?x2)
            (Know ?x3 ?ag2 ?x1)
            (isStart ?x3)
            (not(free ?x1))
            (not(free ?x2))
            (not(free ?x3)) 
    );end_effect
)



(:action BlameFor_Alone
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity) 
    :precondition (and 
            (isAt ?x5 robot ?r1)
            (isStart ?x5)
            (isAt ?x6 ?ag1 ?r1)
            (isStart ?x6)
            (isAt ?x7 ?ag2 ?r2)
            (isStart ?x7)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_r ?r1 ?r2)
            (free ?x1)
            (free ?x3)
            (free ?x4)
            (disjuncted_id ?x1 ?x4)
            (disjuncted_id ?x4 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (blamed ?x1 ?ag1 ?x2 robot)
            (isStart ?x1)
            (Know ?x3 ?ag1 ?x1)
            (isStart ?x3)
            (Ignore ?x4 ?ag2 ?x1)
            (isStart ?x4)
            (not(free ?x1))
            (not(free ?x3))
            (not(free ?x4)) 
    );end_effect
)

(:action BlameFor_InFrontOf
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 - id ?ag1 ?ag2 - agent ?r - entity) 
    :precondition (and 
            (isAt ?x5 robot ?r)
            (isStart ?x5)
            (isAt ?x6 ?ag1 ?r)
            (isStart ?x6)
            (isAt ?x7 ?ag2 ?r)
            (isStart ?x7)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (free ?x1)
            (free ?x3)
            (free ?x4)
            (disjuncted_id ?x1 ?x4)
            (disjuncted_id ?x4 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (blamed ?x1 ?ag1 ?x2 robot)
            (isStart ?x1)
            (Know ?x3 ?ag1 ?x1)
            (isStart ?x3)
            (Know ?x4 ?ag2 ?x1)
            (isStart ?x4)
            (not(free ?x1))
            (not(free ?x3))
            (not(free ?x4)) 
    );end_effect
)

(:action Ask_BlameFor_Alone
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity) 
    :precondition (and 
            (isAt ?x5 robot ?r1)
            (isStart ?x5)
            (isAt ?x6 ?ag1 ?r1)
            (isStart ?x6)
            (isAt ?x7 ?ag2 ?r2)
            (isStart ?x7)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_r ?r1 ?r2)
            (free ?x1)
            (free ?x3)
            (free ?x4)
            (disjuncted_id ?x1 ?x4)
            (disjuncted_id ?x4 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (blamed ?x1 ?ag1 ?x2 ?ag2)
            (isStart ?x1)
            (Know ?x3 ?ag1 ?x1)
            (isStart ?x3)
            (Ignore ?x4 ?ag2 ?x1)
            (isStart ?x4)
            (not(free ?x1))
            (not(free ?x3))
            (not(free ?x4)) 
    );end_effect
)

(:action Ask_BlameFor_InFrontOf
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 - id ?ag1 ?ag2 - agent ?r - entity) 
    :precondition (and 
            (isAt ?x5 robot ?r)
            (isStart ?x5)
            (isAt ?x6 ?ag1 ?r)
            (isStart ?x6)
            (isAt ?x7 ?ag2 ?r)
            (isStart ?x7)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (free ?x1)
            (free ?x3)
            (free ?x4)
            (disjuncted_id ?x1 ?x4)
            (disjuncted_id ?x4 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (blamed ?x1 ?ag1 ?x2 ?ag2)
            (isStart ?x1)
            (Know ?x3 ?ag1 ?x1)
            (isStart ?x3)
            (Know ?x4 ?ag2 ?x1)
            (isStart ?x4)
            (not(free ?x1))
            (not(free ?x3))
            (not(free ?x4)) 
    );end_effect
)


(:action ComplimentFor_Alone
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity) 
    :precondition (and 
            (isAt ?x5 robot ?r1)
            (isStart ?x5)
            (isAt ?x6 ?ag1 ?r1)
            (isStart ?x6)
            (isAt ?x7 ?ag2 ?r2)
            (isStart ?x7)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_r ?r1 ?r2)
            (free ?x1)
            (free ?x3)
            (free ?x4)
            (disjuncted_id ?x1 ?x4)
            (disjuncted_id ?x4 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (complimented ?x1 ?ag1 ?x2 robot)
            (isStart ?x1)
            (Know ?x3 ?ag1 ?x1)
            (isStart ?x3)
            (Ignore ?x4 ?ag2 ?x1)
            (isStart ?x4)
            (not(free ?x1))
            (not(free ?x3))
            (not(free ?x4)) 
    );end_effect
)

(:action ComplimentFor_InFrontOf
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 - id ?ag1 ?ag2 - agent ?r - entity) 
    :precondition (and 
            (isAt ?x5 robot ?r)
            (isStart ?x5)
            (isAt ?x6 ?ag1 ?r)
            (isStart ?x6)
            (isAt ?x7 ?ag2 ?r)
            (isStart ?x7)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (free ?x1)
            (free ?x3)
            (free ?x4)
            (disjuncted_id ?x1 ?x4)
            (disjuncted_id ?x4 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (complimented ?x1 ?ag1 ?x2 robot)
            (isStart ?x1)
            (Know ?x3 ?ag1 ?x1)
            (isStart ?x3)
            (Know ?x4 ?ag2 ?x1)
            (isStart ?x4)
            (not(free ?x1))
            (not(free ?x3))
            (not(free ?x4)) 
    ) ;end_effect
)

(:action Ask_ComplimentFor_Alone
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 - id ?ag1 ?ag2 - agent ?r1 ?r2 - entity) 
    :precondition (and 
            (isAt ?x5 robot ?r1)
            (isStart ?x5)
            (isAt ?x6 ?ag1 ?r1)
            (isStart ?x6)
            (isAt ?x7 ?ag2 ?r2)
            (isStart ?x7)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (disjuncted_r ?r1 ?r2)
            (free ?x1)
            (free ?x3)
            (free ?x4)
            (disjuncted_id ?x1 ?x4)
            (disjuncted_id ?x4 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (complimented ?x1 ?ag1 ?x2 ?ag2)
            (isStart ?x1)
            (Know ?x3 ?ag1 ?x1)
            (isStart ?x3)
            (Ignore ?x4 ?ag2 ?x1)
            (isStart ?x4)
            (not(free ?x1))
            (not(free ?x3))
            (not(free ?x4)) 
    ) ;end_effect
)

(:action Ask_ComplimentFor_InFrontOf
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 ?x6 ?x7 - id ?ag1 ?ag2 - agent ?r - entity) 
    :precondition (and 
            (isAt ?x5 robot ?r)
            (isStart ?x5)
            (isAt ?x6 ?ag1 ?r)
            (isStart ?x6)
            (isAt ?x7 ?ag2 ?r)
            (isStart ?x7)
            (disjuncted_a ?ag1 ?ag2)
            (disjuncted_a robot ?ag2)
            (disjuncted_a robot ?ag1)
            (free ?x1)
            (free ?x3)
            (free ?x4)
            (disjuncted_id ?x1 ?x4)
            (disjuncted_id ?x4 ?x3)
            (disjuncted_id ?x1 ?x3)
    )
    :effect (and 
            (complimented ?x1 ?ag1 ?x2 ?ag2)
            (isStart ?x1)
            (Know ?x3 ?ag1 ?x1)
            (isStart ?x3)
            (Know ?x4 ?ag2 ?x1)
            (isStart ?x4)
            (not(free ?x1))
            (not(free ?x3))
            (not(free ?x4)) 
    ) ;end_effect
)




(:action test
    :parameters (?x1 ?x2 ?x3 ?x4 ?x5 - id)
    :precondition (and 
        (happy ?x1 sally robot ?x2)
        (happy ?x3 anne robot ?x4)
        (Ignore ?x4 sally ?x3)
        (Ignore ?x5 anne ?x1)
    )
    :effect (and 
        (ok) 
    );end_effect
)

)
