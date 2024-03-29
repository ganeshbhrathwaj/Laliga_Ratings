SELECT * INTO LALIGA_STATS
FROM (
select *, case when Position ='Goalkeeper' then 0 
when Position ='Defender' then 1
when Position ='Midfielder' then 2
when Position ='Forward' then 3
end as pos 
from(
SELECT * FROM FC_BARCELONA
UNION
SELECT * FROM REAL_MADRID
UNION
SELECT * FROM ATHLETIC_CLUB
UNION
SELECT * FROM ATLETICO_DE_MADRID
UNION
SELECT * FROM CADIZ_CF
UNION
SELECT * FROM GETAFE_CF
UNION
SELECT * FROM GIRONA_FC
UNION
SELECT * FROM RAYO_VALLECANO
UNION
SELECT * FROM RC_CELTA
UNION
SELECT * FROM RCD_MALLORCA
UNION
SELECT * FROM REAL_BETIS
UNION
SELECT * FROM REAL_SOCIEDAD
UNION
SELECT * FROM SEVILLA_FC
UNION
SELECT * FROM UD_ALMERIA
UNION
SELECT * FROM VALENCIA_CF
UNION
SELECT * FROM VILLARREAL_CF
) 
as t ) as t2;