(define    
    (problem simple_prob)    
    (:domain simple_dom)    
    (:objects    
      Ilenia - person   
      Federico - person
      room - place    
      box - place    
      ball - objecto  
    )    
    (:init    
      (isIn Ilenia room)    
      (isIn Federico room)    
      (isIn ball room)    
      (notSame room box)
    )    
          
    (:goal    
      (isHappy Robot)        
    )    
)  