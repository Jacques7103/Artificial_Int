#Prolog Program
r_triangle(Angle1, Angle2, Angle3) :-
    Angle1 >= 0, Angle1 < 180,
    Angle2 >= 0, Angle2 < 180,
    Angle3 >= 0, Angle3 < 180,
    
    (Angle1 + Angle2 =:= 90 ;
     Angle1 + Angle3 =:= 90 ;
     Angle2 + Angle3 =:= 90).

?- r_triangle(30, 60, 90).