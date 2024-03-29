{% macro convert_to_ml(dose_quantity_value, dose_quantity_unit) %}
    case
        when dose_quantity_unit = 'ML' then dose_quantity_value
        when dose_quantity_unit = 'MG' then dose_quantity_value / 1000
        when dose_quantity_unit = 'MKG' then dose_quantity_value / 1000000
        else dose_quantity_value
    end
{% endmacro %}
