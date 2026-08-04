BEGIN

FUNCTION Sum(n)

    IF n = 1 THEN
        RETURN 1
    ELSE
        RETURN n + Sum(n - 1)
    END IF

END FUNCTION

INPUT n

result ← Sum(n)

DISPLAY result

END
