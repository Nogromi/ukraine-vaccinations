{#
    This macro returns the description of the vaccine_code 
#}

{% macro get_vaccine_type_description(vaccine_code) -%}

    case {{ dbt.safe_cast("vaccine_code", api.Column.translate_type("string")) }}  
        when 'SarsCov2_Pr' then 'Protein'
        when 'SarsCov2_DNA' then 'DNA'
        when 'SarsCov2_RNA' then 'RNA'
        when 'SarsCov2_RVv' then 'Viral Vector Replicating'
        when 'SarsCov2_mRNA' then 'mRNA'
        when 'SarsCov2_nRVv' then 'Viral Vector Non-Replicating'
        when 'SarsCov2_Inact' then 'Inactivated'
        when 'SarsCov2_Rc_lp' then 'Live Attenuated'
        else ''
    end

{%- endmacro %}