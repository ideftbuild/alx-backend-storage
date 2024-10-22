-- The trigger resets the attribute valid_email only when the email has been changed

DELIMITER //

CREATE TRIGGER validate_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	DECLARE is_validated INT DEFAULT 1;
	IF OLD.email <> NEW.email THEN
		SET is_validated = 0;
	END IF;
	UPDATE users
	SET valid_email = is_validated
	WHERE id = NEW.id;
END;
//

DELIMITER ;
