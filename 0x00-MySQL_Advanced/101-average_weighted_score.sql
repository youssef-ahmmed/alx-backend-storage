-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER //

CREATE PROCEDURE `ComputeAverageWeightedScoreForUsers` ()
BEGIN
    UPDATE `users` AS `u`
    SET `average_score` = (
        SELECT
            COALESCE(SUM(`c`.`score` * `p`.`weight`) / NULLIF(SUM(`p`.`weight`), 0), 0)
        FROM
            `corrections` AS `c`
            INNER JOIN `projects` `p` ON `c`.`project_id` = `p`.`id`
        WHERE
            `c`.`user_id` = `u`.`id`
    )
    WHERE
        EXISTS (
            SELECT 1
            FROM `corrections` `c`
            WHERE `c`.`user_id` = `u`.`id`
        );
END //

DELIMITER ;
