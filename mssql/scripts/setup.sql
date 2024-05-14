-- per la connessione a db su vscode scrivere:
-- localhost,1433
-- table_test
-- sa
-- yourStrongPassword!1

CREATE DATABASE test_db;
GO
use test_db
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'table_test')
create table table_test
(
    id int not null primary key IDENTITY(1,1),
    username varchar(100),
    surname varchar(100),
);
GO
-- VALUES (11, N'Customer01');
-- go
