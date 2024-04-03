{% macro gender_translate(patient_gender) %}
   
    case {{ dbt.safe_cast("patient_gender", api.Column.translate_type("string")) }}  
        when 'Чоловіча' then 'Male'
        when 'Жіноча' then 'Female'

    end
{% endmacro %}