
select 
    legal_entity_id,
    legal_entity_name,
    registration_settlement,
    lat,
    lng
from {{ ref('immunization_legal_entities_info') }}