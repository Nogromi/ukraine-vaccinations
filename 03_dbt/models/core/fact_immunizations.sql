with vaccination as (
    select *, 
    from {{ ref('stg_staging_immunizations') }}
),
legal_entities as (
    select legal_entity_id,
     registration_settlement
     from {{ ref('dim_legal_entities') }}
    where lat != 0 or lng!= 0
)

select  vaccination.temp_immunization_id,
        vaccination.division_identifier_value,
        vaccination.vaccine_code,
        vaccination.vaccine_code_description,
        vaccination.patient_age_group,
        vaccination.patient_gender,
        vaccination.manufacturer,
        vaccination.lot_number,
        vaccination.dose_in_ml,
        vaccination.vaccination_protocol_series,
        vaccination.updated_at,
        legal_entities.registration_settlement
from vaccination
inner join legal_entities 
on vaccination.legal_entity_id=legal_entities.legal_entity_id
