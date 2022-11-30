(define
    (problem ToM_prob)
    (:domain ToM_dom)
    (:objects
        robot - agent
        Ann - agent
        Sally - agent
        chest - objecto
        box - objecto
        ball - objecto
        room - place
        elsewhere - place
        p1 p2 p3 p4 p5 - phase
        start end i1 i2 i3 i4 i5 i6 i7 i8 i9 i10 i11 i12 i13 i14 i15 i16 i17 i18 i19 i20 i21 i22 i23 i24 i25 i26 i27 i28 i29 i30 i31 i32 i33 i34 - id
    )

    ; gli oggetti devono essere disgiunti tra loro

    (:init 
        (hasStartId robot start)
        (hasStartId Sally start)
        (hasStartId Ann start)

        (notSame robot Ann)
        (notSame robot Sally)
        (notSame robot chest)
        (notSame robot box)
        (notSame robot ball)
        (notSame robot elsewhere)
        (notSame robot room)
        
        (notSame Ann robot)
        (notSame Ann Sally)
        (notSame Ann chest)
        (notSame Ann box)
        (notSame Ann ball)
        (notSame Ann elsewhere)
        (notSame Ann room)
       

        (notSame Sally robot)
        (notSame Sally Ann)
        (notSame Sally chest)
        (notSame Sally box)
        (notSame Sally ball)
        (notSame Sally elsewhere)
        (notSame Sally room)
        
        
        (notSame chest robot)
        (notSame chest Ann)
        (notSame chest Sally)
        (notSame chest box)
        (notSame chest ball)
        (notSame chest elsewhere)
        (notSame chest room)
        

        (notSame box robot)
        (notSame box Ann)
        (notSame box Sally)
        (notSame box chest)
        (notSame box ball)
        (notSame box elsewhere)
        (notSame box room)
        
        (notSame ball robot)
        (notSame ball Ann)
        (notSame ball Sally)
        (notSame ball chest)
        (notSame ball box)
        (notSame ball elsewhere)
        (notSame ball room)
        
        (notSame elsewhere robot)
        (notSame elsewhere Ann)
        (notSame elsewhere Sally)
        (notSame elsewhere chest)
        (notSame elsewhere box)
        (notSame elsewhere ball)
        (notSame elsewhere room)
        
        (notSame room robot)
        (notSame room Ann)
        (notSame room Sally)
        (notSame room chest)
        (notSame room box)
        (notSame room ball)
        (notSame room elsewhere)
        

        ; first sketch
        (know start robot i1 p1)
        (isIn i1 robot room p1)
        (see start robot i2 p1)
        (isIn i2 Sally room p1)
        (see start robot i3 p1)
        (isIn i3 Ann room p1)
        (see start robot i4 p1)
        (isIn i4 chest room p1)
        (see start robot i5 p1)
        (isIn i5 box room p1)
        (see start robot i6 p1)
        (isHappy i6 Sally end p1)
        (see start robot i7 p1)
        (isHappy i7 Ann end p1)
        (follows p2 p1)

        
        ; second sketch
        (know start robot i8 p2)
        (isIn i8 robot room p2)
        (see start robot i9 p2)
        (isIn i9 Sally room p2)
        (see start robot i10 p2)
        (isIn i10 Ann room p2)
        (see start robot i11 p2)
        (isIn i11 chest room p2)
        (see start robot i12 p2)
        (isIn i12 box room p2)
        (see start robot i13 p2)
        (isHappy i13 Sally end p2)
        (see start robot i14 p2)
        (isHappy i14 Ann end p2)
        (see start robot i15 p2)
        (isIn i15 ball room p2)
        (see start robot i16 p2)
        (isPutting i16 Sally ball chest p2)
        (follows p3 p2)
        (notSameId i9 i10)
        (notSameId i10 i9)
        (notSameId i16 i10)
        (notSameId i10 i16)
        (notSameId i9 i16)
        (notSameId i16 i9) 
        ;(notSameP room ball chest)       

       ;third sketch
    ;    (know start robot i17 p3)
    ;    (isIn i17 robot room p3)
    ;    (see start robot i18 p3)
    ;    (isIn i18 Sally room p3)
    ;    (see start robot i19 p3)
    ;    (isIn i19 Ann room p3)
    ;    (see start robot i20 p3)
    ;    (isIn i20 chest room p3)
    ;    (see start robot i21 p3)
    ;    (isIn i21 box room p3)
    ;    (see start robot i22 p3)
    ;    (isHappy i22 Ann end p3)
    ;    (see start robot i23 p3)
    ;    (isGoing i23 Sally room elsewhere p3)
    ;    (follows p4 p3)

       ;forth sketch
    ;    (know start robot i24 p4)
    ;    (isIn i24 robot room p4)
    ;    (see start robot i25 p4)
    ;    (isIn i25 Ann room p4)
    ;    (see start robot i26 p4)
    ;    ;(isIn i26 chest room p4)
    ;    (see start robot i27 p4)
    ;    ;(isIn i27 box room p4)
    ;    (see start robot i28 p4)
    ;    (isHappy i28 Ann end p4)
    ;    (see start robot i29 p4)
    ;    (isPutting i29 Ann ball box p4)
    ;    (follows p5 p4)

       ;fifth sketch
    ;    (know start robot i30 p5)
    ;    (isIn i30 robot room p5)
    ;    (see start robot i31 p5)
    ;    (isIn i31 Sally room p5)
    ;    (see start robot i32 p5)
    ;   ; (isIn i32 chest room p5)
    ;    (see start robot i33 p5)
    ;   ; (isIn i33 box room p5)
    ;    (see start robot i34 p5)
    ;    (isHappy i34 Sally end p5)

    )

    (:goal (test-ok)
    )
)
