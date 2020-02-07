select
  (1.0 * (select count(app_id) from events where event_id = "click" and year(timestamp) = 2019)) /
  (select count(app_id) from events where event_id = "impression" and year(timestamp) = 2019);