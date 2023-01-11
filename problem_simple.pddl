(define    
    (problem simple_prob)    
    (:domain simple_dom)    
    (:objects    
      Ilenia - person   
      room - place    
      box - place    
      ball - objecto  
    )    
    (:init    
      (isIn Ilenia room)    
      (isIn Serena room)    
      (isIn ball room)    
      (notSame room box)
    )    
          
    (:goal    
      (isHappy Robot)        
    )    
)  