(define 
    (problem simple_prob)
    (:domain simple_dom) 
    (:objects 
        box - place
        ball - objecto
        room - place
        Ilenia - person
        Federico - person    
)
    (:init
        (isIn Ilenia room)
        (isIn Federico room)
        (notSame Ilenia Federico)
        (notSame Federico Ilenia)
        (isIn ball room)
        (notSame room box)
        
    )
    (:goal (and
        (isHappy Robot)
    )  
)    
)