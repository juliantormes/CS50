BEGIN TRANSACTION;

UPDATE shows SET title = 'Adventure Time' WHERE LOWER(title) LIKE LOWER('Adventure Time');
UPDATE shows SET title = 'Arrow' WHERE LOWER(title) LIKE LOWER('Arrow');
UPDATE shows SET title = 'Avatar: The Last Airbender' WHERE LOWER(title) LIKE LOWER('Avatar%The Last Airbender');
UPDATE shows SET title = 'Brooklyn Nine-Nine' WHERE LOWER(title) LIKE LOWER('Brooklyn Nine-Nine');
UPDATE shows SET title = 'Community' WHERE LOWER(title) LIKE LOWER('Community');
UPDATE shows SET title = 'Family Guy' WHERE LOWER(title) LIKE LOWER('Family Guy');
UPDATE shows SET title = 'Friends' WHERE LOWER(title) LIKE LOWER('Friends');
UPDATE shows SET title = 'Game of Thrones' WHERE LOWER(title) LIKE LOWER('Game of Thrones');
UPDATE shows SET title = 'Gilmore Girls' WHERE LOWER(title) LIKE LOWER('Gilmore Girls');
UPDATE shows SET title = 'Grey’s Anatomy' WHERE LOWER(title) LIKE LOWER('Grey’s Anatomy');
UPDATE shows SET title = 'How I Met Your Mother' WHERE LOWER(title) LIKE LOWER('How I Met Your Mother');
UPDATE shows SET title = 'It’s Always Sunny in Philadelphia' WHERE LOWER(title) LIKE LOWER('It’s Always Sunny in Philadelphia');
UPDATE shows SET title = 'Parks and Recreation' WHERE LOWER(title) LIKE LOWER('Parks and Recreation');
UPDATE shows SET title = 'Sherlock' WHERE LOWER(title) LIKE LOWER('Sherlock');
UPDATE shows SET title = 'Squid Game' WHERE LOWER(title) LIKE LOWER('Squid Game');
UPDATE shows SET title = 'The Bachelorette' WHERE LOWER(title) LIKE LOWER('The Bachelorette');
UPDATE shows SET title = 'The Crown' WHERE LOWER(title) LIKE LOWER('The Crown');
UPDATE shows SET title = 'The Office' WHERE LOWER(title) LIKE LOWER('The Office');
UPDATE shows SET title = 'The Queen’s Gambit' WHERE LOWER(title) LIKE LOWER('The Queen’s Gambit');
UPDATE shows SET title = 'The Untamed' WHERE LOWER(title) LIKE LOWER('The Untamed');
-- Correcting "Brooklyn Nine-Nine"
UPDATE shows
SET title = 'Brooklyn Nine-Nine'
WHERE
    LOWER(title) = LOWER('b99')
    OR LOWER(title) = LOWER('Brooklyn 99')
    OR LOWER(title) = LOWER('Brooklyn Nine-Nine');

-- Correcting "Game of Thrones"
UPDATE shows
SET title = 'Game of Thrones'
WHERE LOWER(title) LIKE LOWER('Game of Thrones') AND title != 'Game of Thrones';

-- Correcting "Grey’s Anatomy"
UPDATE shows
SET title = 'Grey’s Anatomy'
WHERE LOWER(title) LIKE LOWER('Grey’s Anatomy') AND title != 'Grey’s Anatomy';

-- Correcting "It’s Always Sunny in Philadelphia"
UPDATE shows
SET title = 'It’s Always Sunny in Philadelphia'
WHERE LOWER(title) LIKE LOWER('It’s Always Sunny in Philadelphia') AND title != 'It’s Always Sunny in Philadelphia';

-- Correcting "Parks and Recreation"
UPDATE shows
SET title = 'Parks and Recreation'
WHERE LOWER(title) LIKE LOWER('Parks and Recreation') AND title != 'Parks and Recreation';

-- Correcting "The Office"
UPDATE shows
SET title = 'The Office'
WHERE LOWER(title) LIKE LOWER('The Office') AND title != 'The Office';

COMMIT;
