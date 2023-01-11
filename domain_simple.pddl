(define    
      (domain simple_dom)    
      (:requirements :strips :typing :negative-preconditions)    
          
      (:types    
      
      person - entity 
      objecto - entity  
      place - entity
      )    
      
      (:constants
        Serena - person 
         Robot - person
      )

      (:predicates    
      (isIn ?e - entity ?p - place)    
      (isSad ?a - person)    
      (isHappy ?a - person)    
      (notSame ?e1 ?e2 - entity)    
          
          
      )    
          
      (:action ask_go_out    
      :parameters (?p - place)    
      :precondition (and (isIn Serena ?p))
      :effect (and(not(isIn Serena ?p))) 
      )    
          
      (:action ask_move_obj    
      :parameters (?x - person ?p1 ?p2 - place ?o - objecto)    
      :precondition (and (not(isIn Serena ?p1)) (isIn ?x ?p1) (isIn ?o ?p1) (notSame ?p1 ?p2))    
      :effect (and (isIn ?o ?p2))    
      )    
          
      (:action ask_call_someone    
      :parameters (?x - person ?p1 ?p2 - place ?o - objecto )    
      :precondition (and (not(isIn Serena ?p1)) (isIn ?x ?p1) (isIn ?o ?p2) (notSame ?p1 ?p2))    
      :effect (and (isIn Serena ?p1))    
      )    
          
      (:action ask_someone_obj_place    
      :parameters (?y - person ?p1 ?p2 - place ?o - objecto )    
      :precondition (and (isIn Serena ?p1) (isIn ?o ?p2) (notSame ?p1 ?p2))    
      :effect (and (isSad ?y))    
      )    
          
      (:action laugh    
      :parameters (?y - person)    
      :precondition (and (IsSad ?y))    
      :effect (and (isHappy Robot))    
      )    
)  
