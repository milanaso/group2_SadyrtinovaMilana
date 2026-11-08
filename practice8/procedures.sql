CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_name IS NULL OR BTRIM(p_name) = '' THEN
        RAISE EXCEPTION 'Name cannot be empty';
    END IF;

    IF p_phone IS NULL OR p_phone !~ '^\+7[0-9]{10}$' THEN
        RAISE EXCEPTION 'Invalid phone number';
    END IF;

    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE first_name = p_name
    ) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE first_name = p_name;
    ELSE
        INSERT INTO contacts(first_name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE bulk_upsert_contacts(
    IN p_contacts JSONB,
    INOUT p_invalid JSONB
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact JSONB;
    v_name TEXT;
    v_phone TEXT;
BEGIN
    p_invalid := '[]'::JSONB;

    FOR v_contact IN
        SELECT value
        FROM jsonb_array_elements(p_contacts)
    LOOP
        v_name := v_contact ->> 'name';
        v_phone := v_contact ->> 'phone';

        IF v_name IS NULL OR BTRIM(v_name) = ''
           OR v_phone IS NULL
           OR v_phone !~ '^\+7[0-9]{10}$' THEN

            p_invalid := p_invalid || jsonb_build_array(v_contact);

        ELSE
            BEGIN
                IF EXISTS (
                    SELECT 1
                    FROM contacts
                    WHERE first_name = v_name
                ) THEN
                    UPDATE contacts
                    SET phone = v_phone
                    WHERE first_name = v_name;
                ELSE
                    INSERT INTO contacts(first_name, phone)
                    VALUES (v_name, v_phone);
                END IF;

            EXCEPTION
                WHEN unique_violation THEN
                    p_invalid := p_invalid || jsonb_build_array(v_contact);
            END;
        END IF;
    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF (p_name IS NULL AND p_phone IS NULL)
       OR (p_name IS NOT NULL AND p_phone IS NOT NULL) THEN
        RAISE EXCEPTION 'Provide either name or phone';
    END IF;

    IF p_name IS NOT NULL THEN
        DELETE FROM contacts
        WHERE first_name = p_name;
    ELSE
        DELETE FROM contacts
        WHERE phone = p_phone;
    END IF;
END;
$$;
