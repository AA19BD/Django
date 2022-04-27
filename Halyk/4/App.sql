CREATE TABLE TextParsing(
    text text
);
INSERT INTO TextParsing(text) VALUES ('Тестовые номер: БИК 044525600 / Расчётный счёт 40702810400260004426. Валидация и проверка контрольного числа расчетного счета/корреспондентского счета.');

-- SELECT * FROM TextParsing;
-- SELECT text, SUBSTRING(text,48,20) AS CheckingAccount FROM TextParsing;

SELECT text, SUBSTRING(text FROM '\d{20}') AS CheckingAccount FROM TextParsing;