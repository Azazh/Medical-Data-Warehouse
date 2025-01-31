{{ config(materialized='table') }}

SELECT
    md5(message_key || channel_name) AS message_id,
    message_key,
    channel_name,
    message_date,
    message_content,
    media_location,
    load_time,
    LENGTH(message_content) AS message_length,
    CASE WHEN media_location != 'N/A' THEN TRUE ELSE FALSE END AS has_media
FROM {{ ref('stg_medical_data') }}