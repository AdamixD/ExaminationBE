from sqlalchemy import text
from database.session import engine


with engine.connect() as connection:
    connection.execute(text(
        """
        INSERT INTO `` (`student_id`,`course_realization_id`) VALUES (1,1);
        INSERT INTO `` (`student_id`,`course_realization_id`) VALUES (1,2);
        INSERT INTO `` (`student_id`,`course_realization_id`) VALUES (1,3);
        """
    ))

    connection.execute(text(
        """
        INSERT INTO table_name (id, semester, course_id, lecturer_id) VALUES 
        INSERT INTO `` (`id`,`title`,`shortcut`) VALUES (1,'Algorytmy i struktury danych','AISDI');
        INSERT INTO `` (`id`,`title`,`shortcut`) VALUES (2,'Analiza i projektowanie systemów informacyjnych','APSI');
        INSERT INTO `` (`id`,`title`,`shortcut`) VALUES (3,'Bazy danych 2','BD2');
        INSERT INTO `` (`id`,`title`,`shortcut`) VALUES (4,'Sieci komputerowe','SKM');
        INSERT INTO `` (`id`,`title`,`shortcut`) VALUES (5,'Nanotechnologie','NAN');
        INSERT INTO `` (`id`,`title`,`shortcut`) VALUES (6,'Programowanie obiektowe','PROI');
        INSERT INTO `` (`id`,`title`,`shortcut`) VALUES (7,'Podstawy automatyki','PODA');
        """
    ))
