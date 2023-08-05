from hestia_earth.schema import EmissionMethodTier, EmissionStatsDefinition, TermTermType
from hestia_earth.utils.tools import list_sum
from hestia_earth.utils.model import filter_list_term_type

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils import _filter_list_term_unit
from hestia_earth.models.utils.constant import Units, get_atomic_conversion, convert_to_unit
from hestia_earth.models.utils.dataCompleteness import _is_term_type_complete
from hestia_earth.models.utils.emission import _new_emission
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "dataCompleteness.soilAmendments": "",
        "inputs": {
            "@type": "Input",
            "term.termType": "soilAmendment",
            "term.units": ["kg CaCO3", "kg MgCO3"]
        }
    }
}
RETURNS = {
    "Emission": [{
        "value": "",
        "methodTier": "tier 1",
        "statsDefinition": "modelled"
    }]
}
TERM_ID = 'co2ToAirLimeHydrolysis'
TIER = EmissionMethodTier.TIER_1.value


def _emission(value: float):
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = TIER
    emission['statsDefinition'] = EmissionStatsDefinition.MODELLED.value
    return emission


def _get_lime_values(cycle: dict, inputs: list):
    # TODO: use lookup table
    values = [convert_to_unit(i, Units.KG_CO2) for i in inputs if len(i.get('value', [])) > 0]
    return [0] if len(values) == 0 and _is_term_type_complete(cycle, {'termType': 'soilAmendments'}) else values


def _run(CaCO3_values: list, MgCO3_values: list):
    value = (
        list_sum(CaCO3_values) + list_sum(MgCO3_values)
    ) * get_atomic_conversion(Units.KG_CO2, Units.TO_C)

    return [_emission(value)]


def _should_run(cycle: dict):
    inputs = filter_list_term_type(cycle.get('inputs', []), TermTermType.SOILAMENDMENT)
    CaCO3_values = _get_lime_values(cycle, _filter_list_term_unit(inputs, Units.KG_CACO3))
    MgCO3_values = _get_lime_values(cycle, _filter_list_term_unit(inputs, Units.KG_MGCO3))

    logRequirements(model=MODEL, term=TERM_ID,
                    CaCO3_values=len(CaCO3_values),
                    MgCO3_values=len(MgCO3_values))

    should_run = all([len(CaCO3_values) > 0, len(MgCO3_values) > 0])
    logShouldRun(MODEL, TERM_ID, should_run, methodTier=TIER)
    return should_run, CaCO3_values, MgCO3_values


def run(cycle: dict):
    should_run, CaCO3_values, MgCO3_values = _should_run(cycle)
    return _run(CaCO3_values, MgCO3_values) if should_run else []
