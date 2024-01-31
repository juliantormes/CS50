-- Retrieve the description of the crime scene that occurred on Humphrey Street on July 28, 2021
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND year = 2021 AND street = 'Humphrey Street';

-- Retrieve the names and transcripts of witnesses who mentioned the thief on the day of the incident
SELECT i.name, i.transcript
FROM interviews i
WHERE month = 7 AND day = 28 AND year = 2021 AND i.transcript LIKE '%thief%'
ORDER BY i.name;

-- Identify individuals who made a withdrawal at the ATM on Leggett Street on the day of the theft
SELECT p.name
FROM people p
WHERE p.id IN (
    SELECT ba.person_id
    FROM atm_transactions at
    JOIN bank_accounts ba ON ba.account_number = at.account_number
    WHERE month = 7 AND day = 28 AND year = 2021 AND
    atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
)
ORDER BY p.name;

-- Identify individuals who had a phone call lasting less than a minute on the day of the theft
SELECT p.name
FROM people p
WHERE p.phone_number IN (
    SELECT pc.caller
    FROM phone_calls pc
    WHERE month = 7 AND day = 28 AND year = 2021 AND duration <= 60
)
ORDER BY p.name;

-- Identify individuals who left the bakery parking lot within ten minutes of the theft
SELECT p.name
FROM people p
WHERE p.license_plate IN (
    SELECT bsl.license_plate
    FROM bakery_security_logs bsl
    WHERE month = 7 AND day = 28 AND year = 2021 AND
    hour = 10 AND minute BETWEEN 15 AND 25 AND activity = 'exit'
)
ORDER BY p.name;

-- Identify individuals who were on the earliest flight out of Fiftyville the day following the theft
SELECT p.name
FROM people p
WHERE p.passport_number IN (
    SELECT ps.passport_number
    FROM passengers ps
    WHERE ps.flight_id IN (
        SELECT f.id
        FROM flights f
        JOIN airports org ON org.id = f.origin_airport_id
        WHERE f.month = 7 AND f.day = 29 AND f.year = 2021 AND
        org.city = 'Fiftyville'
        ORDER BY f.hour, f.minute
        LIMIT 1
    )
)
ORDER BY p.name;

-- Determine the thief based on multiple converging pieces of evidence
SELECT p.name
FROM people p
WHERE p.id IN (
    -- Same subqueries as before, combining conditions from the ATM, phone calls, parking lot, and flight
)
ORDER BY p.name;

-- Identify the individual who received a short phone call from the thief on the day of the theft
SELECT p.name
FROM people p
WHERE p.phone_number IN (
    SELECT pc.receiver
    FROM phone_calls pc
    WHERE month = 7 AND day = 28 AND year = 2021 AND
    caller = (
        SELECT p.phone_number
        FROM people p
        WHERE p.name = 'Bruce'
    ) AND
    duration <= 60
)
ORDER BY p.name;