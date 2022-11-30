(define 
    (domain ToM_dom)
    (:requirements :adl :derived-predicates :strips :fluents :durative-actions :timed-initial-literals :typing :conditional-effects :negative-preconditions :duration-inequalities :equality)
    
    (:types 
        entity
        agent - entity
        objecto - entity
        place - entity
        phase
        id
    )

    (:predicates 
         (see ?id1 - id  ?ag - agent ?id2 - id ?v - phase)
         (know ?id1 - id  ?ag - agent ?id2 - id ?v - phase)
         (hasStartId ?ag - agent ?id - id)
         (isIn ?id - id ?e - entity ?p - entity ?v - phase)
         (isPutting ?id - id ?ag - agent ?o - entity ?p -entity ?v - phase)
         (isGoing ?id - id ?ag - agent ?p1 - entity ?p2 - entity ?v - phase)
         (follows ?v1 - phase ?v2 - phase)
         (isHappy ?id1 - id ?ag - agent ?id2 - id ?v - phase)
         (notSame ?e1 - entity ?e2 - entity)
         (notSameId ?i1 ?i2 - id)
         (notSameP ?e1 ?e2 ?e3 - entity) 
         (test-ok)
    )
    
    (:action works 
        :parameters ( ) 
        :precondition (and (know start robot i8 p2))
        :effect (and (test-ok))
    )
    
;     (:derived (know ?id1 - id ?ag - agent ?id2 - id ?v - phase )
        
;         (see ?id1 ?ag ?id2 ?v)   

;     )

;     (:derived (know ?id1 - id ?ag2 - agent ?id2 - id ?v - phase )
;         (exists ( ?ag1 - agent ?p - entity )
;             (and
;                 (know ?id1 ?ag1 ?id2 ?v)
;                 (hasStartId ?ag1 ?id1)
;                 (isIn ?id2 ?ag2 ?p ?v)

;                 (notSame ?ag1 ?ag2)
;             )
;         )      
;     )


; ; ; ;;;;;;;;;;;;;;;;;;;;;;;RISOLTO;;;;;;;;
;     (:derived (see  ?id1 - id ?ag2 - agent ?id3 - id ?v - phase )
;         (exists (?ag1 - agent ?id2 - id ?p - entity ?e - entity )
;             (and
;                 (know ?id1 ?ag1 ?id2 ?v)
;                 (hasStartId ?ag1 ?id1)
;                 (isIn ?id2 ?ag2 ?p ?v)
;                 (know ?id1 ?ag1 ?id3 ?v)
;                 (isIn ?id3 ?e ?p ?v)
;                 (notSame ?ag2 ?e)
;             )
;         )      
;     )

;     (:derived (know ?id1 - id ?ag2 - agent ?id2 - id ?v - phase )
;         (exists (?ag1 - agent ?o - entity ?p - entity )
;             (and
;                 (know ?id1 ?ag1 ?id2 ?v)
;                 (hasStartId ?ag1 ?id1)
;                 (isPutting ?id2 ?ag2 ?o ?p ?v)
;                 (notSame ?ag1 ?ag2)
;             )
;         )      
;     )

;     
; ;;;;;;;;;;;;;;;;;;;;;;;;CREA PROBLEMI. CAPIRE PERCHé;;;;;;;;
    (:derived (see  ?id1 - id ?ag3 - agent ?id5 - id ?v - phase )
            (exists ( ?id2 ?id3 - id ?ag1 ?ag2 - agent  ?p1 - place ?o ?p2 - objecto)
                (and
                    (know ?id1 ?ag1 ?id2 ?v)
                    (hasStartId ?ag1 ?id1)
                    (isIn ?id2 ?ag2 ?p1 ?v)
                    (know ?id1 ?ag1 ?id3 ?v)
                    (isIn ?id3 ?ag3 ?p1 ?v)
                    (know ?id1 ?ag1 ?id5 ?v)
                    (isPutting ?id5 ?ag2 ?o ?p2 ?v)
                    ;(notSame ?ag1 ?ag2)
                    (notSame ?ag2 ?ag3)
                    (notSameId ?id2 ?id3)
                    (notSame ?o ?p2)
                    ;(notSame ?o ?p1)
                    ;(notSame ?p1 ?p2)
                    ;(notSame ?o chest)
                    ;(notSameP ?p1 ?o ?p2)
                    
                )
            )      
        )

;     (:derived (know ?id1 - id ?ag1 - agent ?id2 - id ?v2 - phase )
;         (exists ( ?ag2 - agent ?o - object ?p - place ?v1 - phase )
;             (and
;                 (know ?id1 ?ag1 ?id2 ?v1)
;                 (hasStartId ?ag1 ?id1)
;                 (isPutting ?id2 ?ag2 ?o ?p ?v1)
;                 (follows ?v2 ?v1) 
;             )
;         )      
;     )

;     (:derived (isIn ?id2 - id ?o - entity ?p - entity ?v2 - phase )
;         (exists (?id1 - id ?ag1 - agent ?ag2 - agent ?v1 - phase )
;             (and
;                 (know ?id1 ?ag1 ?id2 ?v1)
;                 (hasStartId ?ag1 ?id1)
;                 (isPutting ?id2 ?ag2 ?o ?p ?v1)
;                 (follows ?v2 ?v1) 
;             )
;         )      
;     )
    
;     (:derived (know ?id1 - id ?ag - agent ?id2 - id ?v2 - phase )
;         (exists (?o - object ?p - place ?v1 - phase )
;             (and
;                 (know ?id1 ?ag ?id2 ?v1)
;                 (hasStartId ?ag ?id1)
;                 (isPutting ?id2 ?ag ?o ?p ?v1)
;                 (follows ?v2 ?v1) 
;             )
;         )      
;     )


;     (:derived (isIn ?id2 - id ?o - object ?p - place ?v2 - phase )
;         (exists (?id1 - id ?ag - agent ?v1 - phase )
;             (and
;                 (know ?id1 ?ag ?id2 ?v1)
;                 (hasStartId ?ag ?id1) 
;                 (isPutting ?id2 ?ag ?o ?p ?v1)
;                 (follows ?v2 ?v1) 
;             )
;         )      
;     )

;     (:derived (know ?id3 - id ?ag2 - agent ?id2 - id ?v - phase )
;         (exists (?id1 - id ?ag1 - agent ?p1 - place ?p2 - place )
;             (and
;                 (know ?id1 ?ag1 ?id2 ?v)
;                 (hasStartId ?ag1 ?id1)
;                 (isGoing ?id2 ?ag2 ?p1 ?p2 ?v)
;                 (hasStartId ?ag2 ?id3)
;             )
;         )      
;     )
; ;;;;;;;;;;;;;;;;;;;;;;CREA PROBLEMI;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ; (:derived (see  ?id1 - id ?ag3 - agent ?id3 - id ?v - phase )
    ;     (exists (?ag1 - agent ?ag2 - agent ?id2 - id ?p1 - place ?p2 - place )
    ;         (and
    ;             (know ?id1 ?ag1 ?id2 ?v)
    ;             (hasStartId ?ag1 ?id1)
    ;             (isIn ?id2 ?ag2 ?p1 ?v)
    ;             (know ?id1 ?ag1 ?id3 ?v)
    ;             ;(hasStartId ?ag3 ?id4)
    ;             (isIn ?id3 ?ag3 ?p1 ?v)
    ;             ; (know ?id1 ?ag1 ?id5 ?v)
    ;             ; (isGoing ?id5 ?ag2 ?p1 ?p2 ?v)
    ;         )
    ;     )      
    ; )
  
;     (:derived (know ?id1 - id ?ag - agent ?id2 - id ?v2 - phase )
;         (exists (?p1 - place ?p2 - place ?v1 - phase ?ag2 - agent)
;             (and
;                 (know ?id1 ?ag ?id2 ?v1)
;                 (hasStartId ?ag ?id1)
;                 (isGoing ?id2 ?ag2 ?p1 ?p2 ?v1)
;                 (follows ?v2 ?v1) 
;             )
;         )      
;     )

;     (:derived (isIn ?id2 - id ?ag2 - agent ?p2 - place ?v2 - phase )
;         (exists (?id1 - id ?ag - agent ?v1 - phase ?p1 - place )
;             (and
;                 (know ?id1 ?ag ?id2 ?v1)
;                 (isGoing ?id2 ?ag2 ?p1 ?p2 ?v1)
;                 (follows ?v2 ?v1) 

;             )
;         )      
;     )

;     (:derived (know ?id1 - id ?ag - agent ?id2 - id ?v2 - phase )
;         (exists (?p1 - place ?p2 - place ?v1 - phase )
;             (and
;                 (know ?id1 ?ag ?id2 ?v1)
;                 (hasStartId ?ag ?id1)
;                 (isGoing ?id2 ?ag ?p1 ?p2 ?v1)
;                 (follows ?v2 ?v1) 
;             )
;         )      
;     )

    ; (:derived (isIn ?id2 - id ?ag - agent ?p2 - place ?v2 - phase )
    ;     (exists (?id1 - id ?p1 - place ?v1 - phase )
    ;         (and
    ;             (know ?id1 ?ag ?id2 ?v1)
    ;             (hasStartId ?ag ?id1)
    ;             (isGoing ?id2 ?ag ?p1 ?p2 ?v1)
    ;             (follows ?v2 ?v1) 
    ;         )
    ;     )      
    ; )
 )