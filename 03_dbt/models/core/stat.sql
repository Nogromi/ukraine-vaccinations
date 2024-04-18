{{ config(materialized='table') }}

with vaccination_data as (
    select * from {{ ref('fact_vaccinations') }}
)
 select 
    --  grouping 
    registration_settlement as place,
    {{ dbt.date_trunc("month", "vaccination_date") }} as vaccination_month, 
    patient_age_group as age_group,
    patient_gender as gender,
    vaccine_code as vaccine_code,
    -- Additional calculations
    count(temp_immunization_id) as count_vaccination
    from vaccination_data
    group by vaccination_month,patient_age_group,patient_gender, registration_settlement, vaccine_code
