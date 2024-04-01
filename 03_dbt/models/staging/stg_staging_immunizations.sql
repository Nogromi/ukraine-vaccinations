with 

source as (

    select * from {{ source('staging', 'immunizations') }}

),

renamed as (

    select
        temp_immunization_id,
        legal_entity_id,
        division_identifier_value,
        vaccine_code,
        {{ get_vaccine_type_description("vaccine_code") }} as vaccine_code_description,
        patient_age_group,
        patient_gender,
        manufacturer,
        lot_number,
        {{ convert_to_ml('dose_quantity_value', 'dose_quantity_unit') }} as dose_in_ml,
        vaccination_protocol_series,
        updated_at,
        __index_level_0__

    from source

)

select * from renamed


-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}
