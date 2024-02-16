{{
  config(
    materialized='table'
  )
}}

with base as (
    select *
    from {{ source('tap_spacex', 'launchpads') }}
)

SELECT *,
       CURRENT_TIMESTAMP as transformation_updated_at
FROM base