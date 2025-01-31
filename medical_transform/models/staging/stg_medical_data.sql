{{ config(materialized='view') }}

SELECT
    message_id::TEXT AS message_key,
    channel::TEXT AS channel_name,
    date::TIMESTAMP AS message_date,
    text_clean::TEXT AS message_content,
    media_path::TEXT AS media_location,
    scrape_timestamp::TIMESTAMP AS load_time
FROM {{ source('raw', 'raw_medical_data') }}